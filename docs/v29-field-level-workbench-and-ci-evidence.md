# V29｜176渠道操作台：21家精确表单、站点进度隔离与CI故障取证

更新时间：2026-10-31。目标仓库：`chenmu2024/xibanyayuwailian`。**本轮仍为176条历史候选，不是176条已获反向链接。** 没有向外部目录发送表单、没有发送邮件、没有修改外链实际提交台账。

## 一、用户最明显的改进

`docs/backlink-submission-workbench.html` 现在把此前单独存于 `docs/lettering-priority-21-ready-to-fill.md` 的21家平台完整表单字段也嵌入其中。**21家共133个字段行**，逐站展示平台当前历史研究记录的真实字段名、Generador de Lettering对应示例值与独立复制控件；另外155家仍有逐步历史说明。

- 例如 `Herramientas y Recursos #168` 显示 `Nombre o título`、`Tipo`、`Tema principal`、`Público objetivo`、`URL del sitio`、类别、真实Logo、长短西语介绍和实际通知邮箱字段。
- `EpicTools #172` 保持官网只见到 `Website URL` 和 `Category` 两个主要字段，不虚构邮箱或企业地址。
- `PeplioHUB #149` 明确要求真实的≥1200×675横图，且免费推荐页不保证Follow。
- `NoSignupTools #148` 的免费、免登录和真实广告体验门槛继续保留。
- 非适用平台、关停入口、Badge强制反链、教育内容版权/授权等依旧保留，不能因为有一键复制就跳过。

每条表单字段与表述仍是 **2026-10-31以前的研究快照**。不能声称今日重新核对了所有176家官网或独立验证DR/AS/rel/Google实际索引。

## 二、跨网站隔离，防止误导提交记录

V28操作台的本地进度共用一个浏览器存储Key；在用户更换目标网站后容易把旧项目的“已自行提交”错误带到新项目。本次改为 `xibanya-marks-by-domain-v29`，按实际填写的目标主页根主机名独立保存进度。

- `generadordelettering.org`、`conversordeletrasbonitas.org` 等分别维护本机状态。
- 原V28进度在本机有保存且新V29存储为空时，**只迁移到Generador de Lettering域名**；绝不默认将旧状态复制到其他站点。
- 更换网站首页后，离开输入框会刷新当前平台的本地进度与资料卡；已标注条数明确是 **本地手工工作状态，非已获链条数**。
- 新站域名或站名不同于Generador时，字体/Lettering相关的历史文案和标签不能直接复用，操作台会展示需重新描述实际功能的提示，并禁用该样例的复制按钮。
- 原来不加区别拼接 `/herramientas/plantillas-practica` 的教学URL修正为：仅Generador使用其真实练习页；其他站点需明确提供真实教学内容URL。
- 数据仍在浏览器localStorage；导出CSV仅下载至本机，**不会更新GitHub的`data/submission-ledger.csv`**。

## 三、代码与数据验证

- Python历史主表校验：`python3 scripts/validate_csv.py`（V27程序保留、不削弱）。
- Node零依赖HTML校验：`node scripts/validate_workbench.mjs`。设计为检查176条数据连续编号、21个有字段的独立平台、共133行字段、JS语法、无外部脚本/网络请求和进度域名隔离。
- GitHub Actions定义：`.github/workflows/validate-data.yml`，当GitHub Actions的Runner工作正常时执行上述两个步骤。
- 已通过GitHub文件读取结果核对HTML嵌入176条渠道、21家字段资料和域名隔离修复；**尚未运行完整真实浏览器手动点击验收**，不能宣称界面所有路径都实测。

## 四、CI失败的实际证据（重要）

连续若干次GitHub Actions失败，且历史原版Python校验脚本和工作流回退后仍出现失败。用于区分故障所在的实验：

1. `41145795864`：V27历史基线校验**曾成功**，证明此前流程存在可正常通过的版本。
2. `41147393231`：另加完全不需要GitHub checkout、不读取任何项目文件的最小`runner-probe`作业，结果**probe和常规validate都失败**。
3. `41147426029`：将Runner从 `ubuntu-latest` 固定为 `ubuntu-24.04`，两项依然失败。
4. `41147501834`：恢复常规单作业校验并增加Node检查，仍失败。
5. GitHub连接器尝试获取Job logs时返回BlobNotFound，未能取得具体日志；在runner-probe失败的工作流中亦没有可下载的诊断产物。

**因此，本轮不能把失败直接断言为Python语法错误或页面代码错误，也无法证明是GitHub计费、权限、Runner服务故障中的哪一项。** 最小无checkout程序也失败，表明故障至少可能出现在测试脚本执行前的Runner启动/账户/服务层。仓库现保留正常且不跳过失败的校验逻辑；没有伪造成功报告。

如需要定位，请在 GitHub 网页登录对应账户，打开 Actions → 失败的workflow run → `runner-probe`/validate Job 的 Setup job 及错误标注，查看是否有系统明确的Runner分配、账户计费/配额、权限或基础服务提示。问题排除后重新运行 `python3 scripts/validate_csv.py`、`node scripts/validate_workbench.mjs` 和 GitHub CI，取得绿色结果再更新README状态。

## 五、下一步的正常使用

按 [离线操作台使用指南](workbench-quickstart-v28.md) 下载HTML到Windows Chrome，以21家优先来源作为研究顺序。每个真实官网表单完成后本机记一次，务必另核实审核邮件、实际公开链接和正确rel，再将经证明的结果写入正式GitHub台账。**不要根据本机进度自动报告成功外链。**
