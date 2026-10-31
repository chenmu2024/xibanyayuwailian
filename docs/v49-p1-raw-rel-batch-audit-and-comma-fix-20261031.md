# V49｜13家P1已公开案例原始href/rel一键核验（2026-10-31）

## 为什么要做

V47已保存13家P1及其中11家其他网站的公开案例。**已看到直达href，不等于已经确认当前原始rel**。此前V33/V34的6家原始rel也是历史抽样，不自动转成最新结果。用户真正需要区分真实免费收录、样本rel、nofollow/ugc/sponsored和自己网站是否获得链接。

另修复V35原Python验链代码的一处实质错误：原来只按空格拆分rel，可能把合法 `rel="nofollow,ugc"` 当没有限制。Google[官方说明](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)允许空格或逗号分隔。因此现在使用空格/逗号混合拆分，保留原始rel供复核。

## Windows PowerShell：只读批量核验（零付费API）

打开本仓库根目录，运行：

```powershell
py .\scripts\audit_p1_published_links.py
```

默认**最多只对已有的11个样本公开页分别请求一次**，另2家无具体页面标记为无可核验样本，不会虚构产品页面。脚本复用V35的HTTPS公开页面边界、2MB正文上限、跳转限制及30秒最大超时；单线程顺序请求、不提交、不登录、不搜索全站。运行后在本地生成 `p1-public-example-live-audit.csv`，并打印状态数量。

只想先检查三个页面：

```powershell
py .\scripts\audit_p1_published_links.py --max-requests 3 --output p1-sample-three.csv
```

只看将检查什么、不实际访问外网：

```powershell
py .\scripts\audit_p1_published_links.py --max-requests 0 --output p1-dry-run.csv
```

## 报表区分的三种证据

| 字段 | 严格含义 |
| --- | --- |
| `matched_href` | 本次原始HTML里发现与样本完整URL匹配的真实锚点，不是普通文本或只含域名的链接 |
| `live_raw_rel` | **本次**原始HTML的a标签rel，包含可能的逗号分隔nofollow/ugc/sponsored；没有则明确输出(none) |
| `historical_rel_not_current_proof` | V33/V34以前的历史rel，与本次新属性绝对分开；可能来自同平台不同详情页 |
| `status` | found_in_live_raw_html、not_found_in_fetched_raw_html、fetch_or_validation_error、no_verifiable_public_sample或not_scanned_limit，不能互相代替 |

**重要限制：**这11个案例都指向Fontique、Fontshare、AnyFyle等**别人的网站**，不是Generador获得的外链。脚本不会验证Google是否索引、DR/AS、站点自然流量、是否付费/编辑推荐或是否真的传递SEO权重。若对方只在JS运行后生成外链、阻止爬虫或网络失败，报告会保留不确定性而非猜测。不要绕过验证码或反爬。

## 正式用户获链怎么核

等站长亲自提交并拿到**真实公开产品页**后，仍用原有V35单页工具核对自己网站：

```powershell
py .\scripts\verify_published_backlink.py --source "https://平台的真实公开条目" --target "https://generadordelettering.org/" --output lettering-link-evidence.json
```

此处平台URL是**占位符**，不能复制后假称链接存在。离线操作台的提交状态、用户自己确认的href/rel与公开GitHub仓库正式台账均不自动修改。

## 回归测试

```powershell
py -m unittest discover -s scripts -p "test_verify_published_backlink.py" -v
py -m unittest discover -s scripts -p "test_audit_p1_published_links.py" -v
```

测试会使用假HTML与模拟请求，**不实际抓取网站**。新检查覆盖逗号分隔rel、跟踪查询参数、误导性相似域名、错误/超时、无样本、限量跳过、CSV公式注入及固定13来源数量。GitHub Actions之前仍有无runner步骤失败，不能因为写了单元测试就当作云端通过。

**当前仓库仍为176历史条目：P1=13、P2=27、条件=85、待核验=16、排除=34、非外链=1。真实用户新投稿0，确认获链0。**