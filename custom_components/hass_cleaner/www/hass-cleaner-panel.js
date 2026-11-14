/**
 * Hass-Cleaner sidebar panel: missing static references.
 *
 * Read-only. The panel asks the existing WebSocket command
 * `hass_cleaner/references` for the last report and renders the entries with
 * `missing: true`. Terms, column order and coverage follow the Hass-Cleaner
 * app's reference view (source / target type / target / location / coverage).
 *
 * All values come from configuration data, so they are only ever inserted as
 * text nodes, never as HTML.
 */

const TYPE_LABELS = {
  de: {
    entity: "Entität",
    device: "Gerät",
    area: "Bereich",
    action: "Aktion",
    statistic: "Statistik",
    entity_registry: "Entitätsregistrierung",
  },
  en: {
    entity: "Entity",
    device: "Device",
    area: "Area",
    action: "Action",
    statistic: "Statistic",
    entity_registry: "Entity registry",
  },
  nl: {
    entity: "Entiteit",
    device: "Apparaat",
    area: "Gebied",
    action: "Actie",
    statistic: "Statistiek",
    entity_registry: "Entiteitenregister",
  },
};

const KIND_LABELS = {
  de: {
    automation: "Automatisierung",
    script: "Skript",
    dashboard: "Dashboard",
    scene: "Szene",
    group: "Gruppe",
    helper: "Helfer",
    template: "Template",
    statistics: "Statistik",
    energy: "Energie",
  },
  en: {
    automation: "Automation",
    script: "Script",
    dashboard: "Dashboard",
    scene: "Scene",
    group: "Group",
    helper: "Helper",
    template: "Template",
    statistics: "Statistics",
    energy: "Energy",
  },
  nl: {
    automation: "Automatisering",
    script: "Script",
    dashboard: "Dashboard",
    scene: "Scène",
    group: "Groep",
    helper: "Helper",
    template: "Template",
    statistics: "Statistiek",
    energy: "Energie",
  },
};

const STRINGS = {
  de: {
    title: "Referenzprüfung",
    subtitle:
      "Statische Verweise, die ins Leere zeigen. Nur lesend – es wird nichts geändert.",
    refresh: "Neu prüfen",
    refreshing: "Prüfe …",
    search: "Suchen",
    searchPlaceholder: "Ziel, Quelle oder Pfad",
    allKinds: "Alle Quellen",
    allTypes: "Alle Zieltypen",
    count: "{shown} von {total}",
    empty: "Keine toten Verweise gefunden.",
    noReport: "Noch kein Bericht. Starte eine Prüfung.",
    loading: "Bericht wird geladen …",
    error: "Bericht nicht verfügbar ({code}).",
    checkedAt: "Geprüft: {time}",
    statusCompleted: "Vollständig geprüft",
    statusPartial: "Teilweise geprüft",
    statusUnavailable: "Nicht verfügbar",
    statusStarting: "Startet noch",
    incomplete:
      "Bei {count} Quelle(n) ist die Prüfung unvollständig – die Liste kann Lücken haben.",
    colTarget: "Ziel",
    colType: "Zieltyp",
    colSource: "Quelle",
    colPath: "Pfad",
    coverage: "Abdeckung",
    coverageChecked: "geprüft",
    coveragePartial: "teilweise",
    coverageUnavailable: "nicht verfügbar",
    openApp: "App öffnen",
    appHint:
      "Scan, Quarantäne, Registeraufräumen und Exporte gibt es in der Hass-Cleaner-App.",
  },
  en: {
    title: "Reference checks",
    subtitle:
      "Static references that point nowhere. Read-only – nothing is changed.",
    refresh: "Check again",
    refreshing: "Checking …",
    search: "Search",
    searchPlaceholder: "Target, source or path",
    allKinds: "All sources",
    allTypes: "All target types",
    count: "{shown} of {total}",
    empty: "No missing references found.",
    noReport: "No report yet. Start a check.",
    loading: "Loading report …",
    error: "Report unavailable ({code}).",
    checkedAt: "Checked: {time}",
    statusCompleted: "Fully checked",
    statusPartial: "Partially checked",
    statusUnavailable: "Unavailable",
    statusStarting: "Starting",
    incomplete:
      "{count} source(s) could not be checked completely – the list may have gaps.",
    colTarget: "Target",
    colType: "Target type",
    colSource: "Source",
    colPath: "Location",
    coverage: "Coverage",
    coverageChecked: "checked",
    coveragePartial: "partial",
    coverageUnavailable: "unavailable",
    openApp: "Open app",
    appHint:
      "Scan, quarantine, registry cleanup and exports live in the Hass-Cleaner app.",
  },
  nl: {
    title: "Referentiecontrole",
    subtitle:
      "Statische verwijzingen zonder doel. Alleen lezen – er wordt niets gewijzigd.",
    refresh: "Opnieuw controleren",
    refreshing: "Bezig …",
    search: "Zoeken",
    searchPlaceholder: "Doel, bron of pad",
    allKinds: "Alle bronnen",
    allTypes: "Alle doeltypen",
    count: "{shown} van {total}",
    empty: "Geen dode verwijzingen gevonden.",
    noReport: "Nog geen rapport. Start een controle.",
    loading: "Rapport wordt geladen …",
    error: "Rapport niet beschikbaar ({code}).",
    checkedAt: "Gecontroleerd: {time}",
    statusCompleted: "Volledig gecontroleerd",
    statusPartial: "Gedeeltelijk gecontroleerd",
    statusUnavailable: "Niet beschikbaar",
    statusStarting: "Start nog",
    incomplete:
      "Bij {count} bron(nen) is de controle onvolledig – de lijst kan gaten hebben.",
    colTarget: "Doel",
    colType: "Doeltype",
    colSource: "Bron",
    colPath: "Locatie",
    coverage: "Dekking",
    coverageChecked: "gecontroleerd",
    coveragePartial: "gedeeltelijk",
    coverageUnavailable: "niet beschikbaar",
    openApp: "App openen",
    appHint:
      "Scan, quarantaine, registeropschoning en exports staan in de Hass-Cleaner-app.",
  },
};

