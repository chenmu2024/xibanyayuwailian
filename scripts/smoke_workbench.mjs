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
const recent=JSON.parse(html.match(/<script type="application\/json" id="auditV31">([\s\S]*?)<\/script>/)?.[1]||"null");
const v32=JSON.parse(html.match(/<script type="application\/json" id="auditV32">([\s\S]*?)<\/script>/)?.[1]||"null");
const v33=JSON.parse(html.match(/<script type="application\/json" id="auditV33">([\s\S]*?)<\/script>/)?.[1]||"null");
const v34=JSON.parse(html.match(/<script type="application\/json" id="auditV34">([\s\S]*?)<\/script>/)?.[1]||"null");
assert.equal(v34.length,11);
assert.ok(v34.some(x=>x.id===162&&x.rel.includes("sponsored")));
assert.equal(v33.length,6);
assert.ok(v33.find(x=>x.id===74).rel.includes("nofollow"));
assert.equal(v32.length,14);
assert.equal(recent.length,17);
assert.equal(items.length,176);
assert.equal(detailed.length,21);
assert.equal(detailed.reduce((s,x)=>s+x.fields.length,0),161);
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
document.getElementById("auditV31").textContent=JSON.stringify(recent);
document.getElementById("auditV32").textContent=JSON.stringify(v32);
document.getElementById("auditV33").textContent=JSON.stringify(v33);
document.getElementById("auditV34").textContent=JSON.stringify(v34);
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
$("sort").value="follow";$("sort").events.change();
const topFive=$("cards").children.slice(0,5).map(node=>node.children[0].children[0].children[0].textContent);
assert.equal(topFive.join(","),"#075,#168,#148,#151,#128","V33 observed non-nofollow sample priorities must appear first");
$("sort").value="design";$("sort").events.change();
const designTop=$("cards").children.slice(0,5).map(node=>node.children[0].children[0].children[0].textContent);
assert.equal(designTop.join(","),"#159,#163,#164,#172,#165","V34 typography/design published-source sample ordering regression");
$("sort").value="id";$("sort").events.change();
$("search").value="EpicTools";$("search").events.input();
assert.equal($("cards").children.length,1,"EpicTools search should produce exactly one card");
$("search").value="";$("search").events.input();
const tracks=nodes.filter(n=>n.tag==="select"&&n.parent?.className==="track");
assert.ok(tracks.length>=176,"All rows must include local progress controls");
tracks.at(-176).value="已自行提交";tracks.at(-176).onchange();
assert.equal(Object.keys(JSON.parse(storage.get("xibanya-marks-by-domain-v29"))["generadordelettering.org"]).length,1);

const proofBoxes=nodes.filter(n=>n.className==="proof");
assert.ok(proofBoxes.length>=176,"Each directory needs a manual evidence panel");
const proofBox=proofBoxes.at(-176);
const proofInputs=proofBox.children.filter(n=>n.tag==="input");
const selfCheck=proofBox.children.find(n=>n.className==="verify");
assert.equal(proofInputs.length,3);
assert.ok(selfCheck);
proofInputs[0].value="https://generadordelettering.org/editor";
proofInputs[1].value="https://generadordelettering.org/";
proofInputs[2].value="noopener noreferrer nofollow";
selfCheck.onclick();
let stored=JSON.parse(storage.get("xibanya-marks-by-domain-v29"));
assert.ok(!stored["generadordelettering.org"]["1"].proof?.checked,"Self-domain source must never be marked as external proof");
proofInputs[0].value="https://example-directory.test/tools/lettering";
proofInputs.forEach(n=>n.events.change());
stored=JSON.parse(storage.get("xibanya-marks-by-domain-v29"));
assert.equal(stored["generadordelettering.org"]["1"].proof.checked,false,"Editing proof only saves a draft");
selfCheck.onclick();
stored=JSON.parse(storage.get("xibanya-marks-by-domain-v29"));
assert.equal(stored["generadordelettering.org"]["1"].proof.checked,true,"Explicit self-check should save attestation");
assert.equal(stored["generadordelettering.org"]["1"].proof.rel,"noopener noreferrer nofollow");
assert.match($("marked").textContent,/人工自查证据 1 条/);
proofInputs[2].value="noopener sponsored";proofInputs[2].events.change();
stored=JSON.parse(storage.get("xibanya-marks-by-domain-v29"));
assert.equal(stored["generadordelettering.org"]["1"].proof.checked,false,"Rel edits revoke prior self-attestation");
selfCheck.onclick();
assert.match($("marked").textContent,/人工自查证据 1 条/);


