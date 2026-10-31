# 西班牙语网站外链资源库 (xibanyayuwailian)

用于管理西班牙语网站的外链候选、实际申请、审核结果与公开获链证据。**本仓库中的候选数量不代表有效外链数量，也不代表已取得的 Follow 链接数量。**

## 从这里开始

| 文件 | 用途 |
| --- | --- |
| **[docs/v54-live-submission-forms-and-ready-to-fill-pack-20261031.md](docs/v54-live-submission-forms-and-ready-to-fill-pack-20261031.md)** | **V54：7家官方表单现场复核、精确字段、动态验证码与可复制投稿文案** |
| [data/v54-live-submission-form-audit-20261031.csv](data/v54-live-submission-form-audit-20261031.csv) | 7家真实表单字段、选项限制与待确认项 |
| **[docs/v53-current-rendered-dom-rel-and-peplio-downgrade-20261031.md](docs/v53-current-rendered-dom-rel-and-peplio-downgrade-20261031.md)** | **V53：14家已发布第三方外站DOM rel实测（13个样本未见限制词，Peplio真实样本ugc nofollow）；现行P1=12、条件=86** |
| [data/v53-current-rendered-dom-outbound-rel-20261031.csv](data/v53-current-rendered-dom-outbound-rel-20261031.csv) | 14条具体实际href、当前DOM rel及证据范围（不是用户已获链） |
| **[docs/v52-nine-curated-canonical-robots-and-raw-rel-workflow-20261031.md](docs/v52-nine-curated-canonical-robots-and-raw-rel-workflow-20261031.md)** | **V52：9个字体/设计目录真实外站链接、规范网址与robots独立记录；LDS已重获公开证据，并提供只读raw rel验证步骤** |
| [data/v52-curated-published-anchor-metadata-20261031.csv](data/v52-curated-published-anchor-metadata-20261031.csv) | 9家已发布第三方示例的实际href、canonical、robots及历史rel局限 |
| [scripts/audit_curated_v52.py](scripts/audit_curated_v52.py) | **Windows零付费、只读、最多9页**：核对真实原始a href/rel；本机运行后才有实时结果 |
| [scripts/test_audit_curated_v52.py](scripts/test_audit_curated_v52.py) | 6项不联网CSV矩阵/请求上限测试，源码已提交，不代表GitHub Actions通过 |
| **[docs/v51-curated-live-review-and-execution-20261031.md](docs/v51-curated-live-review-and-execution-20261031.md)** | **V51：11家字体/设计/西语目录再次核验，区别实时公开href、历史rel与质量问题；给出最短表单与主题相关性优先级** |
| [data/v51-live-curated-submission-audit-20261031.csv](data/v51-live-curated-submission-audit-20261031.csv) | 11家现场公开实例、真实入口及证据不确定性逐行记录；不代表11条已获链 |
| **[docs/v30-cross-site-field-mapping-and-backup.md](docs/v30-cross-site-field-mapping-and-backup.md)** | **V30：不同西语网站共用176平台填写卡、JSON备份恢复、CSV安全及11项模拟交互测试** |
| [docs/v29-field-level-workbench-and-ci-evidence.md](docs/v29-field-level-workbench-and-ci-evidence.md) | **V29更新：21家平台共133个真实历史字段示例、进度按网站域名隔离、GitHub Actions故障取证** |
| **[docs/backlink-submission-workbench.html](docs/backlink-submission-workbench.html)** | **V28离线可用的176条外链操作台**：可搜索/筛选/排序，独立展开每站入口与逐条步骤，复制自己的西语/英语材料，浏览器本地标注进度并下载CSV；需下载原始HTML后用Chrome打开 |
| [docs/workbench-quickstart-v28.md](docs/workbench-quickstart-v28.md) | 操作台的Windows/Chrome打开方法、进度备份、隐私、条件及避免虚报已获链的规则 |
| **[docs/all-176-backlink-submission-methods.md](docs/all-176-backlink-submission-methods.md)** | **先看这里：176个平台一个接一个，分别列实际入口、具体操作字段、真实填表示例、费用、语言、风险和排除理由；另附7家媒体编辑线索** |
| **[docs/lettering-priority-21-ready-to-fill.md](docs/lettering-priority-21-ready-to-fill.md)** | **最方便直接填写：围绕generadordelettering.org，21家优先研究平台分别给出完整复制用的字段/值/图片要求，需先看各站条件** |
| **[docs/v37-python-backlink-verifier-tested-and-ci-diagnosis.md](docs/v37-python-backlink-verifier-tested-and-ci-diagnosis.md)** | **V37：Python 3.13真实单测11/11通过，修复坏href/空rel/惰性template链接误计，附Git blob哈希及CI独立故障说明** |
| **[docs/v36-domain-isolated-profiles-and-v2-backups.md](docs/v36-domain-isolated-profiles-and-v2-backups.md)** | **V36：多西语网站的名称、简介、邮箱及编辑器URL完全按域名隔离，V2 JSON完整备份与V1兼容恢复** |
| **[docs/v35-evidence-based-backlink-verification.md](docs/v35-evidence-based-backlink-verification.md)** | **V35操作指南：离线记录公开页面href/rel、自查确认，以及Windows免费核验命令** |
| [scripts/verify_published_backlink.py](scripts/verify_published_backlink.py) | **新增：单页公开HTTPS外链检查，无付费API，真正解析a[href]和原始rel，生成可留存JSON** |
| [scripts/test_verify_published_backlink.py](scripts/test_verify_published_backlink.py) | 8组离线单元测试，包含相似域名、防止普通文本冒充链接、nofollow/ugc/sponsored |
| **[docs/v34-five-more-design-font-directories-ready-to-fill.md](docs/v34-five-more-design-font-directories-ready-to-fill.md)** | **V34第二批5家字体/设计目录：逐字段、实际URL、真实获链样本与注意事项** |
| [docs/v34-21-public-link-samples-and-priority-update-20261031.md](docs/v34-21-public-link-samples-and-priority-update-20261031.md) | V34新增21条已发布href/rel证据、样本适用边界与两家降级依据 |
| [data/v34-21-published-link-rel-samples-20261031.csv](data/v34-21-published-link-rel-samples-20261031.csv) | 21条可复核的公开来源页面→真实href→原始rel属性 |
| [data/v34-11-category-presence-checks-20261031.csv](data/v34-11-category-presence-checks-20261031.csv) | 11个实际读取页面对Lettering的检出范围；明确访问失败不等于未收录 |
| **[docs/v33-five-follow-first-ready-to-fill.md](docs/v33-five-follow-first-ready-to-fill.md)** | **直接使用：5家公开样本未见nofollow的外链投稿，逐家真实表单字段和Lettering可复制文案** |
| **[docs/v33-public-link-rel-and-listing-presence-20261031.md](docs/v33-public-link-rel-and-listing-presence-20261031.md)** | **V33：11条真实已发布外站href/rel，9个页面的Lettering出现范围；public.tools公开样本3/3 nofollow** |
| [data/v33-published-outbound-rel-samples-20261031.csv](data/v33-published-outbound-rel-samples-20261031.csv) | 11个可复核的公开详情页外部href、原始rel及样本结论 |
| [data/v33-lettering-public-listing-presence-20261031.csv](data/v33-lettering-public-listing-presence-20261031.csv) | 9个目录当日所读取页面有没有出现Lettering域名；**不等于全站穷尽** |
| **[docs/v32-14-official-source-audit-20261031.md](docs/v32-14-official-source-audit-20261031.md)** | **V32：14家现有平台官网复核，含public.tools/Htrd/FounderOmni真实字段及暂停、隐私、免费托管限制** |
| [data/v32-official-source-audit-20261031.csv](data/v32-official-source-audit-20261031.csv) | 14家官方表单证据、填写字段、当前限制、未提交状态的结构化CSV |
| **[docs/v31-17-live-form-verification-20261031.md](docs/v31-17-live-form-verification-20261031.md)** | **V31优先查看：17家官网实时表单复核，准确字段、费用及互链限制；另说明Lugar Latino直访404** |
| [data/v31-official-form-audit-20261031.csv](data/v31-official-form-audit-20261031.csv) | V31的17家官方表单字段、审核条件与实际获链状态审计表，仍全部未提交 |
| [data/backlinks-master.csv](data/backlinks-master.csv) | V26 累计176条渠道/候选（保留V25的171条，本轮新添5条，含条件/排除），完整保留历史记录 |
| [data/priority-queue.csv](data/priority-queue.csv) | 面向 Generador de Lettering 的15家历史申请候选（含条件、低优先项目），不要全部照单提交 |
| [data/actionable-applications-v22.csv](data/actionable-applications-v22.csv) | V22原版6家经证据分级的可尝试来源历史快照；不是本次21家填写卡，也不保证Follow |
| [data/v26-new-source-audit.csv](data/v26-new-source-audit.csv) | **V26**：五家新渠道的免费、语言、提交入口、Google索引、外链与资格证据 |
| [docs/v26-typography-education-submission-20261031.md](docs/v26-typography-education-submission-20261031.md) | **V26逐站提交说明**：EpicTools、Learnlists、Illustration Tools、Discoverly与YAJU |
| [data/v25-spanish-resource-evidence.csv](data/v25-spanish-resource-evidence.csv) | **V25** 四家新研究来源逐条证据与已提交真相：两家可尝试、两家条件 |
| [docs/v25-spanish-and-design-resource-submissions-20261031.md](docs/v25-spanish-and-design-resource-submissions-20261031.md) | **V25** 西语目录、免费设计工具、GitHub Issue、需核实弹窗与历史强制Badge纠错 |
| [data/v24-curated-submission-audit.csv](data/v24-curated-submission-audit.csv) | **V24**：Unikist、Mark-it、DailyLaunch和Software Como Servicio四站逐项资格、免费/徽章与证据等级 |
| [docs/v24-curated-design-and-spanish-launch-20261031.md](docs/v24-curated-design-and-spanish-launch-20261031.md) | **V24逐站投稿指南**：真实官网入口、精确字段、英语/西语文案及排除原因 |
| [data/v23-design-submission-check.csv](data/v23-design-submission-check.csv) | **V23**：新增3家字体/设计资源目录及Enlineados已有#3资格复核，独立记录免费/语种/限制/审核状态 |
| [docs/v23-spanish-typography-resource-submissions-20261031.md](docs/v23-spanish-typography-resource-submissions-20261031.md) | **V23逐站操作说明**：UX Resources、LDS Library、Fountn、Enlineados；附可复制文案及证据缺口 |
| [data/v22-link-evidence-audit.csv](data/v22-link-evidence-audit.csv) | **10家逐站证据审计**：官方承诺、第三方rel抽样、实例、真实申请状态与DR来源 |
| [data/reusable-free-shortlist.csv](data/reusable-free-shortlist.csv) | 原10家无已确认强制回链徽章的研究清单，含已暂停或需核实渠道，**不等于10家可立即申请** |
| [data/education-resource-submissions.csv](data/education-resource-submissions.csv) | V20：3家教育资源馆藏渠道，明确非广告、教育资格及开放版权硬门槛 |
| [data/submission-ledger.csv](data/submission-ledger.csv) | 跨网站申请台账：以目标域名 × 外链平台注册根域名去重 |
| [docs/submit-guide-v16.md](docs/submit-guide-v16.md) | V16 逐站操作指南、西语/英文文案、已知限制 |
| [docs/v17-new-channels-20261030.md](docs/v17-new-channels-20261030.md) | V17 新增4家的官网证据、适配性、申请步骤、风险与填写模板 |
| [docs/v18-editorial-and-typography-20261030.md](docs/v18-editorial-and-typography-20261030.md) | V18 Typography新入口、4家西语编辑媒体及历史邮件查重报告 |
| [docs/v19-design-quality-and-shortlist-20261030.md](docs/v19-design-quality-and-shortlist-20261030.md) | **V19**：DesignTrash拒收条款、DesignBookmark语言限制、DesignMunk免费Nofollow、严格申请建议 |
| [docs/v20-educational-resource-channels-20261031.md](docs/v20-educational-resource-channels-20261031.md) | **V20**：MERLOT同类素材案例、OER Commons版权要求、Procomún当前HTTP500及逐字段投稿说明 |
| [docs/v21-curated-design-submissions-20261031.md](docs/v21-curated-design-submissions-20261031.md) | **V21**：两家真实设计投稿表单、官方精选规则、editor内页实测与可直接复制英文文案 |
| [docs/v22-backlink-evidence-and-six-actionable-submissions-20261031.md](docs/v22-backlink-evidence-and-six-actionable-submissions-20261031.md) | **V22**：10家证据分级、6家可尝试投稿、历史条件纠错与原创设计素材渠道 |
| [data/editorial-prospects.csv](data/editorial-prospects.csv) | 5家独立编辑推荐线索（新增UI Goodies；不等于免费投稿许可） |
| [data/editorial-outreach-ledger.csv](data/editorial-outreach-ledger.csv) | 跨网站真实编辑部联络历史：防止重复发送 |
| [docs/quality-policy.md](docs/quality-policy.md) | 证据等级、DR/AS/rel 核验、风险与验收定义 |
| [AGENTS.md](AGENTS.md) | AI / Codex 后续研究及更新规范 |
| [scripts/validate_csv.py](scripts/validate_csv.py) | 不依赖收费API的CSV一致性与重复提交键校验 |

