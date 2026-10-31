# V53｜14家真实公开目录的当前外站a标签rel核验与PeplioHUB降级（2026-10-31）

> **结论**：用公开页面的CSS精确匹配 `a[href]` 后，已独立取得14个不同平台（14个已发布他站产品/类别页面）相关出站锚点的**本轮渲染DOM的`rel`值**。其中**13个平台的这些具体样本锚点**未显示`nofollow`/`ugc`/`sponsored`，**1个平台PeplioHUB**在其AnyFyle真实已发布产品页显示`rel="noopener ugc nofollow"`。这些证据不构成整个目录免费档一致属性、Google实际索引、排名效果或用户网站获链证明。
>
> 证据 CSV：[14家逐行记录](../data/v53-current-rendered-dom-outbound-rel-20261031.csv)。本轮**新增渠道0，人工投稿0，generadordelettering.org确认新增获链0**。

## 1. 已发布第三方外站链接逐页核实

| 主库编号 | 平台 | 真实公开第三方案例 | 本轮DOM a[rel] | 判读 |
| --- | --- | --- | --- | --- |
| #159 | Design Resources Archive | [Mixweight](https://resourcesfor.design/resource/mixweight-594817) → `mixweight.pages.dev/?utm_source=...` | `noopener noreferrer` | 该样本未见限制词；真实跟踪参数保留 |
| #164 | Unikist | [Fonts目录](https://unikist.com/categories/fonts) → `fontshare.com` | `noreferrer` | `noreferrer`**不是**`nofollow`，但可能隐藏引荐来源 |
| #151 | DesignTools.fyi | [Font Explorer](https://designtools.fyi/tools/font-explorer-mqp69i9d) → `font.do` | `noopener noreferrer` | Typography独立详情 |
| #123 | LaunchFree | [Fontique](https://launchfree.io/listings/fontique.html) → `fontique.art` | `noopener` | **不再只有官网DoFollow自述**，现取得此特定样本DOM rel；仍非免费档全站保证 |
| #75 | Htrd | [Fontjoy](https://htrd.org/tools/fontjoy) → `fontjoy.com` | `noopener` | 已刊登免费字体搭配工具详情 |
| #148 | NoSignupTools | [FontsWiki](https://nosignuptools.com/tools/fontswiki) → `fontswiki.com` | `noopener noreferrer` | 本轮具体详情页的属性，不用旧分类页替代 |
| #163 | LDS Library | [规范域Fonts列表](https://library.legitdesign.studio/design-resources/fonts) → `fontjoy.com` | `noopener` | V52已恢复规范域可读，不能与旧Vercel别名重复记来源 |
| #165 | Mark-it | [Font分类](https://markitnow.net/font) → `fontmeme.com` | *(无rel属性)* | 只证明具体可见锚点；目录质量仍需判断 |
| #172 | EpicTools | [Penpot](https://epictools.dev/penpot) → `penpot.app` | *(无rel属性)* | 平台有停运、待售、错误目录噪声；仍P2，不凭rel升级 |
| #59 | Navegax | [IAdicto Digital](https://navegax.com/detalle/iadictodigital) → `iadictodigital.com` | *(无rel属性)* | 西语普通详情有可点击外部站点链接；登录才能申请 |
| #128 | Toolfound | [FileOnTap](https://toolfound.com/tool/fileontap) → `fileontap.com` | `noopener` | 单条已验证所有权的详情；用户申请仍须真实所有权验证 |
| #129 | SideProjects.net | [ShareKit](https://sideprojects.net/projects/sharekit) → `sharekit.app` | `noopener` | 发布型产品渠道，需真实开发者帐号 |
| #135 | CtrlAlt.CC | [Goahead](https://ctrlalt.cc/product/goahead) → `goahead.io` | *(无rel属性)* | 登录发布和付费推广位需分开 |
| **#149** | **PeplioHUB** | [AnyFyle](https://peplio.com/anyfyle/) → `anyfyle.com/?ref=pepliohub` | **`noopener ugc nofollow`** | **该普通公开样本不能算无限制Follow，V53从P1降为条件** |

**严格证据范围**：通过第三方只读网页提取器选择目标网站公开页面内具体`a[href]`节点，保留该**渲染DOM元素**的`rel`、`href`。这**不是站点HTTP原始响应body的完整抓取留证**；客户端JS可能创建/修改节点。样本页面也可能与将来批准后的新页面采用不同模板，所以只对上述具体页面有效。某平台有两个相同href的锚点时已同页检查，CSV另记`anchor_count_same_href`。没有篡改任何网站内容。

