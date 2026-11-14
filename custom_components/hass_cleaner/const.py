"""Konstanten der Integration Hass-Cleaner Companion.

Alle Zahlenwerte, die das Verhalten der Prüfung beeinflussen, liegen zentral
hier, damit sie sich an einer Stelle nachvollziehen und anpassen lassen.
"""
from __future__ import annotations

from datetime import timedelta

DOMAIN = "hass_cleaner"

# Aufbau der Berichte über die WebSocket-Schnittstelle und die Diagnose.
SCHEMA_VERSION = 1

# Präfix der Reparaturhinweise ("reference_<hash>"). Dient dazu, ausschließlich
# die eigenen Hinweise zu erkennen und fremde nie anzufassen.
ISSUE_PREFIX = "reference_"

# Intervall der automatischen Hintergrundprüfung.
REFRESH_INTERVAL = timedelta(minutes=5)

# Schutzgrenzen gegen pathologische oder feindliche Konfigurationen.
MAX_WALK_NODES = 100_000
MAX_WALK_DEPTH = 60
MAX_TEMPLATE_LENGTH = 65_536

# Höchstzahl der Verweise, die in einem Reparaturhinweis aufgelistet werden.
MAX_REPAIR_ITEMS = 30

# Dienst zum sofortigen Auslösen einer Prüfung.
SERVICE_REFRESH = "refresh"
