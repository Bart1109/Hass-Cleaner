# Referenzprüfung und native Reparaturhinweise

Referenzprüfungen gibt es seit 1.1.0, HACS-Unterstützung seit 1.1.1. Version 1.2.1 ist veröffentlicht; dieser Stand bereitet 1.2.2 mit eigenem Container-Image vor. Lege eine vollständige Sicherung an und teste zuerst an einer unkritischen Installation. Dieses Merkmal erreicht nicht den Funktionsumfang von Spook und belegt nicht, dass irgendetwas gefahrlos gelöscht werden darf.

## Zwei Bausteine

- **Hass-Cleaner-App:** Prüfung von Speicher und Register, Vorbereitung und Ausführung der Bereinigung. Zeigt eine Referenzaufnahme, die bei jedem neuen Scan erhoben wird.
- **Integration Hass-Cleaner Companion:** läuft im Home-Assistant-Core, liest die geladene Konfiguration und pflegt native Reparaturhinweise. Prüft nach dem Start und alle fünf Minuten, auch wenn die App gestoppt ist. Ein Scan in der App fordert eine frische Prüfung an.

Der Companion ändert nie Automatisierungen, Skripte, Dashboards, Entitäten oder Geräte. Seine einzigen Schreibzugriffe auf Home Assistant sind die Metadaten seiner eigenen Reparaturhinweise. Er führt keine Templates aus und ruft keine Aktionen auf, die er findet.

## Einrichtung

### Über HACS (empfohlen)

Voraussetzung ist ein eingerichtetes und konfiguriertes HACS sowie Home Assistant **2026.9.0 oder neuer**. Dies ist ein benutzerdefiniertes Repository, kein Eintrag im Standardkatalog von HACS.

1. Vollständige Sicherung anlegen. **HACS → Menü (⋮) → Benutzerdefinierte Repositories** öffnen.
2. `https://github.com/Bart1109/Hass-Cleaner` mit Typ **Integration** hinzufügen.
3. **Hass-Cleaner Companion** in HACS suchen und herunterladen. Eine veröffentlichte Version wählen, die zur App-Version passt; keine älteren Releases vor dem Companion (also vor 1.1.0) auswählen.
4. **Home Assistant Core** neu starten, nicht nur die App.
5. **Einstellungen → Geräte & Dienste → Integration hinzufügen** öffnen und nach **Hass-Cleaner Companion** suchen. Den Einrichtungsdialog bestätigen. Es sind keine Token einzugeben.
6. Hass-Cleaner auf die passende App-Version starten oder aktualisieren und **Neuer Scan** ausführen. **Entitäten → Referenzprüfung** öffnen.

HACS verwaltet nur `custom_components/hass_cleaner`, nicht den App-Container. Companion-Aktualisierungen kommen über HACS, App-Aktualisierungen über den App-Store, danach Core neu starten. HACS richtet die Integration nicht selbst ein.

**Schon per ZIP installiert?** Zuerst sichern, dann dieselbe Integration über HACS herunterladen und Core neu starten. Den vorhandenen Integrationseintrag behalten; nicht entfernen und neu hinzufügen und keinen zweiten verschachtelten Ordner anlegen. HACS kann lokale Änderungen an den Integrationsdateien ersetzen.

**Hinweis zur Veröffentlichung:** HACS-Unterstützung gibt es ab Release 1.1.1. Weitere Änderungen brauchen ein neues Release; vorhandene Tags werden durch einen Merge nicht aktualisiert. Einen bestehenden Release-Tag nicht verschieben. Jede Aktualisierung in einer echten Home-Assistant-Installation prüfen.

### Von Hand ohne HACS

Eine Companion-Version verwenden, die zur App passt. `custom_components/hass_cleaner` in das Konfigurationsverzeichnis von Home Assistant kopieren, sodass `/config/custom_components/hass_cleaner/manifest.json` entsteht, oder das ZIP unten verwenden. Core neu starten und die Integration wie oben beschrieben hinzufügen. Nicht in den App-Container kopieren.

Der Laufzeitadapter des Companion zielt auf die APIs von Home Assistant 2026.9. Ältere Versionen sind nicht geprüft. Nur die App zu installieren oder zu aktualisieren installiert oder aktualisiert den Companion nicht.

