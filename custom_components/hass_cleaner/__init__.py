"""Read-only reference checks and native Home Assistant Repairs.

The integration only reads configuration and registries. It never changes
Home Assistant configuration and only manages its own repair issues.
"""
from __future__ import annotations

import asyncio
import logging
import traceback

import voluptuous as vol
from homeassistant.components import websocket_api
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import (
    area_registry as ar,
    device_registry as dr,
    entity_registry as er,
    issue_registry as ir,
)
from homeassistant.helpers.event import async_track_time_interval

from .const import (
    DOMAIN,
    ISSUE_PREFIX,
    MAX_REPAIR_ITEMS,
    REFRESH_INTERVAL,
    SCHEMA_VERSION,
    SERVICE_REFRESH,
)
from .panel import async_register_panel, async_unregister_panel
from .references import analyze, repair_groups
from .sources import collect_extended_sources, statistic_ids

_LOGGER = logging.getLogger(__name__)

DATA_COMMANDS_REGISTERED = f"{DOMAIN}_websocket_commands_registered"


def _empty_report(status: str, **extra) -> dict:
    """Bericht mit einheitlichem Grundgerüst."""
    report = {
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "summary": {},
        "sources": [],
        "references": [],
    }
    report.update(extra)
    return report


async def async_setup(hass: HomeAssistant, config) -> bool:
    """Register the WebSocket command and the manual refresh service once."""
    if not hass.data.get(DATA_COMMANDS_REGISTERED):
        websocket_api.async_register_command(hass, websocket_references)
        hass.data[DATA_COMMANDS_REGISTERED] = True
    if not hass.services.has_service(DOMAIN, SERVICE_REFRESH):
        hass.services.async_register(
            DOMAIN,
            SERVICE_REFRESH,
            _async_handle_refresh,
            schema=vol.Schema({}),
            supports_response=SupportsResponse.OPTIONAL,
        )
    return True


async def _async_handle_refresh(call: ServiceCall) -> dict:
    """Run the check immediately and return the report."""
    monitor = call.hass.data.get(DOMAIN)
    if monitor is None:
        raise HomeAssistantError(translation_domain=DOMAIN, translation_key="not_loaded")
    await monitor.refresh()
    if monitor.report is None:
        raise HomeAssistantError(translation_domain=DOMAIN, translation_key="no_report")
    return monitor.report


@websocket_api.websocket_command(
    {
        vol.Required("type"): "hass_cleaner/references",
        vol.Optional("refresh", default=False): bool,
    }
)
@websocket_api.async_response
async def websocket_references(hass, connection, msg):
    if not connection.user or not connection.user.is_admin:
        connection.send_error(msg["id"], "unauthorized", "Administrator access required")
        return
    monitor = hass.data.get(DOMAIN)
    if monitor is None:
        connection.send_error(msg["id"], "not_loaded", "Set up Hass-Cleaner Companion first")
        return
    if msg["refresh"] or monitor.report is None:
        await monitor.refresh()
    if monitor.report is None:
        connection.send_error(msg["id"], "not_loaded", "Set up Hass-Cleaner Companion first")
        return
    connection.send_result(msg["id"], monitor.report)


async def collect_sources(hass):
    """Keep access to HA runtime configuration isolated in this adapter."""
    sources = []
    for kind in ("automation", "script"):
        component = hass.data.get(kind)
        if component is None:
            if kind in hass.config.components:
                sources.append(
                    {
                        "id": kind,
                        "kind": kind,
                        "name": kind,
                        "error": "Configuration component unavailable",
                    }
                )
            continue
        for entity in list(component.entities):
            sources.append(
                {
                    "id": entity.entity_id,
                    "kind": kind,
                    "name": entity.name or entity.entity_id,
                    "config": getattr(entity, "raw_config", None),
                }
            )
    lovelace = hass.data.get("lovelace")
    dashboards = getattr(lovelace, "dashboards", None)
    if lovelace is not None and dashboards is None:
        sources.append(
            {
                "id": "dashboard:all",
                "kind": "dashboard",
                "name": "Dashboards",
                "error": "Dashboard API unavailable",
            }
        )
    for url_path, dashboard in list((dashboards or {}).items()):
        source = {
            "id": f"dashboard:{url_path if url_path is not None else 'default'}",
            "kind": "dashboard",
            "name": (dashboard.config or {}).get("title", url_path or "Overview"),
        }
        try:
            source["config"] = await dashboard.async_load(False)
        except Exception as exc:
            # Do not log raw exception messages: they can include configuration values.
            source["error"] = f"Dashboard could not be loaded ({type(exc).__name__})"
        sources.append(source)
    sources.extend(await collect_extended_sources(hass))
    return sources


