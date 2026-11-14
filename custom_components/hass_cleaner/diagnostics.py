"""Diagnose-Daten für den Support.

Enthalten bewusst nur Zähler, Statusangaben und Quellen-Metadaten: keine
Konfigurationswerte, keine Templates und keine Referenzziele.
"""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict:
    """Bericht ohne vertrauliche Inhalte für „Diagnose herunterladen“."""
    monitor = hass.data.get(DOMAIN)
    report = getattr(monitor, "report", None)
    if not report:
        return {"status": "unavailable", "reason": "no_report"}

    return {
        "schema_version": report.get("schema_version"),
        "status": report.get("status"),
        "checked_at": report.get("checked_at"),
        "summary": report.get("summary", {}),
        "stage": report.get("stage"),
        "reason": report.get("reason"),
        "sources": [
            {
                "id": source.get("id"),
                "kind": source.get("kind"),
                "status": source.get("status"),
                "dynamic": source.get("dynamic"),
                "custom_cards": source.get("custom_cards"),
                "error": source.get("error"),
            }
            for source in report.get("sources", [])
        ],
        "limitations": report.get("limitations", []),
    }
