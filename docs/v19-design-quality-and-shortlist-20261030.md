# V19｜设计工具目录核验与免费外链严格筛选（2026-10-30）

## 结论与口径

- 历史资源库：**154条**（V18原151条完整保留，本轮新增152–154三条），**不是154条获链**。
- 当前Lettering主申请队列：13家历史候选；新增 `data/reusable-free-shortlist.csv` 中的8家属于**免费优先且主题适配度更高的申请研究对象**。这8家也尚未全部证实Follow/DR/能入选；它们不是已获链。
- 本轮**没有自动提交**，没有新增已获批外链，没有邮件发送。所有未知实时Ahrefs DR、Semrush AS、出站rel均留作待测。
- 主要策略改变：把官网**资格限制、申请门槛、审核周期、是否需要回链徽章、真实外链属性**拆开核验。不要为了“高DR”向明确不符合条件的网站乱投。

## 一、直接投稿：DesignTrash（ID152；条件；不建议给Generador de Lettering投稿）

**入口：** https://designtrash.com/submit

**官方准则：** https://designtrash.com/llms.txt

- 永久普通目录收录不出售；有“Tool link”“Why should it be on DesignTrash?”、名称、分类、可选邮箱，并由真人审阅。
- 收录设计师真正会使用的原创工具、精选灵感资源、工具包、教程和真正有独特设计功能的AI工具。
- **明确拒绝 one-trick keyword sites**，给出的例子就包括 `cursive font generator`（花体字生成器）；还拒绝简单AI wrapper、蹭品牌名站、普通消费者应用与重复提交。每个网站仅审核一次。
- **当前结论：** `generadordelettering.org` 是以搜索关键词为品牌的字体/Lettering工具站；虽有编辑器与练习资源，但与该平台拒绝的典型模式接近。依官方规则，**不建议申请**。不能通过夸大成专业字体文件编辑器绕过审核。
- 未来其他独立设计师工具若具备真正的专业设计流程，可在确定符合规则后**人工**提交：
  1. 打开 `/submit`；
  2. 填真实产品URL、为何值得设计师收藏（具体解决的设计任务，而非SEO宣传）；
  3. 填真实产品名、选准确分类、可选联系人邮箱；
  4. 审核结果与公开条目、rel、robots、引荐流量分别记入台账。
- **免费/Follow：** 官网称人工编辑且不销售普通收录，但页面没有保证出站链接为Follow；DR/AS未实测。

## 二、DesignBookmark（ID153；条件；需实际英语可理解）

**官方资格：** https://designbookmark.com/listing-guidelines

- 官方明确**提交免费，人工审核**，已列出Typography及大量设计工具，详情页有“Visit website”出站访问链接。
- 核心限制：产品需要 `understandable in English`，必须是真正可用的完整工具、`https://` 可公开打开、不是关键词堆砌和跳转页。
- 简介**最多200字符**，必须是真实的一句话，不是宣传词串。官网按**域名+名称**查重，同一产品不能重复。
- **实际入口：** https://designbookmark.com/ —— 首页有 `Submit a tool` 按钮，当前未独立确认按钮生成的最终提交URL；**不要使用 /submit 或 /submit-tool 这种猜测地址**，已查这些直接路径并不能作为成功入口。
- **对纯西语站：** 先从英语用户实际浏览网站的角度测试其是否可理解和完成核心任务。**仅写一段英文提交简介并不能证明产品本身符合“英语可理解”**，不合格就跳过。
- 合格情况下建议填写：
  - Tool name：实际产品品牌名；
  - Website URL：项目实际HTTPS首页；
  - Description示范：`Free Spanish lettering editor for decorative text compositions and PNG, JPG or WEBP image export.`（前提是操作界面对英语用户足够可理解；否则不要提交）
  - Category：Typography或最贴近现有分类。
- 免费不等于Follow，也没有实时DR/AS证明。无需为追求SEO刻意给网站增加无价值的英语空壳页面。

## 三、DesignMunk（ID154；条件；免费档已明确Nofollow）

