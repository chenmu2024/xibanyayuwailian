# AGENTS.md — 外链资源库维护规范

本仓库用于**西班牙语网站通用外链库**，任何 AI、Codex 或维护脚本必须遵守：

1. 先读取 `README.md`、`docs/quality-policy.md`、`data/backlinks-master.csv`、`data/actionable-applications-v22.csv`、`data/v22-link-evidence-audit.csv`、`data/reusable-free-shortlist.csv`、`data/education-resource-submissions.csv`、`data/submission-ledger.csv`、`data/editorial-prospects.csv`、`data/editorial-outreach-ledger.csv`，再查找或更新渠道。
2. 同一根域名的渠道必须跨 V1–V16 历史去重。新增来源先搜索总库；不要为了数量新增同一站点的其他提交URL。
3. 保留全部历史及排除记录，不得因为网站关闭、收费或被降级而偷偷删行；修改状态时写明官方依据与核验日期。
4. 新渠道应先核实**免费、实际可提交、接受西语/目标站型、存在可公开访问的资料页、是否强制互链**；权威值和 Follow 属性只有证据时才填写，未知一律“未核实”。
5. GitHub 数据结构：`data/backlinks-master.csv` 是渠道主表；`data/priority-queue.csv` 是特定目标网站队列；`data/submission-ledger.csv` 是**实际跨网站提交状态**。不要把优先候选写成“已提交/已获链”。
6. 每次编辑后运行 `python scripts/validate_csv.py` 并确认 GitHub Actions 成功；尽量将更新原子化，不覆盖用户其他提交记录。
7. 不进行自动注册、提交、发送邮件或改动网站代码，除非用户明确指示；不得假称申请、审核、获链已完成。
8. 对已有 AdSense 站点优先免费且不要求反链徽章的渠道，尽可能不改变现有用户体验。
9. 文章投稿、设计作品发布、编辑推荐、目录登记应区别归类，不把评论区外链和垃圾目录计为优质。
10. 汇报时提供实际提交链接、变更行、提交状态、commit SHA，并说明未验证项。

本仓库目标是**可追溯、可复用的高质量渠道与已获链台账**，不是不加过滤地累积网站数量。
11. 媒体投稿/编辑推荐必须存入 `data/editorial-prospects.csv`，**不得混入可直接填表的免费目录清单**。官方普通联系表单≠编辑授权投稿≠获链保证。
12. 向任何媒体发送推荐之前先查 `data/editorial-outreach-ledger.csv`、已连接Gmail已发送/收到邮件及各站历史；同一媒体曾收到同一站点推荐，不得无新价值而重复首轮推送。
13. 已证实：2026-10-25 Gràffica 已收到 generadordelettering.org 的 editor/练习SVG 推介；2026-10-12 EDUCACIÓN 3.0 收到 numerosenletras.org 教育资源邮件。不要删除这些事实，仅当取得真实回复或公开链接时更新对应状态。

14. V19之后为每个新西语网站推荐提交来源时，**先用** `data/reusable-free-shortlist.csv`，再查总库资格；排除/条件/免费Nofollow不要混入“已认证高权重免费Follow”清单。不能凭第三方历史DR或官网自述判断实时DR。
15. 对明确拒绝关键词站/简单转换器的目录（例如DesignTrash）不得替Lettering站重复投稿；对明确英语可理解要求的平台（例如DesignBookmark）不能通过仅写英文简介伪装为真正英语可用的产品。
16. 免费档Nofollow与付费Follow必须分开记录（例如DesignMunk）。不能为争取Follow擅自给已有站点添加强制徽章、重复推广或升级付费。
17. 对据称支持GitHub PR投稿的外部项目，必须确认其仓库**真实存在可编辑的数据文件及投稿许可**后，才可称其为“可直接通过PR获得外链”；外部站点写“可提PR”却只有README的情况只能列待核验。

