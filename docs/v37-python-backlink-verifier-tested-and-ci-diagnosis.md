# V37｜真实Python验收、HTML误判修复及Actions故障证据（2026-10-31）

> 这轮专注验证“已经写进GitHub的验链工具是否真的能运行”。**没有新建第三方目录来源、没有代投外链、没有新增任何属于Lettering的已确认反向链接。**

## 1. 首次完成真实Python单元测试

**测试执行环境**：Python 3.13.5、Linux容器，使用Python内置`unittest`，不需要网络、无付费API或第三方Python包。真实执行命令：

```bash
python -m compileall -q verify_published_backlink.py test_verify_published_backlink.py
python -m unittest discover -s . -p 'test_verify_published_backlink.py' -v
```

结果：**Ran 11 tests in 0.008s — OK**；**通过11、失败0、错误0**。

已在本地重建与仓库**字节完全一致**的两份源文件，并使用Git对象blob SHA-1算法核对，确保“本地测的代码”确实就是最终提交在GitHub的代码：

| 文件 | 字节长度 | 本地和GitHub完全一致的Git blob SHA |
| --- | ---: | --- |
| `scripts/verify_published_backlink.py` | 7505 | `8a085d84057e17557a7ffff2f5c937ea68caa20c` |
| `scripts/test_verify_published_backlink.py` | 5404 | `e86742cee41db53c85e774a790aeb850c4c9a2f8` |

这是**真实Python解释器执行的本地测试**；不是GitHub Actions成功记录，不包含任何实际联网访问目录站点的测试。

## 2. 真实测试发现并修复的3处误判风险

**问题A：损坏的第三方href阻止检查后面的有效链接**

某目录HTML中若出现`<a href="http://[">`，旧版`urljoin/urlsplit`会抛出`ValueError`，导致整个目录页检查失败。新版只忽略这条损坏的链接，继续查找其他锚点。新回归测试`test_malformed_anchor_does_not_hide_valid_link`实际通过。

**问题B：某些HTML的rel属性只有名字、没有值**

合法但格式较特殊的`<a rel href="https://...">`会使`HTMLParser`返回`rel=None`，旧代码调用`.lower()`出错。新版把空或无值rel转换为`""`，输出`(none)`并保持“未见限制词”的准确表述。新回归测试`test_valueless_rel_does_not_crash`实际通过。

**问题C：未展示的HTML模板链接被误算为公开反链**

`<template><a href="https://目标域名">...</a></template>`中的锚点通常属于惰性模板、并非当前可见资源链接。旧版HTML解析器会将其计入外链。新版为`template`加嵌套深度跟踪，默认排除这种惰性内容。新回归测试`test_inert_html_template_does_not_count_as_a_live_backlink`实际通过。

旧的8项也全部继续通过：精确路径匹配、真实域名/伪造域名识别、正文文本不计链接、nofollow/ugc/sponsored解析、保留域名/私网拦截、本地fixture明确标识、没有href时退出码1。

## 3. GitHub Actions：证据明确但尚未定位最终根因

**当日新运行**：[失败运行 #41156120728](https://github.com/chenmu2024/xibanyayuwailian/actions/runs/41156120728)，提交`129bd394e1800e7a22452e4b6404c94fc4ec51ed`，结果`failure`，`validate`任务也标记`failure`，但其API`steps=null`，此前相邻运行`steps=[]`，日志下载曾返回`404 BlobNotFound`。

这不是通常的“Python单测某条失败”的直接证据。故障**可能发生在Runner调度/初始化、账户/仓库Actions许可、计费限制或GitHub服务层**；目前没有证据能唯一确定某一个原因。不能为了显示绿色而删掉测试、吞掉错误或伪造`success`状态。

**下次用户可做的零成本检查**：

1. 打开GitHub仓库 [Actions](https://github.com/chenmu2024/xibanyayuwailian/actions)，进入具体失败运行，查看顶部是否有计费、Actions禁用、runner provision、限额或账户验证的提示。
2. 仓库 Settings → Actions → General：检查Actions是否允许运行，`actions/checkout@v4`是否被组织策略阻止。
3. 账号 Settings → Billing and licensing/Usage：检查GitHub Actions预算和可能的用量限制；**公开仓库免费Runner的政策应以当前官方说明为准**，不能直接断定已超额。
4. 如仍0步骤/无日志，携带Run ID和Job ID向GitHub Support提交材料。现有工作流原样保留，避免把Runner层异常误诊成应用代码问题。

可以通过GitHub网页“Re-run jobs”再试一次，但并不能保证修复。**本轮不在GitHub反复启动已知失败的作业，不制造额外开销或重复通知。**

## 4. 工具使用边界继续保留

- `scripts/verify_published_backlink.py` 只验证**用户提供的单一公开HTTPS HTML页**，不向第三方提交申请、不扫描全站、不破解验证码。
- `--html-file`提供的是离线fixture，`mode=offline_fixture_not_live_evidence`；不能把本次11项fixture测试当作实际获链。
- `status=found`仅证明特定HTML具有匹配的`<a href>`。实际Google索引、排名传递、真实引荐量、DR/AS都需要独立证据。
- `rel_result=no_restriction_token_observed`不是“保证Dofollow”。
- V36的176条渠道主库、21家161项真实填写卡、每域名资料/进度/手工证据隔离和V2备份均不改动。

## 5. 关联代码与文档

- [真实运行的验链Python源码](../scripts/verify_published_backlink.py)
- [11项已运行的Python测试](../scripts/test_verify_published_backlink.py)
- [V35完整验证流程](v35-evidence-based-backlink-verification.md)
- [V36不同网站资料隔离](v36-domain-isolated-profiles-and-v2-backups.md)
- [Windows多站外链HTML操作台](backlink-submission-workbench.html)

**V37交付结论**：真实Python 11/11通过、3处源码误判风险已修复；GitHub Actions仍失败且原因未确认；已确认新增Lettering反向链接**0条**。
