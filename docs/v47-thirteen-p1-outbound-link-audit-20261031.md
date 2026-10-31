# V47｜当前13家P1公开href与原始rel证据分层（2026-10-31）

## 核验目的与严格证据标准

本次不是增加目录，而是对当前**13家P1**逐一找其他真实已刊登网站作为样本：它的公开来源URL、页面实际指向站外的完整`a href`、原始HTML `rel`、是否为普通免费条目、以及对Generador de Lettering的实际准入条件。

**统计口径：**

- **13/13** 有明确现行提交身份/渠道和处理路径。
- **11/13** 已实际从可访问的第三方刊登页面抽到一个直达其他网站的`href`；**不是11条本站新增外链**。
- **6/13** 另有之前**V33/V34**留下的原始`rel`网页属性样本（不是本次读取的新原始HTML；若案例不同，分别注明）。
- **2/13**：Product Hunt相关详情访问遭自动访问限制、Peerlist当前公开Weekly Launchpad没发现可核实项目站外href。保留为产品运营/发布渠道，不直接称已核实普通免费Follow。
- 原生网页提取服务返回的是清理后的语义HTML和出站href，**不包含可靠的原始a rel属性**。因此本次未擅自新增当前raw rel，也不能用`robots=index, follow`冒充a标签的`rel`。
- V33/V34里的`noopener`、`noopener noreferrer`、`noreferrer`本身没有`nofollow/ugc/sponsored`，但这仅描述**抽中那条外链**，不能推导Google实际传递多少SEO权重、所有新免费条目属性一致或用户网站现已获批。

## 每家真实样本与具体填写建议

| 平台 | 案例类型 | 已发布公开页 | 当前完整外站href | 旧raw rel | 下一步 |
| --- | --- | --- | --- | --- | --- |
| #2 Product Hunt | 产品Launch | 本轮无可核实项目页 | 未知 | 未知 | 只作为真实产品上线营销活动；需要有新功能故事与素材 |
| #7 Peerlist Launchpad | 周期Launch | 本轮无可核实项目页 | 未知 | 未知 | 只有准备参与对应周活动时才注册发布，需额外核对实际产品公开页 |
| #59 Navegax | 西语普通详情 | [实际样本](https://navegax.com/detalle/iadictodigital) | `https://iadictodigital.com/` | 未知 | 适合西语官网主页，注册后按真实IT/设计类别填表 |
| #75 Htrd | 字体工具详情 | [实际样本](https://htrd.org/tools/fontjoy) | `https://fontjoy.com` | `noopener`（V33/V34历史） | 首页底部Submit a tool；实在免费免登录的工具才可投 |
| #123 LaunchFree | Lettering+西语工具详情 | [实际样本](https://launchfree.io/listings/fontique.html) | `https://fontique.art/` | 未知 | 四步免费投稿优先；仍需站长真实创办动机、Email与人工验证码 |
| #128 Toolfound | 已验所有权的工具详情 | [实际样本](https://toolfound.com/tool/fileontap) | `https://fileontap.com/` | `noopener`（V33/V34历史） | 免费队列可用，但先准备同域邮箱或真实Meta/DNS所有权验证 |
| #129 SideProjects.net | 独立项目发布详情 | [实际样本](https://sideprojects.net/projects/sharekit) | `https://sharekit.app` | 未知 | 需要真实开发者账号与免费队列；按产品Launch而不是普通目录计 |
| #135 CtrlAlt.CC | 设计工具详情 | [实际样本](https://ctrlalt.cc/product/goahead) | `https://goahead.io/` | 未知 | 账号注册→真实提交；不采购$39的曝光位 |
| #148 NoSignupTools | 字体设计工具详情 | [实际样本](https://nosignuptools.com/tools/fontswiki) | `https://fontswiki.com` | `noopener noreferrer`（V33/V34历史） | 免费免登录产品优先；按官网准备真实图标、截图与文字 |
| #149 PeplioHUB | 免费工具独立详情 | [实际样本](https://peplio.com/anyfyle/) | `https://anyfyle.com/?ref=pepliohub` | 未知 | 提供真实16:9截图；AI先审、边缘案例人工；Badge非强制，SEO权重未知 |
| #151 DesignTools.fyi | 字体设计工具详情 | [实际样本](https://designtools.fyi/tools/font-explorer-mqp69i9d) | `https://font.do` | `noopener noreferrer`（V33/V34历史） | Tool URL=/editor、Type=Typography、Price=Free、真实Source of Truth及身份 |
| #159 Design Resources Archive | 字体资源编辑详情 | [实际样本](https://resourcesfor.design/resource/mixweight-594817) | `https://mixweight.pages.dev/?utm_source=ig&utm_medium=social&utm_content=link_in_bio` | `noopener noreferrer`（V33/V34历史） | 投稿/editor页+短英文设计用途；人机数学题回答当前题目而非旧答案 |
| #164 Unikist | Fonts设计资源列表 | [实际样本](https://unikist.com/categories/fonts) | `https://fontshare.com` | `noreferrer`（V33/V34历史） | 选择确切Design Tools分类，≤280字符真实英文简介，表单不保证永久免费 |

