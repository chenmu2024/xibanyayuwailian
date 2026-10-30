# 西班牙语网站外链资源库 (xibanyayuwailian)

用于管理西班牙语网站的外链候选、实际申请、审核结果与公开获链证据。**本仓库中的候选数量不代表有效外链数量，也不代表已取得的 Follow 链接数量。**

## 从这里开始

| 文件 | 用途 |
| --- | --- |
| [data/backlinks-master.csv](data/backlinks-master.csv) | V25 累计171条渠道/候选（保留V24的167条，本轮新增4条；另修正历史#109强制Badge状态），完整保留历史记录 |
| [data/priority-queue.csv](data/priority-queue.csv) | 面向 Generador de Lettering 的15家历史申请候选（含条件、低优先项目），不要全部照单提交 |
| [data/actionable-applications-v22.csv](data/actionable-applications-v22.csv) | **现在先看这张**：6家当前可尝试申请的免费优先渠道，含入口与填写准备（不保证审核/Follow） |
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

**数据基线：2026-10-31 / V25。** 当前历史台账累计 171 条，包含 P1/P2、条件使用、待核验、排除及非外链渠道。过往第三方 DR 和 Follow 抽检信息应视为“历史证据”，不是实时保证。

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
