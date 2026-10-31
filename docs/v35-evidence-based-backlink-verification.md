# V35｜从外链投稿到实际获链：可保存的人工证据与零成本HTML验链

发布日期：2026-10-31。原库仍然是**176个历史渠道候选**、21家精细表单卡、161项字段，V33/V34的公开第三方href样本仍是研究证据，而不是用户网站实际获链。

## 1. 为什么新增这套证据工作流

过去的进度阶段“已自行提交”“审核中”“已上线待验链”并不证明`generadordelettering.org`拥有真实外链；只写一个第三方域名、编辑建议或平台的`Thanks`页面也不够。

V35新增两个环节，互不混淆：

- **离线HTML操作台中的手工自查证据**：每个平台可填写“第三方公开详情页URL”“该页面真正指向本站的完整href”“该<a>标签原始rel属性”。用户必须亲自点“我已亲自检查...”确认，系统**不联网查证**，也不会自动把条目写入GitHub正式台账。
- **零付费HTML验链脚本**：`scripts/verify_published_backlink.py`直接读取你指定的单个公开HTTPS页面，解析真正的`<a href>`，按目标域名或精确目标URL匹配，回传所有实际匹配的href及原始rel，并可以输出JSON证据。没有付费API、没有注册账号、不会提交给对方网站。

这一套能避免常见错误：把用户自己首页、`generadordelettering.org.evil.com`、正文普通文本、外链申请表、页面包含Google搜索的URL、其他人的Fontjoy/StackEdit链接算成你自己的外链。

## 2. Windows PowerShell：真实公开链接核验

在电脑有Python 3.9及以上版本的前提下，打开仓库根目录的PowerShell。若还没有Python，可先用`python --version`或`py -V`核对安装。

**A. 自己的网站真的出现在第三方公开条目之后运行：**

```powershell
python .\scripts\verify_published_backlink.py --source "https://目录网站/真实公开条目地址" --target "https://generadordelettering.org/" --output "lettering-link-evidence.json"
```

`https://目录网站/真实公开条目地址`是占位符，**必须替换为对方真实发布的HTTPS页面**，不是推荐表单、网站首页或尚未取得的虚构slug。脚本只扫描你输入的这一个页面，不会自动爬全站。

**B. 如果想核实精确的`/editor`，而不是任何站内页面：**

```powershell
python .\scripts\verify_published_backlink.py --source "https://目录网站/真实公开条目地址" --target "https://generadordelettering.org/editor" --match exact --output "lettering-editor-evidence.json"
```

默认`--match domain`允许任何真正指向`generadordelettering.org`或`www.generadordelettering.org`的href；`--match exact`只接受目标完全匹配的路径和查询参数（不自动把主页当`/editor`）。

**C. 先演示检查第三方已经存在的公开资源（不是你的外链）：**

```powershell
python .\scripts\verify_published_backlink.py --source "https://htrd.org/tools/fontjoy" --target "https://fontjoy.com" --output "sample-fontjoy-not-my-backlink.json"
```

这是对**其他人网站**的公开真实HTML进行只读测试，不是为Lettering完成投稿。

## 3. 如何阅读结果

| JSON字段 | 含义 |
| --- | --- |
| `status=found` | 在本次读取的HTML`<a href>`中找到了指向目标域名/目标URL的链接 |
| `status=not_found_in_fetched_html` | 本次抓取HTML的锚点未发现对应href；**不等于整站不存在**，可能是JS渲染、别的页面或目录尚未公开 |
| `rel` | 实际HTML的完整rel属性；无rel时为`(none)` |
| `rel_result=nofollow` / `sponsored` / `ugc` | 真实rel明确包含这些限制词；可以同时存在多个 |
| `rel_result=no_restriction_token_observed` | 这条样本未见上述限制词，**不意味着Google保证传权** |
| `mode=live_public_page_fetched` | 程序确实访问了你指定的公开HTTPS页面 |
| `mode=offline_fixture_not_live_evidence` | 测试使用本地HTML，**严禁把这种结果当作线上真实获链** |

