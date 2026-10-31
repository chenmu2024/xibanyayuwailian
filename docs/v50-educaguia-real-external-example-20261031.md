# V50｜Educaguía 误把自有教学页列为公开外链案例的修复（2026-10-31）

## 本轮实际数据问题

V44把`https://generadordelettering.org/herramientas/plantillas-practica`放在#58操作台`example`字段，用户看到“历史公开案例”，易误解成平台已批准。实际上这是我们**准备申请的资源页**，并不是Educaguía指向我们网站的真实反向链接。

现在将#58的`example`改为[Educaguía的公开教育网站总名单](https://www.educaguia.com/listadoEDU.asp)。该名单确有“Actividades educativas - Educaplay”指向https://www.educaplay.com/等**其他第三方站点**的真实外部链接，因此是实际公开展示的参考页面。但是这不是用户网站专属的详情页；其原始rel、Google索引及DR等均尚未独立验证。

## 哪些资料可以用于申请

目标网站经过已核实的四类A4 SVG练字模板和七天练字学习计划，能够针对[官方免费教育网站提交页](https://educaguia.com/inserta-tu-web.asp)的`Recursos Educativos`分类提出真实用途。官网明确人工核查教育相关性、质量与原创程度，且提交自动订阅教育简报。**有资格尝试申请不等于实际批准或取得可传递SEO价值的外链。**

## 数据安全与审计规则

- `example`：第三方目录**实际公开的其他网站案例页**，不能是自己网站准备提交的URL。
- `target`、每个域名独立`edu`：用户**准备给目录推荐的真实教学资源页**，不能表现为历史已刊登案例。
- 真正取得用户外链：必须另有**第三方公开页面实际包含指向Generador域名的`a[href]`**，再核对rel/索引/引荐才可声称获链。
- 操作台本轮新增静态和模拟校验，确保现在176家中没有`example`指向用户网站的情况。

176渠道现行状态未改变：P1 13、P2 27、条件85、待核验16、排除34、非外链1。用户实际新获链0。