18. V20：教育资源共享库必须单列在 `data/education-resource-submissions.csv`。免费会员 ≠ 允许商用广告推广 ≠ 必定Follow；不得将教育库当SEO提交农场。
19. MERLOT 的注册条款严禁广告推广，只有真实学习资料、教学目标、非营销措辞和准确作者信息才可考虑；仅为拿商业网站反向链接而加入不合格。
20. OER Commons 对具体教学内容有严格开放使用/非商业教育许可门槛。除非权利人明确决定，否则不得更改已有网站或练习素材的版权、CC许可证，也不得代替权利人勾选许可。
21. Procomún/INTEF 主要服务教师/教育从业者；不得冒充身份。2026-10-31公开主页抓取返回HTTP500，未恢复前不可声称已验证投稿入口。

22. V21：`TOOOLS.design` 和 `resourcesfor.design` 均有官方投稿表单，但只证实无即时付款/换链字段，**不代表已确认永久免费Follow、已获准收录、已测DR/AS**。2026-10-31官网条件变动需再次确认。
23. 对设计类资源推荐 `https://generadordelettering.org/editor` 的真实可视化编辑功能，不要声称该在线工具提供 TTF/OTF字体文件、SVG打印文件或专业DPI保证；对不同网站必须逐一核对实际功能。
24. 网站已有公开投稿页与真正已被馆藏收录是两个状态，不能把没有收费步骤推断为“获链成功”。每次保持Github源记录、申请队列、短名单与文案一致。

25. V22开始区分三个层级：**历史总库（允许排除）→有证据的研究名单（允许暂时暂停）→当前可尝试申请的行动清单（必须确认公开免费入口）**；不要把一个层级的数据直接充当下一级的成功事实。
26. TopTool在2026-10-31官网明确暂停新申请，不能未经官网恢复证据放入行动清单；品牌认领的DNS/Meta验证不能错写为首次投稿必需步骤。
27. 第三方FinderLaunch把TOOOLS.design标为Nofollow/DR47；Submitator抽样Good Design Tools（60页面390外链、无rel、DR25）是利益相关来源。**任何第三方报告不可冒充我们实时DOM或Ahrefs实测**，必须在数据中保留日期、来源和局限。
28. 新增Freebie Supply仅限有明确授权的原创可免费设计素材；页面不显示可填写表单时标为条件，不得声明可一键投稿。UI Goodies应归编辑媒体线索而不是可自动投稿的目录；必须符合它的设计质量与广告体验规则。
29. 准备行动清单时先复查官方提交页、用户网站实际功能、历史去重、免费和回链限制，不要将“已注册/已填写/已批准/真实Follow/被Google索引”混为一种状态。

30. V23新增3条真实不重复研究候选：Fountn（独立Notion表单未读到，条件）、UX Resources（公开Typography工具投稿）、LDS Library（编辑审核）。不要将新增候选写成已提交，亦不要倒灌成V22的六家行动名单。
31. Enlineados官方明确拒绝免费主机托管的网站：自购域名+免费Cloudflare Pages的合规性需向平台核实；禁止猜选国家/城市。不因纯西语适配就跳过其余资格审核。
32. LDS Library的提交站点是lds-library.vercel.app，运营方为legitdesign.studio；在跨站提交查重时同时核对别名，不能把所有vercel.app子域视为同一来源。Fountn的官网按钮跳Notion，而不是已获编辑收录。

33. V24维护：新增Unikist（#164）、Mark-it（#165）为人工设计投稿候选。DailyLaunch（#166）免费发布不等于免费Dofollow，其官网明确需要回链徽章才改为Dofollow；不能擅自添加。
34. Software Como Servicio（#167）免费收录明确强制自站徽章与Dofollow反向链接，按排除处理；不为已上线AdSense站引入互链。Illustration.tools抓取超时，不作为当前可申请。
35. 新增待审核设计目录需真实可用界面和真实作者/联系资料，官网表单无付款字段≠独立获链/高DR。不同网站同平台重复投递前查目标域名×平台注册根域名。

36. V25：Herramientas y Recursos（#168）和FreeDesignerTools（#169）有可读取的公开建议表单，但仍是候选；没有独立DR/Follow数据，不宣称高权重。后者仅12条馆藏，宣传流量无独立证据。
37. Ghostbyte Library（#170）官网Submit a Resource跳GitHub Issues，不是直接PR；仓库确有data/design/资源文件，但开一个Issue并非官网获链。FounderOmni（#171）只有西语建议按钮可见，尚未证实最终表单及免费资格。
38. 2026-10-31 AI Webcatalog（历史#109）官网明确强制安装徽章并填写该页面的链接，因此改为排除，历史行保留，禁止因为其“免费投稿”就推荐给普通西语网站。
39. Best Productivity Resources为E006编辑媒体，官网只接受本人LinkedIn DM资源建议；不属于免费目录直接填写入口。不得在未经用户允许前自动发私信，也不得把媒体曝光当目录Follow。