程序退出码：0=找到了匹配链接；1=只在本次HTML未找到；2=网络/页面/安全校验错误。网络错误时不生成“已获链”结论。

脚本限制：只接受公开HTTPS、单次最大2MB、合理的网络超时；拒绝本地/私有IP与一些保留域名，限制重定向，并不登录、发布或修改对方网站。对于JS动态生成的链接、人机验证、Cloudflare防护或页面变动仍可能无法判定；无需尝试绕过网站防护。

## 4. 离线操作台：把证据与进度关联到单一目标域名

打开 [V35离线HTML](backlink-submission-workbench.html)，进入某个平台卡片最下方：

1. 正常记录提交进度和备注（仍然不能等于已获链）。
2. **第三方公开条目URL**：如获批之后编辑发给你的真实`https://directory.tld/tools/slug`链接，不要填投稿表单。
3. **页面中的目标href**：精确复制你在第三方页面HTML中看到的`https://generadordelettering.org/... `。
4. **原始rel**：例如`noopener noreferrer`、`noopener nofollow`、`noopener sponsored`；如果该`<a>`标签没有rel属性，输入`(none)`。不要用“Dofollow”代替原始HTML字段。
5. **明确本人确认**：自查无误后点击按钮；若字段变更，旧确认会自动撤销，需重新查证。不同目标网站域名的进度与证据仍各自保存，不互串。
6. 用“备份所有网站JSON”保存完整个人证据，或“导出本地进度CSV”获得包括源页面、实际href、rel、自查日期的新列。请妥善保存邮箱和备注，勿将完整个人备份公开上传。

此**本人确认**仅是用户自己填写和确认的声明，页面没有联网检查或权威第三方证明，不能被当作平台审核通过的自动证据。

## 5. 正式GitHub台账如何记录

正式`data/submission-ledger.csv`仍需要**由用户审核后更新**，而不是操作台自动将所有“已自行提交”变成“已上线”：

- 官方公开条目URL必须真实存在、页面可读。
- 在网页HTML中必须有**指向自己目标域名的真实href**，不能只有品牌文本、其他工具的href或表单回执。
- 如实保存原始rel，若含nofollow/ugc/sponsored必须明确填写，不能写Follow。
- 索引情况和引荐流量独立核实；没有GSC或Analytics证据时填写“未测”，不能从工具截图推断。
- 脚本JSON可以作为**辅助证据**；只有人工确认与网站有一致的目标链接后才更新公开台账。

GitHub Actions失败仍属于**单独的CI可用性问题**。最近失败的job API返回步骤数组为空，执行耗时仅数秒；不能据此唯一判定是Runner、账户额度、工作流配置还是平台故障。原测试没有被删除或跳过。

## 6. 自动化校验代码

```powershell
python -m unittest discover -s scripts -p "test_verify_published_backlink.py" -v
python .\scripts\validate_csv.py
node .\scripts\validate_workbench.mjs
node .\scripts\smoke_workbench.mjs
```

- `test_verify_published_backlink.py`包含8组离线单元测试：真实域名匹配、精确路径、正文文本不是链接、nofollow/sponsored/ugc、阻止私有/保留URL、离线fixture不能冒充线上结果、无href的退出码等，**不调用网络**。
- V35操作台静态检查与模拟DOM**17项交互断言**已在独立V8环境执行通过；新Python测试已提交源码与CI计划，但当前环境无法联网获取源码到本地Python运行器、而GitHub Actions未实际运行步骤，**不虚报Python测试已通过**。

## 7. 关联文件

- [V35 离线操作台](backlink-submission-workbench.html)
- [V34第二批5家字体设计目录](v34-five-more-design-font-directories-ready-to-fill.md)
- [176条原始研究库](../data/backlinks-master.csv)
- [真实申请/获链台账](../data/submission-ledger.csv)
- `scripts/verify_published_backlink.py`（只读HTML验链）
- `scripts/test_verify_published_backlink.py`（离线单元测试）

**截至V35：新增确认获得的Generador de Lettering第三方外链仍是0，项目已有176条历史研究候选。**
