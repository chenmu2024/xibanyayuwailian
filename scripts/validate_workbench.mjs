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

function parseCSV(input) {
  const records=[];let row=[],cell="",quoted=false;
  input=input.replace(/^\uFEFF/,"");
  for(let i=0;i<input.length;i++){
    const ch=input[i];
    if(ch==='"'){if(quoted&&input[i+1]==='"'){cell+='"';i++;}else quoted=!quoted;}
    else if(ch===","&&!quoted){row.push(cell);cell="";}
    else if((ch==="\n"||ch==="\r")&&!quoted){
      if(ch==="\r"&&input[i+1]==="\n")i++;
      row.push(cell);if(row.some(Boolean))records.push(row);
      row=[];cell="";
    }else cell+=ch;
  }
  if(quoted)throw new Error("Unterminated CSV quoted value");
  if(cell||row.length){row.push(cell);records.push(row);}
  const header=records.shift();
  if(!header)throw new Error("Empty CSV");
  return records.map((values,index)=> {
    if(values.length!==header.length)throw new Error("Malformed CSV row "+(index+2));
    return Object.fromEntries(header.map((key,i)=>[key,values[i]]));
  });
}
const master=parseCSV(readFileSync(new URL("../data/backlinks-master.csv",import.meta.url),"utf8"));
const samples=parseCSV(readFileSync(new URL("../data/v33-published-outbound-rel-samples-20261031.csv",import.meta.url),"utf8"));
const v34Samples=parseCSV(readFileSync(new URL("../data/v34-21-published-link-rel-samples-20261031.csv",import.meta.url),"utf8"));
if(master.length!==176)throw new Error("Master CSV must include 176 records");
if(samples.length!==11)throw new Error("V33 real published href audit must keep 11 public anchor observations");
const p74=samples.filter(v=>v["主库编号"]==="74");
if(p74.length!==3||p74.some(v=>!v["HTML原始rel属性"].split(/\s+/).includes("nofollow")))
  throw new Error("Do not lose public.tools 3/3 published nofollow sample evidence");

const all = readJson("items");
const detailed = readJson("detailedCards");
const v33 = readJson("auditV33");
const v34 = readJson("auditV34");
if(v34.length!==11||!v34.some(x=>x.id===5&&x.rel.includes("nofollow"))||!v34.some(x=>x.id===162&&x.rel.includes("sponsored")))throw new Error("V34 rel audit JSON is incomplete");
if(v34Samples.length!==21)throw new Error("V34 must retain 21 published href/rel audit samples");
const source005=v34Samples.filter(x=>x["主库编号"]==="5");
const source162=v34Samples.filter(x=>x["主库编号"]==="162");
if(source005.length!==1||!source005[0]["实际rel原文"].split(/\s+/).includes("nofollow"))
  throw new Error("Free Tools Directory nofollow example was lost");
if(source162.length!==4||source162.some(x=>!x["实际rel原文"].split(/\s+/).includes("sponsored")))
  throw new Error("UX Resources sponsored samples must remain 4 of 4");

if(v33.length !== 6 || !v33.some(x => x.id === 74 && x.rel.includes("nofollow")))
  throw new Error("V33 sampled rel evidence missing or malformed");

if(master.some((row,i)=>Number(row["编号"])!==all[i].id||
 row["平台/域名"]!==all[i].name||row["提交入口URL"]!==all[i].url||
 row["优先级"]!==all[i].level))
  throw new Error("Workbench source mirror is out of sync with master CSV");
if(all[4].level!=="条件"||all[161].level!=="条件")
  throw new Error("V34: The Free Tools Directory and UX Resources must remain conditional");
if(all[73].status!=="条件"||all[73].level!=="条件")
  throw new Error("public.tools must remain conditional after 3/3 nofollow samples");
if (all.length !== 176 || all.some((x, i) => x.id !== i + 1))
  throw new Error("176-numbered catalog is missing an entry");
if (detailed.length !== 21 || new Set(detailed.map(x => x.id)).size !== 21)
  throw new Error("Expected 21 distinct platform-specific field cards");
if (detailed.some(x => !all.some(i => i.id === x.id) || !x.fields?.length))
  throw new Error("Detailed field card missing its source or field names");
const fieldCount = detailed.reduce((n, x) => n + x.fields.length, 0);
if (fieldCount !== 161) throw new Error("Detailed input field count unexpectedly changed: " + fieldCount);
if (/<script[^>]+src=/i.test(html)) throw new Error("Remote JS is forbidden in offline workbench");
if (!html.includes("xibanya-marks-by-domain-v29") || !html.includes("domainOf(site.home)"))
  throw new Error("User submission marks must remain isolated by site domain");
if (html.includes("fetch(") || html.includes("XMLHttpRequest"))
  throw new Error("Offline workbench must not make network requests");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
if (scripts.length !== 1) throw new Error("Expected exactly one executable inline JavaScript block");
new Script(scripts[0][1], { filename: "backlink-submission-workbench.inline.js" });
console.log("OK: 176 master-linked sources, 21 cards/161 fields; V33 11, V34 21 public href-rel samples, correct nofollow/sponsored status and JS syntax.");