### 三个实务细节

**1. 带追踪参数也可为真实直接href，但不能改造证据。** [Peplio AnyFyle](https://peplio.com/anyfyle/)的实际外站目标是`https://anyfyle.com/?ref=pepliohub`，而[Mixweight的Design Resources详情](https://resourcesfor.design/resource/mixweight-594817)是`https://mixweight.pages.dev/?utm_source=ig&utm_medium=social&utm_content=link_in_bio`。这两条链接虽然并非站内/go重定向，最终仍需要单独判断robots、canonical、链接rel及跟踪条件。不应把其href原样替换成去掉查询串的网址再声称是观察结果。

**2. 历史raw rel不能跨不同详情页。** #128 Toolfound的本轮示例是FileOnTap，而历史raw rel`noopener`来自[StencilMaker](https://toolfound.com/tool/stencilmaker-app)。#148 NoSignupTools当前观察FontsWiki详情，但原始`noopener noreferrer`是[Design分类页](https://nosignuptools.com/tools?category=design)Fontswiki的外站链接。即使是同一产品，其详情页和列表页可以使用不同链接模板。

**3. 只读刊登资料不等于正式申请。** 发布型Product Hunt/Peerlist，以及身份核验严格的Toolfound、需要社交/项目账号的CtrlAlt和SideProjects，应单列进度。站方宣传永久页、无手续费或Dofollow不等于实际生成了对自己网站的外链。

## 建议的投入顺序

优先针对确实与Typography/Lettering相关的[LaunchFree](https://launchfree.io/submit.html)、[Design Resources Archive](https://resourcesfor.design/submit)、[Unikist](https://unikist.com/submit)、[DesignTools.fyi](https://designtools.fyi/submit/)和[NoSignupTools](https://nosignuptools.com/submit)手动核对并填表；[Htrd](https://htrd.org/)可列入第二批；[Navegax](https://navegax.com/)优先用于西语专属目录，但须真实注册；[Toolfound](https://toolfound.com/submit)有真实所有权验证门槛。PeplioHUB虽有外部链接，但`nofollow/ugc`未来可变，比较适合作为用户曝光而非Follow承诺。

完整官方来源、保留资格与未证内容：[逐行证据CSV](../data/v47-current-p1-outbound-proof-matrix-20261031.csv)。没有代理注册、代提交、付费、SEO指标捏造、任何新增确认用户站获链。**主库仍是176条：P1 13、P2 27、条件85、待核验16、排除34、非外链1；新增确认用户站外链0**。

## V49｜原始 rel 的逗号分隔漏洞与一次性样本验收

Google 官方允许`rel="nofollow,ugc"`，旧版验链器只按空格拆分会误判为无限制。本次Python已修复；新增[13家P1单次批量原始HTML核验](v49-p1-raw-rel-batch-audit-and-comma-fix-20261031.md)（只实际请求有公开样本的11家），运行结果另存本地CSV；不把V33/V34历史原始rel当成本次实时事实。没有在本会话环境取得新raw rel，因此不改变当前6条历史样本及平台P1级别。