$("home").value="https://other-tool.example/";$("home").events.input();$("home").events.change();
assert.equal($("tool").value,"","Switching domain must clear the old editor URL");
assert.match($("marked").textContent,/已标注 0 条/,"New domain cannot inherit old progress");
assert.match($("marked").textContent,/人工自查证据 0 条/,"Other domains cannot inherit manual backlink evidence");
$("home").value="https://generadordelettering.org/";$("home").events.input();$("home").events.change();
assert.match($("marked").textContent,/已标注 1 条/,"Switching back restores original progress");

$("backup").onclick();
const backup=JSON.parse(blobs.at(-1).parts.join(""));
assert.equal(backup.type,"spanish-backlink-offline-backup");
assert.ok(backup.progress["generadordelettering.org"]);
assert.equal(backup.progress["generadordelettering.org"]["1"].proof.checked,true);
assert.equal(backup.progress["generadordelettering.org"]["1"].proof.rel,"noopener sponsored");
const restored={
  type:"spanish-backlink-offline-backup",version:1,
  profile:{name:"Restored Website",home:"https://restored.example/",tool:"",es:"Spanish short",en:"English short",eslong:"Spanish long",enlong:"English long",email:""},
  progress:{"restored.example":{"172":{stage:"审核中",note:"=HYPERLINK(\"https://untrusted.test\")",proof:{source:"https://directory.valid.org/tools/restored",href:"https://restored.example/",rel:"(none)",checked:true,checkedAt:"2026-10-31"}}}}
};
const invalidCopy=JSON.parse(JSON.stringify(restored));
invalidCopy.progress["restored.example"]["172"].proof.href="https://restored.example.evil.com/";
const beforeInvalid=storage.get("xibanya-marks-by-domain-v29");
await $("restoreFile").events.change({target:{files:[{size:750,text:async()=>JSON.stringify(invalidCopy)}]}});
assert.equal(storage.get("xibanya-marks-by-domain-v29"),beforeInvalid,"Invalid restored proof must not overwrite the user's local data");
await $("restoreFile").events.change({target:{files:[{size:480,text:async()=>JSON.stringify(restored)}]}});
assert.match($("marked").textContent,/restored.example.*已标注 1 条/);
assert.match($("marked").textContent,/人工自查证据 1 条/,"Confirmed manual evidence should survive JSON restore");
$("export").onclick();
const exported=blobs.at(-1).parts.join("");
assert.ok(exported.includes("restored.example"));
assert.ok(exported.includes("审核中"));
assert.ok(exported.includes("第三方公开页")&&exported.includes("实际目标href")&&exported.includes("rel原文"),"CSV needs evidence columns");
assert.ok(exported.includes("https://directory.valid.org/tools/restored")&&exported.includes("本人确认"),"Verified local evidence must export with its source URL");
assert.ok(exported.includes("'=HYPERLINK"),"CSV export must escape spreadsheet formulas");
assert.ok(!exported.includes('"\'"'),"Empty CSV cells must remain empty, not apostrophes");

console.log("PASS: 176 cards, 21 detailed tables, search, per-domain progress, URL reset, JSON backup/restore, CSV formula safety (17 checks including explicit manual href/rel evidence, domain isolation, revocation and V34 typography sorting).");