**数据基线：2026-10-31 / V26。** 当前历史台账累计 176 条，包含 P1/P2、条件使用、待核验、排除及非外链渠道。过往第三方 DR 和 Follow 抽检信息应视为“历史证据”，不是实时保证。

**当前首批优先（2026-10-31）**：[LaunchFree四步真实填写与5家高相关目录执行清单](docs/current-priority-execution.md)；[GitHub Actions无法进入Runner的故障证据](docs/actions-pre-execution-diagnosis.md)。

## 新网站执行流程

1. 首先在 **submission-ledger.csv** 按 `目标站点根域名 + 外链平台注册根域名` 查重，再检查历史外链邮件和其他台账。
2. 在 **backlinks-master.csv** 按语言、站型、费用、相关性和状态筛选；不因为高 DR 就忽视西语资格、审核周期及强制回链条件。
3. 进入真实的提交页，填写原创而且与实际产品一致的介绍，不为操纵排名批量投低质量目录。
4. 提交后立即登记：平台、目标域名、提交日期、状态、账号（不保存密码）。
5. 审核后核验：公开条目 URL、目标 href、rel（nofollow/ugc/sponsored）、页面 robots/noindex、是否可索引、引荐访问及实际效果。
6. **只有公开页面确有正确出站链接时，才记为“已获链”；尚在审核或仅有账号不可记为获链。**

