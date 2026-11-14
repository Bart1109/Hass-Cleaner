"""English and German readable exports. Object names and identifiers are kept verbatim.

German reuses the English builders so both reports keep exactly the same
structure; every user-facing literal is passed through ``t()``. Dutch reports are
built in ``reporting`` and ``plans``.
"""

CATEGORIES = {
    "python_cache": "Generated Python bytecode; the matching source file is present.",
    "python_cache_without_source": "Python bytecode has no matching source file. Removing it may prevent the integration from loading.",
    "old_log": "Old diagnostic log; removing it discards diagnostic history.",
    "editor_artifact": "Editor or operating-system metadata.",
    "brand_cache": "Home Assistant icon cache; icons may need to be downloaded again.",
    "personal_media": "Personal recordings, snapshots or timelapses. Moving them may break links or remove access to personal content.",
    "integration_cache_candidate": "Cache-like path. Active use and automatic regeneration have not been established.",
    "temporary_or_backup": "Possible temporary or backup file. The name alone does not establish that it is unused.",
    "large_orphan_device_group": "Large group of devices without entities. Integration ownership and active use must be checked before removal.",
    "long_unavailable_entities": "Persistent availability problems. Check the integration, device and dependencies before removal.",
}

# German texts keyed by their English source. A missing entry falls back to
# English, so a partially translated report stays readable instead of switching
# to Dutch.
GERMAN = {
    "# Hass-Cleaner audit report": "# Hass-Cleaner Prüfbericht",
    "> AUDIT-ONLY: this report has not deleted, moved or changed anything.":
        "> NUR PRÜFUNG: Dieser Bericht hat nichts gelöscht, verschoben oder verändert.",
    "Started": "Gestartet",
    "Finished": "Beendet",
    "Files checked": "Geprüfte Dateien",
    "Files ignored by policy": "Durch Regeln ignorierte Dateien",
    "Suggested candidates": "Vorgeschlagene Kandidaten",
    "Review yourself": "Selbst prüfen",
    "Protected": "Geschützt",
    "## Cleanup categories": "## Bereinigungskategorien",
    "Category": "Kategorie",
    "Files": "Dateien",
    "Bytes": "Bytes",
    "Assessment": "Bewertung",
    "Guidance": "Hinweis",
    "Suggested candidate": "Vorgeschlagener Kandidat",
    "Restore moved files from quarantine. Review items require explicit acceptance of the content risk.":
        "Verschobene Dateien lassen sich aus der Quarantäne wiederherstellen. Elemente zur eigenen Prüfung erfordern eine ausdrückliche Bestätigung des Inhaltsrisikos.",
    "### System inventory — retained": "### Systeminventar — aufbewahrt",
    "The complete file inventory and original technical details are available in the JSON and CSV exports.":
        "Das vollständige Dateiinventar und die technischen Originaldaten stehen in den JSON- und CSV-Exporten bereit.",
    "## Home Assistant registry audit": "## Prüfung der Home-Assistant-Registry",
    "Metric": "Kennzahl",
    "Count": "Anzahl",
    "### Findings requiring review": "### Befunde mit Prüfbedarf",
    "Integration": "Integration",
    "Sample device IDs": "Beispiel-Geräte-IDs",
    "Type": "Typ",
    "Name": "Name",
    "ID": "ID",
    "Related ID": "Verknüpfte ID",
    "### Informational findings": "### Hinweisende Befunde",
    "unknown": "unbekannt",
    "### Bundles with warnings": "### Bündel mit Warnungen",
    "Domain": "Domäne",
    "Devices": "Geräte",
    "Entities": "Entitäten",
    "Warnings": "Warnungen",
    "Config entry": "Konfigurationseintrag",
    "### Entity review": "### Entitätenprüfung",
    "State": "Zustand",
    "Entity": "Entität",
    "Days": "Tage",
    "Device": "Gerät",
    "Area": "Bereich",
    "### Temporary and persistent signals": "### Vorübergehende und dauerhafte Signale",
    "Total": "Gesamt",
    "Needs attention": "Handlungsbedarf",
    "Monitored": "Beobachtet",
    "Longest observation (hours)": "Längste Beobachtung (Stunden)",
    "Tables show up to 100 findings/entities and 50 bundles/signal groups. JSON and CSV contain all results.":
        "Tabellen zeigen bis zu 100 Befunde/Entitäten und 50 Bündel/Signalgruppen. JSON und CSV enthalten alle Ergebnisse.",
    "Registry information could not be loaded. This does not mean the registry is empty; check the connection and technical report.":
        "Registry-Informationen konnten nicht geladen werden. Das bedeutet nicht, dass die Registry leer ist; prüfen Sie die Verbindung und den technischen Bericht.",
    "## Recovery and execution": "## Wiederherstellung und Ausführung",
    "- Only explicitly selected, non-protected files may enter quarantine after revalidation.":
        "- Nur ausdrücklich ausgewählte, nicht geschützte Dateien dürfen nach erneuter Prüfung in die Quarantäne.",
    "- Review personal or uncertain content and accept its risks before proceeding.":
        "- Prüfen Sie persönliche oder unklare Inhalte und bestätigen Sie deren Risiken, bevor Sie fortfahren.",
    "- A completed Home Assistant backup is strongly recommended; the user confirms their backup choice.":
        "- Ein abgeschlossenes Home-Assistant-Backup wird dringend empfohlen; die Backup-Entscheidung bestätigt der Benutzer selbst.",
    "- Restore files from quarantine. Existing target files are never overwritten.":
        "- Dateien lassen sich aus der Quarantäne wiederherstellen. Vorhandene Zieldateien werden nie überschrieben.",
    "- Registry changes may break dashboards and automations; integrations may recreate objects. Recovery requires a Home Assistant backup.":
        "- Registry-Änderungen können Dashboards und Automatisierungen beschädigen; Integrationen können Objekte neu anlegen. Für die Wiederherstellung ist ein Home-Assistant-Backup nötig.",
    "- Permanent file deletion requires an expired quarantine period and a separate confirmation.":
        "- Dauerhaftes Löschen von Dateien erfordert eine abgelaufene Quarantänefrist und eine gesonderte Bestätigung.",
    "# Hass-Cleaner cleanup preparation": "# Hass-Cleaner Bereinigungsvorbereitung",
    "> PREPARED CLEANUP: nothing has changed. Review the consequences and your backup choice before confirming execution.":
        "> VORBEREITETE BEREINIGUNG: Es wurde nichts verändert. Prüfen Sie die Folgen und Ihre Backup-Entscheidung, bevor Sie die Ausführung bestätigen.",
    "Plan ID": "Plan-ID",
    "Scan ID": "Scan-ID",
    "Executable actions": "Ausführbare Aktionen",
    "## Files": "## Dateien",
    "Path": "Pfad",
    "Action": "Aktion",
    "Quarantine": "Quarantäne",
    "Restore from quarantine; retention: %s days. Existing target files are never overwritten.":
        "Wiederherstellung aus der Quarantäne; Aufbewahrung: %s Tage. Vorhandene Zieldateien werden nie überschrieben.",
    "## Bundles": "## Bündel",
    "## Entities": "## Entitäten",
    "## Recovery and risks": "## Wiederherstellung und Risiken",
    "- Check official relationships, dashboards, scripts and automations before removal.":
        "- Prüfen Sie offizielle Beziehungen, Dashboards, Skripte und Automatisierungen vor dem Entfernen.",
    "- Removing registry objects has no individual undo. Integrations may recreate objects and references may break.":
        "- Das Entfernen von Registry-Objekten lässt sich nicht einzeln rückgängig machen. Integrationen können Objekte neu anlegen, Verweise können brechen.",
    "- Use a complete Home Assistant backup for registry recovery. Creating and checking one is strongly recommended.":
        "- Nutzen Sie ein vollständiges Home-Assistant-Backup zur Wiederherstellung der Registry. Ein solches Backup zu erstellen und zu prüfen wird dringend empfohlen.",
    "- Personal content may be lost or unavailable after moving it. Quarantine does not prove that content is unused.":
        "- Persönliche Inhalte können nach dem Verschieben verloren gehen oder nicht erreichbar sein. Quarantäne belegt nicht, dass Inhalte ungenutzt sind.",
    "- Protected system files remain excluded. Cancel if the consequences are unclear.":
        "- Geschützte Systemdateien bleiben ausgenommen. Brechen Sie ab, wenn die Folgen unklar sind.",
    # Reference section
    "## Reference checks": "## Referenzprüfung",
    "Snapshot": "Momentaufnahme",
    "No references found does not mean removal is safe. Dynamic templates, blueprints, custom cards and unreadable sources limit coverage. Device and area targets indicate potential indirect use.":
        "Keine Verweise gefunden heißt nicht, dass Entfernen sicher ist. Dynamische Templates, Blueprints, eigene Karten und nicht lesbare Quellen begrenzen die Abdeckung. Geräte- und Bereichsziele können auf indirekte Nutzung hinweisen.",
    "Source": "Quelle",
    "Source ID": "Quellen-ID",
    "Target type": "Zieltyp",
    "Target": "Ziel",
    "Location": "Pfad",
    "Missing": "Fehlt",
    "yes": "ja",
    "no": "nein",
    "Coverage": "Abdeckung",
    # CSV label values
    "Static reference; coverage is limited": "Statischer Verweis; die Abdeckung ist begrenzt.",
    "References may break after removal": "Verweise können nach dem Entfernen brechen.",
    "Review the source configuration": "Prüfen Sie die Konfiguration der Quelle.",
    # Category guidance
    "Generated Python bytecode; the matching source file is present.":
        "Erzeugter Python-Bytecode; die zugehörige Quelldatei ist vorhanden.",
    "Python bytecode has no matching source file. Removing it may prevent the integration from loading.":
        "Python-Bytecode ohne passende Quelldatei. Entfernen kann verhindern, dass die Integration lädt.",
    "Old diagnostic log; removing it discards diagnostic history.":
        "Altes Diagnoseprotokoll; Entfernen vernichtet die Diagnosehistorie.",
    "Editor or operating-system metadata.": "Metadaten von Editor oder Betriebssystem.",
    "Home Assistant icon cache; icons may need to be downloaded again.":
        "Icon-Cache von Home Assistant; Icons müssen eventuell erneut geladen werden.",
    "Personal recordings, snapshots or timelapses. Moving them may break links or remove access to personal content.":
        "Persönliche Aufnahmen, Snapshots oder Zeitraffer. Verschieben kann Verweise brechen oder den Zugriff auf persönliche Inhalte entfernen.",
    "Cache-like path. Active use and automatic regeneration have not been established.":
        "Pfad ähnelt einem Cache. Aktive Nutzung und automatische Neuerzeugung sind nicht belegt.",
    "Possible temporary or backup file. The name alone does not establish that it is unused.":
        "Mögliche temporäre Datei oder Sicherung. Der Name allein belegt nicht, dass sie ungenutzt ist.",
    "Large group of devices without entities. Integration ownership and active use must be checked before removal.":
        "Große Gruppe von Geräten ohne Entitäten. Zugehörigkeit zur Integration und aktive Nutzung müssen vor dem Entfernen geprüft werden.",
    "Persistent availability problems. Check the integration, device and dependencies before removal.":
        "Dauerhafte Erreichbarkeitsprobleme. Prüfen Sie Integration, Gerät und Abhängigkeiten vor dem Entfernen.",
    "Review ownership, dependencies and recovery before proceeding. Status alone does not prove that removal is safe.":
        "Prüfen Sie Zugehörigkeit, Abhängigkeiten und Wiederherstellung, bevor Sie fortfahren. Der Status allein belegt nicht, dass das Entfernen sicher ist.",
    "Protected system content; excluded from cleanup.":
        "Geschützter Systeminhalt; von der Bereinigung ausgenommen.",
}


