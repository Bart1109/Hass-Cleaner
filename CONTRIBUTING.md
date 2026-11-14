# Mitarbeit an Hass-Cleaner

Danke, dass du Hass-Cleaner verbessern willst. Sicherheit geht immer vor zusätzlichem Aufräumgewinn.

## Entwicklungsregeln

- Datei- und Registerscans bleiben ausschließlich lesend.
- Jede neue Aufräumregel prüft Typ, Erzeuger, Mindestalter, geschützte Bereiche und den Weg zur Wiederherstellung.
- `unavailable`, `unknown` oder ein integrationsspezifisches Offline-Signal sind nie für sich genommen ein Beweis, dass gelöscht werden darf.
- Für jede Verhaltensänderung gehören Tests dazu.
- Niemals Token, geheime Werte, rohe `.storage`-Inhalte oder private Berichte in Issues oder Commits aufnehmen.

## Lokale Prüfung

```powershell
cd hass_cleaner
python -m unittest discover -s tests -v
node --check web/assets/app.js
```

Optional `pre-commit` installieren und `pre-commit run --all-files` ausführen.

## Pull Requests

Beschreibe, was sich ändert, warum es sicher ist, was bei Fehlern passieren kann und wie die Wiederherstellung funktioniert. Halte Änderungen klein und vermeide unzusammenhängende Formatierungen.

## Nederlands

Bedankt dat je Hass-Cleaner wilt verbeteren. Veiligheid gaat altijd voor extra opruimwinst.

### Ontwikkelregels

- Bestands- en registerscans moeten read-only blijven.
- Een nieuwe opruimregel controleert type, producer, minimumleeftijd, beschermde scopes en herstelroute.
- `unavailable`, `unknown` of een integratiespecifiek offline-signaal is nooit zelfstandig verwijderbewijs.
- Voeg voor iedere gedragswijziging tests toe.
- Neem nooit tokens, geheime waarden, ruwe `.storage`-inhoud of privérapporten op in issues of commits.

### Lokale controle

```powershell
cd hass_cleaner
python -m unittest discover -s tests -v
node --check web/assets/app.js
```

Installeer optioneel `pre-commit` en voer `pre-commit run --all-files` uit.

### Pull requests

Beschrijf wat verandert, waarom het veilig is, wat er bij fouten kan gebeuren en hoe herstel werkt. Houd wijzigingen klein en vermijd ongerelateerde formattering.