## 数据维护规范

- **原始事实与核查结论分开**：保留官方提交政策链接、第三方检测来源、核验时间。
- DR/DA/AS 属于不同第三方指标，不能混用；未知指标请写“未核实”，不填猜测值。
- 相同平台的多条URL按注册根域名汇总，避免跨网站重复推荐。
- “未见已申请”仅表示**当前台账没有记录**，不等于现实中从未申请。
- 不要求为了免费 Follow 在广告已上线的网站安装外部徽章或改变核心页面。
- GitHub 文件中不保存邮箱登录凭据、Token、DNS 验证值等敏感信息。

## 重点对象

- Generador de Lettering — https://generadordelettering.org/
- 后续其他西语站按各自类型建立提交记录；同一个外链平台可以服务多个不同的网站，但每一组合只能登记一次成功提交。

> 本仓库是内部研究与执行台账，不是对所列第三方平台的质量背书。
## 自动质量检查

仓库内置 [GitHub Actions 验证工作流](.github/workflows/validate-data.yml)，当 `data/` 的 CSV 或脚本发生变化时执行 `python3 scripts/validate_csv.py`。
此脚本仅验证数据结构和台账一致性，**不代表实际外链的权威度、Follow 属性或搜索引擎收录情况已经核实**。

## V17 本轮更新（2026-10-30）

- 新增四家：Good Design Tools（P1）、NoSignupTools（P1）、PeplioHUB（P1）、HereIsMySaaS（有条件）。
- Lettering 优先队列由9家更新为12家；未改变已有提交台账的实际状态。
- 自动检查新增**历史记录不得减少至150条以下、编号连续**规则。
- 实时 DR/AS、目标新页面 Follow 属性、Google 索引、真实引荐流量未全面实测；**没有任何新站点被代为提交，新增成功获链数为0**。

## V18 本轮更新（2026-10-30）

