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
assert.equal(items.filter(x=>x.level==="P1"&&x.p1Proof).length,13,"All P1 cards need V47 published-link evidence");
assert.equal(items.filter(x=>x.level==="P1"&&x.p1Proof?.href).length,11,"Exactly 11 P1 sources with directly observed third-party href");
assert.equal(items.filter(x=>x.level==="P1"&&x.p1Proof?.rawRel).length,6,"Old raw-rel evidence must be explicitly separated from current href");
assert.equal(items.find(x=>x.id===149).p1Proof.href,"https://anyfyle.com/?ref=pepliohub","Peplio href tracking query is part of the observed destination");
assert.equal(items.find(x=>x.id===58).level,"P2","Actual practice-sheet resources qualify Educaguía for a reviewable P2 application");
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
  constructor(s){const m=String(s).match(/^(https?):\/\/([^/]+)/);if(!m)throw new Error("Invalid URL");this.protocol=m[1]+":";this.hostname=m[2];}
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
assert.equal(topFive.slice(0,4).join(","),"#075,#148,#151,#128","Active direct-outbound sample candidates must precede conditional redirect sites");
assert.ok(!topFive.includes("#168"),"Conditional #168 cannot outrank active P1/P2 candidates");
$("sort").value="design";$("sort").events.change();
const designTop=$("cards").children.slice(0,5).map(node=>node.children[0].children[0].children[0].textContent);
assert.equal(designTop.join(","),"#159,#163,#164,#075,#148","Design sorting reflects current P1/P2 eligibility and direct evidence");
assert.ok(!designTop.includes("#172")&&!designTop.includes("#171"),"Downgraded sources should not float to design first five");
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
assert.equal($("name").value,"","New domain must not inherit the old site name");
assert.equal($("en").value,"","New domain must not inherit old English marketing copy");
assert.equal($("eslong").value,"","New domain must not inherit old Spanish long description");
assert.equal($("email").value,"","New domain must not inherit previous contact email");
assert.equal($("edu").value,"","New domain must not inherit Generador education URL");
$("edu").value="https://generadordelettering.org/herramientas/plantillas-practica";$("edu").events.input();$("edu").events.change();
assert.equal($("edu").value,"","Foreign education URL must be rejected");
$("edu").value="https://other-tool.example/learning/real";$("edu").events.input();$("edu").events.change();
assert.equal($("edu").value,"https://other-tool.example/learning/real","Local educational page should be accepted");
$("name").value="Another Spanish Tool";$("name").events.input();
$("en").value="Unique English copy for the second site";$("en").events.input();
$("es").value="Descripción española del segundo sitio";$("es").events.input();
$("email").value="owner@other-tool.example";$("email").events.input();
$("tool").value="https://other-tool.example/editor";$("tool").events.input();
let profiles=JSON.parse(storage.get("xibanya-profiles-by-domain-v36"));
assert.equal(profiles["other-tool.example"].email,"owner@other-tool.example");
assert.equal(profiles["other-tool.example"].edu,"https://other-tool.example/learning/real","Second-site education URL must persist independently");
assert.equal(profiles["generadordelettering.org"].name,"Generador de Lettering");

assert.match($("marked").textContent,/已标注 0 条/,"New domain cannot inherit old progress");
assert.match($("marked").textContent,/人工自查证据 0 条/,"Other domains cannot inherit manual backlink evidence");
$("home").value="https://generadordelettering.org/";$("home").events.input();$("home").events.change();
assert.match($("marked").textContent,/已标注 1 条/,"Switching back restores original progress");
assert.equal($("name").value,"Generador de Lettering","Switching back should restore original site identity");
assert.equal($("tool").value,"https://generadordelettering.org/editor","Switching back should restore original editor URL");
assert.equal($("edu").value,"https://generadordelettering.org/herramientas/plantillas-practica","First site keeps its own education URL");
assert.equal($("email").value,"","Contact email cannot leak from another site");
$("home").value="https://other-tool.example/";$("home").events.input();$("home").events.change();
assert.equal($("name").value,"Another Spanish Tool","Second site profile must survive switching away and back");
assert.equal($("email").value,"owner@other-tool.example","Second site's email must be restored only on the right domain");
assert.equal($("tool").value,"https://other-tool.example/editor","Second editor URL must not be replaced by Lettering");
assert.equal($("edu").value,"https://other-tool.example/learning/real","Second site keeps its own education URL");
$("home").value="https://generadordelettering.org/";$("home").events.input();$("home").events.change();


