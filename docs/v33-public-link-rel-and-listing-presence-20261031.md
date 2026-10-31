# V33｜公开外链是否真正存在：11个HTML出站链接属性实测与9页重复检查

- 核查日期：**2026-10-31**
- 目标网站：`https://generadordelettering.org/`，主要工具：`https://generadordelettering.org/editor`
- **本轮新找平台0，实际投稿0，已获得外链0**；只有公开网页的可复核HTML与检索记录。
- 证据性质：读取被测公开网页实际`<a href="...">`标签中的`rel`原文。不是来自DR估算、站长承诺或未经验证的第三方反链报告。

## 1. 最重要的事实：public.tools的3个公开链接样本都是nofollow

| 抽样平台 | 公开条目 | 指向的实际站点 | 从HTML读取的rel | 结论 |
| --- | --- | --- | --- | --- |
| public.tools | [StackEdit.io](https://public.tools/directory/stackedit-io) | `https://stackedit.io` | `noopener noreferrer nofollow` | 本条明确nofollow |
| public.tools | [Dillinger](https://public.tools/directory/dillinger) | `http://dillinger.io` | `noopener noreferrer nofollow` | 本条明确nofollow |
| public.tools | [Glyphr Studio](https://public.tools/directory/glyphr-studio) | `https://www.glyphrstudio.com` | `noopener noreferrer nofollow` | 字体工具样本同样nofollow |

这不是对public.tools站上**所有工具**的断言，但连续三条公开外站链接都带nofollow，足以将原目录中`#074 P1` **调整为“条件”**：如果要自然引荐流量仍可研究；如果核心目的是免费获得Follow外链，则不应优先投入申请时间。官方投稿表单仍可用，这与rel是不同维度。

**public.tools公开[目录](https://public.tools/directory)当日声称收录344个第三方工具**。扫描当时网页展示的目录文本没有发现`generadordelettering.org`；这不代表全网或后台确实没有该域名，更不能称为网站被平台拒绝。

## 2. 更值得关注的已发布公开链接样本

| 平台编号 | 公开样本页面 | 目标真实href | 读取到的rel |
| --- | --- | --- | --- |
| #075 Htrd | [Fontjoy](https://htrd.org/tools/fontjoy) | `https://fontjoy.com` | `noopener` |
| #075 Htrd | [Squoosh](https://htrd.org/tools/squoosh) | `https://squoosh.app` | `noopener` |
| #128 Toolfound | [StencilMaker](https://toolfound.com/tool/stencilmaker-app) | `https://stencilmaker.app/` | `noopener` |
| #128 Toolfound | [Offistrip](https://toolfound.com/tool/offistrip) | `https://calculator.offistrip.com/` | `noopener` |
| #151 DesignTools.fyi | [Font Explorer](https://designtools.fyi/tools/font-explorer-mqp69i9d) | `https://font.do` | `noopener noreferrer` |
| #148 NoSignupTools | [设计工具分类](https://nosignuptools.com/tools?category=design) | `https://fontswiki.com` | `noopener noreferrer` |
| #168 Herramientas y Recursos | [Recursos类别](https://www.herramientasyrecursos.com/directorio/categoria/recursos) | `https://www.aprendeygana.net` | `noopener` |
| #168 Herramientas y Recursos | 同上 | `https://www.herramientasproductivas.com` | `noopener` |

这些链接的`rel` **没有出现nofollow、ugc、sponsored属性**；仅能证明当前被读取的HTML中的标签样本状态。不能证明新申请必被录用、所有页面同样设置、Google一定传递SEO排名信号，也不能以此确认用户网站已获得链接。

尤其要说明：

- **Toolfound #128** 仍需验证用户拥有的域名；没有核实授权或所有权之前，不应代填或宣称已排期。
- **NoSignupTools #148** 严格要求免费且不强制注册，本站有AdSense不能勾选No Ads；实际审核仍可能拒绝。
- **Herramientas y Recursos #168** 的`Recursos`公开页已可找到多个指向第三方站点的链接，西语主题相关；虽然本次没查到Lettering，但属于值得优先准备的真实目录。
- **DesignTools.fyi #151** 的Font Explorer样本与字体排版更贴近，可据实际用途准备真实图片和信息。
- **Htrd #075** 的Fontjoy与Squoosh两个公开样本没有nofollow，也能确证Htrd确实发表工具专页；是否接受Lettering由编辑决定。

## 3. 本站是否已被目录收录：严格按观察范围记录

记录在 [V33目标域名公开页核查CSV](../data/v33-lettering-public-listing-presence-20261031.csv)：

- public.tools：已读取公开目录344工具内容，未检出目标域名；
- Htrd：首页可读工具清单及两个公开详情页，未检出；
- Toolfound：首页公开名单及两个公开详情页，未检出；
- DesignTools.fyi：首页公开资源名单及Font Explorer详情页，未检出；
- NoSignupTools：**仅设计分类**与首页，未检出；
- Herramientas y Recursos：**仅Recursos分类和目录首页**，未检出；
- FounderOmni：**仅西语设计/品牌资源聚合页**，未检出；
- UX Resources：Typography分类当日可读页面未检出、外部资源跳转仍需复核；
- LaunchFree：只扫描首页；猜测的`/launches`地址测试返回404，**不得据此推断所有历史项目页不存在**。

**未检出不等于全站确定未收录，更不等于被拒稿。** 本次没有登录Google Search Console或获得用户真实历史邮件回执，因此目前不宣布任何一个目录拥有用户网站的已验证获链。

## 4. 怎么利用这些事实优化申请顺序

1. **优先准备#075 Htrd、#128 Toolfound、#151 DesignTools.fyi、#148 NoSignupTools、#168 Herramientas y Recursos**：这些平台确实已有能指向外部网站、样本未带nofollow的公开链接，而且与免费工具/设计资源方向相符。
2. 若只能选2个先填，建议 **#075 Htrd** 和 **#168 Herramientas y Recursos**：前者有Fontjoy字体相关实例和五字段简单表单；后者为实际西语Recursos目录、分类页有真实外部链接。需要如实提供网站功能，不能保证批准。
3. **#128 Toolfound** 有真实公开工具专页，但免费发布还需域名所有权验证；能完成验证时再申请。
4. **#074 public.tools** 不删除：仍提供真实可用投稿，但3/3公开详情样本为nofollow，按“获取Follow”目标从P1降为条件；对自然用户引流可以保留。
5. **#171 FounderOmni** 的公开设计聚合页面出现推荐资源入口，但本次无法确认具体公开资源对第三方目标站的href/rel，继续标记“未证实”，不能与Htrd同等定级。
6. **#162 UX Resources** 的Typography类目录可读取，但此轮未取得能明确指向一个独立工具网站的公开资源链接作为rel样本，继续待验。

## 5. 复核数据与不可跨越的证据边界

- [11条公开真实出站链接属性证据CSV](../data/v33-published-outbound-rel-samples-20261031.csv)
- [9个目录页面的Lettering域名出现情况CSV](../data/v33-lettering-public-listing-presence-20261031.csv)
- [176条主库](../data/backlinks-master.csv) 仍为研究来源而非成功提交记录。
- [实际提交台账](../data/submission-ledger.csv) 本轮没有修改：实际获链0，不允许根据第三方公开样本创建属于Lettering的虚假反链。
- 本轮没有查询到独立可靠的DR/DA/AS与Google索引/Referral Sessions，因此本轮不提供不真实的权重数字。
- 所有页面HTML检查均指向第三方站已有公开样本而非用户网站。nofollow和非nofollow结论只对列出的具体标签生效；将来获得Lettering自己的详情页后必须**重新检查准确href、rel、索引与流量**。

## 6. 建议的真实验收流程（若手工申请）

访问平台官网 → 查是否已收录同一域名 → 填真实姓名、首页/编辑器、说明和截图 → 自己完成验证码/邮箱所有权验证 → 保存回执与实际公开条目URL → 新开公开页检查是否有`href="https://generadordelettering.org/..."` → 读取链接的`rel` → 再记录实际外链台账。**没公开条目就不计数**。

**本轮状态：完成公开现有样本审查，未开展第三方投稿。**
