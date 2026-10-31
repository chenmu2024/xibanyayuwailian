# V44｜教育资源入选条件纠错及离线操作台排序修复（2026-10-31）

## 一、Educaguía #58从条件恢复P2

用户网站现已真实存在[四份A4练习SVG](https://generadordelettering.org/herramientas/plantillas-practica)：笔画、小写、大写字母、装饰连接，可打印/在浏览器中下载。另有[七天练习计划](https://generadordelettering.org/blog/plan-practica-lettering-siete-dias)，明确逐日练习步骤和检查标准。这意味着已有可供艺术、Lettering学习的实际教育内容，不能继续将其视作完全没有教育用途的普通图片编辑工具。

[Educaguía教育网站免费提交](https://educaguia.com/inserta-tu-web.asp)（打开后第1步选`Recursos Educativos`）允许提交真实教育相关网站，人工审核并自动订阅教育简报，是否接受混合工具站仍取决于编辑。精选Logo仅作为额外展示，非明确的普通收录强制回链。不要把练字SVG下载页面能力误称为`/editor`能下载SVG，也不能虚构教师、学校或课程认证。[教育软件单独申请](https://educaguia.com/inserta-tu-app.asp)有学科/年龄/作者等字段，不应为普通图片编辑器填假数据。

| 官网表单与真实资料 | 应填写/说明 |
|---|---|
| 官网第一步 | `Recursos Educativos` |
| 建议实际申请URL | `https://generadordelettering.org/herramientas/plantillas-practica` |
| 名称（若后续表单要求） | `Plantillas de Práctica de Lettering` |
| 描述（按后续字段真实限制） | `Hojas A4 gratuitas para practicar lettering en español: cuatro guías SVG de trazos, minúsculas, mayúsculas y conexiones, con ejercicios de siete días y autoevaluación.` |
| 补充教学计划（仅允许多个链接时） | `https://generadordelettering.org/blog/plan-practica-lettering-siete-dias` |
| 真实身份/验证码 | 本人如实填写，不冒充教学机构 |
| 订阅与验链 | 官网自动加教育通讯；提交/审核不等于公开外链，最终必须查实际href、rel和索引 |

## 二、排序问题与修复

过去操作台的`followPriority/designPriority/featured`排序缺少现行级别闸门，导致一些旧样本虽已降为条件或有内容质量问题，仍可能靠历史排名展示在第一屏。新算法让**有效P1/P2且有真实公开样本**优先，其次为未配样本序号的P1/P2；条件/排除只能在后面出现（仍可检索）。例如不再让有中转的#168、条件#171、降级#172位于字体设计高相关来源前。

跨站复制URL亦增加防错：普通工具链接若不属于当前目标网站域名则不自动提供；教育目录只对已真实核实的Generador练习资源提供专用链接，其他网站不能把自己随意填写的普通工具页默认当成教育资源。

## 三、证据边界

历史176来源不增加；现行**P1 16，P2 25，条件84，待核验16，排除34，非外链1**。历史目录样本不代表目标站获链；本轮没有自动发邮件、注册、提交、付款或新增确认外链。JS脚本语法及CSV和JSON镜像可在提交前检查，GitHub Actions此前启动前失败仍需单独检查是否真实恢复。