$("backup").onclick();
const backup=JSON.parse(blobs.at(-1).parts.join(""));
assert.equal(backup.type,"spanish-backlink-offline-backup");
assert.equal(backup.version,2,"New backup must include per-domain profiles");
assert.equal(backup.profiles["other-tool.example"].email,"owner@other-tool.example");
assert.equal(backup.profiles["other-tool.example"].edu,"https://other-tool.example/learning/real","New V2 backup includes educational resources");
const oldV2=JSON.parse(JSON.stringify(backup));delete oldV2.profile.edu;
for(const profile of Object.values(oldV2.profiles))delete profile.edu;
assert.equal(backup.profiles["generadordelettering.org"].name,"Generador de Lettering");
const tampered=JSON.parse(JSON.stringify(backup));
tampered.profiles["other-tool.example"].home="https://generadordelettering.org/";
const beforeTampered=storage.get("xibanya-profiles-by-domain-v36");
await $("restoreFile").events.change({target:{files:[{size:950,text:async()=>JSON.stringify(tampered)}]}});
assert.equal(storage.get("xibanya-profiles-by-domain-v36"),beforeTampered,"Cross-domain profile import must be rejected without data loss");
await $("restoreFile").events.change({target:{files:[{size:950,text:async()=>JSON.stringify(backup)}]}});
assert.equal($("home").value,"https://generadordelettering.org/","V2 restore should retain current profile");
assert.equal(JSON.parse(storage.get("xibanya-profiles-by-domain-v36"))["other-tool.example"].email,"owner@other-tool.example","V2 restore must retain all profile emails by website");
await $("restoreFile").events.change({target:{files:[{size:990,text:async()=>JSON.stringify(oldV2)}]}});
assert.equal($("edu").value,"","Legacy V2 backup without edu must be accepted, not silently filled");
assert.equal(JSON.parse(storage.get("xibanya-profiles-by-domain-v36"))["other-tool.example"].edu,"","Legacy V2 profiles must be migrated");

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
assert.equal($("name").value,"Restored Website","V1 restore must preserve legacy profile");
assert.equal($("edu").value,"","Legacy V1 restores with empty education URL");
assert.equal(JSON.parse(storage.get("xibanya-profiles-by-domain-v36"))["restored.example"].name,"Restored Website","V1 backup should migrate its single profile");

assert.match($("marked").textContent,/人工自查证据 1 条/,"Confirmed manual evidence should survive JSON restore");
$("export").onclick();
const exported=blobs.at(-1).parts.join("");
assert.ok(exported.includes("restored.example"));
assert.ok(exported.includes("审核中"));
assert.ok(exported.includes("第三方公开页")&&exported.includes("实际目标href")&&exported.includes("rel原文"),"CSV needs evidence columns");
assert.ok(exported.includes("https://directory.valid.org/tools/restored")&&exported.includes("本人确认"),"Verified local evidence must export with its source URL");
assert.ok(exported.includes("'=HYPERLINK"),"CSV export must escape spreadsheet formulas");
assert.ok(!exported.includes('"\'"'),"Empty CSV cells must remain empty, not apostrophes");

console.log("PASS: 176 cards, 21 detailed tables, per-domain education HTTPS URLs and V1/V2 backups, search, per-domain marks and CSV proof.");