Für ein lokal installierbares ZIP im Wurzelverzeichnis des Repositories `python tools/package_companion.py` ausführen. Das ZIP in das Konfigurationsverzeichnis von Home Assistant entpacken; es enthält bereits den Pfad `custom_components/hass_cleaner`. Eine vorhandene Companion-Installation vor dem Ersetzen prüfen und sichern.

## Was geprüft wird

### Umfang von Teil 1

Alle sieben Quellenfamilien sind vertreten: Automatisierungen, Skripte, Dashboards, Szenen, Gruppen, Helfer/Templates sowie Energie- und Statistik-Konfiguration. Das ist statische Abhängigkeitsprüfung, keine vollständige Auswertung jeder benutzerdefinierten Integration oder jedes berechneten Templates. Ein Abnahmetest in einer echten Home-Assistant-Installation bleibt Voraussetzung für die Veröffentlichung.

- **Szenen:** Mitglieder zur Laufzeit, auch dynamisch erzeugte Szenen. Eine von einer Integration bereitgestellte Szene ohne offengelegte Mitglieder gilt ausdrücklich als nicht verfügbar.
- **Gruppen:** Altgruppen zur Laufzeit, konfigurierte Gruppen-Helfer und YAML-Gruppendefinitionen (auch Kurzschreibweise als Liste).
- **Helfer/Templates:** Daten und Optionen der Konfigurationseinträge sowie relevante YAML-Abschnitte und -Plattformen, wobei Includes und Packages von Home Assistant aufgelöst werden. Von Optionen überlagerte Datenwerte bleiben ausgenommen. Die unterstützten Domains stehen in `custom_components/hass_cleaner/sources.py`: group, template, min/max, integral, utility meter, statistics, derivative, threshold, filter, history statistics, generic thermostat/hygrostat, switch-as-X, time-of-day, Eingabe-Helfer, counter, timer, schedule, random, trend und Bayesian-Helfer. Benutzerdefinierte Helfer-Domains werden nicht automatisch ausgewertet.
- **Energie/Statistiken:** Energieeinstellungen, Preis-Entitäten, Statistik-Dashboardkarten und ausdrückliche Entitätsfilter des Recorders. Statistiken werden gegen die Recorder-Metadaten geprüft (einschließlich externer Statistiken), nicht gegen den aktuellen Entitätszustand. Historische Statistiken können gültig bleiben, nachdem die Entität verschwunden ist. Ist der Recorder nicht lesbar, gilt die Prüfung als unbekannt und es entsteht kein Reparaturhinweis für eine fehlende Statistik.
- YAML-Quellen für Helfer und Templates stellen die **aktuell gespeicherte Konfiguration** dar, die bis zum Neuladen von der geladenen Konfiguration abweichen kann. UI-Helferquellen nennen die IDs ihrer Konfigurationseinträge; YAML-Pfade bezeichnen Positionen in der Konfiguration, nicht Zeilennummern in der Quelldatei.
- Entitätsdetails zeigen die Anzahl passender Quellkonfigurationen je Kategorie. Mehrfache Verweise in einer Quelle erhöhen deren Zähler nicht. Dieselbe Entität kann sowohl Verweise auf eine vorhandene Entität als auch auf aufbewahrte Statistiken haben.

| Quelle oder Ziel | Abdeckung |
|---|---|
| Geladene Automatisierungen und Skripte | Statische Ziele für Entität, Gerät, Bereich und Dienst/Aktion, auch verschachtelte Aktionen und Bedingungen |
| Geräteautomatisierungen | Bekannte UUIDs des Entitätsregisters werden zu Entitäts-IDs aufgelöst; fehlende UUIDs werden gemeldet |
| Storage- und YAML-Dashboards | Konfiguration, die Home Assistant lädt, einschließlich üblicher Entitätslisten und Zielfelder |
| Templates | Literale Aufrufe wie `states('sensor.temperature')` und `states.sensor.temperature` werden erkannt, auch in eigenständigen Template-Definitionen; sie werden nie ausgeführt |
| Vorhandene Entitäten | Registerentitäten plus Laufzeitzustände; deaktivierte Entitäten gelten nicht allein deshalb als fehlend, weil sie keinen Zustand haben |
| Fehlende Aktionen | Vergleich mit den nach dem Start registrierten Diensten/Aktionen von Home Assistant |