const STYLE = `
  :host {
    display: block;
    height: 100%;
    overflow: auto;
    background: var(--primary-background-color);
    color: var(--primary-text-color);
  }
  .wrap {
    max-width: 1200px;
    margin: 0 auto;
    padding: 16px;
    box-sizing: border-box;
  }
  header {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 8px 16px;
    margin-bottom: 4px;
  }
  h1 {
    font-size: 20px;
    font-weight: 500;
    margin: 0;
  }
  .subtitle {
    color: var(--secondary-text-color);
    font-size: 14px;
    flex: 1 1 300px;
  }
  .actions {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  button {
    font: inherit;
    color: var(--text-primary-color, #fff);
    background: var(--primary-color);
    border: none;
    border-radius: 4px;
    padding: 8px 14px;
    cursor: pointer;
  }
  button[disabled] {
    opacity: 0.6;
    cursor: default;
  }
  a {
    color: var(--primary-color);
    font-size: 14px;
  }
  .meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px 16px;
    align-items: center;
    font-size: 14px;
    color: var(--secondary-text-color);
    margin: 8px 0 12px;
  }
  .chip {
    border-radius: 12px;
    padding: 2px 10px;
    font-size: 13px;
    border: 1px solid var(--divider-color);
  }
  .chip.partial {
    border-color: var(--warning-color, #ffa600);
    color: var(--warning-color, #ffa600);
  }
  .chip.unavailable {
    border-color: var(--error-color, #db4437);
    color: var(--error-color, #db4437);
  }
  .notice {
    border-left: 4px solid var(--warning-color, #ffa600);
    background: var(--card-background-color);
    padding: 10px 12px;
    font-size: 14px;
    border-radius: 4px;
    margin-bottom: 12px;
  }
  .toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 12px;
  }
  .toolbar input,
  .toolbar select {
    font: inherit;
    color: var(--primary-text-color);
    background: var(--card-background-color);
    border: 1px solid var(--divider-color);
    border-radius: 4px;
    padding: 8px 10px;
  }
  .toolbar input {
    flex: 1 1 240px;
  }
  .table {
    background: var(--card-background-color);
    border-radius: 4px;
    overflow: hidden;
  }
  .head,
  .row {
    display: grid;
    grid-template-columns:
      minmax(180px, 1.4fr) 130px minmax(150px, 1fr) minmax(200px, 1.6fr);
    gap: 4px 16px;
    padding: 10px 12px;
    align-items: baseline;
  }
  .head {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--secondary-text-color);
    border-bottom: 1px solid var(--divider-color);
    padding-bottom: 8px;
  }
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .row {
    border-bottom: 1px solid var(--divider-color);
  }
  .row:last-child {
    border-bottom: none;
  }
  .target,
  .path {
    font-family: var(--code-font-family, monospace);
    font-size: 14px;
    word-break: break-all;
  }
  .path {
    color: var(--secondary-text-color);
    font-size: 13px;
  }
  .type {
    font-size: 13px;
    color: var(--secondary-text-color);
  }
  .source {
    font-size: 14px;
    word-break: break-word;
  }
  .source small {
    display: block;
    color: var(--secondary-text-color);
    font-size: 12px;
  }
  .state {
    color: var(--secondary-text-color);
    font-size: 15px;
    padding: 24px 0;
  }
  details {
    margin-top: 12px;
    font-size: 14px;
    color: var(--secondary-text-color);
  }
  details summary {
    cursor: pointer;
  }
  details ul {
    margin-top: 8px;
  }
  details li {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding: 4px 0;
    border-bottom: 1px solid var(--divider-color);
  }
  .hint {
    margin-top: 12px;
    font-size: 13px;
    color: var(--secondary-text-color);
  }
  .sr {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(0 0 0 0);
  }
  @media (max-width: 700px) {
    .head { display: none; }
    .row { grid-template-columns: 1fr; }
    .type::before { content: ""; }
  }
`;