def t(text, language="en"):
    """Return the export text for the selected language, falling back to English."""
    return GERMAN.get(text, text) if language == "de" else text


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, rows, language="en"):
    headers = [t(header, language) for header in headers]
    return ["", "| " + " | ".join(headers) + " |", "|" + "---|" * len(headers),
            *["| " + " | ".join(cell(value) for value in row) + " |" for row in rows], ""]


def guidance(category, risk="review", language="en"):
    if risk == "protected":
        return t("Protected system content; excluded from cleanup.", language)
    return t(CATEGORIES.get(category, "Review ownership, dependencies and recovery before proceeding. "
                                      "Status alone does not prove that removal is safe."), language)


def report_markdown(report, language="en"):
    scan = report["scan"]
    summary = report["review_summary"]
    lines = [t("# Hass-Cleaner audit report", language), "",
             t("> AUDIT-ONLY: this report has not deleted, moved or changed anything.", language), "",
             f"- {t('Scan ID', language)}: `{scan['id']}`",
             f"- {t('Started', language)}: {scan.get('started_at')}",
             f"- {t('Finished', language)}: {scan.get('finished_at')}",
             f"- {t('Files checked', language)}: {scan.get('visited_files', 0)}",
             f"- {t('Files ignored by policy', language)}: {scan.get('ignored_files', 0)}",
             f"- {t('Suggested candidates', language)}: {summary['proposed_for_cleanup_count']}",
             f"- {t('Review yourself', language)}: {summary['requires_manual_review_count']}",
             f"- {t('Protected', language)}: {summary['protected_count']}",
             "", t("## Cleanup categories", language), ""]
    cleanup = report.get("cleanup_guidance", {})
    recipes = cleanup.get("safe_recipes", []) + cleanup.get("investigation_recipes", [])
    lines += table(["Category", "Files", "Bytes", "Assessment", "Guidance"],
                   [(item["category"], item["file_count"], item["size_bytes"],
                     t("Suggested candidate", language) if item["kind"] == "safe" else t("Review yourself", language),
                     guidance(item["category"], language=language)) for item in recipes], language)
    lines += ["", t("Restore moved files from quarantine. Review items require explicit acceptance of the content risk.", language),
              "", t("### System inventory — retained", language), ""]
    lines += table(["Category", "Files", "Bytes"],
                   [(item["category"], item["count"], item["size_bytes"]) for item in cleanup.get("inventory", [])], language)
    lines += ["", t("The complete file inventory and original technical details are available in the JSON and CSV exports.", language),
              "", t("## Home Assistant registry audit", language), ""]
    registry = scan.get("registry_audit", {})
    lines += [f"{t('Status', language)}: {cell(registry.get('status', 'unavailable'))}"]
    if registry.get("status") == "completed":
        lines += table(["Metric", "Count"], sorted(registry.get("summary", {}).items()), language)
        lines += ["", t("### Findings requiring review", language), ""]
        anomalies = registry.get("anomalies", [])
        lines += table(["Category", "Integration", "Sample device IDs", "Guidance"],
                       [(item.get("category", ""), item.get("domain", ""), ", ".join(item.get("sample_device_ids", [])),
                         guidance(item.get("category", ""), language=language)) for item in anomalies[:100]], language)
        findings = registry.get("findings", [])
        review = [item for item in findings if item.get("severity") == "review"]
        lines += table(["Type", "Name", "ID", "Category", "Related ID"],
                       [(item.get("subject_type", ""), item.get("name", ""), item.get("subject_id", ""),
                         item.get("category", ""), item.get("related_id", "")) for item in review[:100]], language)
        lines += ["", t("### Informational findings", language), ""]
        counts = {}
        for item in findings:
            if item.get("severity") == "info":
                key = item.get("category", "unknown")
                counts[key] = counts.get(key, 0) + 1
        lines += table(["Category", "Count"], sorted(counts.items()), language)
        lines += ["", t("### Bundles with warnings", language), ""]
        bundles = [item for item in registry.get("bundles", []) if item.get("review_count", 0)]
        lines += table(["Integration", "Domain", "Devices", "Entities", "Warnings", "Config entry"],
                       [(item["title"], item["domain"], len(item["devices"]), len(item["entities"]),
                         item["review_count"], item["config_entry_id"]) for item in bundles[:50]], language)
        workspace = registry.get("entity_workspace", {})
        lines += ["", t("### Entity review", language), ""]
        lines += table(["State", "Count"], sorted(workspace.get("summary", {}).get("by_status", {}).items()), language)
        entities = [item for item in workspace.get("items", []) if item.get("selectable_for_plan")]
        lines += table(["Entity", "State", "Days", "Integration", "Device", "Area"],
                       [(item["entity_id"], item.get("status", ""), item.get("duration_days", 0),
                         item.get("integration", ""), item.get("device_name", ""), item.get("area_name", ""))
                        for item in entities[:100]], language)
        lines += ["", t("### Temporary and persistent signals", language), ""]
        lines += table(["Integration", "Total", "Needs attention", "Monitored", "Longest observation (hours)"],
                       [(item["integration"], item.get("total", 0), item.get("attention", 0), item.get("watch", 0),
                         round(float(item.get("max_duration_seconds", 0)) / 3600, 1))
                        for item in workspace.get("signal_groups", [])[:50]], language)
        lines += ["", t("Tables show up to 100 findings/entities and 50 bundles/signal groups. "
                        "JSON and CSV contain all results.", language)]
    else:
        lines += [t("Registry information could not be loaded. This does not mean the registry is empty; "
                    "check the connection and technical report.", language)]
    lines += ["", t("## Recovery and execution", language), "",
              t("- Only explicitly selected, non-protected files may enter quarantine after revalidation.", language),
              t("- Review personal or uncertain content and accept its risks before proceeding.", language),
              t("- A completed Home Assistant backup is strongly recommended; the user confirms their backup choice.", language),
              t("- Restore files from quarantine. Existing target files are never overwritten.", language),
              t("- Registry changes may break dashboards and automations; integrations may recreate objects. "
                "Recovery requires a Home Assistant backup.", language),
              t("- Permanent file deletion requires an expired quarantine period and a separate confirmation.", language), ""]
    from .references import markdown_lines
    lines += markdown_lines(registry.get("references", {}), language)
    return "\n".join(lines)


