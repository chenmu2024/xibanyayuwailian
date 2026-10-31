# V45｜多站独立教育资源URL，保持旧进度兼容（2026-10-31）

原离线操作台虽然按域名隔离资料、176条目录进度，却只对generadordelettering.org硬编码教育资源目标，不能复用到其他真实带教程的网站。这版在站点资料中新增**“真实教育资源URL（可选，仅当前站点）”**字段。

- 教育类渠道需要该站确实已有可用的教学材料，网址必须是**当前站点HTTPS同域**地址；非HTTPS或跨域地址不会存储。
- 没有教育内容就把字段留空，点“复制目标网址”不会自动拿通用工具页或首页伪装成教学资源。
- Generador示例使用[已核实的练字SVG学习页](https://generadordelettering.org/herramientas/plantillas-practica)。切换到另一站时这个字段自动清空，填写新站真实教育URL后可单独保存；切回原网站恢复原值。
- 旧版JSON备份`version:1`和`version:2`缺少新增字段仍允许恢复；新字段一律按空值迁移，不杜撰教育资源。用户的名称、描述、邮箱、旧提交阶段与公开外链人工核验证据不应丢失。
- 浏览器`localStorage`键不变，JSON备份版本仍为2；不访问第三方API、不自动提交网站，也不自动检验资料是否真能打开。现场实际教育资格仍须人工判断。

[离线操作台](backlink-submission-workbench.html) · [原多站隔离文档](v36-domain-isolated-profiles-and-v2-backups.md)

保留176条历史研究来源，**已确认新增生成器网站获链0**。