**官网投稿：** https://designmunk.com/submit/

**设计质量要求：** https://designmunk.com/guidelines/

- 免费Standard $0，人工审核，页面标明**标准免费链接为 Nofollow**，预计约2–3周；$9单次的Premium才提供官网标称的Do-follow，**不符合零费用原则**。
- 它是优秀网站设计展示库，不是字体功能工具目录。
- 适合：排版、交互、响应式界面和原创页面设计本身确实有展示价值的网站；存在真实清晰的设计选择及完整产品资料。
- 不适合：明显模板化/一键AI网站、广告/弹窗干扰、半成品、重复外观或明显响应式bug页面。
- 如确实符合，官网依次填写Submission Type、Name、真实URL、设计说明、联系信息；**只选Standard $0**。注意免费档并不能当成已验证的SEO Follow资源。
- 目标网站是否有足够独特的设计，建议先进行实际桌面和手机视觉审查，而不是因为出现“Typography”一词就申请。

## 四、额外排查但不新增到主库的假机会

**Font Blend**（https://fontblend.com/typography-tools/）：
- 官网介绍支持通过GitHub提交资源数据PR；
- 但其官方指向的仓库 https://github.com/Skabir2023/FontBlend 当前只有 README，无公开资源数据文件可直接提交PR。
- 因此**不能凭一句“可开PR”就记为有完整可操作的投稿入口**。可作为未来编辑推荐研究线索，暂不提供未经核实的仓库修改教程。
- 官网选择外链会特别审核许可证、质量和过度追踪；不应无依据承诺其会为西语字体转换器提供链接。

**字体文件投稿平台**（如1001 Free Fonts、Font Meme）：
- 官网要求提交**本人原创的真实TTF/OTF等字体文件、许可证及ZIP归档**；
- Lettering编辑器和Unicode文本转换器并不自然具备这些文件。**不应为外链伪造一个字体zip**，不列入当前通用提交优先队列。

## 五、严格免费优先清单

见 [data/reusable-free-shortlist.csv](../data/reusable-free-shortlist.csv)：保留高相关而且无已知“必须在本站安装长期徽章”的8家渠道，逐项注明实际免费资格与必须实测的缺口。

- 最高相关可先研究：LaunchFree、NoSignupTools、PeplioHUB。
- 有图片/表单准备及资格核验：DesignTools.fyi、Toolfound、TopTool。
- 免费/收录条款证据不充分、不能直接称作免费Follow：Good Design Tools、CtrlAlt.CC。
- **不建议为SEO Follow优先提交**：DesignMunk免费档、The Free Tools Directory的低DR仅补充、任何强制回链的高DR目录、DesignTrash明确排除的关键词工具站。

## 六、每个新西语网站应怎么执行

1. 从主库 `data/backlinks-master.csv` 按网站真实类型筛选；
2. 先用8家清单核验该站是否符合免费、语言、广告、完成度、注册/所有权条件；
3. 对某个**目标域名 + 平台根域名** 查 `data/submission-ledger.csv` 和历史邮件；不重复登记同一网站；
4. 获取真实公开资料页后核对准确外链 href、rel、canonical、robots、Google真实索引证据、引荐访问，未核验项仍标记未知；
5. 只有审核通过且公开链接指向你的目标页，才可计入“已经获链”；官网承诺、表单接受、注册成功都不等于获链。

## 公开证据清单

- https://designtrash.com/submit
- https://designtrash.com/llms.txt
- https://designtrash.com/best/typography
- https://designbookmark.com/listing-guidelines
- https://designbookmark.com/
- https://designbookmark.com/tool/grabient
- https://designmunk.com/submit/
- https://designmunk.com/guidelines/
- https://fontblend.com/typography-tools/
- https://github.com/Skabir2023/FontBlend

**质量门槛：** 除域名外零成本、真实与读者相关、没有违背站方投稿资格、没有虚假关键词堆砌/强制回链/付费购买SEO，且不能把外链数量当成效果。