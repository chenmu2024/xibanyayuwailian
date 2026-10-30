# 西班牙语网站外链资源库 (xibanyayuwailian)

用于管理西班牙语网站的外链候选、实际申请、审核结果与公开获链证据。**本仓库中的候选数量不代表有效外链数量，也不代表已取得的 Follow 链接数量。**

## 从这里开始

| 文件 | 用途 |
| --- | --- |
| [data/backlinks-master.csv](data/backlinks-master.csv) | V18 累计151条渠道/候选（V17原150条保留，本轮新增1条），完整保留历史记录 |
| [data/priority-queue.csv](data/priority-queue.csv) | 面向 Generador de Lettering 的当前13家重点渠道，按实际执行顺序排列 |
| [data/submission-ledger.csv](data/submission-ledger.csv) | 跨网站申请台账：以目标域名 × 外链平台注册根域名去重 |
| [docs/submit-guide-v16.md](docs/submit-guide-v16.md) | V16 逐站操作指南、西语/英文文案、已知限制 |
| [docs/v17-new-channels-20261030.md](docs/v17-new-channels-20261030.md) | V17 新增4家的官网证据、适配性、申请步骤、风险与填写模板 |
| [docs/v18-editorial-and-typography-20261030.md](docs/v18-editorial-and-typography-20261030.md) | V18 Typography新入口、4家西语编辑媒体及历史邮件查重报告 |
| [data/editorial-prospects.csv](data/editorial-prospects.csv) | 独立编辑推荐候选清单（不等于免费投稿许可） |
| [data/editorial-outreach-ledger.csv](data/editorial-outreach-ledger.csv) | 跨网站真实编辑部联络历史：防止重复发送 |
| [docs/quality-policy.md](docs/quality-policy.md) | 证据等级、DR/AS/rel 核验、风险与验收定义 |
| [AGENTS.md](AGENTS.md) | AI / Codex 后续研究及更新规范 |
| [scripts/validate_csv.py](scripts/validate_csv.py) | 不依赖收费API的CSV一致性与重复提交键校验 |

**数据基线：2026-10-30 / V18。** 该版历史台账累计 151 条，包含 P1/P2、条件使用、待核验、排除及非外链渠道。过往第三方 DR 和 Follow 抽检信息应视为“历史证据”，不是实时保证。

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
