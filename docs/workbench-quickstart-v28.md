# 西语外链提交操作台｜使用指南（V29，兼容V28）

> 工具页面：[`backlink-submission-workbench.html`](backlink-submission-workbench.html)  
> 数据基线：2026-10-31，来源于 `data/backlinks-master.csv`。共176条历史来源，既有优先候选，也有暂停、受限或明确排除来源；不是176个能免费获得Follow的链接，也不代表已递交。**本地标注不等于真实成功获链**。

## 一、Windows / Chrome 怎么打开

1. 访问GitHub仓库的操作台文件：[打开HTML源码所在位置](https://github.com/chenmu2024/xibanyayuwailian/blob/main/docs/backlink-submission-workbench.html)。
2. 点击页面右上方的 **Download raw file**（或点 **Raw** 再右键另存为），保存到Windows电脑。保留 `.html` 扩展名，例如 `backlink-submission-workbench.html`。
3. 用Chrome双击打开下载的HTML。**不要只在GitHub代码预览里点开**；代码预览不是实际运行页面。
4. 该HTML已经内嵌176条历史记录和运行所需样式、JavaScript；**不需要服务器、API Key、数据库、账户、付费字体或扩展程序**。可断网查看历史资料、筛选与复制；点击第三方官网入口时才需要上网。
5. 页面顶部有网站名称、主页、工具页、西语和英文说明及邮箱；默认为 `generadordelettering.org` 的案例。更换为其他西语站时，**逐个改成真实信息**。工具不会根据网址自动生成、验证或替换实际功能陈述。

## 二、怎样用来实际申请

1. 默认按“21家优先卡片”排序，输入平台名称或关键词也能找到平台名称、类别、限制：目前内置176个历史渠道。可切换 `原编号` 或 `平台名称` 排序。
2. 使用状态筛选查看P1/P2候选、有条件、待核验、暂停、排除、非外链。**“候选”只代表历史P1/P2分组，不是保证免费、可投稿、Follow或高DR。**
3. 点击一张卡片展开：官方提交入口 / 历史规则依据 / 同类公开案例（如存在） / 适用性 / 费用审核 / 原始逐步填写方式 / 排除原因。
4. 确认合规后，使用 `网站名称`、`目标网址`、西语短描述等复制按钮；按当前官网实际出现的字段提交，**不要把复制功能当成自动填表或外链已建立**。
5. 只有你手动填了第三方官网表单，并看到确认信息时，才能在操作台的“本地提交进度”选择 `已自行提交`；只有对方网站真正刊登了可访问资料页，才可以选择 `已上线待验链` 并记录URL。
6. 从操作台点击 `导出本地进度CSV`，将自己做过的记录保存在电脑。**浏览器localStorage只属于当前浏览器/设备，不同步GitHub，清除站点数据可能丢失。** 即使文件在`file://`模式下浏览器不允许localStorage，导出CSV仍是本地备份途径。
7. 真正需要团队共享或跨浏览器记账时，以 `data/submission-ledger.csv` 为正式事实台账，人工核对后再更新，不得把未核查的“本地自行标记”导入成官方获链事实。

## 三、栏目与数量说明

原始主表共176条：P1 30、P2 21、条件77、待核验14、排除33、非外链1。操作台会按用户网站通用性再突出部分资格阻断，所以**UI的当前有效分组与历史原始分组可能不同**，这是有意的：例如 `#026 TopTool` 虽历史优先级P1，当前明确暂停；`#003 Enlineados` 有免费主机资格疑问。两套标签不能视为重新实时验证过的结果。

## 四、不能做的事

- 不要把 `#109 AI Webcatalog`、`#167 Software Como Servicio` 或 `#175 Discoverly` 的免费方案当免回链目录。其现有规则要求徽章/互链。
- 不要给 `#176 YAJU` 虚构墨西哥公司或地址，也不要给需要英语实际功能的目录只填英语投稿文案就声称产品有英文版。
- 不要把 `#155 MERLOT`、`#156 OER Commons`、`#157 Procomún` 当SEO垃圾目录；教育资格、原始作者权利及开放许可必须满足。
- 不要误把微博式创作、媒体邮箱推荐、GitHub Issue、网站索引提交服务、付费上榜套餐，当作已经获得高权重Follow。
- 不要在本地进度备注里保存邮箱密码、API Token或任何敏感证书。
- 不要将操作台导出的CSV称作独立核验通过的外链数据库；它只是使用者自留工作日志。

## 五、其他文件

- [176站逐条长文版](all-176-backlink-submission-methods.md)：可在GitHub直接阅读；每站保持原编号。
- [21家优先填写字段卡](lettering-priority-21-ready-to-fill.md)：针对Generador de Lettering准备更细的字段值、图标/截图尺寸与英语/西语说明。
- [全部历史渠道CSV](../data/backlinks-master.csv)：分类和平台规则的事实底稿。
- [实际提交记录CSV](../data/submission-ledger.csv)：平台、目标域名、提交日期、审核与公开获链证据。
- 操作台不依赖这些文件联网加载。若以后将历史CSV增到177条，应**同步重新生成HTML内嵌数据**并重新核对JSON记录与主表、运行脚本语法测试、尝试GitHub Actions校验；目前GitHub Actions未提供本轮成功记录，不能声称已通过。

## 六、V29新增：21家真正逐字段表格与多网站隔离

- 在操作台搜索 `Herramientas y Recursos` 或 `LaunchFree`，点击卡片展开，在历史步骤下方可见**逐字段填写表**。21家优先来源共133行，旁边的复制按钮分别复制网站名称、URL、类别、说明等；`#172 EpicTools`只显示已见到的URL与分类，不会捏造额外字段。
- 更换顶部`网站名称`、`网站首页`或`具体工具页`后，离开输入框即可刷新示例；如果新站不是Generador，Lettering独有描述/类别会提示重新编写，并且对应复制按钮禁止直接复制旧文案。
- 将网站首页切换到**不同域名**时，如果工具URL还指向原网站，会自动清空该工具URL；请手工填新站真正可用的工具或教育页，避免将旧站的/editor页面误投。
- 以网站**主机域名**分隔本地申请进度；从 `generadordelettering.org` 切到另一域名不会继承旧站的“已提交”状态。切回来还能找到原记录（在同一浏览器、未清理LocalStorage的情况下）。老V28进度若存在只尝试迁移到Generador，其他网站不共享。
- `导出本地进度CSV`按当前网站主页列出操作日志；只代表个人操作记录，不能自动同步到GitHub，也不能算获链成功。
- 代码检查新增 `node scripts/validate_workbench.mjs`。GitHub Actions目前运行仍失败，最小Runner探针也同样失败，日志不能取得；需明确区分数据静态核对与完整CI/真实浏览器验收。见 [V29事实记录](v29-field-level-workbench-and-ci-evidence.md)。

## 七、V30：在多个网站间安全复用与备份

- **切换到其他西语网站**：先修改顶部站名和网站首页，离开输入框后再填该网站的工具页，注意原域名的旧工具页会清空。把新站实际的`西语短描述 / 英文短描述 / 西语长描述 / 英文长描述`逐项改写，不能沿用Generador预填的Lettering功能。
- **现在21家逐字段表能识别新网站资料**：真实填写过新的介绍后，`Description` / `Descripción`可复制当前新站说明；类别、价格、标签、国家、作者身份、用户隐私等不可能推导的信息保持手工选择和禁用复制。
- **保存所有网站进度**：点击`备份所有网站JSON`，下载到电脑。文件包含你填写的站名、邮箱、简介和全部网站的本地进度/备注，务必私密保存，**不要上传公开GitHub**。
- **恢复到另一台电脑**：先下载操作台HTML，在Chrome打开，点击`恢复进度备份`、选择个人JSON文件；程序检查结构并明确询问是否覆盖本地数据，同意后更新全部网站进度。请自己再核对恢复的站名、URL、状态。
- 原`导出本地进度CSV`还在，文件名包含当前域名；仅导出当前站点状态，针对Excel危险公式型文本增加防护。要跨电脑/跨所有网站同步，请用JSON，而非单站CSV。
- 离线页面的实际V8 DOM模拟11项通过，映射逻辑7项通过；可在Node环境运行`node scripts/smoke_workbench.mjs`复现基本交互。**GitHub Actions Runner持续失败，未获得整套CI绿灯**，并不代表外链已提交或审批。

## 八、V31：17家官网复核结果和新增填表字段（2026-10-31）

本轮不是新找17家，而是**重新核查历史176条中的17家**，结果存于 [V31官网提交复核](v31-17-live-form-verification-20261031.md)。离线HTML里这17家卡片会显示最新核验提示。21家优先填写卡的字段数量从133增至**149行**。

特别注意：**Lugar Latino #014** 直接投递地址返回404，因此暂缓；**Good Design Tools #147** 不存在旧记录误写的Category/Tags，官网Tally要求费用、优惠/联盟和真实图标；**LaunchFree #123** 需要真实创建者身份与自我介绍；**Toolfound #128** 需要持有域名并完成邮箱/Meta/DNS验证；**DesignTools.fyi #151** 必须如实回答Source of Truth、Size及公司身份勾选。

平台自称免费或Dofollow不代表实际发布详情页有Follow链接；没有真人提交的记录也不应计入外链数量。

## 九、V32：14家优先复查、161项具体字段

2026-10-31再次从176条旧平台中核实14条，并同步到HTML操作台。此时**21家重点卡片有161条字段行**。所有被复核渠道可在详情里看到V32提醒。主要变化是 #074 public.tools、#075 Htrd、#171 FounderOmni的准确表单；#057 ToolGuide（120字符、必须有工作工具用途）、#076 NoUploadTools（真实隐私保障且拒session replay）及#141 GainWeb（免费无保证）。

**特别注意**：#026 TopTool已经暂停新投，#003 Enlineados明确排除免费托管站，#152 DesignTrash排除单一关键词生成器，#161 Fountn真实投稿落地页本轮不可读。这些不是默认提交项目；不可为了骗审核而添加假证书或假国家身份。详情见 [V32官方复核报告](v32-14-official-source-audit-20261031.md)。

静态数据完整性和11项模拟交互检查已通过，第三方真正审核/实际Follow/索引/流量仍待取得公开证据。GitHub Actions当前暂无可确认的本轮成功记录。

## 十、V33：打开真实外链样本与Follow优先排序

请下载[最新HTML操作台](backlink-submission-workbench.html)，顶部排序选`V33公开样本优先（非保证）`。它会先展示Htrd、Herramientas y Recursos、NoSignupTools、DesignTools.fyi、Toolfound五个已有公开href样本中未见nofollow的研究候选；点击相应卡片会显示V33实测的原始rel及“查看V33实际公开样本”链接。

**不能把这些公开样本计入Lettering获链。** public.tools已核对3个详情页，每条真实外站href都含`nofollow`，虽然可免费填表，按Follow目标已从P1调整为条件。另9个目录只是已检视公开页面内未发现本站，不代表全站肯定未收录。详细表格见 [V33独立href及本站出现情况核验](v33-public-link-rel-and-listing-presence-20261031.md)。

V33还校正了静态Node数据验证与模拟交互脚本的职责，并新增对176条主表和11个真实链接属性证据的同步检查。GitHub Actions既往失败仍需通过网站作业日志定位，不得仅凭页面可打开声称CI成功。

## 十一、V34：第二批字体/设计外链样本排序及真实填写

离线操作台版本升级V34。顶部排序现在有`V34字体设计样本优先（非保证）`，前5名为 **#159 Design Resources Archive、#163 LDS Library、#164 Unikist、#172 EpicTools、#165 Mark-it**。这些站点与字体/排版/设计资源更相近，已抽查其公开样本href和rel；[点击查看5家逐字段填表资料](v34-five-more-design-font-directories-ready-to-fill.md)。

注意两处降级：**#005 The Free Tools Directory**真实字体工具条目含nofollow；**#162 UX Resources**的4个字体工具条目均含sponsored，二者已从P1改为条件。无法将这些部分样本结果绝对化为全站规则。完整21条真实外站href/rel及11页目标域名检查见 [V34核验报告](v34-21-public-link-samples-and-priority-update-20261031.md)。

当前主库176、21家优先卡161个字段，新增11家样本标注。V33 Follow样本排序仍独立保留。静态与模拟交互13项通过不等于真实浏览器或CI通过；没有任何新站外提交、审核通过或Lettering获链记录。

## 十二、V35：真实外链人工验收、零付费Python脚本和备份

外链目录填写完成后不要立即记“已获链”。**获得第三方公开条目URL**后，在V35操作台展开对应平台，最下方可以填写：①对方公开条目完整HTTPS URL ②该页面真实指向你网站的`href` ③此链接在HTML的原始`rel`。然后**亲自点“我已亲自检查...”**确认；该确认只存在于你的本地浏览器，**没有自动联网核验，不能当成已获Follow**。如果改动链接或rel，会自动撤销旧确认，必须重新查验。

V35的备份JSON仍包含所有站点的进度与备注，同时包含上述证据与自查状态；CSV新增源页面、href、rel、自查日期等列。包含隐私信息的JSON不要上传公开GitHub。

如要**真实联网读取指定第三方公开页面HTML**，Windows中在仓库目录运行免费脚本：
```powershell
python .\scripts\verify_published_backlink.py --source "https://实际目录域名/实际公开条目" --target "https://generadordelettering.org/" --output "lettering-backlink-evidence.json"
```
填入对方实际公示的URL，**不能使用占位符URL或提交表单URL**。退出码0=发现真实匹配`a[href]`；1=只在该页HTML未检出；2=请求或安全验证错误。支持`nofollow`、`ugc`、`sponsored`分类，且不会假设Google一定传权。详细字段和演示请看 [V35完整教程](v35-evidence-based-backlink-verification.md)。

V35的离线操作台模拟验收已通过；新的Python离线8项测试**已编写但尚未在真实Python运行器成功执行**。GitHub Actions原有故障仍须单独定位，不能声称CI已恢复。