Jedes Ergebnis enthält Quellenname und -ID, Zieltyp und -ID sowie einen Pfad wie `$.actions[0].target.entity_id`. Feldindizes beginnen bei **0**. Pfade bezeichnen Positionen in der geladenen Konfiguration, nicht Zeilennummern in YAML-Dateien. Die App unterstützt Seitennavigation, Filter „alle/fehlend“, Abdeckung je Quelle, Abhängigkeiten von Entitäten und Bündeln sowie Exporte als JSON, CSV und Markdown.

## Abdeckung und Aussagekraft

- `completed` bedeutet, dass die unterstützte statische Prüfung abgeschlossen wurde, **nicht** dass die gesamte Installation erschöpfend geprüft wurde.
- Dynamische oder berechnete Templates, Blueprint-Erweiterung, benutzerdefinierte Karten, Dashboard-Strategien und nicht lesbare Quellen begrenzen die Abdeckung. Literale Verweise können trotzdem gemeldet werden, die Quelle gilt dann aber als teilweise geprüft.
- Nicht abgedeckt: beliebige Python-Logik und Logik benutzerdefinierter Integrationen, nicht gelistete Helfer-Domains, jede YAML-Integration, indirekte Semantik von Skripten und Templates sowie beliebige Eigenschaften benutzerdefinierter Karten. Ziele über Label oder Etage sowie Platzhalter- und Domainfilter des Recorders kennzeichnen eine begrenzte Abdeckung. Dies ist kein allgemeiner Home-Assistant-Interpreter.
- Automatisierungen, Skripte und Laufzeitmitgliedschaften nutzen die geladene Konfiguration; YAML-Helfer und -Templates die gespeicherte. Ein Neuladen ändert das Verhalten erst nach der Prüfung. Manche Quellen, die nie geladen wurden, sind unter Umständen nicht auffindbar; prüfe deshalb auch die Konfigurationsfehler von Home Assistant selbst.
- Eine registrierte, aber nicht verfügbare Entität ist **nicht fehlend**. Eine Aktion, die während eines Neuladens der Integration kurzzeitig verschwindet, kann einen vorübergehenden Hinweis erzeugen; prüfe erneut, nachdem sich die Integration erholt hat.
- Ziele über Gerät und Bereich können ausgewählte Entitäten indirekt betreffen. Sie werden als mögliche Nutzung gezeigt, nicht als Beweis, dass jede ausgewählte Entität tatsächlich betroffen ist.
- Null Funde belegen nie, dass Entfernen sicher ist. Sicherungswahl und ausdrückliche Risikoakzeptanz bleiben im normalen Bereinigungsablauf erforderlich.

## Ablauf mit Reparaturhinweisen

**Einstellungen → System → Reparaturen** öffnen. Der Companion fasst fehlende Ziele je Quelle zu einem stabilen Hinweis zusammen, mit bis zu 30 Beispielpfaden. Die App und die Exporte enthalten alle Funde.

1. Die genannte Automatisierung, das Skript oder das Dashboard öffnen.
2. Den Verweis korrigieren, das fehlende Ziel wiederherstellen oder den Verweis entfernen, wenn er nicht mehr gebraucht wird.
3. YAML-Änderungen bei Bedarf neu laden. Bis zu fünf Minuten warten oder einen neuen Scan in der App anfordern.
4. Der Hinweis verschwindet, sobald die Quelle vollständig prüfbar ist und keine fehlenden Verweise mehr übrig sind. Auch das nachgewiesene Entfernen einer Quelle löst ihren Hinweis nach vollständiger Prüfung auf.

Eine automatische Schaltfläche **Beheben** gibt es bewusst nicht. Absichtlich fehlende Verweise werden mit den üblichen Bedienelementen der Reparaturen ignoriert. Wiederholte Prüfungen behalten dieselbe Hinweisidentität und setzen den Status „ignoriert“ nicht zurück. Wie Home Assistant Ausblendungen über seine eigenen Aktualisierungen hinweg behandelt, liegt bei Home Assistant; Entfernen oder Neuladen des Companion entfernt dessen Hinweise und kann die Ausblendhistorie zurücksetzen.

