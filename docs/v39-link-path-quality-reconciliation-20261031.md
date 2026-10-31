# V39｜公开外链路径质量复核与前版误判纠错（2026-10-31）

> **新增目录0、对外提交0、本站新增确认外链0。** 本轮只在原176家渠道里核对普通详情页链接是否真的直接指向外站，历史rel样本是否具有代表性。原始rel未知保持未知，未测DR/AS或Google真实索引。

## 核验结果与实际页面

### #168 Herramientas y Recursos：普通工具按钮经站内跳转，不能拿页脚样本代表免费获链

[Recursos分类页](https://www.herramientasyrecursos.com/directorio/categoria/recursos)上的`https://www.aprendeygana.net`和`https://www.herramientasproductivas.com`原始rel在V33分别记录为`noopener`。这2个真实href实际位于**“Más de nuestra red”页脚关联站**，不是第三方正常刊登的`Visitar sitio`主按钮。

另已打开[普通Agenvas条目](https://www.herramientasyrecursos.com/sitio/agenvas-7a4477)：点击`Visitar sitio`先到`https://www.herramientasyrecursos.com/salir/agenvas-7a4477`，随后重定向至`https://agenvas.com/`。这种站内中转**不等于普通详情直接`<a href="https://agenvas.com/">`外链**。它仍可能产生引荐流量，也不能断定SEO必然无效；但没有充分证据可把此平台当作“免费直接Follow”，质量优先级应由历史P1降至**条件（引荐候选）**。

官方[西语建议表单](https://www.herramientasyrecursos.com/directorio/sugerir)存在，但真实获批与网站自身链接仍待人工申请后验收。

### #151 DesignTools.fyi：旧版本已有真正字体工具原始rel

[Typography栏目](https://designtools.fyi/tags/typography)公开9个工具，含[Font Explorer](https://designtools.fyi/tools/font-explorer-mqp69i9d)，显示指向`https://font.do`的外站链接。仓库V33已记录该锚点`rel="noopener noreferrer"`；**本轮不是首次测到其rel**。V38新检查的Affinity页面虽有真实站外href，但对该新样本没有读到原始rel。不要把新旧样本混为一个实时Follow保证。

[官方投稿页](https://designtools.fyi/submit/)有Typography、Free、真实姓名邮箱和Source of Truth，适合真实Lettering编辑器`/editor`，但纯西语是否获批不保证。

### #171 FounderOmni：真实字体资源详情可以打开原站

[西语设计资源库](https://founderomni.com/es/library/design-brand-assets/)现展示74项资源。独立的[Fontpair](https://founderomni.com/es/library/design-brand-assets/design-brand-assets-fontpair-f007476b/)资源页存在`Abrir recurso`，指向`https://www.fontpair.co/`；[Hero Patterns](https://founderomni.com/es/library/design-brand-assets/design-brand-assets-hero-patterns-0ea1791d/)则指向`https://heropatterns.com/`。**这两条是真实公开资源页的外站链接，但本轮没有取得锚点raw rel**；不能宣布Follow、已Google索引。

纠错：#171的西语表单`Tipo de solicitud`、`Categoría`、`Nombre de la ficha`、`URL pública`、推荐原因和可选邮箱在V32已经核实。V38写成首次获得六项字段不准确；本轮实际补强的是**两个真实公开外链详情样本**。

## 下一步真正值得填写的优先队列

按现有证据综合考虑主题相关性、已刊登详情链接形式及是否有真实官方表单：**#159 Design Resources Archive → #151 DesignTools.fyi → #164 Unikist、#163 LDS Library、#172 EpicTools、#165 Mark-it → #171 FounderOmni**。#168只作为西语引荐候选后置；#147主站异常、#161最终表单不明、#174超时继续暂缓。

任何平台仅有公开表单、其它项目已有href、原始rel样本、meta robots=index,follow，都不等于`generadordelettering.org`已获得链接。需取得对方**公开页面指向目标域名的真实a[href]、原始rel、是否可索引**再登记；无用户明确请求时不代提交。

## 数据文件与审计边界

[6条具体链接路径及限制CSV](../data/v39-sample-link-path-audit-20261031.csv)。该表区分普通产品详情按钮、站内中转以及页脚关联网站；V33原始rel仍可追溯但不可错用作普通提交待遇。
