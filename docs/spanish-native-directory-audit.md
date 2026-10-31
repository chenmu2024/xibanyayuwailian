# 西语本土目录的真实入驻资格与获链质量审计｜2026-10-31

研究范围限定原176历史条目中的 **#4 DrSEO.eu、#58 Educaguía、#59 Navegax**。没有新增目录、没有第三方真实提交，也没有任何确认新增属于`generadordelettering.org`的外链。[7条可复核官网页/证据CSV](../data/spanish-native-directory-audit.csv)。

## 1. #59 Navegax：保留P1，但必须登录（不是直接填表）

- [官网西语首页](https://navegax.com/)公开声明“Registrar un sitio web ... completamente gratis”，支持西语网站的类型/分类。
- 实测点击“Añadir Web”后进入[erroragregar](https://navegax.com/erroragregar)：“Para poder añadir un Sitio Web debe acceder mediante un usuario registrado, o registrar un nuevo usuario.” 即没有账号时会被阻止，必须先真实注册或登录。
- [IAdicto Digital具体普通站点资料](https://navegax.com/detalle/iadictodigital)公开`Ir al Sitio Web`，实际指向`https://iadictodigital.com/`外部网站。这不是自家页脚或站内重定向案例，确实存在普通目录站外链接；本轮没有获取原始HTML `rel`，没有独立核验Google索引或DR。

**如自行填写**：官网主页→Añadir Web→用户登录/注册→按实际选`Informática, Tecnología, e Internet`或切合当前页的艺术类别→标题 `Generador de Lettering`→URL `https://generadordelettering.org/`→简介使用实际西语功能说明：

> Editor gratuito de lettering en español para crear diseños de texto personalizados con estilos, colores, contornos y sombras. Permite exportar imágenes en PNG, JPG y WebP.

本人邮箱、账号、作者资料、国家/所在地如被要求必须如实填写，不得默认写西班牙地址。先检索本人历史提交记录以免重复；获批后核对真实href及raw rel。

## 2. #58 Educaguía：P1→条件，普通字图工具不应冒充教育网站

[官网教育网站免费申请页](https://educaguia.com/inserta-tu-web.asp)明确：

- **只接受教育相关网站**，网站会被人工访问审阅其实际质量/用途。
- 申请会自动加入其**教育通讯订阅**，不是一个未见风险的“无后续邮件免费投”。
- 对“最好的”资源会提供“Sitio Web recomendado”的徽章HTML以获取**额外优先展示**；官方文本没有说普通免费收录一律强制加徽章，不应错误当作强制双向交换。
- [Software Educativo实际分类](https://educaguia.com/software-educativo.asp)确有Educaplay等在线教育产品外部链接，但这不能证明泛用Lettering编辑器一定符合要求。

**决策**：只有目标网站已确实存在可供学校美术课、练习字体艺术、教师教学的真实材料或课堂内容，才考虑“Recursos Educativos”及合适分类，并按实际现有内容提交。不能为了外链虚构教学栏目、课件、教辅、作者资质或学生年龄范围。否则不提交。

## 3. #4 DrSEO.eu：P1→P2，免费规则真实但所见外链样本是Premium

- [西语首页](https://drseo.eu/es/)和[价格页](https://drseo.eu/es/pricing/)明确免费基本档`€0 para siempre`，包含公开资料页、类目、描述和外部网站链接。增值`Premium Profile €19`（一次）及`Featured €9/月`为可选，不应为获取普通目录链接去付钱。
- [英文提交入口](https://drseo.eu/submit/)可读取完整真实表单：网站名称、网站URL、主类别、简短介绍、可选Logo及（若适用）地区、真实联系人姓名邮箱、Google登录或密码创建账号和真人验证码。**2026-10-31爬虫访问[西语入口](https://drseo.eu/es/submit/)出现403，只能说明这次请求失败，不能断言网站停止接受提交**。
- [ACC64独立公开详情](https://drseo.eu/es/listing/acc64/)存在真实`Visitar web`到`https://acc64.com`外部href，但该页明确标注`Premium Profile · Patrocinado`，**不能把它当成Free未付费公开资料的rel/曝光样本**。主站示例还包括GitHub、Canva、Notion、Shopify等品牌资料，不能凭这些自称Reviewed推断自助投稿收录率。
- 页面底部付费介绍标注支付测试模式，与免费审核无直接逻辑冲突；不用于判断作弊或诈骗。更重要的是缺乏目标主题具体免费刊登页及其raw rel证据。

**决策**：P2低工作量提交候选，只用Free €0方案。不填虚假实体地址、业务电话；资料与账户信息必须本人真实，手工完成验证码。欲升级至P1先找到**真正标为Free的普通详情页**并验证直接站外href及原始rel，再实证实际收录和引荐。

## 4. 审计边界与主表同步

- 主库状态：#59继续P1；#4由P1→P2；#58由P1→条件；原176历史渠道总数不变。
- 新分布：P1 17、P2 24、条件84、待核验16、排除34、非外链1。主库、176条逐站手册、离线操作台已同步；修正HTML可见统计旧排除33误写。
- **没有实际申请、收录回执、属于本站的公开href或Follow、真实DR/AS、Google索引或引荐流量数据**。第三方的目录存在、可点击网址或`robots=index,follow`均非真实SEO效果保证。

## V43 备注：Bitakoras不是另一个适合字图编辑器的目录

[Navegax公开详情](https://navegax.com/detalle/iadictodigital)推荐的[Bitakoras](https://bitakoras.com/)明确只接受博客，两站数据库不共享、账户需分别注册。Generador de Lettering目前是在线文字图像编辑器，不能把博客限定渠道记为额外的工具站外链。
