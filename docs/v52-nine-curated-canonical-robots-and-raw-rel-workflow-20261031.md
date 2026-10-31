# V52｜9家字体／设计目录已发布外链的页面级SEO证据与只读原始rel批量核验

核查日期：2026-10-31（北京时间）。范围：原V51已有来源，不新增目录；没有代注册、代提交、发邮件或改写用户网站。**当前确认新增Generador反向链接仍是0。**

## 核心增量：不是“看见链接”就叫Follow

已通过公开页面读取，明确分离以下证据层级：

1. **实际公开第三方外部href**：页面中存在指向别人的工具或字体站的可读外链。V52有9个不同平台的样本，见 [9平台逐行元信息CSV](../data/v52-curated-published-anchor-metadata-20261031.csv)。
2. **页面canonical和meta robots**：判断是否指向自己、是否出现显式`index, follow`。这种页面元信息**不是**HTML锚点的`rel`，也不是Google是否真的已索引的证据。
3. **HTML锚点raw rel**：本轮使用了经过渲染清洗的网页内容；虽能取得实际外站href及<head>元信息，但**不会原样保留a标签全部属性**。因此本轮不新增任何“现时raw rel实测已Follow”的结论。V33/V34历史rel仍是历史。
4. **用户真正获得反链**：需要独立公开页面的`a href`确实指向 `generadordelettering.org`（可包括具体内页），再验证其原始rel与是否索引；V52只是第三方证据。

## 逐站公开链接与页面级元信息

| 编号/平台 | 公开页面与真实外站href | 本轮canonical | 本轮meta robots | 判读 |
| --- | --- | --- | --- | --- |
| #159 Design Resources Archive | [Mixweight](https://resourcesfor.design/resource/mixweight-594817) → `https://mixweight.pages.dev/?utm_source=ig&utm_medium=social&utm_content=link_in_bio` | 自指 | 未返回明确meta robots | Typography真实独立详情；旧V34 rel不能当最新 |
| #164 Unikist | [Fonts目录](https://unikist.com/categories/fonts) → `https://fontshare.com` | 提取结果未返回明确canonical | `index, follow` | 分类62项，不是对本站批准；真实提交须选Design Tools |
| #151 DesignTools.fyi | [Font Explorer](https://designtools.fyi/tools/font-explorer-mqp69i9d) → `https://font.do` | 自指 | `index, follow` | 独立字体工具详情，仍需姓名邮箱 |
| #123 LaunchFree | [Fontique](https://launchfree.io/listings/fontique.html) → `https://fontique.art/` | 自指 | `index, follow` | 独立Lettering工具，官网自述dofollow而非当前a rel实测 |
| #75 Htrd | [Fontjoy](https://htrd.org/tools/fontjoy) → `https://fontjoy.com` | 自指 | `index, follow, max-image-preview:large, max-snippet:-1` | 免注册免费工具；“精选”强度仍未知 |
| #148 NoSignupTools | [FontsWiki](https://nosignuptools.com/tools/fontswiki) → `https://fontswiki.com` | 自指 | 未返回明确meta robots | 真正免费无需登录，广告站不能虚报No Ads |
| #163 LDS Library | [规范域Fonts目录](https://library.legitdesign.studio/design-resources/fonts) → `https://fontjoy.com/` | 自指 | 未返回明确meta robots | **V51先前抓取失败，V52换公开网页读取方式已成功** |
| #165 Mark-it | [Fonts目录](https://markitnow.net/font) → `https://fontmeme.com/` | 自指 | `max-image-preview:large` | 这不是显式的`index,follow`；编辑精选性仍不等于高SEO权重 |
| #172 EpicTools | [Penpot](https://epictools.dev/penpot) → `https://penpot.app/` | 自指 | `index, follow` | 有真实出站，但全站存在关闭或错误产品被列为Curated的质量噪声，继续后置 |

### #163 LDS Library：旧域名和规范域属于同一家

这次已能读取正式[Suggest a resource](https://library.legitdesign.studio/submit)和[Fonts目录](https://library.legitdesign.studio/design-resources/fonts)。旧版`https://lds-library.vercel.app/submit`与Fonts分类也可读取，但两页canonical都指向`library.legitdesign.studio`的对应路径。因此**不可以分别算两个来源、更不可两站重复投稿**。

最新公开抓取可见“Suggest a resource”、团队审核及周二资源周报说明；因为动态表单的所有实际字段未在此次网页文本中全部取得，**仍应按打开时的表单核对真实类别、作者和联系人字段**，不能声称已完成投递。

## 原始HTML rel的9页只读核验工具

新增 [scripts/audit_curated_v52.py](../scripts/audit_curated_v52.py) 和 [离线测试](../scripts/test_audit_curated_v52.py)。它**复用V49的HTTPS安全读取、单页2MB上限、最大5次跳转、精确href（包含跟踪参数）与逗号分隔rel判定**。默认最多只检查本报告中9条**其他网站的公开样本页**，没有申请表单POST、注册、Google搜索或全站爬取；不会把现场结果自动回写GitHub。

在Windows PowerShell中，在仓库根目录运行：

~~~powershell
# 先看9条将检查的页面，不访问外网（每条标记未扫描）
py .\scripts\audit_curated_v52.py --max-requests 0 --output v52-preview.csv

# 先尝试3个真实公开页面，单次不超过3个GET
py .\scripts\audit_curated_v52.py --max-requests 3 --output v52-three-pages.csv

# 如上轮完成再完整核查9个公开页面（至多9个GET）
py .\scripts\audit_curated_v52.py --max-requests 9 --output v52-raw-rel.csv

# 单元测试，仅模拟CSV与请求数量，不联网
py -m unittest discover -s scripts -p "test_audit_curated_v52.py" -v
~~~

输出`found_in_live_raw_html`才表示**本地当前拿到匹配的第三方a[href]及raw rel**；如果没找到，可能是JS加载/网络限制/站点改版/URL变化，只能记`not_found_in_fetched_raw_html`；若是报错则保留`fetch_or_validation_error`。目标仍然是其他人的域名，**即便9/9成功也不意味着Generador获得9条外链**。

## 修复/验证边界

- V52单独增加9行证据表，不把这9家误计为新平台；主库仍是176条、P1 13条。
- #58 Educaguía、#171 FounderOmni没有在本轮取得适合该脚本的完整HTTPS第三方样本目标；不借无关或HTTP页面编造标准HTTPS实例，也不使用用户自己的SVG页冒充已发布案例。
- 本次远程读取无法保留真实raw a[rel]，因此只提供**可以由站长电脑实际运行**的零付费核验脚本；未在当前执行环境联网运行该脚本，不能声称已有9条raw rel实时值。
- 2026-10-31历史GitHub Actions依然失败；已观察到最近一次验证从创建到失败仅约3秒、账单报告Linux runner运行0ms，且其job步骤清单为空、日志404。**可判断没有拿到有效的实际执行步骤记录，但不能唯一定位是账户、Runner调度、权限或YAML问题，也不能声称CI通过。**
- 后续优先顺序：#159 → #151/#164 → #163（本人实际核对表单后）→ #123 → #75/#148；#165、#172后置。任何用户真正提交后须留下时间、邮件回执，获批后验本域href/rel。
