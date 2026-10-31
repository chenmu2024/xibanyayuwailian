# V54｜高相关字体目录实时投稿表单复核与可填写包（2026-10-31）

## 本轮目标与结论

不再增加目录数量，而是把已筛出的高相关渠道转成可执行、不会误填的真实投稿材料。此次只读检查7个现有目录的官方表单，并再次读取目标网站主页、编辑器及练字资源页。**没有登录、没有输入个人资料、没有调用表单POST、没有提交。**

目标网站当前可访问：

- 首页：[https://generadordelettering.org/](https://generadordelettering.org/)；西语主页明确写明免费、无需注册、PNG/JPG/WebP导出。
- 主产品：[https://generadordelettering.org/editor](https://generadordelettering.org/editor)；实际支持字体、大小、颜色、字间距、描边、阴影、旋转、背景、画布与撤销/重做；导出PNG/JPG/WebP。
- 限制边界：这是浏览器里的文字图像编辑器，不是TTF/OTF字库生成器，不是SVG矢量设计软件，也不保证专业印刷DPI。投稿文案不应扩大功能。

## 1. 本轮最推荐先提交：#159 Design Resources Archive

<badge>最短表单</badge>

入口：[https://resourcesfor.design/submit](https://resourcesfor.design/submit)

### 现场真实字段

- `Link URL *`：必填URL。
- `Description *`：必填，至少10字符。
- `Prove you're human`：实时简单算术题，必填。
- `subscribeEmail`：仅用于周报，可选。
- 没有看到名称、个人姓名、个人邮箱或账号注册字段。

**重要：验证码是动态变化的。**本轮先后读取到`3 + 5`和`6 + 8`两个题目，第二次读取时答案是14。不要把14写死；用户实际打开时按页面当前题目计算。

### 建议填写

| 字段 | 内容 |
| --- | --- |
| Link URL | `https://generadordelettering.org/editor` |
| Description | 见下方可复制文案 |
| 验证题 | 按当前页面现题作答；本轮第二次读到6+8=14 |
| 周报邮箱 | 可留空，不需要为投稿订阅 |

**Description（英文，可直接复制）**

> A free Spanish-language browser lettering editor for creating decorative text images. Customize fonts, size, colors, spacing, outlines, shadows, rotation and canvas background, then export your design as PNG, JPG or WebP. No account required.

说明：页面表单没有独立产品名称字段；链接和说明是核心。表单显示POST提交，但本轮没有触发提交。官方页面介绍其为半精选资源目录；不能保证通过、永久展示或Follow。

## 2. #164 Unikist：第二个低摩擦候选

入口：[https://unikist.com/submit](https://unikist.com/submit)

现场提取到的字段：Resource name、Website URL、Category、Pricing、Short description（maxlength=280）、Your email。页面静态表单未显示HTML required属性，邮箱字段没有必填标记；分类和价格是前端动态combobox，静态页面未展开选项，**不能把猜测的选项说成已核实**。

建议：

- Resource name：`Generador de Lettering`
- Website URL：`https://generadordelettering.org/editor`
- Category：打开实际下拉后，若存在则选`Design Tools`；若没有，不要选不相干分类。
- Pricing：确认当前核心功能免费后选`Free`。
- Short description：使用下面不超过280字符的说明。
- Your email：可选；若填写，用真实可接收审核结果的邮箱。

**Short description**

> Free Spanish-language lettering editor for creating decorative text graphics. Customize fonts, size, colors, spacing, outlines, shadows and backgrounds, then export PNG, JPG or WebP. No account required.

## 3. #163 LDS Library：表单字段已完整核实

唯一规范入口：[https://library.legitdesign.studio/submit](https://library.legitdesign.studio/submit)

- Resource name（必填）：`Generador de Lettering`
- Link（必填）：`https://generadordelettering.org/editor`
- Category：`Design Resources`（真实下拉选项；没有独立Fonts）
- Pricing：`Free`（功能确实免费时）
- What is it?（选填）：`A free Spanish-language browser lettering image editor.`
- Why is it useful?（选填）：可用Unikist长说明。
- Your email（选填）：真实邮箱。
- 隐藏反垃圾字段`website`：留空。

旧`lds-library.vercel.app` canonical归一到正式域，禁止重复投稿。官方称每周人工审核，不能保证入选。

## 4. #151 DesignTools.fyi：主题匹配高，但需要真实身份

入口：[https://designtools.fyi/submit/](https://designtools.fyi/submit/)

本轮真实字段与限制：

- 必填：Tool Name、Tool URL、Your Name、Email。
- 可选：X/Twitter handle、Description、Logo、代表公司勾选。
- Logo可不上传；如上传只接受PNG/JPEG/WebP，方形，最小250×250像素。
- Categories是复选框：Type组含Typography、Images等；Source of Truth组含Figma、Production Code、Generated Code、other；Price组含Open Source、Free、Paid；Size组含Micro、Large、Medium、Small。
- 隐藏`website`字段是honeypot，必须留空；隐藏timestamp由页面自动生成。
- **不要勾选“I work for or represent this company”，除非你确实代表某公司。**

建议选项：Type只选`Typography`；Source of Truth若按实际运行网站的实现形态填写可选`Production Code`；Price选`Free`。Size并非已核实的强制字段，若不确定可留空。X账号和Logo都可不填。

Tool Name：`Generador de Lettering`

Tool URL：`https://generadordelettering.org/editor`

Description：

> Free Spanish-language browser lettering editor with fonts, colors, spacing, outlines, shadows and canvas controls. Export custom text graphics as PNG, JPG or WebP.

## 5. #75 Htrd：免费免登录工具目录

入口：[https://htrd.org/](https://htrd.org/) 首页底部的`Submit tool`表单；不要误用首页独立的Newsletter表单。

现场真实字段：

- Tool name（必填，最多80字符）
- Website（必填，最多300字符）
- Category（动态下拉，静态提取没有返回选项）
- Your email（选填，最多120字符）
- Why is it great?（选填，最多600字符）
- 隐藏`company` honeypot留空。

建议：

- Tool name：`Generador de Lettering`
- Website：`https://generadordelettering.org/editor`
- Category：必须打开下拉后按实际选项选择；静态抓取未获得可核实的具体类别，不照搬旧文档中的Text / Design猜测。
- Why is it great?：

> A free Spanish-language lettering editor that works in the browser without an account. Users can customize fonts, size, colors, spacing, outlines, shadows, rotation and canvas backgrounds, then export PNG, JPG or WebP images. It is useful for creating decorative text graphics for invitations, social posts and personal projects.

## 6. #148 NoSignupTools：可投，但注意广告标签

入口：[https://nosignuptools.com/submit](https://nosignuptools.com/submit)

现场字段：

- Tool Name、Tool URL
- Category（动态下拉，未展开选项）
- Short Description（最多140字符）
- Detailed Description
- Tool Icon：PNG/JPG/SVG/WebP，最多1MB，建议正方形
- Screenshots：最多6张，PNG/JPG/WebP，每张最多2MB
- Your Name、Your Email均标为optional
- 页面存在`No Ads`等属性标签。

短说明：

> Free Spanish lettering editor for creating custom text graphics. Export PNG, JPG or WebP without an account.

详细说明可用Unikist长说明。

**不要选择`No Ads`**：该站有AdSense接入，不符合无广告声明。Open Source、Dark Mode、Offline Access等也必须逐项按事实判断，不能为了标签曝光而勾选。类别下拉未打开前，不预设Design一定存在。

## 7. #123 LaunchFree：暂缓，不是第一家

入口：[https://launchfree.io/submit.html](https://launchfree.io/submit.html)

当前四步表单确实要求Launch Name、URL、Tagline、Category、100–1200字符Description、Why did you build this、Your Name、Email、Short Bio、How did you hear about us、Terms和Cloudflare Turnstile。MRR和最多3个截图URL可选。

它有真实西语工具刊登样本，但需要真实创办故事、本人身份、邮箱和个人简介。**不能代写成用户亲身经历，也不能编造MRR。**因此虽然平台自称免费和Dofollow，投稿摩擦高于#159/#164/#163，放在后面。

## 8. 当前建议实际顺序

| 顺序 | 平台 | 原因 | 主要卡点 |
| ---: | --- | --- | --- |
| 1 | #159 Design Resources Archive | 最短表单、主题强相关、只需URL+介绍+动态验证码 | 需当场算验证码 |
| 2 | #164 Unikist | 表单短，设计/字体目录 | 打开下拉确认类别和价格 |
| 3 | #163 LDS Library | 字段完整透明，真实设计资源分类 | 每周人工审核 |
| 4 | #151 DesignTools.fyi | Typography直接匹配，真实外链样本 | 真实姓名和邮箱必填 |
| 5 | #75 Htrd | 免费免登录工具定位匹配 | 首页表单、分类动态加载 |
| 6 | #148 NoSignupTools | 无需注册工具定位匹配 | 需图标/截图可选，类别动态加载 |
| 7 | #123 LaunchFree | 有真实Lettering/西语案例 | 真实个人故事、身份、验证码 |

**本轮状态**：0个表单提交；0个审核结果；0条Generador新增确认反链。所有表单都只是公开读取，用户自行检查后提交。后续每个平台按“提交时间→回执→公开详情页→指向本站的实际href→该锚点rel→Google索引→GSC引荐流量”分层验收，不用第三方别人的外链代替本站成果。

## 9. 本轮核验局限

- 动态下拉（Unikist、NoSignupTools、Htrd）没有在静态HTML中展开；本报告不虚构其当前选项。
- Design Resources Archive验证码动态变化，必须在提交当刻重新看题。
- 未测试表单提交后的审核周期或是否接受纯西语网站。
- 没有检查或修改网站代码、广告、页面内容。
- 所有外链属性样本仍只证明第三方已刊登页面，不是用户网站已经获链。

逐行字段：[V54 CSV](../data/v54-live-submission-form-audit-20261031.csv)。
