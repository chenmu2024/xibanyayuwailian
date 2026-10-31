# V40｜高相关西语、字体与设计目录：规范域名与外链质量核验（2026-10-31）

**目标：质量优先，而非增加来源数。新增目录0、实际投稿0、生成本站新确认反链0。** [逐条9个公开页面样本CSV](../data/v40-curated-link-evidence-20261031.csv)。9行为不同页面样本，其中LDS与Mark-it各有两个页面，**不是9家外链网站**。

## 关键发现一：LDS Library（#163）正式规范域名与历史别名

原历史入口 [lds-library.vercel.app/fonts分类](https://lds-library.vercel.app/design-resources/fonts) 和 [旧投稿页](https://lds-library.vercel.app/submit) 可访问，但它们的HTML canonical都指向 `library.legitdesign.studio` 的相同路径。重新读取 [规范域Fonts页](https://library.legitdesign.studio/design-resources/fonts) 和 [规范域Suggest a resource](https://library.legitdesign.studio/submit) 均成功，canonical自指。当前平台唯一优先填写地址是 **https://library.legitdesign.studio/submit**，历史Vercel来源保留为别名。严禁因为两个地址注册根域不同就算两次独立申请或两条外链。

V34旧域Fontjoy、Fontshare两个实际外站a[href]的raw rel为`noopener`，这只是当时那个**旧域页面**的历史证据；本次新规范域链接虽可见，但未读取其原始rel。不能用旧样本保证新申请页面Follow，亦不能以canonical或meta robots宣称Google实际收录。

## 关键发现二：Mark-it（#165）应从P1降为P2

[真实Font栏目](https://markitnow.net/font)目前有Font Library、Font Bolt、Font Get、Font Space、Google Fonts等较少的字体目录直达外站链接；[人工建议表单](https://markitnow.net/submit-a-resource)仍可读，且[编辑政策](https://markitnow.net/editorial-policy)明确质量与人工审核。这并非空站，也不代表投稿无效。

但[主页All Resources](https://markitnow.net/)转到 `markit-x-os-design-directory.vercel.app` 的独立交互网站；本轮公开内容抽取只能确认展示简介和项目模板链接，**没有获得可核验的具体资源外站a[href]**。不能据此断言该应用全站没链接，也不能将其模板GitHub仓库误认为Mark-it真正免费上榜入口。原V34首页Fontmeme和CMD Supply真实外站href无rel的样本照旧保留，但以“免费独立高权重外链”为目标时，现有证据不足以列第一梯队。因此降P2并后置。

## 其它优先目录继续按真实样本复核

- **#159 [Design Resources Archive](https://resourcesfor.design/submit)**：Typography栏目已有[Mixweight](https://resourcesfor.design/resource/mixweight-594817)及Type Garden独立详情直接外站href，历史V34两条raw rel `noopener noreferrer`。投稿页Link URL、Description、人机验证，人工审核；未保证永久免费获链。
- **#151 [DesignTools.fyi](https://designtools.fyi/submit/)**：Font Explorer公开详情直达font.do，历史V33原始rel `noopener noreferrer`；Typography/Free真实分类，姓名邮箱须实填。
- **#164 [Unikist](https://unikist.com/submit)**：Fonts分类现62条、Design Tools分类36条，含Fontshare、Photopea等真实外站链接；对`generadordelettering.org/editor`建议选择设计创作工具分类，不能谎称下载字体文件。
- **#172 [EpicTools](https://epictools.dev/submit)**：Font Tester及Penpot有普通Curated独立详情外站链接；V34 Penpot等样本未带rel限制词。Partner显式follow不代表免费Curated待遇，仍只投真实Design类。
- **#171 FounderOmni**：有Fontpair及Hero Patterns独立资源详情外站href，V32已经验证西语表单字段，raw rel未知；仍属条件候选。

## 本站真实能力及提交资料边界

[Generador de Lettering编辑器](https://generadordelettering.org/editor)实际支持自定义文字、样式、颜色、描边、阴影、背景、旋转与PNG/JPG/WebP图片导出。不能宣传TTF/OTF下载、矢量SVG文件导出或专业印刷DPI保证。网站界面是西语，不可只写英语投稿介绍便声称已提供完整英文版。

## 决策与实测边界

本轮主库#163使用规范域，#165从P1变P2；同步176主库/手册/离线HTML及V34历史填写指南，**保留V23、V34原始证据**不改写。最终排序优先#159、#151、#164、#172，#163使用规范域一次申请；#165后置。DR/AS尚未实测，收费/免费长期资格与具体发表页rel未知，所有提交状态继续留在未提交。只有第三方公开页真正出现指向`generadordelettering.org`的HTML href时，才能另行记录实际获链。