40. V26新增EpicTools #172（仅URL+Design分类可尝试）；Learnlists #173仅教育教学资源有条件，不得投稿普通字体转换首页；Illustration Tools #174官网直访超时，搜索快照不代表当前可投。
41. Discoverly #175官方要求免费提交前先安装Featured badge，与第三方免徽章线索相矛盾，以官网优先，排除；YAJU #176明确只收墨西哥有实际关系网站，不能只凭西语或虚构国家地点投稿。
42. The Creative Vault E007为编辑邮件资源建议，必须存入editorial-prospects，不能冒充免费表单、已联系或已获链；没有用户许可时不自动发送。

43. V27新增一份可复用总手册`docs/all-176-backlink-submission-methods.md`，按主库原编号独立列出176个渠道；每条的步骤都从当时记录整理，**并不构成全部平台当日重新实测或已经拿到链接**。历史新增/更新来源后应同步重建总手册和相应链接，保持逐条对应。
44. `docs/lettering-priority-21-ready-to-fill.md`专门针对Generador de Lettering为21条优先研究候选提供真实字段和值；卡片不是实际完成提交/获链/Follow的证明。切换其他网站必须更换品牌、域名、真实功能、截图、价格、作者与资格。
45. 从此用户要填写方式，应优先给出`一站一个入口 + 分步骤 + 具体字段值 + 真实限制`，而非长表或只给排名/DR；遇到排除、暂停、无法访问、版权/教育/地域/强制badge，明确写“不提交”。不得因总库176条就称有176条可免费申请。
46. 新增`docs/all-176-backlink-submission-methods.md`为历史资料的衍生文档，`data/backlinks-master.csv`和`data/submission-ledger.csv`仍是事实来源；不能因为填写卡有示例，就更新台账为已提交、已上线或独立测得Follow。

47. V28新增本地单文件操作台`docs/backlink-submission-workbench.html`。本文件内嵌历史176条数据，仅供检索、复制真实材料和localStorage本机标注；不可把浏览器手动标注的“已自行提交/已上线待验链”自动当作GitHub提交台账或完成外链验收。
48. 更新`data/backlinks-master.csv`时，应同步更新V27逐站长文、V28HTML操作台（内嵌全部新条目）及其操作指南；GitHub Actions应检验数据ID、入口和名称完全对应，防止长文/HTML数据过期。
49. V28 HTML须保持离线、零付费依赖，无第三方分析/跟踪、远程脚本、密钥及自动站外网络提交。用户换新网站时不能自动沿用Generador de Lettering功能/教育版权/地区实体事实，须人工改写；本地进度CSV仅是用户的工作记录。

50. V29：网页操作台不仅包含176条历史候选，还直接存储21家平台共133个字段行；任何更新字段的版本需同步维护 `docs/lettering-priority-21-ready-to-fill.md` 和HTML嵌入数据，不得将历史表单字段冒充当日实时全部复核。
51. V29：操作台本地进度必须以目标站主机名隔离，不能把Lettering申请状态带到其他西语域名；切换品牌/域名后，旧项目的字体与PNG输出功能文案必须要求重新核实，不能仅替换站名就自动复制。
52. V29：不得把GitHub Actions红灯冒充绿色；至少有一次不检出项目源码、不依赖Python的Runner probe同样失败，暂无有效日志。保持仓库现有真实历史台账，不得为获取绿色徽章删除实质校验项。仓库 `docs/v29-field-level-workbench-and-ci-evidence.md` 记录了证据和后续验收。