class ReferenceMonitor:
    """Hält den jeweils letzten Bericht und serialisiert die Prüfläufe."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self.report: dict | None = None
        self.lock = asyncio.Lock()
        self.closed = False

    async def refresh(self, _now=None) -> None:
        async with self.lock:
            if self.closed:
                return
            hass = self.hass
            if not hass.is_running:
                self.report = _empty_report("starting")
                return
            stage = "sources"
            try:
                sources = await collect_sources(hass)
                stage = "registries"
                entity_registry = er.async_get(hass)
                known = {
                    "entity": set(entity_registry.entities) | set(hass.states.async_entity_ids()),
                    "entity_aliases": {
                        entry.id: entry.entity_id for entry in entity_registry.entities.values()
                    },
                    "device": set(dr.async_get(hass).devices),
                    "area": set(ar.async_get(hass).areas),
                    "action": {
                        f"{domain}.{service}"
                        for domain, services in hass.services.async_services().items()
                        for service in services
                    },
                }
                stage = "statistics"
                known["statistic"] = await statistic_ids(hass)
                stage = "analysis"
                report = await hass.async_add_executor_job(analyze, sources, known)
                if self.closed:
                    return
                stage = "repairs"
                self.reconcile(report)
                self.report = report
            except Exception as exc:
                if not self.report or self.report.get("status") != "unavailable":
                    # Code locations only: no exception text, source lines or locals.
                    locations = " -> ".join(
                        f"{frame.name}:{frame.lineno}"
                        for frame in traceback.extract_tb(exc.__traceback__)
                    )
                    _LOGGER.warning(
                        "Reference check failed: stage=%s type=%s locations=%s",
                        stage,
                        type(exc).__name__,
                        locations,
                    )
                self.report = _empty_report(
                    "unavailable",
                    reason="check_failed",
                    stage=stage,
                    error="Reference check failed; previous repair issues have been retained",
                )

    @callback
    def reconcile(self, report: dict) -> None:
        """Create and resolve only this integration's own repair issues."""
        if self.closed:
            return
        groups = repair_groups(report)
        registry = ir.async_get(self.hass)
        # A failed/partial source must not falsely resolve its existing issue.
        complete = {s["id"] for s in report["sources"] if s["status"] == "checked"}
        seen = {s["id"] for s in report["sources"]}
        for (domain, issue_id), issue in list(registry.issues.items()):
            if domain != DOMAIN or not issue_id.startswith(ISSUE_PREFIX) or issue_id in groups:
                continue
            source_id = (issue.data or {}).get("source_id")
            if source_id in complete or (
                source_id not in seen and report["status"] == "completed"
            ):
                ir.async_delete_issue(self.hass, DOMAIN, issue_id)
        for issue_id, group in groups.items():
            details = "\n".join("- " + item for item in group["items"][:MAX_REPAIR_ITEMS])
            ir.async_create_issue(
                self.hass,
                DOMAIN,
                issue_id,
                is_fixable=False,
                is_persistent=False,
                severity=ir.IssueSeverity.ERROR,
                translation_key="missing_references",
                translation_placeholders={
                    "source": group["source"],
                    "references": details,
                    "count": str(len(group["items"])),
                },
                data={"source_id": group["source_id"]},
                learn_more_url=(
                    "https://github.com/Bart1109/Hass-Cleaner/blob/main/docs/reference-checks.md"
                ),
            )


async def async_setup_entry(hass: HomeAssistant, entry) -> bool:
    previous = hass.data.pop(DOMAIN, None)
    if previous is not None:
        previous.closed = True
    monitor = ReferenceMonitor(hass)
    hass.data[DOMAIN] = monitor
    entry.async_on_unload(
        async_track_time_interval(hass, monitor.refresh, REFRESH_INTERVAL)
    )
    if not await async_register_panel(hass):

        async def _register_panel(_event):
            await async_register_panel(hass)

        entry.async_on_unload(
            hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STARTED, _register_panel)
        )
    if hass.is_running:
        await monitor.refresh()
    else:

        async def started(_event):
            await monitor.refresh()

        entry.async_on_unload(
            hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STARTED, started)
        )
    return True


async def async_unload_entry(hass: HomeAssistant, entry) -> bool:
    monitor = hass.data.pop(DOMAIN, None)
    if monitor is not None:
        # A running check must not create issues after the entry was unloaded.
        monitor.closed = True
    async_unregister_panel(hass)
    for domain, issue_id in list(ir.async_get(hass).issues):
        if domain == DOMAIN and issue_id.startswith(ISSUE_PREFIX):
            ir.async_delete_issue(hass, DOMAIN, issue_id)
    return True