def plan_markdown(plan, language="en"):
    summary = plan["summary"]
    lines = [t("# Hass-Cleaner cleanup preparation", language), "",
             t("> PREPARED CLEANUP: nothing has changed. Review the consequences and your backup choice "
               "before confirming execution.", language), "",
             f"- {t('Plan ID', language)}: `{plan['id']}`", f"- {t('Scan ID', language)}: `{plan['scan_id']}`",
             f"- {t('Files', language)}: {summary['file_count']}", f"- {t('Entities', language)}: {summary['entity_count']}",
             f"- {t('Devices', language)}: {summary.get('device_count', 0)}",
             f"- {t('Executable actions', language)}: {summary['executable_actions']}",
             "", t("## Files", language), ""]
    lines += table(["Path", "Bytes", "Assessment", "Action", "Guidance"],
                   [(item["path"], item["before"]["size_bytes"], item.get("risk", "review"), t("Quarantine", language),
                     guidance(item["before"]["category"], item.get("risk", "review"), language)) for item in plan["files"]],
                   language)
    lines += ["", t("Restore from quarantine; retention: %s days. Existing target files are never overwritten.", language)
              % plan["settings"]["retention_days"],
              "", t("## Bundles", language), ""]
    lines += table(["Integration", "Domain", "Devices", "Entities"],
                   [(item["title"], item["domain"], item["before"]["device_count"], item["before"]["entity_count"])
                    for item in plan["bundles"]], language)
    lines += ["", t("## Entities", language), ""]
    lines += table(["Entity", "State", "Days", "Integration", "Device"],
                   [(item["entity_id"], item.get("status", ""), item.get("duration_days", 0),
                     item.get("integration", ""), item.get("device_name", "")) for item in plan["entities"]], language)
    lines += ["", t("## Recovery and risks", language), "",
              t("- Check official relationships, dashboards, scripts and automations before removal.", language),
              t("- Removing registry objects has no individual undo. Integrations may recreate objects and "
                "references may break.", language),
              t("- Use a complete Home Assistant backup for registry recovery. Creating and checking one is "
                "strongly recommended.", language),
              t("- Personal content may be lost or unavailable after moving it. Quarantine does not prove that "
                "content is unused.", language),
              t("- Protected system files remain excluded. Cancel if the consequences are unclear.", language), ""]
    from .references import markdown_lines
    lines += markdown_lines(plan.get("reference_review", {}), language)
    return "\n".join(lines)
