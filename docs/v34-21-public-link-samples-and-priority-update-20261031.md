# V34｜21个已公开外链样本：字体、设计与西语目录的href/rel实测（2026-10-31）

**边界声明**：本报告从原176家历史渠道里继续抽检，新增来源0、实际代投0、为`generadordelettering.org`新增确认外链0。21条链接**都指向其他人的项目**，不是目标网站的已获外链。全部判断针对2026-10-31读取的**具体公开页面上实际`<a href>`的`rel`属性**；未见nofollow不等于Google一定传权，也不能推论整站所有页面/免费档待遇。

## 1. 需要优先纠正的两个P1误区

### #005 The Free Tools Directory：至少一个直接相关的字体项目为nofollow

在[已发布1000 Font Generator条目](https://thefreetoolsdirectory.com/sites/1000-font-generator)中，链接实际指向`https://1000fontgenerator.com/`，其`rel="noopener nofollow"`。对Lettering而言这个样本更有参考价值，因为同样属于字体/装饰字在线工具。不能凭该1条就宣布所有条目都nofollow，但以**免费Follow链接**为首要目标时，应从P1降低为**条件**，若只是希望自然曝光仍可研究。

### #162 UX Resources：四个Typography工具样本均带sponsored

| 公开工具详情 | 实际外站href | HTML rel |
| --- | --- | --- |
| [Minglyph](https://uxresources.info/resource.php?slug=minglyph) | `https://minglyph.com/` | `noopener sponsored` |
| [Fontmojo](https://uxresources.info/resource.php?slug=fontmojo) | `https://fontmojo.com/` | `noopener sponsored` |
| [Cursive Generator](https://uxresources.info/resource.php?slug=cursive-generator) | `https://cursivegenerator.work/` | `noopener sponsored` |
| [Fontshare](https://uxresources.info/resource.php?slug=fontshare) | `https://www.fontshare.com/` | `noopener sponsored` |

这4条样本中含免费工具和字体生成器，但实际外站anchor都标了`sponsored`。这不是证明所有免费投稿都会得到sponsored，也**不是**证明这4个资源实际付了钱；它只是对HTML属性的观察。以普通Follow为主要目标时#162不应再列最高优先，状态由P1降为条件。如果目标是设计师真实曝光，可以保留。

## 2. 与Lettering高度相关、且样本未标nofollow/ugc/sponsored的来源

| 平台 | 检查的公开资源 | 真实href/rel | 具体适用性 |
| --- | --- | --- | --- |
| #159 Design Resources Archive | [MixWeight](https://resourcesfor.design/resource/mixweight-594817)、[Type Garden](https://resourcesfor.design/resource/type-garden-cc9e7c) | `noopener noreferrer` ×2 | 排版/字体实验工具，强相关，人工精选 |
| #163 LDS Library | [Fonts类别](https://lds-library.vercel.app/design-resources/fonts)中的Fontjoy、Fontshare | `noopener` ×2 | 真实8个字体资源，免费资源精选 |
| #164 Unikist | [Fonts类别](https://unikist.com/categories/fonts)中的Fontshare、Velvetyne | `noreferrer` ×2 | 公开字体分类直接外链 |
| #165 Mark-it | [首页](https://markitnow.net/)中的Fontmeme、CMD Supply | 无`rel` ×2 | 真实字体及设计工具链接；需提供真实作者 |
| #169 FreeDesignerTools | [首页](https://www.freedesignertools.com/)中的Figma、Unsplash | `noopener noreferrer` ×2 | 当前首页仅12个主流工具，入选难度/效果不明 |
| #172 EpicTools | [Penpot](https://epictools.dev/penpot)、[Stockimg AI](https://epictools.dev/stockimg_ai)、[Snappify](https://epictools.dev/snappify) | 无`rel` ×3 | 真实Curated详情外链，不是外链农场承诺 |
| #141 GainWeb | [Latest Links](https://gainweb.org/latest-links.html)中的Paul Hoda、Removemate | 无`rel` ×2 | 存在出站href，但免费档不保证审核且SEO目录相关性低，不因此升优先 |

**EpicTools特别注意**：[Design分类](https://epictools.dev/category/design)中另有标记`Partner`的reShorts外链使用`rel="follow"`；**Partner位与普通Curated资源详情必须分开**，不能据此声称免费表单自动给Partner待遇。观察到没有rel的Curated详情，才是与普通投稿更有意义的样本。

## 3. 尚不能确定公开链接属性的平台

- #149 [PeplioHUB](https://peplio.com/pepliohub/)：页面可读，但此次提取的公开`a[href]`里没有辨认出目标产品站的外站href。可能由交互组件或脚本实现跳转，**不能把“抽取器没看到”写成“没有外链”或“有Follow链接”**。官网本身提示可调整nofollow/ugc，待后续真实详情页核查。
- #147 [Good Design Tools](https://www.gooddesign.tools/tools/type-trials)：此次访问返回`target_unreachable`，不代表整个网站已关闭，也不能验证其详情页实际rel；暂保持未知，不虚构结论。
- #141 GainWeb虽出现无rel外链，但也有付费等级，不能把`Latest Links`中出现的某条链接假定为Regular Free免费投稿成功，亦不建议为Follow支付费用。

## 4. Lettering是否已收录：只针对公开抽查页

本轮对11个页面/类别分别记录检出范围，见 [V34网站出现情况CSV](../data/v34-11-category-presence-checks-20261031.csv)。当日读取的字体分类、资源详情和首页未检出`generadordelettering.org`。其中Good Design Tools页面**访问失败**而非未检出。此结果**不覆盖所有分页、历史存档、搜索引擎已索引页面或其他渠道**；未检出不等于没有被收录、被拒或被处罚。

## 5. 更新后的Lettering下一批人工申请顺序

先做高相关且不需要强制badge的**#159 Design Resources Archive、#163 LDS Library、#164 Unikist、#172 EpicTools、#165 Mark-it**。这些平台有真实字体/设计资源入口和当前公开样本，具体字段仍须以当日官方表单为准。已经完成的V33第一批Htrd、Herramientas y Recursos、NoSignupTools、DesignTools.fyi、Toolfound继续保留，不因发现新一批而抹掉。

下一批的手工填写资料已汇总至 [V34五家逐站填写清单](v34-five-more-design-font-directories-ready-to-fill.md)；**没有代用户发投稿**。

**不要过度承诺**：即使某条公开anchor没有nofollow，也可能被Google不同处理；DR/DA/AS仍然未独立测量，不能仅凭“看见非nofollow”称为高权重。

## 6. 可复核的数据与台账隔离

- [21条公开href/rel原始属性CSV](../data/v34-21-published-link-rel-samples-20261031.csv)：精确保存来源页面、实际对外URL、`rel`和是否Partner/Curated。
- [11个目标域名公开页出现范围CSV](../data/v34-11-category-presence-checks-20261031.csv)：明确“未检出”与“抓取失败”不同。
- [V33此前11条公开证据](../data/v33-published-outbound-rel-samples-20261031.csv)：保留原样，不将V34相同平台混入旧样本。
- [176条历史主库](../data/backlinks-master.csv)：对#005/#162做基于公开链接质量的优先级调整，但不删除它们。
- [用户实际提交与获链台账](../data/submission-ledger.csv)：**本轮不填写成功记录**。只有该网站自己的公开链接页面实际包含`generadordelettering.org`的href，才能记录已获链，之后才能测其rel与索引。

截至本轮，没有独立证据证明为Lettering新增任何第三方反向链接。