Eine nicht lesbare oder nur teilweise prüfbare Quelle löst ihren bisherigen Hinweis nicht fälschlich auf. Ein zuvor gemeldeter Hinweis kann deshalb bestehen bleiben, bis die Quelle vollständig lesbar ist oder die restlichen fehlenden Verweise unabhängig davon behoben sind und die Quelle vollständig geprüft werden kann. In der App erscheint das als begrenzte Abdeckung.

## Vor dem Aufräumen des Registers

Die Vorbereitung enthält die direkten Verweise der ausgewählten Objekte und mögliche Abhängigkeiten über Gerät und Bereich, einschließlich des Scanzeitpunkts. Prüfe diese vor der Bestätigung. War der Companion während der Vorbereitung verfügbar, prüft die App die Verweise und aktuellen Registerzuordnungen vor dem ersten Entfernen erneut. Eine geänderte Abhängigkeit oder geänderte Quellenabdeckung erfordert einen neuen Scan und eine neue Prüfung. Eine nicht verfügbare Nachprüfung stoppt die Ausführung, ohne das Register zu verändern.

War der Companion zum Zeitpunkt der Vorbereitung nicht verfügbar, zeigt die App diese Einschränkung ausdrücklich und behält die bestehende, vom Nutzer gesteuerte Bereinigungswahl. Die Prüfung ist keine atomare Transaktion von Home Assistant: Konfiguration während der Ausführung nicht bearbeiten und nicht neu laden. Für das Entfernen aus dem Register gibt es kein individuelles Rückgängig; die Wiederherstellung kann eine vollständige Sicherung erfordern.

## Datenschutz und Fehlersuche

Den Companion verlassen nur Quellennamen und -IDs, Ziel-IDs, Konfigurationspfade, Abdeckung und Prüfzeitpunkt. Vollständige Konfigurationen, Dienstnutzlasten und Template-Inhalte werden nicht übertragen. IDs und Namen können dennoch persönliche Informationen preisgeben: Berichte vor dem Teilen prüfen.

Der WebSocket-Befehl `hass_cleaner/references` ist ausschließlich für Administratoren. Die App nutzt ihre normal konfigurierte Supervisor-Authentifizierung. Es sind keine Browser-Token und keine neuen Secrets nötig. Wird die Authentifizierung verweigert oder fehlt der Companion, läuft der normale Register- und Dateiscan weiter und die Referenzprüfung zeigt **nicht verfügbar**, niemals fälschlich „alles in Ordnung“.

Bei „nicht verfügbar“: Installationspfad prüfen, Core neu starten, die Companion-Integration hinzufügen, die Core-Protokolle ansehen und einen neuen Scan in der App ausführen. Automatisch erzeugte Dashboards ohne lesbare Konfiguration können eine begrenzte Abdeckung zeigen. Reparaturhinweise anderer Integrationen (auch von Spook) werden weder gelöscht noch verändert. Beide parallel zu betreiben kann zu überlappenden Warnungen führen.

## Prüfung vor der Veröffentlichung

Lokale automatisierte Tests decken den Analyzer, die WebSocket-Brücke, die Verträge des HA-Adapters, den Lebenszyklus der Reparaturhinweise, Seitennavigation, Exporte und die erneute Prüfung vor der Bereinigung ab. Vertragstests bilden die Schnittstellen von Home Assistant nach; sie belegen keine erfolgreiche Installation im Betrieb.

Auf einer entbehrlichen Home-Assistant-Instanz 2026.9:

1. Den Companion installieren und einrichten und einen sauberen Start ohne wiederkehrende Fehler prüfen.
2. Eine Testautomatisierung, ein Testskript und ein manuelles Dashboard anlegen, die auf eine absichtlich nicht vorhandene Entität verweisen. Genaue Pfade, drei Quellenhinweise, Ergebnisse in der App sowie englischen, niederländischen oder deutschen Text prüfen.
3. Einen Verweis korrigieren und neu laden. Prüfen, dass sein Hinweis verschwindet. Einen anderen Hinweis ignorieren und prüfen, dass wiederholte Prüfungen die Wahl beibehalten.
4. YAML-Dashboards, eine deaktivierte registrierte Entität, einen Gerätetrigger über eine Register-UUID und ein dynamisches Template prüfen. Bestätigen, dass deaktivierte Entitäten nicht als fehlend gelten und die dynamische Abdeckung als begrenzt ausgewiesen wird.
5. Ein Testdashboard vorübergehend unlesbar machen. Bestätigen, dass sein bisheriger Hinweis bleibt und die App begrenzte Abdeckung zeigt.
6. Das Aufräumen des Registers nur für entbehrliche Testentitäten vorbereiten, eine Abhängigkeit ändern und prüfen, dass die Ausführung vor jedem Entfernen stoppt.
7. Core neu starten, den Companion neu laden und entfernen und prüfen, dass geplante Arbeit und die Zuordnung der Hinweise korrekt bleiben.
8. Den Companion stoppen und entfernen und bestätigen, dass die App weiter scannt und die Referenzprüfung ausdrücklich als nicht verfügbar ausweist.
9. Entbehrliche Verweise in Szenen, Gruppen, Helfern und Templates anlegen. Sowohl über die Oberfläche erzeugte Helfer als auch YAML-Packages prüfen; bestätigen, dass eine Altgruppe nur einmal erscheint und das Ändern einer Helfer-Option die alte Abhängigkeit entfernt.
10. Eine externe Statistik und eine aufbewahrte Statistik prüfen, deren Entität nicht mehr existiert. Sie dürfen keine Reparaturhinweise für fehlende Entitäten erzeugen. Eine tatsächlich fehlende Statistik soll einen Fund ergeben; ein nicht verfügbarer Recorder soll stattdessen eine unbekannte Prüfung anzeigen.

## Seitenleisten-Panel

Der Companion fügt der Seitenleiste ein schreibgeschütztes Panel **Referenzprüfung** hinzu (`mdi:link-variant-off`). Es zeigt die Verweise des letzten Berichts — Quelle, Quellen-ID, Zieltyp, Ziel, Pfad und ob das Ziel fehlt oder seine Prüfung nicht verfügbar ist — mit Filtern und einer Abdeckungsliste. Das Panel ruft nur den vorhandenen WebSocket-Befehl `hass_cleaner/references` auf; es liest nichts von der Festplatte und ändert nichts.

Das Panel braucht die HTTP-Schicht und das Frontend. Das Manifest deklariert dafür `websocket_api`, `http`, `frontend` und `panel_custom` als Abhängigkeiten, damit Home Assistant Frontend und Panel-Helfer vor der Registrierung bereitstehen; wird das Frontend erst später bereit, wird die Registrierung über `EVENT_HOMEASSISTANT_STARTED` nachgeholt. Das Panel ist auf Administratoren beschränkt und wird beim Entladen des Konfigurationseintrags entfernt. Sein Name unterscheidet sich bewusst vom eigenen Seitenleisteneintrag der App „Hass-Cleaner“, damit beide unterscheidbar bleiben.

---

## English

Reference checks were introduced in 1.1.0; HACS support shipped in 1.1.1. Version 1.2.1 is released; this checkout prepares 1.2.2 with its own container image. Keep a complete backup and test on a non-critical installation first. This feature does not provide Spook feature parity or prove that anything is safe to delete.

### Two components

- **Hass-Cleaner app:** storage and registry review, cleanup preparation and execution. Displays a reference snapshot collected during each new scan.
- **Hass-Cleaner Companion integration:** runs inside Home Assistant Core, reads loaded configuration and maintains native Repairs. Checks after startup and every five minutes, including while the app is stopped. An app scan requests a fresh check.

The companion never changes automations, scripts, dashboards, entities or devices. Its only Home Assistant writes are its own Repairs issue metadata. It never executes templates or calls the actions it finds.

### Installation

#### HACS (recommended)

Requires HACS to be installed and configured, and Home Assistant **2026.9.0 or newer**. This is a custom repository, not a listing in the default HACS catalog.