53. V30：21家细节字段应当通过真实字段名、用户明确更新的网站描述和同域规范链接生成可复制内容；不可向新项目套用Generador的旧字体功能文案。类别、标签、定价、国家、作者身份、隐私承诺、教育许可等必须人工按事实选，不可靠推断一律锁定复制。
54. V30离线备份JSON包含用户可能填写的邮箱及备注，是本地个人文件，不应写入公开GitHub；用户点击导入才可恢复，必须校验版本/大小/域名/1–176编号/状态，覆盖前要求明确确认。CSV导出应阻断以=+-@开头的电子表格公式注入。
55. V30新增`scripts/smoke_workbench.mjs`交互模拟测试，覆盖176条渲染、21家字段、检索、域名隔离、JSON备份导入、CSV安全。该脚本为Node零付费依赖；任何自动构建不得因外部Runner故障而假报测试成功。历史事实以主表和提交台账为准。

56. V31按`data/v31-official-form-audit-20261031.csv`保存17个已有来源的官方表单字段核对证据；0新来源、0实际提交。不得把本文件的“可以研究填写”写成已申请或获得Follow。
57. #014 Lugar Latino官方提交页2026-10-31直访404、搜索索引仍保留历史表单，因此主库改为待核验；必须真人浏览器或后续官方恢复验证再投，不得因平台P1历史标签继续推荐立即填写。
58. #147 Good Design Tools已通过官方Tally表单核验**没有Category/Tags字段**，而有定价/优惠/联盟/2MB指定图标/Email；#123 LaunchFree有真实创办人和4阶段身份/验证要求；#128 Toolfound要求域名验证；#151 DesignTools.fyi有Source of Truth和公司代表复选框。
59. V31填写手册/离线HTML的21家优先平台字段合计已从133变为149，任何修改须同步其操作台JSON和Node测试；所有申请、获批、href、Follow、索引均要独立留证。

60. V32已对历史总库14家再次做官网可读表单复核：`data/v32-official-source-audit-20261031.csv`和`docs/v32-14-official-source-audit-20261031.md`为本轮证据基线，不应视为14家新平台或14条已获反向链接。
61. V32官网硬限制：#003 Enlineados禁止免费托管（自定义域名不等于不属于免费主机）；#026 TopTool目前暂停；#057 ToolGuide以工作效率为编辑门槛且短描述≤120字符；#076 NoUploadTools禁止session replay且隐私特征勾选必须真实、有广告不得声称No ads；#152 DesignTrash拒绝关键词型一招式工具；#170 Ghostbyte的Issue不是已公开上榜链接。
62. V32新增可操作证据：#074 public.tools官方Tally为4字段、#075 Htrd页尾5字段、#171 FounderOmni西语弹层有公开字段，发布和Follow仍属待验；#141 GainWeb免费档不保证审核；#161 Fountn最终表单不可读。不能把“免费可填”夸大为保证Follow或已获链。
63. V32更新`docs/backlink-submission-workbench.html`的176主库镜像、21家共161项字段和14条当日核验提示；任何改动需同步`scripts/validate_workbench.mjs`、`scripts/smoke_workbench.mjs`及176站长文。GitHub Actions红灯必须明确披露，不得假报绿色。

64. V33实际出站链接与官方提交资格必须区分：证据见`data/v33-published-outbound-rel-samples-20261031.csv`。public.tools的3条已发布样本均含`nofollow`，因此#074按Follow目标从P1降为条件，但不宣称所有页面均nofollow；其它平台少量样本未带nofollow也不能声称全站均Follow。
65. 任何`已获外链`必须有用户目标域名真实公开href，不能借第三方Fontjoy/StackEdit/FontsWiki/StencilMaker的外链代替本站；来源目录内容未检出只能按具体检查URL、日期和页面范围记录，不能断言全站被拒或未收录。
66. V33新增九个页面的核查范围见`data/v33-lettering-public-listing-presence-20261031.csv`，每次重新复核需独立保存原页与实际href/rel证据。GitHub或服务器失败不得冒充通过。
67. Node验证脚本保持正确职责：`scripts/validate_workbench.mjs`验证176条主表同步、21家字段、公开样本与JS语法，`scripts/smoke_workbench.mjs`负责运行模拟DOM交互；V33修复曾经交换文件内容的故障。未经测试不要交换或随意重命名。

