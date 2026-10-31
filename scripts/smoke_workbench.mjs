#!/usr/bin/env node
// V30: dependency-free DOM simulation of the offline workbench.
// This does not simulate a complete Chrome browser or verify any external backlink.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { Script } from "node:vm";

const html=readFileSync(new URL("../docs/backlink-submission-workbench.html",import.meta.url),"utf8");
const source=html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert.ok(source,"Executable JS block not found");
const items=JSON.parse(html.match(/<script id="items" type="application\/json">([\s\S]*?)<\/script>/)?.[1]||"null");
const detailed=JSON.parse(html.match(/<script type="application\/json" id="detailedCards">([\s\S]*?)<\/script>/)?.[1]||"null");
assert.equal(items.length,176);
assert.equal(detailed.length,21);
assert.equal(detailed.reduce((s,x)=>s+x.fields.length,0),133);
assert.ok(!/<script[^>]+src=/i.test(html),"No external JS allowed");
assert.ok(!html.includes("fetch("),"No network requests allowed");

const nodes=[],ids=new Map(),storage=new Map(),blobs=[];
class Element {
  constructor(tag,id){this.tag=tag;this.id=id;this.children=[];this.events={};this.style={};this.textContent="";this.value="";this.files=[];nodes.push(this);}
  append(...xs){for(const x of xs){this.children.push(x);if(x&&typeof x==="object")x.parent=this;}}
  replaceChildren(...xs){this.children=xs.flatMap(x=>x?.tag==="fragment"?x.children:[x]);for(const x of this.children)if(x)x.parent=this;}
  addEventListener(k,fn){this.events[k]=fn;}
  click(){this.clicked=true;return this.onclick?.();}
  remove(){if(this.parent)this.parent.children=this.parent.children.filter(x=>x!==this);}
  select(){this.selected=true;}
}
const document={
  body:new Element("body"),
  getElementById(id){if(!ids.has(id))ids.set(id,new Element("div",id));return ids.get(id);},
  createElement(tag){return new Element(tag);},
  createDocumentFragment(){return new Element("fragment");}
};
document.getElementById("items").textContent=JSON.stringify(items);
document.getElementById("detailedCards").textContent=JSON.stringify(detailed);
const localStorage={getItem:key=>storage.get(key)||null,setItem:(key,val)=>storage.set(key,String(val))};
class MockURL{
  constructor(s){const m=String(s).match(/^https?:\/\/([^/]+)/);if(!m)throw new Error("Invalid URL");this.hostname=m[1];}
  static createObjectURL(blob){return "blob:unit-"+blobs.indexOf(blob);}
  static revokeObjectURL(){}
}
class MockBlob{constructor(parts,{type}={}){this.parts=parts;this.type=type;blobs.push(this);}}
const noopTimeout=()=>1;
new Script(source,{filename:"offline-workbench.js"}).runInNewContext({
  document,localStorage,URL:MockURL,Blob:MockBlob,
  navigator:{clipboard:{writeText:async()=>{}}},
  confirm:()=>true,setTimeout:noopTimeout,clearTimeout:()=>{}
});
const $=id=>document.getElementById(id);
assert.equal($("cards").children.length,176,"Initial cards should render");
assert.match($("count").textContent,/176 \/ 176/);
$("search").value="EpicTools";$("search").events.input();
assert.equal($("cards").children.length,1,"EpicTools search should produce exactly one card");
$("search").value="";$("search").events.input();
const tracks=nodes.filter(n=>n.tag==="select"&&n.parent?.className==="track");
assert.ok(tracks.length>=176,"All rows must include local progress controls");
tracks.at(-176).value="已自行提交";tracks.at(-176).onchange();
assert.equal(Object.keys(JSON.parse(storage.get("xibanya-marks-by-domain-v29"))["generadordelettering.org"]).length,1);

$("home").value="https://other-tool.example/";$("home").events.input();$("home").events.change();
assert.equal($("tool").value,"","Switching domain must clear the old editor URL");
assert.match($("marked").textContent,/已标注 0 条/,"New domain cannot inherit old progress");
$("home").value="https://generadordelettering.org/";$("home").events.input();$("home").events.change();
assert.match($("marked").textContent,/已标注 1 条/,"Switching back restores original progress");

$("backup").onclick();
const backup=JSON.parse(blobs.at(-1).parts.join(""));
assert.equal(backup.type,"spanish-backlink-offline-backup");
assert.ok(backup.progress["generadordelettering.org"]);
const restored={
  type:"spanish-backlink-offline-backup",version:1,
  profile:{name:"Restored Website",home:"https://restored.example/",tool:"",es:"Spanish short",en:"English short",eslong:"Spanish long",enlong:"English long",email:""},
  progress:{"restored.example":{"172":{stage:"审核中",note:"=HYPERLINK(\"https://untrusted.test\")"}}}
};
await $("restoreFile").events.change({target:{files:[{size:480,text:async()=>JSON.stringify(restored)}]}});
assert.match($("marked").textContent,/restored.example.*已标注 1 条/);
$("export").onclick();
const exported=blobs.at(-1).parts.join("");
assert.ok(exported.includes("restored.example"));
assert.ok(exported.includes("审核中"));
assert.ok(exported.includes("'=HYPERLINK"),"CSV export must escape spreadsheet formulas");
assert.ok(!exported.includes('"\'"'),"Empty CSV cells must remain empty, not apostrophes");

console.log("PASS: 176 cards, 21 detailed tables, search, per-domain progress, URL reset, JSON backup/restore, CSV formula safety (11 checks).");
