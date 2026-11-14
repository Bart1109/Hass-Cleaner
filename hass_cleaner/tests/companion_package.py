"""Load companion modules as part of their package.

The companion's modules share constants through relative imports, so loading a
single file with ``spec_from_file_location`` no longer works. A synthetic
package entry keeps the relative imports working without importing the Home
Assistant integration itself.
"""
from __future__ import annotations

import importlib
import sys
import types
from pathlib import Path

COMPANION = Path(__file__).resolve().parents[2] / "custom_components" / "hass_cleaner"
PACKAGE = "companion_package"


def load(module: str):
    """Import ``module`` from the companion directory as ``companion_package.<module>``."""
    if PACKAGE not in sys.modules:
        holder = types.ModuleType(PACKAGE)
        holder.__path__ = [str(COMPANION)]
        sys.modules[PACKAGE] = holder
    return importlib.import_module(f"{PACKAGE}.{module}")