1. Make a complete backup. Open **HACS → menu (⋮) → Custom repositories**.
2. Add `https://github.com/Bart1109/Hass-Cleaner` with type **Integration**.
3. Find **Hass-Cleaner Companion** in HACS and download it. Choose a published release matching your app version; do not select older releases that predate the companion (before 1.1.0).
4. Restart **Home Assistant Core**, not just the app.
5. Open **Settings → Devices & services → Add integration** and search for **Hass-Cleaner Companion**. Confirm the setup screen. There are no tokens to enter.
6. Start/update Hass-Cleaner to the matching app version and run **New scan**. Open **Entities → Reference checks**.

HACS manages only `custom_components/hass_cleaner`, not the app container. Install companion updates through HACS and app updates through the App Store, then restart Core. HACS does not automatically configure the integration.

**Already installed from ZIP?** Back up first, then download the same integration through HACS and restart Core. Keep the existing integration entry; do not remove/re-add it or create a second nested folder. HACS may replace local edits to the integration files.

**Publishing note:** HACS support is available from release 1.1.1. Future changes need a new release; existing tags are not updated by a merge. Do not move an existing release tag. Validate each update in a real Home Assistant installation.

#### Manual installation (without HACS)

Use a companion release matching the app. Copy `custom_components/hass_cleaner` into your Home Assistant configuration directory, resulting in `/config/custom_components/hass_cleaner/manifest.json`, or use the ZIP below. Restart Core and add the integration as described above. Do not copy it into the app container.

The companion runtime adapter targets the Home Assistant 2026.9 APIs. Older versions have not been verified. Installing/updating the app alone does not install/update the companion.

For a local installable ZIP, run `python tools/package_companion.py` from the repository root. Extract the ZIP into the Home Assistant configuration directory; it already contains the `custom_components/hass_cleaner` path. Review and back up any existing companion installation before replacing its files.

### What gets checked

#### Part 1 implementation scope

All seven source families are now represented: automations, scripts, dashboards, scenes, groups, helpers/templates and energy/statistics configuration. This is static dependency checking, not complete interpretation of every custom integration or computed template. Live Home Assistant acceptance testing remains a release requirement.

- **Scenes:** runtime membership, including dynamically created scenes. An integration-provided scene without exposed members is explicitly unavailable.
- **Groups:** runtime legacy groups, configured group helpers and YAML group definitions (including list shorthand).
- **Helpers/templates:** config-entry data/options and relevant YAML sections/platforms, with includes/packages resolved by Home Assistant. Options-shadowed data values are excluded. Supported domains are listed in `custom_components/hass_cleaner/sources.py`: group, template, min/max, integral, utility meter, statistics, derivative, threshold, filter, history statistics, generic thermostat/hygrostat, switch-as-X, time-of-day, input helpers, counter, timer, schedule, random, trend and Bayesian helpers. Custom helper domains are not automatically interpreted.
- **Energy/statistics:** energy preferences, price entities, statistics dashboard cards and explicit Recorder entity filters. Statistics are checked against Recorder metadata (including external statistics), not against live entity states. Historical statistics can remain valid after the entity disappears. If Recorder cannot be read, verification is unknown and no missing-statistic Repair is created.
- YAML helper/template sources represent the **current saved configuration**, which can differ from loaded configuration until reloaded. UI helper sources identify their configuration-entry IDs; YAML paths identify configuration positions rather than source-file line numbers.
- Entity details show counts of matching source configurations by category. Repeated references in one source do not inflate that source count. The same entity can have both live-entity references and retained-statistics references.

| Source or target | Coverage |
|---|---|
| Loaded automations and scripts | Static entity, device, area and service/action targets, including nested actions and conditions |
| Device automations | Resolve known entity-registry UUIDs to entity IDs; flag missing UUIDs |
| Storage and YAML dashboards | Configuration loaded through Home Assistant, including standard entity lists and target fields |
| Templates | Parse literal calls such as `states('sensor.temperature')` and `states.sensor.temperature`, including standalone template definitions; never execute them |
| Existing entities | Registry entities plus runtime states; disabled entities are not considered missing merely because they have no state |
| Missing actions | Compared with currently registered Home Assistant services/actions after startup |

