# Hass-Cleaner

[Deutsch](#deutsch) · [English](#english) · [Nederlands](#nederlands) · [Wiki](https://github.com/Bart1109/Hass-Cleaner/wiki) · [Releases](https://github.com/Bart1109/Hass-Cleaner/releases)

> **Betreuung:** Bart1109 · **Basis:** Hass-Cleaner von dkwolf1 · **Maintained by** Bart1109, **powered by** dkwolf1

## Deutsch

Hass-Cleaner ist eine Home-Assistant-App, die Speicher, veraltete Entitäten und Registerbeziehungen prüft, bevor irgendetwas aufgeräumt wird. Sicherheit, eine informierte Entscheidung der Nutzer und die Wiederherstellbarkeit stehen vor dem freigewordenen Speicherplatz.

> **Veröffentlichungsstand:** Version 1.2.0 ist für den kontrollierten frühen Einsatz veröffentlicht, einschließlich Installation über HACS, deutscher Oberfläche und dem Seitenleisten-Panel „Referenzprüfung“. Version 1.2.1 brachte die deutsche Dokumentation und die eigenen Repository-Verweise, ohne funktionale Änderung. Version 1.2.2 liefert das App-Image aus `ghcr.io/bart1109/hass-cleaner`. Dieser Stand bereitet **1.2.3** vor: deutsche Texte für die Bestätigungsdialoge und deutsche Berichts-Downloads aus der Oberfläche. Hass-Cleaner liefert Fakten, Empfehlungen, Sicherungsoptionen und Hinweise zur Wiederherstellung; die endgültige Entscheidung über das Aufräumen trifft der Nutzer.

**Companion-Vorschau seit 1.1.0.** [Referenzprüfung und native Reparaturhinweise](docs/reference-checks.md) nutzen die optionale, separat installierte Integration **Hass-Cleaner Companion**. Eine Veröffentlichung ist kein Beleg für vollständige Referenzabdeckung. Ein Abnahmetest in einer echten Home-Assistant-Installation bleibt erforderlich.

> [!WARNING]
> **Testversion — mit Vorsicht verwenden.** Hass-Cleaner kann Dateien, Home-Assistant-Registerobjekte und Recorder-Daten verändern. Prüfe jede Auswahl und lege nach Möglichkeit vorher eine vollständige Home-Assistant-Sicherung an. Teste wenn möglich an einer unkritischen Installation. Die Nutzung erfolgt auf eigenes Risiko; Quarantäne und Wiederherstellung verringern das Risiko, können aber nicht garantieren, dass jede Integration oder Nutzerkonfiguration unbeeinflusst bleibt.

### Was ist Hass-Cleaner?

Hass-Cleaner hilft Home-Assistant-Nutzern, angesammelte Daten übersichtlich und kontrolliert zu beurteilen. Die App findet unter anderem alte Protokolle, neu erzeugbare Cache-Dateien, dauerhaft nicht verfügbare Entitäten und inkonsistente Registerbeziehungen.

Ein Fund ist nie für sich genommen ein Beweis, dass gelöscht werden darf. Die App erklärt, warum etwas gefunden wurde, welches Risiko besteht, welche Folgen möglich sind und wie die Wiederherstellung funktioniert.

### Kernfunktionen

- Sicherer Speicherscan mit einem klaren Exportdialog: lesbarer Markdown-Bericht, CSV für Tabellenkalkulationen und JSON für die technische Analyse.
- Einsteigerfreundliche Aufräumkategorien und die Aktion **Bereinigung vorbereiten**.
- Entitätsfilter nach Status, Dauer, Integration, Gerät und Bereich.
- Optionaler Companion: statische Verweise in Automatisierungen, Skripten, Dashboards, Szenen, Gruppen, unterstützten Helfern/Templates sowie Energie- und Statistik-Konfiguration; native Reparaturhinweise für fehlende Ziele und Abhängigkeitskontext vor dem Aufräumen des Registers. Die Grenzen der Abdeckung werden ausdrücklich benannt.
- Gruppierung von Geräten und Entitäten nach Integration oder Gerät.
- Scanunterschiede für neue, geänderte, wiederhergestellte und verschwundene Signale.
- Offizielle Recorder-Bereinigung von Home Assistant mit separater Bestätigung.
- Quarantäne für sichere, persönliche und ausdrücklich geprüfte Dateien; geschützte Kerndateien bleiben ausgenommen.
- Vom Nutzer gesteuertes Entfernen registrierter Entitäten und unterstützter Gerätebündel über die offizielle Home-Assistant-API.
- Löschbare lokale Scan- und abgeschlossene Quarantäneprotokolle für einen sauberen Start.
- Wiederherstellungstest und Rückspielen, ohne vorhandene Dateien zu überschreiben.

### Sicherheitsmodell ab 1.0.x

Eine Datei gelangt nur dann in die Quarantäne, wenn alle Bedingungen erfüllt sind:

1. Sie gehört zum letzten abgeschlossenen Scan.
2. Typ, Pfad, Alter, Risikoklasse und geschützte Bereiche stimmen unmittelbar vor der Ausführung noch mit dem Scan überein.
3. Größe, Änderungszeit und SHA-256 stimmen mit dem Scan überein.
4. Der Nutzer wählt ausdrücklich eine von Supervisor geprüfte Sicherung, eine selbst geprüfte aktuelle Sicherung oder das Fortfahren ohne Sicherung.
5. Wer von der empfohlenen geprüften Sicherung abweicht, muss das Risiko zusätzlich bestätigen.
6. Der Nutzer bestätigt den Vorgang mit `QUARANTAINE`.

Die gesamte Auswahl wird geprüft, bevor die erste Datei verschoben wird. Die Quarantäne speichert den ursprünglichen Pfad, die Prüfsumme, den Nutzer, den Sicherungsnachweis und die Ablaufzeit. Die Wiederherstellung verlangt `HERSTEL` und überschreibt nie eine vorhandene Datei.

Nach der eingestellten Aufbewahrung von 1–10 Tagen wird nichts automatisch gelöscht. Endgültiges Entfernen wird erst nach Ablauf möglich, prüft die Prüfsumme erneut und verlangt `VERWIJDER`.

Persönliche oder unsichere Inhalte erfordern eine zusätzliche Bestätigung des Inhalts. Das Aufräumen des Registers erfordert einen angezeigten Hinweis, eine Sicherungswahl, eine Risikobestätigung und die Bestätigung der genauen Anzahl. Nur zur Laufzeit vorhandene Entitäten und geschützte Kerndateien bleiben technisch ausgeschlossen.

### Dokumentation

Das [Hass-Cleaner-Wiki](https://github.com/Bart1109/Hass-Cleaner/wiki) enthält das Benutzerhandbuch, darunter:

- Installation und Aktualisierung;
- der empfohlene erste Scan;
- Dateiklassifizierung und Quarantäne;
- Prüfung von Entitäten und Bündeln;
- Recorder-Bereinigung und Sicherungen;
- Einstellungen, Berichte und Fehlersuche;
- Hinweise zu Sicherheit und Wiederherstellung;
- eine knappe niederländische Schnellstartanleitung.

Versionsbezogene Änderungen stehen in [CHANGELOG.md](hass_cleaner/CHANGELOG.md), geplante Arbeit und Freigabekriterien in [ROADMAP.md](ROADMAP.md).

### Sprachen

- Projektdokumentation und GitHub-Kommunikation nutzen Deutsch als primäre Sprache; Englisch und Niederländisch bleiben als vollständige Abschnitte erhalten.
- Oberfläche und Home-Assistant-App-Einstellungen unterstützen Automatisch, English, Nederlands und Deutsch. Deutsche Berichte, CSV-Exporte sowie die Einrichtungs- und Reparaturtexte des optionalen Companion sind ebenfalls vorhanden.
- Automatisch nutzt die Browser- oder Home-Assistant-Anzeigesprache und fällt bei nicht unterstützten Sprachen auf Englisch zurück.
- Beide Konfigurationsorte wirken: geänderte App-Einstellungen überschreiben die gespeicherten Werte der Oberfläche, unveränderte Felder behalten die Auswahl aus der Oberfläche. Speichern in Hass-Cleaner wendet die neue Auswahl erneut an. Supervisor-Optionen werden durch UI-Speichern nicht überschrieben.

### Installation von GitHub

1. In Home Assistant **Einstellungen → Apps → App-Store → Repositories** öffnen.
2. `https://github.com/Bart1109/Hass-Cleaner` hinzufügen.
3. **Hass-Cleaner** installieren.
4. App starten und die Weboberfläche öffnen.
5. Zuerst einen Scan ausführen und den Bericht prüfen, bevor eine Aktion vorbereitet wird.

GitHub Actions baut die Version aus `hass_cleaner/config.yaml` für `amd64` und `aarch64`. Nachdem das Container-Image veröffentlicht ist, kann Home Assistant diese Version über dieses Repository installieren oder aktualisieren. Der Companion ist eine separate Integration und nicht Teil des App-Containers.

### Companion über HACS installieren

Mit eingerichtetem HACS und Home Assistant 2026.9.0 oder neuer `https://github.com/Bart1109/Hass-Cleaner` unter **HACS → Menü (⋮) → Benutzerdefinierte Repositories** hinzufügen, Typ **Integration**. **Hass-Cleaner Companion** herunterladen, Home Assistant Core neu starten und die Integration unter **Einstellungen → Geräte & Dienste** hinzufügen. Dieselbe Release-Version wie die App verwenden.

HACS aktualisiert den Companion, der App-Store die App. Das ZIP bleibt für die manuelle Installation verfügbar. Siehe [Installations- und Migrationshinweise](docs/reference-checks.md). Dieses Repository steht nicht im Standardkatalog von HACS.

### Quarantänespeicher in 1.2.0

Neue Vorgänge verschieben Dateien atomar nach `/homeassistant/.hass-cleaner-quarantine` (das Konfigurationsverzeichnis von Home Assistant) und behalten dabei die Originaldatei, statt sie zu kopieren und zu löschen. Dieser Ordner wird von Scans ausgenommen. Verschiebungen über Dateisystemgrenzen werden ohne Kopier-/Lösch-Ersatz abgelehnt. Bestehende Quarantäne im App-Speicher bleibt unterstützt.

Nimm sowohl den Konfigurationsordner als auch die App-Daten in deine Sicherungen auf: Das Wiederherstellungsmanifest bleibt in den App-Daten. Entferne den versteckten Quarantäneordner nicht von Hand. Verschieben innerhalb desselben Dateisystems gewinnt keinen Speicherplatz; das endgültige Löschen nach Ablauf schon. Stoppe aktive Schreiber vor dem Aufräumen; ein späterer Schreibvorgang kann die gespeicherte Prüfsumme entwerten und eine manuelle Wiederherstellung erzwingen.

### Lokale Entwicklung und Tests

Führe die folgenden Befehle im Verzeichnis `hass_cleaner` aus:

```powershell
$env:HASS_CLEANER_CONFIG_ROOT = "$PWD\..\dev-fixtures\homeassistant"
$env:HASS_CLEANER_DATA_ROOT = "$PWD\..\data"
$env:HASS_CLEANER_HOST = "127.0.0.1"
$env:HASS_CLEANER_PORT = "8099"
python -m hass_cleaner
```

Danach `http://127.0.0.1:8099` öffnen.

```powershell
python -m unittest discover -s tests -v
node --check web/assets/app.js
```

### Aufbau des Repositories

```text
repository.yaml
hass_cleaner/
  config.yaml
  Dockerfile
  DOCS.md
  CHANGELOG.md
  translations/
  hass_cleaner/
  web/
  tests/
```

### Lizenz und Mitarbeit

Beiträge sind willkommen, aber Aufräumregeln müssen im Zweifel ablehnen und Tests, Folgenabschätzung sowie einen Weg zur Wiederherstellung enthalten. Siehe [CONTRIBUTING.md](CONTRIBUTING.md).

---

## English

Hass-Cleaner is a Home Assistant App for inspecting storage, stale entities and registry relationships before anything is cleaned up. Safety, informed user choice and recovery come before reclaimed space.

> **Release status:** version 1.2.0 is published for controlled early use, including HACS installation support, the German interface and the “Referenzprüfung” sidebar panel. Version 1.2.1 added the German documentation and the repository links, with no functional change. Version 1.2.2 ships the app image from `ghcr.io/bart1109/hass-cleaner`. This checkout prepares **1.2.3**: German wording for the confirmation dialogs and German report downloads from the interface. Hass-Cleaner provides facts, advice, backup options and recovery guidance; the user makes the final cleanup decision.

**Companion preview in 1.1.0.** [Reference checks and native Repairs](docs/reference-checks.md) use an optional, separately installed **Hass-Cleaner Companion** integration. Publication is not a claim of complete reference coverage. Live Home Assistant acceptance testing is still required.

> [!WARNING]
> **Test version — handle with care.** Hass-Cleaner can modify files, Home Assistant registry objects and Recorder data. Review every selection and preferably create a full Home Assistant backup first. Test on a non-critical installation where possible. Use is at your own risk; quarantine and recovery safeguards reduce risk, but cannot guarantee that every integration or user configuration remains unaffected.

### What is Hass-Cleaner?

Hass-Cleaner helps Home Assistant users review accumulated data in a clear and controlled way. It can identify old logs, rebuildable cache files, persistently unavailable entities and inconsistent registry relationships.

A finding is never treated as deletion evidence by itself. The App explains why it was found, its risk, possible consequences and the available recovery path.

### Main features

- Safe storage scanning with one clear export dialog: a readable Markdown report, CSV for spreadsheet analysis and JSON for technical analysis.
- Beginner-friendly cleanup categories and a clear **Prepare cleanup** action.
- Entity filters for state, duration, integration, device and area.
- Optional companion: static references in automations, scripts, dashboards, scenes, groups, supported helpers/templates and energy/statistics configuration; native Repairs for missing targets and dependency context before registry cleanup. Coverage limits are explicit.
- Device and entity grouping by integration or device.
- Scan differences for new, changed, recovered and disappeared signals.
- Official Home Assistant Recorder purge with separate confirmation.
- Quarantine for safe, personal and explicitly user-reviewed files; protected core files remain excluded.
- User-directed removal of registered entities and supported device bundles through Home Assistant's official API.
- Clearable local scan and completed-quarantine logs for a clean start.
- Restore testing and recovery without overwriting existing files.

### 1.0.x safety model

A file can enter quarantine only when all conditions are satisfied:

1. It belongs to the latest completed scan.
2. Its type, path, age, risk class and protected scopes still match the scan immediately before execution.
3. Its size, modification time and SHA-256 still match the scan.
4. The user explicitly chooses a Supervisor-verified backup, a manually checked recent backup or proceeding without a backup.
5. Deviating from the recommended verified backup requires an additional risk acknowledgement.
6. The user confirms the operation with `QUARANTAINE`.

The complete selection is validated before the first file is moved. Quarantine records the original path, checksum, user, backup evidence and expiry time. Recovery requires `HERSTEL` and never overwrites an existing file.

Nothing is deleted automatically after the configured 1–10 day retention period. Permanent removal becomes available only after expiry, verifies the checksum again and requires `VERWIJDER`.

Personal or uncertain content requires an additional content acknowledgement. Registry cleanup requires displayed advice, a backup choice, risk acknowledgement and exact count confirmation. Runtime-only entities and protected core files remain technically excluded.

### Documentation

The [Hass-Cleaner Wiki](https://github.com/Bart1109/Hass-Cleaner/wiki) contains the user guide, including:

- installation and updates;
- the recommended first scan;
- file classification and quarantine;
- entity and bundle review;
- Recorder cleanup and backups;
- settings, reports and troubleshooting;
- safety and recovery guidance;
- a concise Dutch quick-start.

For version-specific changes, see [CHANGELOG.md](hass_cleaner/CHANGELOG.md). For planned work and release criteria, see [ROADMAP.md](ROADMAP.md).

### Languages

- Project documentation and GitHub communication use German as the primary language; English and Dutch remain available as full sections below.
- Interface and Home Assistant App settings support Automatic, English, Nederlands and Deutsch. German reports, CSV exports and the optional companion's setup/Repairs texts are available as well.
- Automatic uses the browser or Home Assistant display language and falls back to English for unsupported languages.
- Both configuration locations work: changed App configuration fields override their saved UI values; unchanged fields retain your UI choices. Saving in Hass-Cleaner applies your new choices again. Supervisor options are not rewritten by UI saves.

### Install from GitHub

1. In Home Assistant, open **Settings → Apps → App store → Repositories**.
2. Add `https://github.com/Bart1109/Hass-Cleaner`.
3. Install **Hass-Cleaner**.
4. Start the App and open its web interface.
5. Run a scan first and review the report before preparing an action.

GitHub Actions builds the version in `hass_cleaner/config.yaml` for `amd64` and `aarch64`. After the container is published, Home Assistant can install or update that version through this repository. The companion is a separate integration, not part of the app container.

### Companion installation through HACS

With HACS configured and Home Assistant 2026.9.0 or newer, add `https://github.com/Bart1109/Hass-Cleaner` under **HACS → menu (⋮) → Custom repositories**, type **Integration**. Download **Hass-Cleaner Companion**, restart Home Assistant Core, then add it under **Settings → Devices & services**. Use the same release version as the app.

HACS updates the companion; the App Store updates the app. The ZIP remains available for manual installation. See [installation and migration instructions](docs/reference-checks.md#installation). This repository is not in the default HACS catalog.

### Quarantine storage in 1.2.0

New operations atomically move files into `/homeassistant/.hass-cleaner-quarantine` (the Home Assistant configuration directory), retaining the original file rather than copying and unlinking it. This folder is excluded from scans. Cross-filesystem moves are rejected without a copy/delete fallback. Existing quarantine in app storage remains supported.

Keep both the configuration folder and the app data in your backups: the recovery manifest stays in the app data. Do not manually remove the hidden quarantine folder. Moving files on the same filesystem does not free disk space; permanent deletion after expiry does. Stop active writers before cleanup; a later write may invalidate the stored checksum, requiring manual recovery instead of automatic restore.

### Local development and tests

Run the following commands from the `hass_cleaner` directory:

```powershell
$env:HASS_CLEANER_CONFIG_ROOT = "$PWD\..\dev-fixtures\homeassistant"
$env:HASS_CLEANER_DATA_ROOT = "$PWD\..\data"
$env:HASS_CLEANER_HOST = "127.0.0.1"
$env:HASS_CLEANER_PORT = "8099"
python -m hass_cleaner
```

Then open `http://127.0.0.1:8099`.

```powershell
python -m unittest discover -s tests -v
node --check web/assets/app.js
```

---

## Nederlands

> [!WARNING]
> **Testversie — voorzichtig gebruiken.** Hass-Cleaner kan bestanden, Home Assistant-registerobjecten en Recorder-gegevens wijzigen. Controleer iedere selectie en maak vooraf bij voorkeur een volledige Home Assistant-back-up. Test waar mogelijk eerst op een niet-kritische installatie. Gebruik is op eigen risico; quarantaine en herstelvoorzieningen verkleinen het risico, maar kunnen niet garanderen dat iedere integratie of gebruikersconfiguratie zonder gevolgen blijft werken.

### Wat is Hass-Cleaner?

Hass-Cleaner helpt Home Assistant-gebruikers om verzamelde gegevens begrijpelijk en gecontroleerd te beoordelen. De App zoekt onder andere naar oude logs, opnieuw op te bouwen cachebestanden, langdurig onbeschikbare entities en afwijkende registerrelaties.

Een gevonden onderdeel is nooit automatisch verwijderbewijs. De App toont waarom iets is gevonden, wat het risico is, wat er kan gebeuren en hoe herstel werkt.

### Belangrijkste functies

- Veilige opslagscan met één duidelijk exportvenster: een leesbaar Markdownrapport, CSV voor spreadsheetanalyse en JSON voor technische analyse.
- Begrijpelijke opruimcategorieën en de actie **Opschoning voorbereiden**.
- Entities filteren op status, duur, integratie, apparaat en ruimte.
- Apparaten en entities bundelen per integratie of apparaat.
- Verschillen tussen scans: nieuw, gewijzigd, hersteld en verdwenen.
- Officiële Home Assistant Recorder-purge met afzonderlijke bevestiging.
- Quarantaine voor veilige, persoonlijke en door de gebruiker beoordeelde bestanden; beschermde kernbestanden blijven uitgesloten.
- Gebruikersgestuurde verwijdering van geregistreerde entities en ondersteunde apparaatbundels via de officiële Home Assistant-API.
- Wisbare lokale scan- en afgeronde quarantainelogboeken voor een schone start.
- Hersteltest en terugplaatsen zonder bestaande bestanden te overschrijven.

### Veiligheidsmodel van 1.0.x

Een bestand kan alleen naar quarantaine als aan alle voorwaarden wordt voldaan:

1. Het bestand komt uit de laatste voltooide scan.
2. Bestandstype, pad, leeftijd, risicoklasse en beschermde scopes komen vlak voor uitvoering nog overeen met de scan.
3. Grootte, wijzigingstijd en SHA-256 komen overeen met de scan.
4. De gebruiker kiest bewust voor een door Supervisor geverifieerde back-up, een zelf gecontroleerde recente back-up of doorgaan zonder back-up.
5. Afwijken van de aanbevolen geverifieerde back-up vereist een extra risicobevestiging.
6. De gebruiker bevestigt de actie met `QUARANTAINE`.

De volledige selectie wordt gecontroleerd voordat het eerste bestand wordt verplaatst. Quarantaine bewaart het oorspronkelijke pad, de checksum, de gebruiker, het back-upbewijs en de vervaldatum. Herstel vereist `HERSTEL` en overschrijft nooit een bestaand bestand.

Na de ingestelde bewaartermijn van 1–10 dagen wordt niets automatisch gewist. Definitief verwijderen is pas daarna beschikbaar, voert opnieuw een checksumcontrole uit en vereist `VERWIJDER`.

Persoonlijke of onzekere inhoud vereist een extra inhoudsbevestiging. Registeropschoning vereist adviesweergave, back-upkeuze, risicobevestiging en een exact aantal. Runtime-only entities en beschermde kernbestanden blijven technisch uitgesloten.

### Documentatie

De [Hass-Cleaner Wiki](https://github.com/Bart1109/Hass-Cleaner/wiki) bevat de uitgebreide Engelstalige handleiding en een korte Nederlandse snelstart. Onderwerpen zijn onder andere:

- installatie en updates;
- de aanbevolen eerste scan;
- bestandsclassificatie en quarantaine;
- beoordeling van entities en bundels;
- Recorder-opschoning en back-ups;
- instellingen, rapporten en probleemoplossing;
- veiligheid en herstel.

Versiegebonden wijzigingen staan in [CHANGELOG.md](hass_cleaner/CHANGELOG.md). Gepland werk en releasecriteria staan in [ROADMAP.md](ROADMAP.md).

### Talen

- Projectdocumentatie en GitHub-communicatie gebruiken Engels als primaire taal en Nederlands als tweede taal.
- De interface en Home Assistant App-instellingen ondersteunen Automatisch, English, Nederlands en Deutsch. Ook het rapport en de CSV-export zijn in het Duits beschikbaar.
- Automatisch gebruikt de browser- of Home Assistant-weergavetaal en valt bij een niet-ondersteunde taal terug op Engels.
- Beide configuratieplekken werken: gewijzigde App-instellingen krijgen per veld voorrang; overige UI-keuzes blijven behouden. Opnieuw opslaan binnen Hass-Cleaner past je nieuwe keuze toe.

### Installeren vanuit GitHub

1. Open in Home Assistant **Instellingen → Apps → App store → Repositories**.
2. Voeg `https://github.com/Bart1109/Hass-Cleaner` toe.
3. Installeer **Hass-Cleaner**.
4. Start de App en open de webinterface.
5. Voer eerst een scan uit en beoordeel het rapport voordat je een actie voorbereidt.

GitHub Actions bouwt de versie uit `hass_cleaner/config.yaml` voor `amd64` en `aarch64`. Gepubliceerd: **1.2.0** met HACS-ondersteuning, Duitse interface en het zijpaneel “Referenzprüfung”. Versie 1.2.1 bracht de Duitse documentatie en de verwijzingen naar deze repository, zonder functionele wijziging. Versie 1.2.2 levert de app-image van `ghcr.io/bart1109/hass-cleaner`. Deze checkout bereidt **1.2.3** voor: Duitse teksten voor de bevestigingsdialogen en Duitse rapportdownloads. Installeer de aparte [companion](docs/reference-checks.md#nederlands-kort) via HACS door deze repository toe te voegen als type **Integratie**. De ZIP blijft een alternatief; de companion zit niet in de app-container.

Vanaf 1.2.0 worden nieuwe quarantainebestanden atomair naar `.hass-cleaner-quarantine` in de Home Assistant-configuratiemap verplaatst. Bestaande quarantaine blijft ondersteund. Bewaar zowel de configuratiemap als appdata in je back-up; verwijder de verborgen map niet handmatig. Verplaatsen maakt nog geen schijfruimte vrij. Verplaatsingen tussen bestandssystemen worden geblokkeerd. Stop actieve schrijvers vooraf; latere wijzigingen kunnen de checksum ongeldig maken en handmatig herstel vereisen.

### Lokaal ontwikkelen en testen

Voer de volgende opdrachten uit vanuit de map `hass_cleaner`:

```powershell
$env:HASS_CLEANER_CONFIG_ROOT = "$PWD\..\dev-fixtures\homeassistant"
$env:HASS_CLEANER_DATA_ROOT = "$PWD\..\data"
$env:HASS_CLEANER_HOST = "127.0.0.1"
$env:HASS_CLEANER_PORT = "8099"
python -m hass_cleaner
```

Open daarna `http://127.0.0.1:8099`.

```powershell
python -m unittest discover -s tests -v
node --check web/assets/app.js
```

## Repository layout

```text
repository.yaml
hass_cleaner/
  config.yaml
  Dockerfile
  DOCS.md
  CHANGELOG.md
  translations/
  hass_cleaner/
  web/
  tests/
```

## License and contributions

Contributions are welcome, but cleanup rules must fail closed and include tests, impact information and a recovery path. See [CONTRIBUTING.md](CONTRIBUTING.md).