class HassCleanerPanel extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this._hass = null;
    this._report = null;
    this._error = null;
    this._loading = false;
    this._filters = { text: "", kind: "", type: "" };
    this._built = false;
    this._language = "en";
  }

  set hass(hass) {
    const first = this._hass === null;
    this._hass = hass;
    this._language = this._detectLanguage(hass);
    if (!this._built) {
      this._build();
    }
    this._applyText();
    if (first) {
      this._load();
    }
  }

  set narrow(narrow) {
    this._narrow = narrow;
  }

  set panel(panel) {
    this._panel = panel;
  }

  _detectLanguage(hass) {
    const raw =
      (hass && hass.locale && hass.locale.language) ||
      (hass && hass.language) ||
      "en";
    const short = String(raw).split("-")[0].toLowerCase();
    return STRINGS[short] ? short : "en";
  }

  _t(key, values) {
    let text = (STRINGS[this._language] || STRINGS.en)[key] || STRINGS.en[key] || key;
    if (values) {
      for (const [name, value] of Object.entries(values)) {
        text = text.replace(`{${name}}`, value);
      }
    }
    return text;
  }

  _label(dictionary, key) {
    const table = dictionary[this._language] || dictionary.en;
    return table[key] || key;
  }

  _build() {
    const style = document.createElement("style");
    style.textContent = STYLE;

    const wrap = document.createElement("div");
    wrap.className = "wrap";

    const header = document.createElement("header");
    this._title = document.createElement("h1");
    this._subtitle = document.createElement("div");
    this._subtitle.className = "subtitle";
    const actions = document.createElement("div");
    actions.className = "actions";
    this._refreshButton = document.createElement("button");
    this._refreshButton.type = "button";
    this._refreshButton.addEventListener("click", () => this._load(true));
    this._appLink = document.createElement("a");
    this._appLink.href = "/config/apps";
    actions.append(this._refreshButton, this._appLink);
    header.append(this._title, this._subtitle, actions);

    const meta = document.createElement("div");
    meta.className = "meta";
    this._statusChip = document.createElement("span");
    this._statusChip.className = "chip";
    this._checkedAt = document.createElement("span");
    this._count = document.createElement("span");
    meta.append(this._statusChip, this._checkedAt, this._count);

    this._notice = document.createElement("div");
    this._notice.className = "notice";
    this._notice.hidden = true;

    const toolbar = document.createElement("div");
    toolbar.className = "toolbar";

    const searchLabel = document.createElement("label");
    searchLabel.className = "sr";
    this._searchLabel = searchLabel;
    this._search = document.createElement("input");
    this._search.type = "search";
    this._search.addEventListener("input", () => {
      this._filters.text = this._search.value.trim().toLowerCase();
      this._renderList();
    });
    searchLabel.append(this._search);

    this._kindLabel = document.createElement("label");
    this._kindLabel.className = "sr";
    this._kind = document.createElement("select");
    this._kind.addEventListener("change", () => {
      this._filters.kind = this._kind.value;
      this._renderList();
    });
    this._kindLabel.append(this._kind);

    this._typeLabel = document.createElement("label");
    this._typeLabel.className = "sr";
    this._type = document.createElement("select");
    this._type.addEventListener("change", () => {
      this._filters.type = this._type.value;
      this._renderList();
    });
    this._typeLabel.append(this._type);

    toolbar.append(searchLabel, this._kindLabel, this._typeLabel);

    this._table = document.createElement("div");
    this._table.className = "table";
    this._head = document.createElement("div");
    this._head.className = "head";
    this._list = document.createElement("ul");
    this._table.append(this._head, this._list);

    this._state = document.createElement("div");
    this._state.className = "state";

    this._coverage = document.createElement("details");
    this._coverageSummary = document.createElement("summary");
    this._coverageList = document.createElement("ul");
    this._coverage.append(this._coverageSummary, this._coverageList);
    this._coverage.hidden = true;

    this._hint = document.createElement("div");
    this._hint.className = "hint";

    wrap.append(
      header,
      meta,
      this._notice,
      toolbar,
      this._table,
      this._state,
      this._coverage,
      this._hint
    );
    this.shadowRoot.append(style, wrap);
    this._built = true;
  }

  _applyText() {
    this._title.textContent = this._t("title");
    this._subtitle.textContent = this._t("subtitle");
    this._refreshButton.textContent = this._loading
      ? this._t("refreshing")
      : this._t("refresh");
    this._refreshButton.disabled = this._loading;
    this._appLink.textContent = this._t("openApp");
    this._appLink.title = this._t("appHint");
    this._hint.textContent = this._t("appHint");
    this._searchLabel.setAttribute("aria-label", this._t("search"));
    this._search.placeholder = this._t("searchPlaceholder");
    this._kindLabel.setAttribute("aria-label", this._t("allKinds"));
    this._typeLabel.setAttribute("aria-label", this._t("allTypes"));

    const columns = [
      this._t("colTarget"),
      this._t("colType"),
      this._t("colSource"),
      this._t("colPath"),
    ];
    this._head.replaceChildren(
      ...columns.map((text) => {
        const cell = document.createElement("span");
        cell.textContent = text;
        return cell;
      })
    );

    this._renderStatus();
    this._renderCoverage();
    this._renderFilters();
    this._renderList();
  }

  async _load(refresh) {
    if (!this._hass || this._loading) {
      return;
    }
    this._loading = true;
    this._error = null;
    this._applyText();
    try {
      this._report = await this._hass.callWS({
        type: "hass_cleaner/references",
        refresh: refresh === true,
      });
    } catch (error) {
      this._report = null;
      this._error = (error && (error.code || error.message)) || "unknown";
    } finally {
      this._loading = false;
      this._applyText();
    }
  }

  _missing() {
    const references = (this._report && this._report.references) || [];
    return references.filter((reference) => reference.missing === true);
  }

  _renderStatus() {
    const report = this._report;
    if (!report) {
      this._statusChip.textContent = "";
      this._statusChip.hidden = true;
      this._checkedAt.textContent = "";
      this._count.textContent = "";
      this._notice.hidden = true;
      return;
    }
    const status = report.status || "unavailable";
    const labelKey =
      status === "completed"
        ? "statusCompleted"
        : status === "partial"
          ? "statusPartial"
          : status === "starting"
            ? "statusStarting"
            : "statusUnavailable";
    this._statusChip.hidden = false;
    this._statusChip.className = `chip ${status}`;
    this._statusChip.textContent = this._t(labelKey);

    if (report.checked_at) {
      const date = new Date(report.checked_at);
      const time = Number.isNaN(date.getTime())
        ? report.checked_at
        : date.toLocaleString(this._language);
      this._checkedAt.textContent = this._t("checkedAt", { time });
    } else {
      this._checkedAt.textContent = "";
    }

    const incomplete = (report.sources || []).filter(
      (source) => source.status !== "checked"
    ).length;
    this._notice.hidden = incomplete === 0;
    if (incomplete > 0) {
      this._notice.textContent = this._t("incomplete", { count: incomplete });
    }
  }

  _renderCoverage() {
    const sources = (this._report && this._report.sources) || [];
    this._coverage.hidden = sources.length === 0;
    if (sources.length === 0) {
      this._coverageList.replaceChildren();
      return;
    }
    const labelFor = (status) =>
      status === "checked"
        ? this._t("coverageChecked")
        : status === "partial"
          ? this._t("coveragePartial")
          : this._t("coverageUnavailable");
    this._coverageSummary.textContent = `${this._t("coverage")} (${sources.length})`;
    this._coverageList.replaceChildren(
      ...sources.map((source) => {
        const row = document.createElement("li");
        const name = document.createElement("span");
        name.textContent = source.name || source.id;
        const value = document.createElement("span");
        value.textContent = labelFor(source.status);
        row.append(name, value);
        return row;
      })
    );
  }

  _renderFilters() {
    const previousKind = this._filters.kind;
    const previousType = this._filters.type;
    const missing = this._missing();
    const kinds = [...new Set(missing.map((item) => item.source_kind))].sort();
    const types = [...new Set(missing.map((item) => item.target_type))].sort();

    const fill = (select, values, allLabel, labelFor, selected) => {
      select.replaceChildren();
      const all = document.createElement("option");
      all.value = "";
      all.textContent = allLabel;
      select.append(all);
      for (const value of values) {
        const option = document.createElement("option");
        option.value = value;
        option.textContent = labelFor(value);
        select.append(option);
      }
      select.value = values.includes(selected) ? selected : "";
    };

    fill(
      this._kind,
      kinds,
      this._t("allKinds"),
      (value) => this._label(KIND_LABELS, value),
      previousKind
    );
    fill(
      this._type,
      types,
      this._t("allTypes"),
      (value) => this._label(TYPE_LABELS, value),
      previousType
    );
    this._filters.kind = this._kind.value;
    this._filters.type = this._type.value;
  }

  _visible() {
    const { text, kind, type } = this._filters;
    return this._missing().filter((item) => {
      if (kind && item.source_kind !== kind) {
        return false;
      }
      if (type && item.target_type !== type) {
        return false;
      }
      if (!text) {
        return true;
      }
      return [
        item.target_id,
        item.source_name,
        item.location,
        item.target_type,
        item.source_kind,
      ]
        .filter(Boolean)
        .some((value) => String(value).toLowerCase().includes(text));
    });
  }

  _renderList() {
    if (!this._built) {
      return;
    }
    const total = this._missing().length;
    const visible = this._visible();
    this._count.textContent = this._report
      ? this._t("count", { shown: visible.length, total })
      : "";

    if (this._loading && !this._report) {
      this._showState(this._t("loading"));
      return;
    }
    if (this._error) {
      this._showState(this._t("error", { code: this._error }));
      return;
    }
    if (!this._report) {
      this._showState(this._t("noReport"));
      return;
    }
    if (visible.length === 0) {
      this._showState(
        total === 0
          ? this._t("empty")
          : this._t("count", { shown: 0, total })
      );
      return;
    }

    this._state.hidden = true;
    this._table.hidden = false;
    this._list.replaceChildren(
      ...visible.map((item) => {
        const row = document.createElement("li");
        row.className = "row";

        const target = document.createElement("span");
        target.className = "target";
        target.textContent = item.target_id;

        const type = document.createElement("span");
        type.className = "type";
        type.textContent = this._label(TYPE_LABELS, item.target_type);

        const source = document.createElement("span");
        source.className = "source";
        source.textContent = item.source_name;
        const kind = document.createElement("small");
        kind.textContent = this._label(KIND_LABELS, item.source_kind);
        source.append(kind);

        const path = document.createElement("span");
        path.className = "path";
        path.textContent = item.location;

        row.append(target, type, source, path);
        return row;
      })
    );
  }

  _showState(message) {
    this._state.hidden = false;
    this._state.textContent = message;
    this._table.hidden = true;
    this._list.replaceChildren();
  }
}

if (!customElements.get("hass-cleaner-panel")) {
  customElements.define("hass-cleaner-panel", HassCleanerPanel);
}