## 2. PeplioHUB #149 为什么降级

之前官网已明言保留改写外链为nofollow/ugc的权利，但只有公告、未获得实例。现在[普通已发布产品AnyFyle](https://peplio.com/anyfyle/)的站外“Visit website”按钮确实包含`rel="noopener ugc nofollow"`，且完整href带`?ref=pepliohub`。因此对于目前“免费、主题相关、尽量得到普通Follow外链”的目标，Peplio**不再属于P1高优先名单**，保留为**条件**（有兴趣通过引荐获得用户时可考虑，不能夸大Link Equity）。

本轮只修改真实事实的对应数据/优先级；不删除历史V17/V34“当时不确定”记录，也不假设Peplio全站所有页面永久nofollow。

现行176条总库状态：

| P1 | P2 | 条件 | 待核验 | 排除 | 非外链 | 历史合计 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **12** | **27** | **86** | **16** | **34** | **1** | **176** |

与V52相比，只有#149 **P1 -1、条件 +1**。原V47“13家P1观察矩阵”仍是**2026-10-31较早时段的历史快照**，不能悄悄删掉Peplio旧样本；当前P1运行时门槛更新为12，已有公开href样本10，保留历史raw rel样本6。

## 3. 当前真正优先人工填写的队列
> **后续更新说明（V54）**：上面顺序是V53按样本证据强弱排的历史队列；V54现场读取7家真实投稿表单后，按主题相关性与实际填写摩擦调整当前执行顺序为 **#159 → #164 → #163 → #151 → #075 → #148 → #123**。以[V54实时表单报告](v54-live-submission-forms-and-ready-to-fill-pack-20261031.md)为当前执行依据。


第一梯队：#159 [Design Resources Archive](https://resourcesfor.design/submit)、#151 [DesignTools.fyi](https://designtools.fyi/submit/)、#164 [Unikist](https://unikist.com/submit)、#163 [LDS Library规范域](https://library.legitdesign.studio/submit)。这四家在字体/视觉排版工具上有直接的第三方公开链接证据；#163当前完整真实表单已证实`Category=Design Resources`，**没有Fonts下拉项**，并且旧Vercel别名不重复投稿。

第二梯队：#123 [LaunchFree](https://launchfree.io/submit.html)、#75 [Htrd](https://htrd.org/)、#148 [NoSignupTools](https://nosignuptools.com/submit)；需要真实创办人材料、真实免费免登录资格或截图图标。其它#165 Mark-it、#172 EpicTools等仍按V51质量门槛后置，Peplio #149只作非Follow引荐曝光备选。

每站必须按“**独立目标网站根域 × 对方平台规范根域**”查历史记录。已有真实提交才更新`data/submission-ledger.csv`，有公开条目且原始HTML/DOM存在指向**自己**网站的准确href才能进一步核验rel；另外检查实际索引、引荐流量。**在本轮没有人工提交、没有新获批、没有用户站实际已获外链。**

## 4. GitHub文件一致性与验证限制

- 已新增本报告与14行CSV；同步`data/backlinks-master.csv`（仅#149级别与事实）、`data/priority-queue.csv`、`data/reusable-free-shortlist.csv`、176家逐站指南、21家可填写卡和HTML操作台；必要的JS校验断言同步变为**12当前P1 / 10当前P1有第三方href / 6当前P1历史raw rel**。旧V47快照和旧V34当时无匹配的记录不因本次得到新证据而冒充先前已知。
- **GitHub Actions仍然未通过**。在[最新先前运行41174331989](https://github.com/chenmu2024/xibanyayuwailian/actions/runs/41174331989)中job标记failure但API无步骤、日志404，不能凭此定位具体是哪个代码校验失败；仅作独立字段和计数检查，不声称项目全部自动测试已通过。
- V52的`scripts/audit_curated_v52.py`保留，可由站长本地免费再拉HTTP原始HTML，验证有无源代码与当前渲染DOM差异；默认最多9个起始站外案例URL、可能有限重定向，不发申请、不登录，不读取其他站的隐私数据。

**结论**：比继续堆目录更有价值的是已经取得14条**可复核的真实样本外链属性**，识别出Peplio的ugc/nofollow，从优先目录中排除以减少无效填写。所有“成功获链”仍必须等待用户网站被对方真正公开刊登，不能将第三方字体案例冒充本站外链。