68. V34新增`data/v34-21-published-link-rel-samples-20261031.csv`（21条已发布外站href、具体页面和原始rel）与`data/v34-11-category-presence-checks-20261031.csv`（11个有限范围页面检查）。所有样本指向其他人的网站，不代表已为Lettering取得任何链接。
69. V34 #005 The Free Tools Directory的1000 Font Generator真实公开样本rel含nofollow；#162 UX Resources的4个Typography资源详情样本含sponsored。两者由P1调整为条件；不推断这些平台所有链接都相同，也不把第三方免费投稿当免费Follow保证。
70. V34 #159资源详情、#163/#164字体分类、#165设计资源、#172 EpicTools Curated详情中已实测到未带nofollow/ugc/sponsored的公开外站href；EpicTools Partner显式follow与免费Curated必须分开。不得用抽样rel代替新申请审核/真实条目rel。
71. V34 `docs/backlink-submission-workbench.html`新加11家实际公开href/rel提示和单独的`design`排序，保留V33旧排序及跨域进度隔离。`scripts/validate_workbench.mjs`应检查V34 21条原始样本、#005 nofollow、#162 4/4 sponsored；`scripts/smoke_workbench.mjs`新增第二批排序回归。修改主库、CSV、HTML或测试要同步。
72. GitHub Actions本轮如未得到明确绿色运行，只能报告独立V8校验结果及Actions尚未修复，不能假报获批外链或CI成功。

73. V35：操作台只可把“用户已亲自查验”记作**本地自我确认**，不能转换成GitHub正式台账上的已核验链接。必须提供第三方公开HTTPS页面、指向同一个目标域名的真实href和原始rel；字段修改撤销确认。进度按域名隔离；JSON备份/恢复对proof对象严格校验，旧V30格式仍需兼容。
74. V35 `scripts/verify_published_backlink.py`用于只读HTTPS公开页面href/rel检查，禁止它自动申请外链、访问登录后页面或尝试绕过Cloudflare/验证码。输出`found`只代表指定HTML见到<a href>，`not_found_in_fetched_html`只是限定单页未发现；没有nofollow不保证Google SEO传权，`--html-file`离线fixture不可充当线上证据。
75. V35 `scripts/test_verify_published_backlink.py`的8组不联网测试已提交并接入.github/workflows/validate-data.yml，必须在真实Python/CI通过后才可宣称其测试完成。GitHub Actions run若返回0个job步骤，不足以唯一确定故障原因，禁止无证据归因于账户或Runner。V35的V8离线工作台模拟测试与Python测试状态必须分别表述。

76. V36操作台新增`xibanya-profiles-by-domain-v36`作为每域名完整网站资料的唯一当前数据表，与`xibanya-marks-by-domain-v29`逐域名进度配合。新域名不得继承其他网站的名称、邮箱、西语/英语文案或工具URL；切回旧站必须恢复原资料。
77. V36 JSON备份的`version:2`需要`profile`、`profiles`和`progress`，恢复时要检查每个profiles的`home`和`tool`域名一致、字段类型与长度及域名数量。必须向下兼容V1：其其他域名历史进度可以恢复，但缺失的其他站资料无法补造。
78. V36必须维持`scripts/validate_workbench.mjs`结构校验以及`scripts/smoke_workbench.mjs`模拟23项检查，覆盖跨站文本/email泄漏、跨域JSON篡改、V2备份与V1迁移；不能把模拟V8声称为真实Windows Chrome端到端，也不宣称GitHub Actions CI或Python新单测已经成功。

79. V37已在真实Python 3.13.5解释器执行验链11项测试且0失败，Git blob SHA与仓库最终两份Python源码完全一致（见`docs/v37-python-backlink-verifier-tested-and-ci-diagnosis.md`）；与GitHub Actions未恢复是两个不同事实，不得以CI失败否认已完成本地测试，也不能以本地通过谎称CI绿色。
80. V37解析真实HTML的`<a href>`时必须容忍个别无效href与只有属性名的空rel；排除`<template>`中的惰性锚点。维持3个新回归测试和8个原测试。不得把fixture中的目标URL算成真实外链，也不得从HTML没有nofollow推论Google保证排名。
81. Actions当前task在数秒内失败且API步骤为空、日志历史返回BlobNotFound，明确保持原因“尚待确认”，避免无证据改runner、删质量门槛或无限重试。