Each result includes a source name and ID, target type and ID, and a path such as `$.actions[0].target.entity_id`. Array indexes start at **0**. Paths identify positions in loaded configuration, not YAML file line numbers. The app supports pagination, all/missing filtering, per-source coverage, entity and bundle dependencies, and JSON/CSV/Markdown exports.

### Coverage and interpretation

- `completed` means the supported static check completed, **not** that the entire installation was exhaustively checked.
- Dynamic/computed templates, blueprint expansion, custom cards, dashboard strategies and unreadable sources limit coverage. Literal references can still be reported, but the source is marked partial.
- Not covered: arbitrary Python/custom-integration logic, unlisted helper domains, every YAML integration, indirect script/template semantics and every custom-card property. Label/floor targets and Recorder wildcard/domain filters mark limited coverage. This is not a general Home Assistant interpreter.
- Automations/scripts and runtime memberships use loaded configuration; YAML helpers/templates use the saved configuration. Reload changes before checking the running behaviour. Some sources that never loaded may not be discoverable; inspect Home Assistant's own configuration errors too.
- A registered but unavailable entity is **not missing**. An action that temporarily disappears during an integration reload can produce a temporary issue; recheck after the integration has recovered.
- Device and area targets can affect selected entities indirectly. They are shown as potential use, not proof that every selected entity is actually affected.
- Zero findings never proves that removal is safe. The backup choice and explicit user risk acceptance remain required by the normal cleanup workflow.

### Repairs workflow

Open **Settings → System → Repairs**. The companion groups missing targets into one stable issue per source, with up to 30 example paths. The app and exports contain the full findings.

1. Open the named automation, script or dashboard.
2. Correct the reference, restore the missing target, or remove the reference if it is no longer needed.
3. Reload YAML changes where needed. Wait up to five minutes, or request a new app scan.
4. The issue disappears when that source can be fully checked and no missing references remain. Verified removal of a source also resolves its issue after a complete check.

There is deliberately no automatic **Fix** button. Ignore intentional missing references using the normal Repairs controls. Repeated checks retain the same issue identity and do not reset ignored status. Home Assistant controls dismissal behaviour across its own upgrades; removing/reloading the companion removes its issues and can reset dismissal history.

An unreadable or partial source does not falsely resolve its previous issue. A previously reported issue may therefore remain until the source is fully readable or its remaining missing references are independently addressed and the source can be fully checked. This is shown as limited coverage in the app.

### Before registry cleanup

The preparation contains the selected objects' direct references and potential device/area dependencies, including the scan time. Review these before confirming. When the companion was available during preparation, the app rechecks references and current registry associations before the first removal command. A changed dependency or changed source coverage requires a new scan and review. An unavailable recheck stops execution without changing the registry.

If the companion was not available at preparation time, the app shows that limitation explicitly and retains the existing user-directed cleanup choice. The check is not an atomic Home Assistant transaction: avoid editing/reloading configuration while executing cleanup. No individual undo is available for registry removal; recovery may require a full backup.

### Privacy and troubleshooting

Only source names/IDs, target IDs, configuration paths, coverage and check time leave the companion. Full configurations, service payloads and template bodies are not exported. IDs and names can still reveal personal information: review reports before sharing them.

The WebSocket command `hass_cleaner/references` is administrator-only. The app uses its normally configured Supervisor authentication. No browser tokens or new secrets are required. If authentication is refused or the companion is missing, the normal registry/file scan continues and reference checks show **unavailable**, never a false all-clear.

If unavailable: verify installation path, restart Core, add the companion integration, check Core logs, and run a new app scan. Automatic/generated dashboards without a readable configuration may show limited coverage. No repairs from other integrations (including Spook) are deleted or modified. Running both can result in overlapping warnings.

### Validation before release

Local automated tests cover the analyzer, WebSocket bridge, HA adapter contracts, Repairs lifecycle, pagination, exports and cleanup revalidation. Contract tests mock Home Assistant interfaces; they do not demonstrate a successful live installation.

On a disposable Home Assistant 2026.9 instance:

1. Install/configure the companion and verify a clean startup with no repeated errors.
2. Add a test automation, script and manual dashboard referring to a deliberately nonexistent entity. Verify exact paths, three source issues, app results and English, Dutch or German text.
3. Correct a reference and reload it. Verify its issue resolves. Ignore another issue and verify repeated checks preserve the choice.
4. Check YAML dashboards, a disabled registered entity, a device trigger using a registry UUID, and a dynamic template. Confirm disabled entities are not missing and dynamic coverage is partial.
5. Temporarily make a test dashboard unreadable. Confirm its prior issue remains and the app shows limited coverage.
6. Prepare registry cleanup only for disposable test entities, change a dependency, and verify execution stops before any removal.
7. Restart Core, reload/remove the companion, and verify scheduled work and issue ownership behave correctly.
8. Stop/remove the companion and confirm the app still scans with an explicit unavailable reference status.
9. Create disposable scene/group/helper/template references. Check both UI-created helpers and YAML packages; verify a legacy group is listed once and changing a helper option removes the old dependency.
10. Verify an external statistic and a retained statistic whose entity no longer exists. They must not produce missing-entity Repairs. An actually missing statistic should produce a finding; unavailable Recorder access should instead show unknown verification.

### Sidebar panel

The companion adds a read-only panel named **Referenzprüfung** to the sidebar (`mdi:link-variant-off`). It shows the references of the last report — source, source ID, target type, target, path, and whether the target is missing or its verification is unavailable — with filters and a coverage list. The panel only calls the existing `hass_cleaner/references` WebSocket command; it reads nothing from disk and changes nothing.

The panel needs the HTTP layer and the frontend. The manifest therefore declares `websocket_api`, `http`, `frontend` and `panel_custom` as dependencies, so Home Assistant sets those up before the integration starts; if the frontend only becomes ready later, registration is retried on `EVENT_HOMEASSISTANT_STARTED`. The panel is limited to administrators and is removed when the config entry is unloaded. Its name deliberately differs from the app's own sidebar entry “Hass-Cleaner”, so both stay distinguishable.

## Nederlands kort

De zeven categorieën uit deel 1 zijn aangesloten, inclusief scènes, groepen, ondersteunde helpers, losse templates en energie/statistieken. Geldige historische/externe statistieken worden niet als verdwenen entiteit gemeld. Zonder Recorder is de statistiekcontrole expliciet onbekend. Niet alle aangepaste helpers of dynamische templates zijn interpreteerbaar; praktijktests blijven nodig voordat dit releaseklaar is.

- Met HACS en Home Assistant 2026.9.0 of nieuwer: voeg `https://github.com/Bart1109/Hass-Cleaner` toe via **HACS → menu (⋮) → Aangepaste repositories**, type **Integratie**. Download **Hass-Cleaner Companion**, herstart Home Assistant Core en voeg de integratie toe via **Instellingen → Apparaten & diensten**. Kies dezelfde releaseversie als de app. HACS-ondersteuning is beschikbaar vanaf 1.1.1; de integratie staat niet in de standaardcatalogus.
- De ZIP blijft een alternatief zonder HACS. Al handmatig geïnstalleerd? Maak een back-up, download via HACS en herstart Core; behoud de bestaande integratie. Werk voortaan de companion via HACS bij en de app via de App Store.
- Start een nieuwe appscan. Onder **Entiteiten → Referentiecontrole** staan bronnen, doelen, exacte configuratiepaden en beperkte dekking.
- Meldingen staan bij **Instellingen → Systeem → Reparaties**. Corrigeer zelf de configuratie; de companion controleert iedere vijf minuten. Er wordt niets automatisch hersteld of verwijderd.
- App en companion zijn afzonderlijke onderdelen en moeten afzonderlijk worden bijgewerkt. 1.2.0 is uitgebracht; deze checkout bereidt 1.2.1 met Duitse documentatie voor. Praktijktests blijven nodig.
- Geen verwijzingen gevonden betekent **niet** veilig verwijderen. Templates, blueprints, aangepaste kaarten en onleesbare bronnen kunnen gebruik verbergen. Maak een volledige back-up en controleer de gevolgen.
