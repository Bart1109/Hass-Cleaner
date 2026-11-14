# Hass-Cleaner Roadmap

[Deutsch](#deutsch) · [English](#english) · [Nederlands](#nederlands)

## Deutsch

Aktuell veröffentlichte Version: **1.1.1**, einschließlich Referenzprüfung, Reparaturhinweisen und HACS-Unterstützung. Dieser Stand bereitet **1.2.0** vor: Schutz vor gleichzeitigen Quarantänevorgängen, Referenzdiagnostik, Korrekturen beim Aktualisieren von Listen, Berichtigungen an Dokumentation und Übersetzungen, eine deutsche Oberfläche samt Exporten sowie das schreibgeschützte Seitenleisten-Panel „Referenzprüfung“ des Companion. Alle Releases bleiben für kontrollierte frühe Tests gedacht, nicht als Sicherheitsgarantie. Siehe [das Changelog](hass_cleaner/CHANGELOG.md).

### Grundsatz

Sicherheit geht vor zusätzlichem Aufräumgewinn. Ein Release erfolgt erst, wenn riskante Situationen nachweislich blockiert werden und die Wiederherstellung getestet werden kann.

### Abgeschlossen

| Version | Status | Inhalt |
|---|---|---|
| 0.7.2 | Abgeschlossen | Verlässliche Zeitmessung, Unterschiede zwischen Scans, gespeicherte Nutzerentscheidungen, Sicherheitsvorkehrungen und Seitennavigation/Performance. |
| 0.7.3 | Abgeschlossen | Klarere Entitätssignale, kompakte Bündel und getrennte Behandlung von temporären, dauerhaften, `unavailable`-, `unknown`- und integrationsspezifischen Problemen. |
| 0.8.0 | Abgeschlossen | Funktionierende Quarantäne für nachweislich sichere Dateien, Stapelprüfung, SHA-256-Manifeste und sichere Wiederherstellung. |
| 0.9.0 | Abgeschlossen | Überprüfung der Supervisor-Sicherung, Wiederherstellungstest, Aufbewahrungsfrist und ausdrückliches Löschen nach Ablauf. |
| 0.9.1 | Abgeschlossen | Zulässige Sicherungsprüfung, wiederverwendbarer Nachweis, bewusste optionale Sicherungswahl und auswählbare Entitätsprüfung. |
| 1.0.0 | Veröffentlicht | Vom Nutzer gesteuerte Bereinigung, Ausführung im Register, persönliche Inhalte, sauberer Start und harter Schutz des Kemsystems. |
| 1.0.1 | Veröffentlicht | Technische Härtung: absturzsichere Ausführung, Seitennavigation, atomare Speicherung, Barrierefreiheit und verlässliches Frontend-Caching. |
| 1.0.2 | Veröffentlicht | Wiederherstellungs- und Registerjournale, sichere Konfigurationssynchronisierung, begrenzter Scan-Speicher, robuste Anfrageprüfung und verbesserte zweisprachige Exporte. |
| 1.1.0 | Veröffentlicht | Companion mit Referenzprüfung und nativen Reparaturhinweisen. |
| 1.1.1 | Veröffentlicht | HACS-Installation und Anleitungen. |
| 1.2.0 | Vorbereitet | Atomare Quarantäne, Diagnostik, Aktualisierung der Listen, Dokumentation und Übersetzungen, deutsche Oberfläche und das Seitenleisten-Panel „Referenzprüfung“ des Companion. |

### Praktische Prüfung für frühe Tester

- Das neue Release über den echten GitHub-/GHCR- und HACS-Ablauf installieren oder aktualisieren.
- Eine vollständige Sicherung starten und den Abschluss auf Home Assistant OS prüfen.
- Sowohl eine sichere Datei als auch einen bewusst akzeptierten Prüfkandidaten in die Quarantäne verschieben.
- Den Wiederherstellungstest ausführen und dieselbe Datei tatsächlich zurückspielen.
- Prüfen, dass eine geänderte oder geschützte Datei und eine falsche Bestätigung blockiert werden.
- Eine kleine Gruppe von Testentitäten entfernen und die Wiederherstellung aus einer Home-Assistant-Sicherung üben.
- Die Recorder-Bereinigung mit einer kleinen, sicheren Testkonfiguration prüfen.
- Die Oberfläche auf Desktop und Mobilgerät testen.
- Die niederländische, englische und deutsche Ingress-Oberfläche samt automatischer Sprachwahl in Regressionstests weiter abdecken.
- Nutzertests mit mehreren Integrationen und Speicherprofilen durchführen.
- Bekannte Probleme dokumentieren und jeden releaseblockierenden Fehler beheben.

### 1.0.0 — Erste öffentliche Testversion

- Für kontrollierte frühe Tests veröffentlicht; unerwartetes Verhalten mit dem lesbaren und dem technischen Scanbericht melden.
- Stabile Vereinbarung für Quarantäne und Wiederherstellung.
- Zweisprachige Oberfläche, Dokumentation und Home-Assistant-Einstellungen.
- Nur ausdrücklich vom Nutzer ausgewähltes Entfernen von Entitäten, Geräten und Registereinträgen über offizielle APIs.
- Sichere Migration bestehender Berichte, Pläne und Quarantänedaten.

### Nach 1.0

- Weitere allgemeine Cache-Profile mit nachgewiesenem Wiederherstellungsverhalten.
- Bessere Speichertrends und geschätzte Einsparung je Integration.
- Optionale Hinweise auf abgelaufene Quarantäne und dauerhafte Entitätsprobleme.
- Weitere Sprachen über separate Übersetzungsdateien.
- Das Löschen im Register bleibt eine bewusste Entscheidung; die Wiederherstellung erfordert eine Home-Assistant-Sicherung.

## Nederlands

### Uitgangspunt

Veiligheid gaat vóór extra opruimwinst. Een release gaat pas door wanneer risicovolle situaties aantoonbaar worden geblokkeerd en herstel getest kan worden.

### Afgerond

| Versie | Status | Inhoud |
|---|---|---|
| 0.7.2 | Afgerond | Betrouwbare tijdmetingen, verschillen tussen scans, opgeslagen gebruikersbeslissingen, beveiliging en paginering/performance. |
| 0.7.3 | Afgerond | Duidelijkere entitysignalen, compacte bundels, apart onderscheid tussen tijdelijk, langdurig, `unavailable`, `unknown` en integratiespecifieke problemen. |
| 0.8.0 | Afgerond | Werkende quarantaine voor bewezen veilige bestanden, batchvalidatie, SHA-256-manifest en veilig herstel. |
| 0.9.0 | Afgerond | Supervisor-back-upverificatie, hersteltest, bewaartermijn en expliciete verwijdering na verval. |
| 0.9.1 | Afgerond | Toegestane back-upcontrole, hergebruik van back-upbewijs, bewuste optionele back-upkeuze en selecteerbare entitybeoordeling. |
| 1.0.0 | Uitgebracht | Gebruikersgestuurde cleanup, registeruitvoering, persoonlijke inhoud, schone start en behoud van harde systeembescherming. |
| 1.0.1 | Uitgebracht | Technische hardening: crashbestendige uitvoering, paginering, atomaire opslag, toegankelijkheid en betrouwbaar frontendcachebeleid. |
| 1.0.2 | Uitgebracht | Herstel- en registerjournals, veilige configuratiesynchronisatie, begrensd scangeheugen, robuuste verzoekvalidatie en verbeterde tweetalige exports. |
| 1.1.0 | Uitgebracht | Companion met referentiecontrole en native Reparaties. |
| 1.1.1 | Uitgebracht | HACS-installatie en instructies. |
| 1.2.0 | Voorbereid | Atomaire quarantaine, diagnostiek, lijstverversing, documentatie/vertalingen, Duitse interface en het zijpaneel “Referenzprüfung” van de companion. |

### Praktijkcontrole voor vroege testers

- De nieuwe release installeren of bijwerken via de echte GitHub/GHCR- en HACS-workflow.
- Volledige back-up starten en voltooiing op Home Assistant OS verifiëren.
- Zowel een veilige als een bewust gekozen reviewkandidaat naar quarantaine verplaatsen.
- Hersteltest uitvoeren en hetzelfde bestand werkelijk terugplaatsen.
- Controleren dat een gewijzigd of beschermd bestand en een verkeerde bevestiging worden geblokkeerd.
- Een kleine set test-entities verwijderen en herstel vanuit een Home Assistant-back-up oefenen.
- Recorder-purge met een kleine, veilige testinstelling controleren.
- Interface testen op desktop en mobiel.
- Nederlandse en Engelse Ingress-interface en automatische taalkeuze in regressietests blijven controleren.
- Minimaal enkele gebruikerstests uitvoeren met verschillende integraties en opslagprofielen.
- Bekende problemen documenteren en alle releaseblokkerende fouten oplossen.

### 1.0.0 — Eerste publieke testversie

- Gepubliceerd voor gecontroleerde vroege tests; meld onverwacht gedrag met het leesbare en technische scanrapport.
- Stabiel quarantaine- en herstelcontract.
- Tweetalige interface, documentatie en Home Assistant-instellingen.
- Alleen expliciet door de gebruiker geselecteerde entity-, apparaat- en registerverwijdering via officiële API's.
- Veilige migratie van bestaande rapporten, plannen en quarantainegegevens.

### Na 1.0

- Meer generieke, aantoonbaar herstelbare cacheprofielen.
- Betere opslagtrends en geschatte winst per integratie.
- Optionele meldingen voor verlopen quarantaine en langdurige entityproblemen.
- Uitbreiding naar extra talen via losse vertaalbestanden.
- Registerverwijdering blijft een bewuste keuze; herstel vereist een Home Assistant-back-up.

---

## English

Current published release: **1.1.1**, including reference checks, Repairs and HACS support. This checkout prepares **1.2.0**: quarantine concurrency protection, reference diagnostics, list refresh fixes, documentation/translation corrections, a German interface and exports, and the companion's read-only “Referenzprüfung” sidebar panel. All releases remain intended for controlled early testing, not a guarantee of safety. See [the changelog](hass_cleaner/CHANGELOG.md).

### Principle

Safety takes priority over reclaimed space. A release proceeds only when risky situations are demonstrably blocked and recovery can be tested.

### Completed

| Version | Status | Scope |
|---|---|---|
| 0.7.2 | Completed | Reliable duration tracking, scan differences, saved user decisions, security controls and pagination/performance. |
| 0.7.3 | Completed | Clearer entity signals, compact bundles and separate treatment of temporary, persistent, `unavailable`, `unknown` and integration-specific problems. |
| 0.8.0 | Completed | Working quarantine for proven-safe files, batch validation, SHA-256 manifests and safe recovery. |
| 0.9.0 | Completed | Supervisor backup verification, restore testing, retention and explicit post-expiry deletion. |
| 0.9.1 | Completed | Permitted backup verification, reusable evidence, an explicit optional backup choice and selectable entity reviews. |
| 1.0.0 | Released | User-directed cleanup, registry execution, personal content, clean-start controls and hard core-system protection. |
| 1.0.1 | Released | Technical hardening: crash-safe execution, pagination, atomic storage, accessibility and reliable frontend caching. |
| 1.0.2 | Released | Recovery and registry journals, safe configuration synchronization, bounded scan memory, robust request validation and improved bilingual exports. |
| 1.1.0 | Released | Companion reference checks and native Repairs. |
| 1.1.1 | Released | HACS installation support and instructions. |
| 1.2.0 | Prepared | Atomic quarantine, diagnostics, list refresh, documentation/translations, German interface and the companion's “Referenzprüfung” sidebar panel. |

### Practical checks for early testers

- Install or update the new release through the real GitHub/GHCR and HACS workflows.
- Start a full backup and verify completion on Home Assistant OS.
- Move both a safe file and an explicitly accepted review candidate into quarantine.
- Run the restore test and restore that file to its original location.
- Confirm that changed or protected files and incorrect confirmations are blocked.
- Remove a small set of test entities and rehearse recovery from a Home Assistant backup.
- Validate Recorder purge with a small and safe test configuration.
- Test the interface on desktop and mobile.
- Keep the Dutch and English Ingress interface and automatic language selection covered by regression tests.
- Run user tests across several integrations and storage profiles.
- Document known issues and resolve every release-blocking defect.

### 1.0.0 — First public test release

- Released for controlled early testing; report unexpected behaviour with the readable and technical scan reports.
- Stable quarantine and recovery contract.
- Bilingual interface, documentation and Home Assistant settings.
- Only explicitly user-selected entity, device and registry removal through official APIs.
- Safe migration of existing reports, plans and quarantine data.

### After 1.0

- More generic cache profiles with proven recovery behaviour.
- Better storage trends and estimated savings per integration.
- Optional notifications for expired quarantine and persistent entity problems.
- Additional languages through separate translation files.
- Keep registry deletion user-directed; recovery requires a Home Assistant backup.