82. V38质量核验只抽查现有176条中14个高相关设计/字体/西语目录，不把它们当14个新增渠道。报告见`docs/v38-high-relevance-public-evidence-20261031.md`、逐项CSV见`data/v38-high-relevance-public-evidence-20261031.csv`。本轮新增实际申请0、获链0，原始href/rel不明时只记录外站URL可见，禁止推断Follow。
83. V38 #171 FounderOmni西语库已能读到`Tipo de solicitud`、`Categoría`、`Nombre de la ficha`、`URL pública`、推荐理由与可选邮箱，并有Hero Patterns单独公开详情指向原站，推翻旧的“只见按钮/完整字段未知”阻断说明；但费用、原始rel、审核仍未知。#168独立详情访问超时不能称Follow；#169仅12条公开工具，广告性用户数宣传不得视为流量实测。
84. 不得在只修改审计CSV时宣称旧主库、176条手册、离线HTML、实际提交台账已同步。后续若要正式修改主库#171，必须原子同步176条指南及HTML镜像、更新相应校验并实测，不可在镜像冲突时错误宣称已完成。

85. V39：#168 Herramientas y Recursos普通资源详情`Visitar sitio`经过`/salir/slug`内部中转；V33的两条rel=noopener直链来自页脚关联站，不是免费普通条目收录后的实际外链质量证据，正式从P1降为条件。
86. V39：#171西语表单字段首次核验是V32，不能宣称V38才首次发现。Fontpair与Hero Patterns独立公开详情外站href可见，但raw rel未取得、目标站未获链。#151 Font Explorer在V33已记录原始`noopener noreferrer`，不能重复计数。
87. 本轮修改主库、176手册和HTML镜像时，仍须分开记录历史外站样本与用户自己确认的目标域名真实获链；当前新增实际申请与获链均0，CI是否成功需单独核查。

88. V40 #163 LDS Library旧lds-library.vercel.app与规范域library.legitdesign.studio是同一个编辑平台，旧域Fonts和Submit页面的canonical均指向规范域同路径，规范域也可访问。只算一家、不可重复投；V23/V34历史原始rel样本应保留来源旧域。
89. V40 #165 Mark-it主域/font只有少量字体网址，首页All Resources跳另一个Vercel交互目录，暂未核实具体刊登href；旧首页Fontmeme样本不能推出申请自动取得独立Follow，故从P1降为P2。
90. V40主库、176指南、HTML镜像应同步；0真实新提交、0用户站新获链，历史rel非实时当前新产品或Google索引保证。

91. V41：除了原始`href/rel`，还应审计人工精选的真实内容品质。EpicTools #172的Newest Additions出现过期域名拍卖和Cloudflare拦截，虽然标Curated；所以从P1降P2。V34旧真实href/rel数据不删除，不把Partner/Curated混成一类。
92. V41：对每个渠道按实际表单字段填写。#159数学反人机问答为动态题、禁止硬编码旧题目；#164 Short description受280字符上限；#151姓名邮箱与公司代表资格须真；#163 LDS当前规范页只取到投稿介绍，所列更细字段来自V23历史记录，不能说本轮重查全量字段；#172仅URL+Category。
93. V41已创建五家人工填写准备卡和逐字段CSV，文本仅针对generadordelettering.org/editor且应二次实站校验，严禁复用到其他网站不改产品信息。实际投稿成功只在人工完成并有凭证后登记；raw rel、索引、访问量各需独立证据。

94. 当前LaunchFree #123 首批高优先证据含Fontique（Creator Tools/Lettering）、Free Text Symbols（Fancy Text）及Rueda Decide（西语工具）三个实际公开详情的站外href。FAQ的永久免费/Dofollow是官方陈述，raw rel和本站获链未实证。填写真实开发动机/创建者信息，详见docs/current-priority-execution.md。
95. GitHub Actions运行41160234903 job124415981348失败但steps=null、日志404、计费0ms，无证据表明任何验证脚本曾执行；不得谎称Python/JS测试失败，也不得无诊断提高付费预算。见docs/actions-pre-execution-diagnosis.md。
96. 优先延续有真实同类投稿成功样本的来源，维护现行申请包而非无限追加版本号。76等发布数量不等于人工严审，也不等于用户网站获链。
