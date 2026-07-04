const fs = require("fs");

const html = fs.readFileSync("outputs/healthstat-ai-multidataset.html", "utf8");
const ids = Array.from(html.matchAll(/id="([^"]+)"/g)).map(match => match[1]);
const duplicateIds = Array.from(new Set(ids.filter((id, index) => ids.indexOf(id) !== index)));
const referencedIds = Array.from(html.matchAll(/\$\("([^"]+)"\)/g)).map(match => match[1]);
const missingReferencedIds = Array.from(new Set(referencedIds.filter(id => !ids.includes(id))));
const navSections = Array.from(html.matchAll(/data-section="([^"]+)"/g)).map(match => match[1]);
const sectionIds = Array.from(html.matchAll(/<section class="section[^"]*" id="([^"]+)"/g)).map(match => match[1]);
const missingSections = Array.from(new Set(navSections.filter(section => !sectionIds.includes(section))));

console.log(JSON.stringify({
  idCount: ids.length,
  duplicateIds,
  referencedIdCount: referencedIds.length,
  missingReferencedIds,
  navSections: Array.from(new Set(navSections)),
  missingSections
}, null, 2));
