# 西班牙语网站外链资源库 (xibanyayuwailian)

用于管理西班牙语网站的外链候选、实际申请、审核结果与公开获链证据。**本仓库中的候选数量不代表有效外链数量，也不代表已取得的 Follow 链接数量。**

## 从这里开始

| 文件 | 用途 |
| --- | --- |
| [data/backlinks-master.csv](data/backlinks-master.csv) | V20 累计157条渠道/候选（V19原154条保留，本轮新增3条），完整保留历史记录 |
| [data/priority-queue.csv](data/priority-queue.csv) | 面向 Generador de Lettering 的13家历史申请候选（含部分不推荐项），不要全部照单提交 |
| [data/reusable-free-shortlist.csv](data/reusable-free-shortlist.csv) | **优先看这张**：8家免强制回链徽章的免费/待核验渠道，区分资格与证据缺口 |
| [data/education-resource-submissions.csv](data/education-resource-submissions.csv) | V20：3家教育资源馆藏渠道，明确非广告、教育资格及开放版权硬门槛 |
| [data/submission-ledger.csv](data/submission-ledger.csv) | 跨网站申请台账：以目标域名 × 外链平台注册根域名去重 |
| [docs/submit-guide-v16.md](docs/submit-guide-v16.md) | V16 逐站操作指南、西语/英文文案、已知限制 |
| [docs/v17-new-channels-20261030.md](docs/v17-new-channels-20261030.md) | V17 新增4家的官网证据、适配性、申请步骤、风险与填写模板 |
| [docs/v18-editorial-and-typography-20261030.md](docs/v18-editorial-and-typography-20261030.md) | V18 Typography新入口、4家西语编辑媒体及历史邮件查重报告 |
| [docs/v19-design-quality-and-shortlist-20261030.md](docs/v19-design-quality-and-shortlist-20261030.md) | **V19**：DesignTrash拒收条款、DesignBookmark语言限制、DesignMunk免费Nofollow、严格申请建议 |
| [docs/v20-educational-resource-channels-20261031.md](docs/v20-educational-resource-channels-20261031.md) | **V20**：MERLOT同类素材案例、OER Commons版权要求、Procomún当前HTTP500及逐字段投稿说明 |
| [data/editorial-prospects.csv](data/editorial-prospects.csv) | 独立编辑推荐候选清单（不等于免费投稿许可） |
| [data/editorial-outreach-ledger.csv](data/editorial-outreach-ledger.csv) | 跨网站真实编辑部联络历史：防止重复发送 |
| [docs/quality-policy.md](docs/quality-policy.md) | 证据等级、DR/AS/rel 核验、风险与验收定义 |
| [AGENTS.md](AGENTS.md) | AI / Codex 后续研究及更新规范 |
| [scripts/validate_csv.py](scripts/validate_csv.py) | 不依赖收费API的CSV一致性与重复提交键校验 |

**数据基线：2026-10-31 / V20。** 该版历史台账累计 157 条，包含 P1/P2、条件使用、待核验、排除及非外链渠道。过往第三方 DR 和 Follow 抽检信息应视为“历史证据”，不是实时保证。

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
