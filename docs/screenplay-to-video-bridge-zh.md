# 剧本到视频衔接

这个仓库还是剧本优先，不是要变成一个视频生成工具仓。

但现实里，越来越多剧本工作会继续往下游走，进入：
- 概念样片；
- previz；
- AI 视频生成；
- 商业内容快速验证；
- 视觉 proof-of-concept。

所以问题不再只是“会不会写剧本”，而是“会不会把剧本安全地翻成下游视觉容器”。

## 最关键的边界

剧本和视频生成 brief 不是同一个容器。

剧本负责的是：
- 人物关系；
- 场景功能；
- 冲突推进；
- 情绪与叙事承诺。

视频衔接 brief 负责的是：
- 这一小段到底保哪一下动作；
- 镜头如何组织；
- 时长怎么压缩；
- 哪些不变量必须保住；
- 哪些要明确避免。

如果不分开，最容易出现两个极端：
- 把剧本压扁成镜头词堆，戏剧死掉；
- 把所有叙事说明都留在 brief 里，结果下游根本抓不住重点。

## 这层真正做什么

它做的是翻译，不是替代。

好的 `screen_to_video_brief` 会保住上游 scene 的戏剧任务，然后把它压缩成一个短时长、主动作清楚、主镜头逻辑明确、约束分层干净的可执行简报。它不会把自己伪装成剧本，也不会伪装成工具说明书。

## 相关资产

- `screen_to_video_brief`
- `ka.screenplay-to-video-boundary`
- `ka.video-generation-shot-economy`
- `ka.prompt-delegation-levels`
- `wp.screen-to-video-brief`
- `rb.screen-to-video-brief`

