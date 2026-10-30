# V25｜西语直接提交、设计资源免费工具、开源Issue渠道和历史Badge纠错

**日期：2026-10-31**。目标网站： https://generadordelettering.org/ 。历史主库 **167 → 171**，新增4条研究记录，并将历史 **AI Webcatalog #109** 按最新官方强制徽章规则改为**排除**。本轮未向第三方提交表单、GitHub Issues或发送站外私信；新增已获外链 **0**。

## 优先级总览
1. **Herramientas y Recursos #168**：真正西语目录，有公开详情页 + 可操作建议表单。**A级先试**。
2. **FreeDesignerTools #169**：公开设计工具建议表单，功能高度匹配但网站只有12条馆藏，不能冒充高权重。**B级可试**。
3. **Ghostbyte Library #170**：官网点提交确实是外部GitHub Issues，仓库有真实源码数据和其他用户开放Issue。**C级可建议，不等于直接获链**。
4. **FounderOmni #171**：西语设计库有“建议资源”按钮；未实测展开后的完整表单/费用/账号要求。**C级继续核查，不列当前可投**。
5. **AI Webcatalog #109**：2026-10-31官网明确免费审核也要**在自己网站插徽章并提供回链页面**；而且仅收AI工具，因此**排除**，不再作为新西语网站通用提交渠道。

全部新来源：实时 Ahrefs DR、Semrush AS、网页实际 `rel` 和 Google 收录状态均**未独立实测**。目录无付款字段不能被夸大为“官方永久免费Follow”。

## 01. Herramientas y Recursos｜首推西班牙语

- 官方入口：https://www.herramientasyrecursos.com/directorio/sugerir
- 真实公开工具样例：https://www.herramientasyrecursos.com/sitio/validar-epub-pecia-b4db48
- 官方主目录：https://www.herramientasyrecursos.com/directorio/
- 示例为免登录浏览器EPUB验证工具，有独立资料页和“Visitar sitio”外部按钮。**只有存在站外链接的展示证据，未实测链接rel/引荐或真实Google索引。**

### 推荐逐字段填写（按实际页面核对）

| 字段 | 填写示例 |
|---|---|
| Nombre o título | Generador de Lettering |
| Tipo | Herramienta web gratuita |
| Tema principal | Diseño, tipografía y lettering |
| Público objetivo | Estudiantes, creadores de contenido, diseñadores y público general |
| URL del sitio | https://generadordelettering.org/ |
| Categorías | `Recursos`，其他仅选真实对应选项（最多3类） |
| Logo o imagen | 真实网站徽标，PNG/JPG/WebP，官方限2MB |
| Descripción breve | Herramienta gratuita en español para crear diseños de lettering y personalizar texto en el navegador. |
| Descripción completa | 见下方段落 |
| Redes sociales | 有真实官方账号才填，不能编造 |
| RSS | 只有真实可用订阅源才填 |
| Correo para avisos | 用户自己可收信的真实邮箱（仓库不储存） |

**Descripción completa 可复制**：

```text
Generador de Lettering es una herramienta gratuita en español para personalizar letras y crear composiciones de texto decorativo desde el navegador. Permite probar estilos visuales, ajustar colores, contornos, sombras y otros parámetros de diseño en su editor gráfico. Es útil para preparar imágenes de texto para invitaciones, tarjetas, publicaciones en redes sociales y proyectos creativos. El editor permite exportar la composición como imagen PNG, JPG o WebP. No es una biblioteca de fuentes descargables TTF u OTF. El sitio también reúne recursos y herramientas relacionados con lettering.
```

填好后手动点 `Enviar propuesta`；保存确认和实际审核邮件。不为西语目录伪造地理归属。人工审核结果未知。

## 02. FreeDesignerTools｜设计类免费工具

- 直接表单：https://www.freedesignertools.com/suggest/
- 现有目录：https://www.freedesignertools.com/
- 已收录Google Fonts、Photopea等工具；当前仅12个条目。官网主页“50M+ users”等宣传没有可靠独立证明，**不得当成目录自身流量**。

填写：
- `Tool Name`：Generador de Lettering
- `Website URL`：https://generadordelettering.org/editor
- `Description`：`Free Spanish-language browser lettering editor. Customize text artwork with fonts, colors, outlines, shadows and canvas settings, then export images in PNG, JPG or WebP. No account required.`
- `Tags`：按表单实际操作添加 `Typography`、`Lettering`、`Text design`
- 点 `Submit Tool for Review`；不要额外加付费或徽章。

