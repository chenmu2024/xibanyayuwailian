# GitHub Actions持续失败：启动前诊断证据（2026-10-31）

仓库：[xibanyayuwailian](https://github.com/chenmu2024/xibanyayuwailian)，工作流：`.github/workflows/validate-data.yml`。

## API已读出的客观状态

- [运行41160234903](https://github.com/chenmu2024/xibanyayuwailian/actions/runs/41160234903)：push触发、completed/failure，开始2026-10-31T02:29:30Z，约3秒后结束。
- 仅一个`validate` job：`id=124415981348`，`status=completed`、`conclusion=failure`；`steps=null`、`logs_url=null`，没有分配可识别的runner。
- 运行timing接口显示`billable.UBUNTU.total_ms=0`，该job持续0ms；job日志下载产生404 BlobNotFound。没有`Set up job`、checkout、Python/Node测试的任何可用执行日志。
- 既然缺少步骤与日志，就**不能证明校验脚本执行失败**；运行前置阶段异常的确切根因**未知**，尤其不能单凭0ms推断一定是Billing、Runner、权限或工作流语法。

## 实际下一步（不自动产生费用）

1. 用户打开[Actions运行41160234903](https://github.com/chenmu2024/xibanyayuwailian/actions/runs/41160234903)，先查看运行页顶部/validate工作块是否有明确红色**系统错误说明**；如有，保存完整原文。
2. 在仓库`Settings → Actions → General`检查Actions允许运行的设置，是否限制GitHub托管runner；只读检查，不先修改付费配置。
3. 在GitHub账号的`Settings → Billing and licensing`检查Actions使用/额度/预算/付款错误提示。用户坚持免费方案；**无需自动开支预算或绑定银行卡**。可参考[GitHub官方排错说明](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows)。
4. 在本地零费用临时运行：`python3 scripts/validate_csv.py`、`node scripts/validate_workbench.mjs`、`node scripts/smoke_workbench.mjs`、`python3 -m unittest discover -s scripts -p test_verify_published_backlink.py -v`。即使本地全过，也**不能声称Actions已绿**。
5. 只有新一次Actions运行出现正常Set up job、Checkout、测试步骤，并且最终conclusion=success，才标记CI故障修复。GitHub前置系统错误若持续则需将run URL和证据发给GitHub支持。

请避免在没有新诊断信息时反复修改有效测试代码，造成更多失败工作流记录。
