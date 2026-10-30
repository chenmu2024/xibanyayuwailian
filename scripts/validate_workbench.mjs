#!/usr/bin/env node
// V29 offline-workbench sanity tests. No dependencies or network access.
import { readFileSync } from "node:fs";
import { Script } from "node:vm";

const html = readFileSync(new URL("../docs/backlink-submission-workbench.html", import.meta.url), "utf8");
const readJson = (id) => {
  const escaped = id.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const expression = new RegExp('<script(?:\\s+[^>]*)?\\s+id="' + escaped + '"(?:\\s+[^>]*)?>([\\s\\S]*?)<\\/script>', "i");
  const match = html.match(expression);
  if (!match) throw new Error("Missing JSON data script: " + id);
  return JSON.parse(match[1]);
};
const all = readJson("items");
const detailed = readJson("detailedCards");
if (all.length !== 176 || all.some((x, i) => x.id !== i + 1))
  throw new Error("176-numbered catalog is missing an entry");
if (detailed.length !== 21 || new Set(detailed.map(x => x.id)).size !== 21)
  throw new Error("Expected 21 distinct platform-specific field cards");
if (detailed.some(x => !all.some(i => i.id === x.id) || !x.fields?.length))
  throw new Error("Detailed field card missing its source or field names");
const fieldCount = detailed.reduce((n, x) => n + x.fields.length, 0);
if (fieldCount !== 133) throw new Error("Detailed input field count unexpectedly changed: " + fieldCount);
if (/<script[^>]+src=/i.test(html)) throw new Error("Remote JS is forbidden in offline workbench");
if (!html.includes("xibanya-marks-by-domain-v29") || !html.includes("domainOf(site.home)"))
  throw new Error("User submission marks must remain isolated by site domain");
if (html.includes("fetch(") || html.includes("XMLHttpRequest"))
  throw new Error("Offline workbench must not make network requests");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
if (scripts.length !== 1) throw new Error("Expected exactly one executable inline JavaScript block");
new Script(scripts[0][1], { filename: "backlink-submission-workbench.inline.js" });
console.log("OK: 176 offline sources, 21 exact-field cards, 133 fields, JS syntax valid, domain-isolated progress.");
