# V36｜多网站独立外链资料：彻底隔离名称、简介、邮箱及编辑器URL

更新日期：2026-10-31。仓库仍为176个历史候选、21家详细操作卡（161项字段）。**本版本没有新增申请、没有取得新的真实外链。**

## 1. 之前的真实问题

V35之前，操作台虽然按目标域名保存每个渠道的“未处理/审核中”进度与验链证据，但网站资料（`name`、`home`、`tool`、西语及英语短/长描述、联系邮箱）只有一套全局`localStorage`记录。

当你从`generadordelettering.org`切到另一西语站时，旧网站的**名称、宣传内容或Email可能留在新站输入框中**。尽管大部分字段有V30“不可跨站自动填充”的保护，这仍然是潜在的错投/隐私风险。

## 2. V36已更改的行为

- 每个目标网站域名都保存一份**独立的网站资料**，使用浏览器本地键`xibanya-profiles-by-domain-v36`；原有`xibanya-marks-by-domain-v29`进度与证据键保持不变，不删除老记录。
- 第一次切到新域名：默认只保留用户刚输入的该站主页，其余**站名、编辑器地址、西语短文/长文、英语短文/长文、邮箱全部留空**，等待你填写真实内容；绝不借用Lettering示例文本或上一个站点的Email。
- 切回已经编辑过的网站：自动恢复该站原本的全部字段，独立恢复其对应176条渠道进度及人工验链证据。
- 修改**同一域名**的主页路径、HTTPS URL时保留当前网站的字段。只有主页域名发生变动时才切换网站资料；非法/不完整网址会提示修改。
- 仍然是**离线HTML**，无外部JS、无收费API、无后台存储。更换浏览器、清空浏览器站点数据或换电脑不会自动云同步，必须自己备份。

## 3. V2 JSON备份：可完整保存多个网站

以前的V1备份只保存**当前一家网站的资料**，虽然包含各域名的历史进度，却不能恢复其他网站的名称、简介和邮箱。

V36升级至`spanish-backlink-offline-backup` **`version:2`**：

```json
{
  "type": "spanish-backlink-offline-backup",
  "version": 2,
  "profile": {
    "name": "当前真实站名",
    "home": "https://one-site.example.org/",
    "tool": "https://one-site.example.org/editor",
    "es": "真实西语短文",
    "en": "English short description",
    "eslong": "真实西语长文",
    "enlong": "English long description",
    "email": ""
  },
  "profiles": {
    "one-site.example.org": {
      "name": "当前真实站名",
      "home": "https://one-site.example.org/",
      "tool": "https://one-site.example.org/editor",
      "es": "真实西语短文",
      "en": "English short description",
      "eslong": "真实西语长文",
      "enlong": "English long description",
      "email": ""
    }
  },
  "progress": {
    "one-site.example.org": {}
  }
}
```

上方仅展示格式，**不是用户真实站点或实际获链**。真实备份还包含`exportedAt`以及该浏览器已保存的其他网站资料与状态。

- **V2导出**：点击“备份所有网站JSON”，一次保留全部网站资料、渠道进度、备注、V35人工href/rel自查证据。
- **V1兼容导入**：旧格式仍支持；可恢复**旧V1保存的当前网站资料**和所有网站历史进度。但V1从未包含其他网站的资料，所以无法凭空恢复以前未备份的邮箱/简介；请重新填写这些网站资料。
- **V2导入**：要求每个`profiles[domain]`的主页实际属于该域名；编辑器链接不得跳到另一个站；资料字段必须是有限长度的字符串；最多200个网站。跨域字段造假、缺少活动网站资料的备份会拒绝恢复，原有数据不被覆盖。
- **隐私**：备份可能含联系人邮箱、评论和个人上传的验链证据。不要把完整个人备份提交到公开GitHub仓库。

## 4. Windows Chrome最简单的操作

1. 下载 [V36离线操作台HTML](backlink-submission-workbench.html)，打开它。
2. 保持`generadordelettering.org`时，查看原先的主页、编辑器和西语/英文介绍。
3. 将顶部`home`改为另一独立网站的`https://`完整URL，按Tab或点击页面空白，使“change”事件生效。新域名应出现**空白的站名、简介、邮箱和编辑器**。
4. 为新站补充真实网站材料；打开任何外链平台都只引用这个站的数据，不能复制Lettering特定的声明。
5. 将`home`改回`https://generadordelettering.org/`并离开输入框，旧站的站名、编辑器、简介和渠道进度应恢复；再切到第二站，它的材料也会恢复。
6. 点击“备份所有网站JSON”。文件中应有`version:2`和`profiles`字段。更换电脑时用“恢复进度备份”导入。

## 5. 验收与限制

- 独立V8环境中重新执行了**176条主库一致性**、21家161项字段、V33/V34公开href样本、HTML语法校验与**23项离线DOM交互模拟**，均通过。
- 新增测试覆盖：新站不继承Lettering的名称、长短描述和邮箱；旧站切回恢复原始编辑器；第二站的URL/Email独立持久化；V2完整备份与跨域资料篡改拒绝；V1旧备份迁移；V35外链证据及CSV导出仍可用。
- **并未在真实Windows Chrome浏览器执行端到端测试**，因此应如上手工核对。
- GitHub Actions仍然报告失败；最近job执行步骤列表为空，日志下载404 BlobNotFound，**根因没有被确认**，不能随意归因于代码或Runner。Python独立8项单元测试尚缺真实Python解释器执行记录，不得宣传已经通过。

## 6. 资料路径

- [V36操作台](backlink-submission-workbench.html)
- [V35公开href/rel证据自查说明](v35-evidence-based-backlink-verification.md)
- [176历史渠道主库](../data/backlinks-master.csv)
- [21家具体填写卡](lettering-priority-21-ready-to-fill.md)
- [验证脚本](../scripts/validate_workbench.mjs)与[DOM回归测试](../scripts/smoke_workbench.mjs)

**V36结果：真实获链新增0条、实际第三方申请0条。**

## V45补充：专门的教育页面字段

操作台在每个网站资料里新增可选的`edu`：只填已有公开教学资源的**本域HTTPS页面**。跨域链接会被拒绝，教育目录不会再套用普通编辑器路径。

**兼容性**：原localStorage资料及进度键未更换，JSON备份版本继续为2。旧V1和V2备份没有`edu`时，会自动按空值恢复；用户需要时再填。新V2备份保留各网站自己的`edu`值，不会自动复制到另一个站点。[V45说明](v45-education-url-backward-compatible-20261031.md)。
