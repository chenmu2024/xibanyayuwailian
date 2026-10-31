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