**仅当前公开表单无收费、无强制徽章字段**，不表示获得免费永久刊登或Follow，编辑可拒绝纯西语资源。

## 03. Ghostbyte Library｜官网推荐=GitHub Issue，别当PR已获链

- 官方站：https://library.ghostbyte.dev/
- 官网Submit a Resource直达：https://github.com/ghostbyte-dev/ghostbyte-library/issues
- 建议新Issue：https://github.com/ghostbyte-dev/ghostbyte-library/issues/new
- 真实类别：https://library.ghostbyte.dev/fonts
- 公开源码：`https://github.com/ghostbyte-dev/ghostbyte-library/blob/main/data/design/fonts.ts` 与 `data/design/tools.ts`
- 已有字体图像相关提案Issue #9，2026-10-31检查为Open：https://github.com/ghostbyte-dev/ghostbyte-library/issues/9

如决定建议，先查Issues避免同域重复。点击 `New issue` 需GitHub账号登录。建议正文（可复制）：

```markdown
Title: Resource suggestion: Generador de Lettering — free Spanish lettering editor

- Resource: Generador de Lettering
- Website: https://generadordelettering.org/editor
- Suggested category: Design Tools / Typography
- Pricing: Free; the core editor does not require signing in.
- What it does: A Spanish-language browser editor for composing decorative text artwork with font, color, outline, shadow and canvas controls. It can export PNG, JPG and WebP images.
- What it does not do: This is not an installable TTF/OTF font foundry or a professional SVG/font-file exporter.
- Relevance: Helpful for Spanish-speaking creators preparing visual text artwork for cards and social graphics. Please review only if it fits the library's editorial criteria.
```

**提交Issue本身不是外链落地成功**。只有仓库维护者接纳、真正新增资源条目并在外部网站可公开点击到本站，才记录为已上线并实查rel。

## 04. FounderOmni｜西语设计库但正式提交未核

- 研究页面：https://founderomni.com/es/library/design-brand-assets/
- 页面有 `Sugerir un recurso` 控件。Fontpair、Accessible Palette等例子表明会展示第三方资源。
- 本轮无法独立确认控件弹窗最终字段、账户及是否免费，因此不应给用户虚假的“填写姓名邮箱按提交即可”教程，也不加入可立即申请表。
- 仅建议手工打开控件核查资格后再决定提交当前编辑器。

## 05. 两条需要避坑的旧站纠错

**AI Webcatalog #109**：2026-10-31 官方 https://ai-webcatalog.space/es/submit 的西语或自动跳转到俄语的提交页，都明确 `badge obligatorio`（徽章及徽章所在页URL必须填写）。这不符合无强制反链政策，而且目录只收AI工具。**历史主表原#109保留、更新证据和优先级为排除**。没有删除旧记录。

**illustration.tools**：搜索缓存能看到内嵌“Submit a Resource”文本、Typography栏目及Resource Name/Link输入，但本轮官网直接HTTP读取超时，另一网页抓取服务返回invalid_url。仅能记录待核验观察，**当前不得升为已证实可投、不得凭搜索索引断言表单正常**。

## 06. 额外编辑媒体线索（与目录清单分开）

**Best Productivity Resources**（加入`data/editorial-prospects.csv` E006）：https://bestproductivityresources.com/how-to-submit 有明确人工编辑投稿政策，要求通过作者本人LinkedIn DM提供资源名、URL、分类、免费/付费及价值一句话。无需购买普通目录位，但**并无一般表单或自动批准**，与纯Typography的匹配度低于前述西语网站。**只记未联系，不代发私信，不当当前可填目录。**

## 后续验收标准

- 申请前检查本仓库目标根域名×平台根域名的真实提交台账与现有公开页面，避免重复。
- 用户手动提交后再登记实际日期、确认邮件、审核状态；不能把本轮研究新行写成已提交。
- 审核通过后查详情页真实目标 `href`、`rel`、`robots`、`canonical`、Google索引和引荐访问。
- 本轮仅研究渠道；未提交、未发邮件、未编辑网站、未修改许可证、不安装付费/互链徽章。