- 总库新增 `DesignTools.fyi` (#151)：官网具有正式的 Typography 投稿表单；免费资格、DR/AS、获批后的 Follow 属性未全面核验。
- Lettering 优先队列更新至 **13家**。
- 新增独立的**编辑媒体线索（4家）**与**既往编辑部联系台账（2条已发送记录）**：Gràffica 已于2026-10-25收到本网站介绍；EDUCACIÓN 3.0 于2026-10-12收到另一网站的教学材料。不能短期重复发送。
- 历史151个候选并不代表151条有效外链；本轮实际新增成功外链**0条**，未替用户发送新邮件或提交新表单。

## V19（2026-10-30）实际进展

- 新增 **DesignTrash、DesignBookmark、DesignMunk** 三家来源至总库（152–154）；它们都有明确**资格限制或免费Nofollow问题**，均未放进Lettering主优先队列。
- 新增8家更严格的免费优先/免强制徽章研究清单，先确认语言、广告、工具类型及免费规则，**不能把8家等同于8条已获链或8家已确认Follow**。
- DesignTrash明确拒绝关键词单功能生成器（举例cursive font generator），因此不建议对其投递Generador de Lettering。
- DesignMunk免费收录明确Nofollow；付费升级不得算“免费Follow”。
- Font Blend网页虽然提议通过GitHub提交资源PR，但公开仓库现仅README，没有能直接修改的资源数据文件；未列为可直接投稿入口。
- 自动校验基线调整为154条，并新增8家严格清单的重复根域名和必填依据检查。实际新增已获链仍为 **0条**；本轮没有第三方提交或邮件发送。

## V20 更新（2026-10-31）

- 总库新增 **MERLOT (#155)、OER Commons (#156)、Procomún / INTEF (#157)**，累计157条；全部是**有条件**的教育资源渠道，不纳入普通目录的8家免回链清单。
- 已查到 MERLOT 在2026-10-24收录同类型免费可打印字母描红练习资源，但它**禁止利用社区推广商业产品**；只能诚实提交具体学习材料，不得以广告获链为目的。
- OER Commons馆藏要求明确教育使用许可证；当前站点练习资源公开版权声明并不能证明具备教学再分发权，**未经用户明确授权不提交或更改许可证**。
- Procomún由西班牙INTEF提供，面向教师及教育从业者；本轮平台首页返回500，因此暂不能实测注册投稿。
- 所有 DR/AS/rel/索引数据未冒充实测；新提交数0、成功获链数0。

## V21 更新（2026-10-31）

- 新增 **TOOOLS.design（#158）** 和 **Design Resources Archive（#159）**：均直接验证官方投稿表单；前者官方称人工选中率少于4%，后者已有字体/排版实验工具的真实公开展示页。
- 当前网站 `https://generadordelettering.org/editor` 直接核验过画布/文字设计及PNG/JPG/WebP导出；设计类目录应优先说明这一**真实功能**，不声称会导出TTF、OTF、SVG或印刷文件。
- 可实际操作的原历史队列由13增至**15家**；更严格的免费优先研究清单由8增至**10家**。两家新渠道均未测得最新DR/AS，也不能保证出站Follow或Google索引。
- Usetools.Design 普通收录目前明确需€9.99，因此不应列入免费外链；Itmeo Index虽有字体工具馆藏，但没找到真实官方提交表单，不列入“可直接申请”。
- 没有向外部表单提交网站，也没有把新增候选计入已获链。**V21新获链0条。**

## V22 更新（2026-10-31）

- 总库新增 **Freebie Supply（#160）**：官方只接受原创免费素材，当前Submit Freebie页面无法核实实际可填写字段；这**不是**可立即提交的免费高DR渠道。
- 原10家重点候选完成证据分级审计：**TopTool官方暂停新投稿；Toolfound新的初次投稿步骤为URL、Email、Logo；TOOOLS.design第三方标为Nofollow/参考DR47；Good Design Tools第三方抽样60页390条外链无rel，参考DR25但仍需复测**。
- 建立6家可尝试申请的独立执行名单：LaunchFree、NoSignupTools、Design Resources Archive、Toolfound、PeplioHUB、DesignTools.fyi。只表示当前有公开入口及免费基础条件，**不等于审核或Follow已确认**。
- 编辑推荐新增 **UI Goodies（E005）**，由人工设计编辑选择，官网不出售普通入选；对广告干扰严重的站点可能拒绝。
- 现有15家历史队列、10家研究清单与实际提交台账都保留；本轮**实际新提交0，新增已获链0**。

## V23 更新（2026-10-31）

- 在160条完整历史记录基础上，新增3条未见同根域重复的设计/排版资源候选：**Fountn（#161，条件）、UX Resources（#162，可尝试）、LDS Library（#163，可尝试）**。当前共163条。
- 本次独立复核了历史已有的 **Enlineados（#3）**：只收西语且官网免费，但其**拒绝免费主机站点**，因此自购域名+免费Cloudflare Pages托管是否符合需先确认，绝不能虚填地点。
- V22的6家行动清单仍独立保留；V23新三家记录于新证据表，避免因混用口径改写V22十家审计结果。
- 实际新增提交 **0**、获批 **0**、已确认公开获链 **0**；所有新渠道的实时DR/AS、外链rel及索引保持“未实测”。

## V24 更新（2026-10-31）

- 主库从163增至 **167条**：Unikist (#164，设计工具投稿)、Mark-it (#165，设计资源人工精选)、DailyLaunch (#166，有西语免费产品发布，但网站需badge才获官网承诺的Follow)、Software Como Servicio (#167，免费强制Dofollow徽章，**排除**)。
- 两家公开设计投稿表单可尝试，但本轮**未独立实测DR/AS、目标页rel、Google索引、审核成功率**。DailyLaunch不计无条件免费Follow；Software Como Servicio不能以免费名义要求AdSense站装回链。
- 已核对The Tool Directory旧来源#9已是正确新版提交页，避免重复新增。Illustration.tools仍直接抓取超时，不算当前可执行。
- 本轮新增成功提交 **0**，经审核确认的新外链 **0**；V22的6家、V23的4项以及既往真实联络历史均保留不变。

## V25 更新（2026-10-31）

- 历史总库从167增至 **171条**：Herramientas y Recursos (#168，纯西语目录真实投稿表单)、FreeDesignerTools (#169，真实设计工具建议表单)、Ghostbyte Library (#170，官方GitHub Issue但采纳未知)、FounderOmni (#171，有西语资源建议控件但展开后的实际提交资格未核实)。
- **纠错现有#109 AI Webcatalog**：官网现在明确免费审核也必须安装Badge及填写徽章落地页，且仅适合AI工具；改为排除。保留历史行与证据。
- 编辑推荐线索新增 Best Productivity Resources E006，官网要求作者LinkedIn私信，**不属于可直接提交的普通目录表单**。
- 本轮实际第三方递交 **0**、新获批 **0**、新真实获链 **0**；实时DR/AS、真实rel、Google索引和引荐访问均未独立验收。

## V26 更新（2026-10-31）

- 主库171→**176条**：EpicTools（#172，有可用的Design提交入口及独立字体工具案例）、Learnlists（#173，仅真实教育实践资源适用）、Illustration Tools（#174，搜索索引有字段但官网实时访问受阻）、Discoverly（#175，强制badge，排除）、YAJU（#176，必须有真实墨西哥关联，本网站排除）。
- 新增独立**编辑邮件线索E007 The Creative Vault**；不与可填表的普通目录混淆，本轮没有发送任何邮件。
- 这批仅 EpicTools 为当前优先可尝试入口；其免费投稿不等于已获Follow。真实DR/AS、目标页rel、Google实际索引未实测。
- 实际新申请0、获批0、新确认获链0；保存全部历史和既有提交台账。

## V27｜已存档176个渠道全部逐站填写方法（2026-10-31）

**本次不新增外链渠道，仍是176条历史记录。** 将`data/backlinks-master.csv`第1至176号全部转成独立的可点击操作段落：每段均包含官网/表单、适用网站和语言、收费审核、历史具体步骤、Lettering填写示例、平台限制及证据层级。另从编辑媒体台账引入E001–E007七家联系线索，但不会把它们冒充普通目录。

- **全量手册（176个独立操作段落）**：[docs/all-176-backlink-submission-methods.md](docs/all-176-backlink-submission-methods.md)
- **优先填写卡（21家、平台真实字段/准备图片）**：[docs/lettering-priority-21-ready-to-fill.md](docs/lettering-priority-21-ready-to-fill.md)
- 历史分类：**P1 30条 / P2 21条 / 条件77条 / 待核验14条 / 排除33条 / 非外链1条**。其中#026 TopTool官网暂停新申请，#003 Enlineados免费托管资格需询问；这些属于历史状态而非今日全量复核。
- 2026-10-31官方重核证实：TopTool当前暂停；Enlineados官方排除免费主机站点。已在手册单列醒目警告。
- 本次**不发送邮件、不申请第三方账号、不实际提交网站、不装回链徽章、不修改历史递交台账**；新增成功获链仍未确认，DR/AS与真实Follow也不冒称已测。

## V28｜单文件离线操作台（2026-10-31）

- 在 `docs/backlink-submission-workbench.html` 新增一份**无需API、服务器、外部脚本、付费工具**的完整搜索页面，内嵌主表176条历史记录。
- 可以搜索站点/域名/限制、按资格和优先级筛选、展开真实历史提交步骤、打开官网、复制Generador de Lettering示例名称、URL、英西语说明、联系方式（需用户填写）。
- 能在浏览器本机使用LocalStorage自留提交进度/备注，并导出CSV备份。**不联网发送、不自动注册、不提交第三方表单、不修改GitHub真实提交台账**。
- 重要：请在GitHub找到HTML文件后点击**Download raw file**下载，再在Windows Chrome本地打开；仅在GitHub代码浏览页面无法实际操作。
- 已附 [操作台打开及使用说明](docs/workbench-quickstart-v28.md)，已经人工检查内嵌数据与主表176个编号、站名和入口一一对应，并检查页面JS语法及无第三方JS。历史数据仍176条，**新增已获反链为0，未独立验证DR/AS、Follow和索引**。

**V28验收说明（2026-10-31）**：操作台静态JSON包含176条，逐项名称、ID、提交入口与当前总库相符，JavaScript语法检查通过；不存在外部脚本。仓库GitHub Actions最近运行未通过，而且无法取得具体作业日志；虽然已恢复先前成功的原版验证脚本与工作流配置，**不能宣称本次GitHub Actions已通过**。操作台本身已上传，但仍需用户用Chrome本地打开做界面实际操作验收。

## V29｜离线操作台真正逐字段可复制（2026-10-31）

- 仍是原来的 **176个历史渠道**，**没有新增已获链**。现在21家优先来源的**133个字段行**被直接嵌入HTML操作台，每家独立展示原始真实字段、历史示例与独立复制按钮；不再只是让用户去看另一份Markdown。
- 不同西语网站的提交工作记录改为按**目标域名独立本地存储**，兼容迁移旧V28对Lettering的记录，禁止把旧网站“已提交”套到另一个新站。
- 当切换到新品牌或域名，Lettering特有介绍、功能类别和教学资源路径不再作为可直接复制的事实；要用新站真实功能重写。
- 保留历史Python验证，加了 `scripts/validate_workbench.mjs`，用于当Runner恢复时检查176条JSON、21家字段133行、页面JavaScript语法和无外部网络依赖。
- **CI仍显示失败，未取得绿色结果**：曾添加不依赖checkout/用户代码的Runner探针也失败，换成`ubuntu-24.04`仍失败；无法取得GitHub失败作业的日志，故不能确定确切原因，更不能声称全部测试通过。证据详见 [V29执行与CI记录](docs/v29-field-level-workbench-and-ci-evidence.md)。

## V30｜跨站真实填写 + 备份恢复（2026-10-31）

- **不新增外链渠道**：仍是176条历史记录，21家重点平台共133行字段。升级后新站可直接使用自己在顶部改写的西语/英语短描述与长说明；原Lettering专用文案不会冒充别的网站真实功能。类别/收费/地域/身份须人工核实。
- **多站独立进度真正可备份**：新增“备份所有网站JSON”和“恢复进度备份”，含使用者当前网站资料及所有目标域名的本地标注。恢复时检查渠道编号、文件大小、阶段与实际域名并提示是否覆盖。**备份可能含邮箱与备注，不得上传公开仓库**。
- 仍保留当前域名CSV导出，并增加对电子表格危险公式起始字符的转义，减少Excel/Sheets直接打开的注入风险。
- **本轮V8模拟交互11项通过**（176渲染、EpicTools检索、状态、域名隔离、JSON备份/恢复、CSV等），单独字段映射逻辑7项通过；新增可复现`scripts/smoke_workbench.mjs`。不等于真实Chrome端到端或第三方目录提交测试。
- **GitHub Actions暂未成功**：此前最小Runner探针不依赖项目代码也失败，连接器无法提供日志；因此继续保留`ci失败/原因未定`的明确状态。使用说明和[详细证据](docs/v30-cross-site-field-mapping-and-backup.md)均已更新。没有修改真实递交台账，没有生成已获链记录。

## V31｜17家官网表单实测，纠正旧字段（2026-10-31）

- 主库仍为**176条历史外链渠道**，分类已更新为：P1 29、P2 21、条件77、待核验15、排除33、非外链1。#014 Lugar Latino虽然搜索索引仍有西语提交入口，但本轮官方入口多次直访404，改为**待核验**，暂不当可操作来源。
- 本轮对**17家已有来源**重新读取官网真实表单，核实入口、限制、需不需要图片/邮箱、是否强制badge，**0家重复新增**。审查记录见 [17家官方复核说明](docs/v31-17-live-form-verification-20261031.md) 和 [机器可读审计表](data/v31-official-form-audit-20261031.csv)。
- **修正#147 Good Design Tools**：其Tally投稿并没有旧卡所写Category/Tags；实际包括工具名、网址、介绍、定价、优惠、联盟计划、图标（JPG/JPEG/WebP/SVG≤2MB）和Email。**#123 LaunchFree** 的创建者姓名、Short Bio、产品起因、验证码不可省略。**#128 Toolfound** 申请免费但必须完成域名所有权验证。**#151 DesignTools.fyi** 有Source of Truth/Size/公司代表复选框。
- 更新 [176完整逐站手册](docs/all-176-backlink-submission-methods.md)、[21家精确填表卡](docs/lettering-priority-21-ready-to-fill.md) 与 [离线操作台](docs/backlink-submission-workbench.html)。现在21家共有**149项**已整理的字段行，17家卡片有V31官方复核提醒。
- **第三方正式申请0、实际新增反向链接0、真实Follow/DR/AS/Google索引不作未经核验的保证**。GitHub Actions前期Runner/作业仍失败，静态核对不等于本轮CI绿灯。

## V32｜第二批14家原有渠道实际表单复核（2026-10-31）

- **本轮只研究已收录的14家来源，不增加新平台，也未为Lettering提交任何表单。** 主库仍176家；最新分类 **P1 25、P2 21、条件79、待核验16、排除34、非外链1**，不是成功获链数。
- **值得优先研究填写**：`#074 public.tools` 已确认官网页脚Tally真实四字段和Graphics & Design类别；`#075 Htrd` 首页底部有真实五字段表单；`#171 FounderOmni` 西语设计资源馆藏已确认弹层字段“Tipo de solicitud / Categoría / Nombre de la ficha / URL pública / Por qué / 邮箱可选”。免费收录与实际rel仍需等待审核/独立核查。
- **需要先确认资格**：`#057 ToolGuide`重点是工作效率软件，描述上限120字符不是120词；`#076 NoUploadTools`禁止会话回放且隐私勾选至少一项，AdSense站不得选No ads；`#003 Enlineados`明确禁止免费主机；`#141 GainWeb`的Regular Free不保证审核。
- **暂时跳过**：`#026 TopTool`官网暂停，`#152 DesignTrash`官方拒此类单一关键词生成器，`#160 Freebie Supply`真实填表未成功读取，`#161 Fountn`外部提交通道无法解析，`#170 Ghostbyte Library`只是GitHub Issue建议而非公开获链。教育类`#173 Learnlists`有严格互动学习内容门槛。
- [完整V32审计说明](docs/v32-14-official-source-audit-20261031.md)和[CSV](data/v32-official-source-audit-20261031.csv)已建立，`data/backlinks-master.csv`、176条长文、21家具体字段卡及[离线HTML操作台](docs/backlink-submission-workbench.html)已同步。重点21家现在**161行字段**，HTML上该14家带V32提醒。
- **验证边界**：本次自有V8执行了数据结构检测和模拟交互11项，均通过；不是实际浏览器端到端或第三方目录获链。GitHub Actions曾出现Runner层故障，未得到本轮GitHub CI成功记录。申请0、获链0、真实Follow/DR/AS和索引均未证实。

## V33｜从“可投稿”升级为“实际公开href/rel抽样核验”（2026-10-31）

- **本轮实际检查11条已发布链接样本，另查9个目录页面是否出现本站域名**，无外链提交、无邮件发送。不同平台实际出站链接价值差异极大，**免费表单不等于可获得Follow外链**。
- **#074 public.tools原P1降为条件**：三条真实公开详情（StackEdit、Dillinger、Glyphr Studio）外部工具链接的HTML均含`rel="noopener noreferrer nofollow"`。这只证明三条样本，并不代表该平台所有页面；其投稿表单仍有效，若目标是引荐流量可以保留但Follow优先级下降。
- **已读到非nofollow样本**：Htrd（Fontjoy、Squoosh各1条）、Toolfound（StencilMaker、Offistrip各1条）、DesignTools.fyi（Font Explorer）、NoSignupTools（FontsWiki）、Herramientas y Recursos（Recursos两个第三方链接）。这些样本均未看到nofollow/ugc/sponsored，但不保证Google传递排名信号、更不保证审核和Lettering获链。
- **Lettering未检出范围**：已读取的public.tools 344工具目录内容，及Htrd首页、Toolfound首页、DesignTools首页、NoSignupTools设计类别、西语Recursos分类、FounderOmni西语设计页、UX Resources/Typography与LaunchFree首页等；这些只是**检查范围内未检出**，不得报告“整站一定没有”或“被拒”。
- **主库仍176条**：最新P1 **24**、P2 **21**、条件 **80**、待核验16、排除34、非外链1。优先执行5家公开样本未带nofollow的研究候选：Htrd、Herramientas y Recursos、NoSignupTools、DesignTools.fyi、Toolfound（后者必须核验域名所有权）。离线V33操作台加入真实rel提醒和“V33公开样本优先”排序。
- 为防止镜像数据错乱，`scripts/validate_workbench.mjs`现在将176条离线页面JSON与主表CSV逐条核对，并核对11条真实样本及public.tools 3/3 nofollow事实。V33还修复了上版两份Node验证脚本内容错放路径的问题。**GitHub Actions旧Runner失败问题尚无可信绿色结果**；本地验证通过不等于CI通过。V33新增第12项交互排序回归检查，并修复测试文件职责对调问题。
- [详情与边界](docs/v33-public-link-rel-and-listing-presence-20261031.md)。实际新增为Lettering确认的反向链接仍是 **0**。

## V34｜字体和设计类平台的21条真实公开href/rel复核（2026-10-31）

- 本轮**没有新增目录来源**，在原176家内检查21条其他网站已发布的外部href，另做11个类别/详情页的目标域名出现核查。**没有代投网站，没有替Lettering获得新的确认外链**。
- **#005 The Free Tools Directory** 已发表的`1000 Font Generator`详情页真实href带`rel="noopener nofollow"`；**#162 UX Resources** 4条Typography工具（Minglyph、Fontmojo、Cursive Generator、Fontshare）的真实外站href均`rel="noopener sponsored"`。两者在免费普通Follow目标下由P1调为**条件**，不声称整站全是nofollow或sponsored。
- **第二批5家设计/字体目录优先人工研究**：`#159 Design Resources Archive`、`#163 LDS Library`、`#164 Unikist`、`#172 EpicTools`、`#165 Mark-it`。字体、排版、设计类的已公开样本未见nofollow/ugc/sponsored，但免费投稿获批、自己条目的rel及DR/AS仍未证实。EpicTools的Partner展示与Curated详情严格区分。
- 还抽查`#169 FreeDesignerTools`与`#141 GainWeb`出站链接；GainWeb的免费/收费来源难以区分，不据此升优先。`#149 PeplioHUB`没有抽出可识别的产品官网静态href，`#147 Good Design Tools`样本详情读取失败，均保持未知，不误判成无外链或Follow。
- 当前主库分类：**P1 19、P2 23、条件83、待核验16、排除34、非外链1，共176家**。V34离线HTML新加11家实际href/rel提醒及“V34字体设计样本优先（非保证）”排序。21家优先卡仍含161项实际表单字段。可以直接从[第二批5家填写指南](docs/v34-five-more-design-font-directories-ready-to-fill.md)逐站操作。
- V34校验：独立V8执行`scripts/validate_workbench.mjs`逻辑，验证176条主表、V33的11条和V34的21条证据、21家字段；`scripts/smoke_workbench.mjs`模拟DOM与两种排序，共**13项**交互检查通过。**这些不代表GitHub Actions CI或实际Chrome点击已通过**，也不代表第三方申请成功。

## V35｜外链申请后必须有可验证的公开href（2026-10-31）

- **版本继续使用176条候选主库，没有增加任何未经核实的平台，也没有新提交或确认获链。** 本轮转向完善公开获链证据与收录跟进：把“已填表”“审核中”“已上线待验链”与实际发布的HTML链接证据严格隔离。
- [V35离线工作台](docs/backlink-submission-workbench.html)为每家平台新增**真实第三方公开条目URL、指向自己站点的实际href、原始rel**三个字段，以及“我已亲自检查”的按钮。用户明确点击才记为**本地人工自查确认**；字段编辑会撤销之前确认；每个目标域名分别保存，不会跨网站借用。**本地自查不是联网确认，更不会自动写入GitHub正式submission-ledger。**
- 原CSV导出追加公开页/href/rel/自查状态/自查日期；JSON全站备份与导入严格保留并校验V35证据字段，旧版本不含证据的备份仍兼容。
- [零付费公开HTML验链脚本](scripts/verify_published_backlink.py) 允许Windows本地 `python scripts/verify_published_backlink.py --source "真实第三方公开页HTTPS" --target "https://generadordelettering.org/"`，读取指定公开页实际`<a href>`、匹配真实目标域名与`rel`，生成JSON。不假设跨页收录、不爬全站、不登录、不提交、不绕过验证，受HTTPS、私网限制及2MB大小约束。
- **已实测**：V8独立运行离线HTML结构核验及含人工证据保存、无效源拒绝、改动撤销、跨域隔离、备份与CSV导出的交互模拟；正常通过。**尚未实测**：8组Python离线测试在真实Python解释器的执行结果；仓库已增加测试源码并接入Actions，但Actions仍在任务启动前/无步骤状态失败，不夸大为通过。
- 详细示例及Windows操作见 [V35完整说明](docs/v35-evidence-based-backlink-verification.md)。实际为`generadordelettering.org`新增确认外链仍是**0**。

## V36｜多网站资料隔离，旧网站的信息不再被误填给新站（2026-10-31）

- 操作台以前只隔离`submission marks`，网站名称、站点简介、联系邮箱和工具URL却是单个全局资料。V36改为 **`xibanya-profiles-by-domain-v36`** 逐域名储存：新网站第一次切入时，只保留自己主页；名称、西语/英语长短说明、邮箱、编辑器URL全部留空。切回旧网站时自动恢复该站自己的完整资料和原提交进度。
- 现在备份格式为**V2**：包含`profile`（当前站）+`profiles`（所有站）+`progress`（所有站原进度与人工href/rel证据）。旧版**V1文件仍能恢复**，但它只曾记录一个站的资料，不能还原从未备份的其他站简介或Email。
- V2恢复加入跨域资料真实性校验：`profiles[域名].home`须与域名匹配、`tool`不得是另一个域名链接、资料和域名数量均有限制；无效文件不得覆盖本机数据。**所有资料仍存本地，不会自动发布外链或发送至GitHub。**
- 已通过独立V8运行的176主表、21家161项字段、V33/V34公开链接证据、HTML语法与**23项模拟交互检查**，包括跨域切换、返回旧站、V2多站备份、V1兼容迁移及非法跨域导入拒绝。不是实际Chrome端到端或GitHub Actions成功运行。
- **[查看V36完整Windows操作说明](docs/v36-domain-isolated-profiles-and-v2-backups.md)**。仓库仍176条历史候选，本轮第三方实际提交0、确认新增获链0。GitHub Actions继续失败，其job步骤/日志仍不可用，根因未证实。

## V37｜实际运行Python验证与外链误判修复（2026-10-31）

- 此轮**真实Python 3.13.5执行**`python -m unittest discover -s . -p 'test_verify_published_backlink.py' -v`，结果**11 tests OK**，语法编译也通过；两份测试文件与GitHub提交后的Git blob SHA**逐字节一致**：`verify_published_backlink.py`=`8a085d84057e17557a7ffff2f5c937ea68caa20c`，`test_verify_published_backlink.py`=`e86742cee41db53c85e774a790aeb850c4c9a2f8`。
- 修复三种误判：损坏的`<a href>`不再中断整页检查；空值`rel`不会导致崩溃；HTML`<template>`内惰性链接不再被算成真实公开锚点。新增3个回归测试、原8项仍通过。**不代表已经联网确认目标网站获链。**
- **[完整V37测试证据与GitHub Actions故障说明](docs/v37-python-backlink-verifier-tested-and-ci-diagnosis.md)**：最新Actions仍失败，validate任务缺少已执行步骤记录，因此不能声称CI通过，也不能擅自归因为Python测试失败或Runner限制。
- 主库、目录、实际提交记录没有增删；**176条来源/21家161项字段，新确认反向链接0、申请0**。V36每域名资料隔离和V2备份保持有效。

## V38｜高相关西语、字体和设计目录公开证据优先（2026-10-31）

- **[V38 14家逐站实时公开核验与3张新填写卡](docs/v38-high-relevance-public-evidence-20261031.md)**；**[机器可读公开证据CSV](data/v38-high-relevance-public-evidence-20261031.csv)**。这一轮不新增目录，仅复核原176家中的14家：具体提交表单、相关第三方公开资料页、是否实际出现站外href、受限入口及风险。
- 新发现：#171 FounderOmni此前只见建议按钮，这次已读到西语表单完整字段，并观察到Hero Patterns公开独立详情指向原站；#168西语目录能见文字图形同类项目，但单条详情页仍超时；#151 DesignTools.fyi有104个工具及Typography栏目与独立公开外站链接。#169 FreeDesignerTools虽可投稿，首页只有12项，质量优先级后置。
- **不要误记**：本轮再次验证的是其他人的公开链接形式，raw rel不是每页都能独立获取；既未提交，也未给generadordelettering.org新增已确认外链。V38证据文件是待同步主表的细化审计，不直接改176主库、衍生手册或离线HTML的事实镜像。当前依然**0条本轮确认获链**。

## V39｜真实出站链接路径核验与176项同步（2026-10-31）

- [V39链接路径质量报告](docs/v39-link-path-quality-reconciliation-20261031.md)与[6个样本CSV](data/v39-sample-link-path-audit-20261031.csv)：#168普通详情通过`/salir/`站内中转，旧两条`noopener`外链实际来自页脚关联站，因此从P1降至**条件**，不作为已验证普通Follow；#151的Font Explorer原始rel早在V33已记录；#171六项表单字段早在V32已核，本轮新确认Fontpair和Hero Patterns独立详情外站href，但原始rel未知。
- 已同步176主库、176条逐站手册、离线操作台；新增来源0、实际申请0、本站新确认外链0。GitHub Actions未因此被证明成功。

## V40｜高相关字体目录规范域名与刊登路径质量（2026-10-31）

- [V40最新审计](docs/v40-curated-font-design-quality-audit-20261031.md)与[9条公开网页样本CSV](data/v40-curated-link-evidence-20261031.csv)。在原176渠道中核查真实的编辑目录资源链接和提交资格，不新增泛目录。
- #163 LDS Library的旧lds-library.vercel.app目录/表单canonical指向library.legitdesign.studio，同路径在规范域可访问；主库与填写卡更换规范域入口，仅算一个渠道。
- #165 Mark-it的/font虽有真实直接外链，但资源较少，首页All Resources转到独立Vercel交互目录且无法确认普通收录详情；P1降为P2。当前P1 20、P2 22、条件83、待核验16、排除34、非外链1，共176；本站新增实际申请0、确认新获链0。

## V41｜目录真实编辑质量复核 + 逐字段准备包（2026-10-31）

- [V41核验结论与5家可填写申请包](docs/v41-editorial-quality-and-ready-to-submit-pack-20261031.md)；[逐字段机器可读CSV](data/v41-field-by-field-submission-pack-20261031.csv)；[公开事实/风险CSV](data/v41-editorial-quality-evidence-20261031.csv)。不再依靠目录总数或某条nofollow以外的`rel`判断质量。
- **#172 EpicTools从P1降为P2**：其“Newest Additions”将过期域名拍卖页面与Cloudflare安全拦截内容标为Curated，显示编辑过滤有明显噪声。仍保留已确认的真正产品详情站外href和两字段官方表单，不误称平台无外链。
- #159 Design Resources Archive实时验证的表单仅有Link URL、Description、当页人机题目，旧数学题目不可复用；#164 Unikist严格按≤280字符；#151 DesignTools.fyi姓名/邮箱真实且“代表公司”选项依事实；#163 LDS新规范域可访问但完整表单字段本轮未重新抓取，仍按V23历史字段待人工复核。
- 历史176家：**P1 19、P2 23、条件83、待核验16、排除34、非外链1**。实际新投稿0、本站新确认获链0；未独立实测DR/AS、Google索引和本网站获批页raw rel。CI仍须独立运行验证，不能从提交成功推断通过。

## 当前执行优先级与CI阻断证据（2026-10-31）

- **[现行首批真正可人工执行的高相关渠道清单](docs/current-priority-execution.md)**。LaunchFree有真实Fontique（Lettering）、Free Text Symbols（Fancy Text）和西语Rueda Decide的独立公开页，可优先试申请。完整四步材料已核对Tagline 54字符、Description 252字符，真实开发动机/个人身份不能代编；另附[5条原始公开证据](data/current-priority-evidence.csv)。官网自称Dofollow，并非本轮raw rel已证实。
- **[CI启动前故障诊断](docs/actions-pre-execution-diagnosis.md)**：实测运行41160234903的validate job steps=null、billable duration=0ms、没有runner及日志，无法把failure归咎于Python/Node测试，也不能声称修复。仓库/账户Actions设置与Billing须以网页系统错误为准，优先免费排查。
- 现有176家总库和P1 19 / P2 23 / 条件83等历史分类不变；没有代提交或获得本站确认外链。

## 西语本土目录有效性核验（2026-10-31）

- [西语三个渠道逐站核验与人工步骤](docs/spanish-native-directory-audit.md)；[7项可追溯公开页面和资格声明](data/spanish-native-directory-audit.csv)。#59 Navegax公开西语详情真实直达外站，但必须注册；#58 Educaguía明确只收教育资源且申请自动加入教育通讯，缺真实教学资源时勿投，P1→条件；#4 DrSEO的€0基本档明确存在，但本次具体直链样本为Premium/Patrocinado，不能当免费rel，P1→P2。
- 最新176条分类 **P1 17、P2 24、条件84、待核验16、排除34、非外链1**；HTML展示已修正历史误写的“排除33”和现时优先/条件统计。新增候选0、真实申请0、本站新确认获链0。

## V43｜开放式泛目录筛选与免账号提交（2026-10-31）

- [Zearches免费填写与低质量证据](docs/open-directory-quality-audit.md)及[6条逐页证据CSV](data/open-directory-quality-evidence.csv)：#27 Zearches确实无账号/付费/强制回链，但11,600+自动收录、约2,923家软件站、10条/页，且公开分类存在违反其自述内容限制的记录。**P1降条件**，不放首批优质链接队列。正式直达投稿页为https://zearches.com/submit-website-free.php，隐藏反垃圾字段不可填，捐款非强制。
- #59 Navegax推荐的Bitakoras只接受博客，工具站不可另算新渠道。176家总量不变，最新**P1 16、P2 24、条件85、待核验16、排除34、非外链1**；真实提交0、确认用户站新获链0。

## V44｜Educaguía教育实证与操作台排队纠错（2026-10-31）

- [V44详细核查](docs/v44-education-qualification-and-workbench-priority-20261031.md)：目标站已实际公开4种SVG A4练字模板和7天练字计划，#58 Educaguía据真实材料从条件升为P2申请候选；仍须教育目录人工审核且自动订阅教育通讯，不代表获批。
- 离线HTML的公开链接/字体设计/历史推荐排序修复：条件/排除渠道不会再靠陈旧样本排名位于当前P1/P2前面；跨网站复制教育资源URL不再用其他网站普通工具页填充，其他自动网址需要同域名。
- **当前176家：P1 16、P2 25、条件84、待核验16、排除34、非外链1。** 尚无用户实际投稿与新增确认反链。Node测试断言已更新，但CI是否执行仍须另行核验。

## V45｜多站教育资源URL独立字段（2026-10-31）

离线填写台新增可选`edu`网址，按当前网站独立保存真实教学资料页。教育渠道只复制同域HTTPS教育网址；未填写时为空，不会套用普通工具地址。旧V1/V2 JSON备份即使没有该字段仍可兼容导入，其他站点资料和进度保留。详见[V45操作与测试报告](docs/v45-education-url-backward-compatible-20261031.md)。**外链仍未经实际提交或验收。**

## V46｜原P1十六家官方资格及公开外链证据复核（2026-10-31）

- [16家逐项定位与3家降级解释](docs/v46-p1-official-eligibility-and-link-evidence-20261031.md)；[15项官网/现有网站证据CSV](data/v46-p1-official-evidence-20261031.csv)。#6 kis.tools 要求核心无干扰广告、输出无商用限制，本网站广告展示和素材授权未证实，降条件。#88 Resource.fyi 免费普通目录与编辑Best-of是不同展示，降P2。#147 Good Design Tools的Tally表单正常但目标主页/详情本轮返回502、填写邮箱会同意周更邮件，降P2。
- SideProjects.net仍P1：官网Free $0永久产品页与站方宣传Dofollow，真实新链接raw rel未测，需登录。PeplioHUB在V46时仍为P1（V53已有ugc nofollow实证、现降条件）：AI首先审核、必要时人工、可选Badge影响提前排期，平台可能改nofollow/ugc；都是免费曝光候选而非SEO效果承诺。
- 原176总量不变，**V46时**分类为P1 13、P2 27、条件85、待核验16、排除34、非外链1；V53最新为P1 12、P2 27、条件86。申请和确认新获链仍为0。

## V47｜13家P1的公开出站证据逐条落地（2026-10-31）

- [13家实际发布链接与验收边界](docs/v47-thirteen-p1-outbound-link-audit-20261031.md) + [13行可审计矩阵CSV](data/v47-current-p1-outbound-proof-matrix-20261031.csv)；现行13家P1都有HTML操作台证据段。11家读到已刊登的**其他网站**的直接站外href，6家有旧V33/V34针对来源页的原始`rel`历史样本；其余2家产品Launch暂没有可核验具体独立第三方站外href。多数本轮网页只能抽取清理后的HTML，不能从其推断原始rel。
- **纠正旧版填写工作单**：Educaguía已因网站真实Lettering练习纸和七天计划恢复P2，不再在现行申请表中显示V42过期条件。PeplioHUB详情出站href含`?ref=pepliohub`，Mixweight详情出站含UTM，必须与无跟踪的直接URL、raw rel分开理解；Unikist旧`noreferrer`会影响referrer统计，不等于nofollow。
- V47时主库176与P1 13/P2 27/条件85等分类不变（V53现已降Peplio、最新P1 12/条件86）；这只是证据深化，用户实际申请0，本站新增确认获链0。

## V48｜前五家直接填写材料（2026-10-31）

[当前5家逐字段申请包](docs/v48-top5-forms-ready-to-fill-20261031.md)与[38组字段CSV](data/v48-top5-submission-fields-20261031.csv)已按当日官方表单刷新。NoSignupTools真实图标≤1MB、可选截图最多6张各≤2MB，本站有广告不可勾No Ads；LaunchFree个人真实资料/为什么开发不可编造；DesignTools.fyi不可伪称公司代表。早期176家手册首页过期统计更新到P1 13、P2 27、条件85。**仍未代提交，新增确认外链0。**

## V49｜一条免费命令复核13家P1原始HTML的rel（2026-10-31）

[Windows PowerShell教程](docs/v49-p1-raw-rel-batch-audit-and-comma-fix-20261031.md)：`py .\scripts\audit_p1_published_links.py`。读取现有13家P1证据CSV、只抓其中11个真实公开详情页的原始HTML，一次一页、无付费API，单独记录实际完整href、本次raw rel和历史rel。另修复`nofollow,ugc`逗号写法被旧脚本误报无限制的错误，增加离线单元测试。**没有在本仓库声称本轮已实际运行在线批量抓取，其他网站的原始rel不等于Generador已获得外链**。

## V50｜Educaguía公开案例误标自家网址修正

#58在旧操作台“历史公开案例”误放用户自有练字教学页，现在改为[Educaguía公开教育网站目录](https://www.educaguia.com/listadoEDU.asp)；名录的确有[Educaplay](https://www.educaplay.com/)等外站href，但不证明用户站已获批。拟提交目标仍是实际练字资料，不能把自己的网址视为反向链接。静态和模拟测试新增防误标断言。[详细V50修正](docs/v50-educaguia-real-external-example-20261031.md)。

## V53｜最新可执行质量分层（2026-10-31）

最新[14家真实站外链接DOM属性证据](docs/v53-current-rendered-dom-rel-and-peplio-downgrade-20261031.md)：13个特定公开样本未观察到nofollow/ugc/sponsored，PeplioHUB #149的[AnyFyle公开详情](https://peplio.com/anyfyle/)含`rel="noopener ugc nofollow"`，从P1降条件。**当前P1=12、P2=27、条件=86、待核验=16、排除=34、非外链=1，合计176**。以前README的P1 13/16/19等数字是当时历史快照，不能作为最新提交名单。历史第三方样本不是Generador获链：**真正新增确认链接0**。V54按现场表单摩擦重排为#159→#164→#163→#151→#075→#148→#123；不要凭无nofollow样本宣称SEO权重。

## V54｜7家高相关目录官方表单现场复核（2026-10-31）

[完整现场字段、限制与可复制英文说明](docs/v54-live-submission-forms-and-ready-to-fill-pack-20261031.md)｜[7家逐行表单CSV](data/v54-live-submission-form-audit-20261031.csv)。V54确认#159表单只有URL/介绍/动态算术题必填，验证码会变；#164动态分类/价格未展开；#151需要真实姓名邮箱，Logo可选；#075需区分首页工具投稿表单与Newsletter；#148不要选No Ads；#123需真实创办故事与身份。**尚未人工提交，本站新增确认外链仍为0。**
