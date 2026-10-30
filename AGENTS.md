# AGENTS.md — 外链资源库维护规范

本仓库用于**西班牙语网站通用外链库**，任何 AI、Codex 或维护脚本必须遵守：

1. 先读取 `README.md`、`docs/quality-policy.md`、`data/backlinks-master.csv`、`data/reusable-free-shortlist.csv`、`data/submission-ledger.csv`、`data/editorial-prospects.csv`、`data/editorial-outreach-ledger.csv`，再查找或更新渠道。
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
