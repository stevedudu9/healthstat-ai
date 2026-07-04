const fs = require("fs");
const vm = require("vm");

const html = fs.readFileSync("outputs/healthstat-ai-multidataset.html", "utf8");
const match = html.match(/<script>([\s\S]*)<\/script>/);
if (!match) throw new Error("script not found");

function makeElement(id = "") {
  return {
    id,
    classList: { toggle() {} },
    style: {},
    value: "",
    textContent: "",
    innerHTML: "",
    dataset: {},
    addEventListener() {},
    getAttribute(name) {
      if (name === "data-risk-input") return this.dataset.riskInput;
      return this[name];
    },
    getBoundingClientRect() {
      return { width: 640, height: 320 };
    },
    getContext() {
      return {
        scale() {},
        clearRect() {},
        fillRect() {},
        fillText() {},
        beginPath() {},
        moveTo() {},
        lineTo() {},
        stroke() {},
        set fillStyle(value) { this._fillStyle = value; },
        get fillStyle() { return this._fillStyle; },
        set font(value) { this._font = value; },
        get font() { return this._font; },
        set textBaseline(value) { this._textBaseline = value; },
        get textBaseline() { return this._textBaseline; },
        set textAlign(value) { this._textAlign = value; },
        get textAlign() { return this._textAlign; }
      };
    }
  };
}

const ids = [
  "sideStatus", "kpiGrid", "detectConfidence", "detectionTimeline", "outcomeLabel",
  "clinicalInsights", "variableMap", "previewLabel", "previewTable", "qualityGrid",
  "summaryLabel", "summaryTable", "simulatorLabel", "riskForm", "scoreRing",
  "riskScore", "riskClass", "riskExplanation", "modelGrid", "templateLabel",
  "interpretationList", "reportBody", "pageTitle", "pageSub", "csvFile", "csvPaste",
  "analyzePaste", "clearPaste", "scorePatient", "downloadReport", "jumpUpload",
  "startUpload", "startDemo", "outcomeChart", "numericChart", "associationChart",
  "importanceChart"
];
const elementMap = new Map(ids.map(id => [id, makeElement(id)]));
const navButtons = ["dashboard", "data", "eda", "model", "explain", "report"].map(section => {
  const el = makeElement();
  el.dataset.section = section;
  return el;
});
const sections = navButtons.map(btn => {
  const el = makeElement(btn.dataset.section);
  return el;
});
const sampleButtons = ["heart", "diabetes", "breast", "stroke"].map(key => {
  const el = makeElement();
  el.dataset.demo = key;
  el.textContent = key;
  return el;
});

const document = {
  body: { scrollWidth: 1280, textContent: "" },
  createElement() {
    return makeElement();
  },
  getElementById(id) {
    if (!elementMap.has(id)) elementMap.set(id, makeElement(id));
    return elementMap.get(id);
  },
  querySelectorAll(selector) {
    if (selector === ".nav-button") return navButtons;
    if (selector === ".sample") return sampleButtons;
    if (selector === ".section") return sections;
    if (selector === "[data-risk-input]") return this.__riskInputs || [];
    return [];
  },
  querySelector(selector) {
    if (selector === ".section.active") return sections[0];
    return null;
  }
};

const sandbox = {
  console,
  document,
  window: { devicePixelRatio: 1, innerWidth: 1280, addEventListener() {} },
  alert(message) { throw new Error(message); },
  Blob: function Blob() {},
  URL: { createObjectURL() { return "blob:test"; }, revokeObjectURL() {} }
};

const tests = `
const results = {};
for (const key of ["heart", "diabetes", "breast", "stroke"]) {
  loadRows(parseCsv(demoData[key]), key + " demo");
  const p = state.profile;
  document.__riskInputs = p.model.features.map(col => {
    const stat = p.stats.find(s => s.col === col);
    const el = { dataset: { riskInput: col }, getAttribute(name) { return name === "data-risk-input" ? col : ""; }, value: "" };
    if (stat && stat.type === "numeric") el.value = String(stat.mean || 0);
    else el.value = String(state.rows.find(r => r[col] !== "")?.[col] || "");
    return el;
  });
  calculateRisk();
  results[key] = {
    detected: p.disease.name,
    target: p.target,
    rows: p.rowCount,
    modelReady: p.model.ready,
    features: p.model.features.length,
    accuracy: p.model.ready ? p.model.metrics.accuracy : null,
    f1: p.model.ready ? p.model.metrics.f1 : null,
    auc: p.model.ready ? p.model.metrics.auc : null,
    riskScore: document.getElementById("riskScore").textContent,
    reportHasModelValidation: document.getElementById("reportBody").innerHTML.includes("Model validation"),
    noBadText: !/[Nn]aN|undefined|null/.test([
      document.getElementById("sideStatus").innerHTML,
      document.getElementById("modelGrid").innerHTML,
      document.getElementById("reportBody").innerHTML,
      document.getElementById("riskExplanation").innerHTML
    ].join(" "))
  };
}
globalThis.__results = results;
`;

vm.runInNewContext(`${match[1]}\n${tests}`, sandbox, { timeout: 5000 });
console.log(JSON.stringify(sandbox.__results, null, 2));
