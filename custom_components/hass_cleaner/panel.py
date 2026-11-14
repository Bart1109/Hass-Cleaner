"""Sidebar panel with the missing references of the last report.

The panel is a read-only view: it calls the existing WebSocket command
``hass_cleaner/references`` and renders the result. No configuration is read
from disk here and nothing is changed.
"""
from __future__ import annotations

import inspect
import logging
from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# The app registers its own ingress panel named "Hass-Cleaner"; a second entry
# with the same name would be indistinguishable in the sidebar. The companion
# panel therefore carries the name of what it shows.
PANEL_URL_PATH = "hass-cleaner"
PANEL_TITLE = "Referenzprüfung"
PANEL_ICON = "mdi:link-variant-off"
PANEL_COMPONENT = "hass-cleaner-panel"
PANEL_STATIC_URL = f"/{DOMAIN}_panel"
PANEL_ASSET = "hass-cleaner-panel.js"

# The static path is registered once per Home Assistant run: the HTTP layer
# keeps it across config entry reloads.
DATA_STATIC_REGISTERED = f"{DOMAIN}_panel_static_registered"
DATA_PANEL_REGISTERED = f"{DOMAIN}_panel_registered"


def asset_directory() -> Path:
    """Directory that is served to the frontend."""
    return Path(__file__).parent / "www"


def panel_supported(hass: HomeAssistant) -> bool:
    """The panel needs the HTTP layer and the frontend component."""
    return hass.http is not None and "frontend" in hass.config.components


async def async_register_panel(hass: HomeAssistant) -> bool:
    """Register the static asset and the sidebar panel. Idempotent."""
    if hass.data.get(DATA_PANEL_REGISTERED):
        return True
    if not panel_supported(hass):
        _LOGGER.debug("Sidebar panel skipped: http or frontend is not ready")
        return False
    directory = asset_directory()
    if not (directory / PANEL_ASSET).is_file():
        _LOGGER.warning("Sidebar panel skipped: asset %s is missing", PANEL_ASSET)
        return False
    if not hass.data.get(DATA_STATIC_REGISTERED):
        await hass.http.async_register_static_paths(
            [StaticPathConfig(PANEL_STATIC_URL, str(directory), True)]
        )
        hass.data[DATA_STATIC_REGISTERED] = True
    # Home Assistant made this helper a coroutine in recent versions; older
    # releases return None. Support both instead of pinning the caller.
    result = panel_custom.async_register_panel(
        hass,
        frontend_url_path=PANEL_URL_PATH,
        webcomponent_name=PANEL_COMPONENT,
        sidebar_title=PANEL_TITLE,
        sidebar_icon=PANEL_ICON,
        module_url=f"{PANEL_STATIC_URL}/{PANEL_ASSET}",
        embed_iframe=False,
        require_admin=True,
        config={},
    )
    if inspect.isawaitable(result):
        await result
    hass.data[DATA_PANEL_REGISTERED] = True
    return True


@callback
def async_unregister_panel(hass: HomeAssistant) -> None:
    """Remove the panel when the config entry is unloaded."""
    if not hass.data.pop(DATA_PANEL_REGISTERED, None):
        return
    frontend.async_remove_panel(hass, PANEL_URL_PATH, warn_if_unknown=False)
