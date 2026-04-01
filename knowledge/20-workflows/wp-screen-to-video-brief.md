---
{
  "id": "wp.screen-to-video-brief",
  "type": "workflow_protocol",
  "title": "剧本到视频生成桥接协议",
  "goal": "把 scene、广告段落或适配片段桥接成 screen_to_video_brief，在不丢失戏剧意图的前提下，为 Sora、Seedance 或通用视频生成链路提供更可执行的视觉 brief。",
  "input_contract": ["scene draft or scene card", "target runtime", "prompt runtime or platform", "visual target", "invariants and hard boundaries", "source excerpt or source spans"],
  "output_contract": ["screen_to_video_brief"],
  "preconditions": [
    "已知要桥接的场景或片段",
    "已知目标时长、clip 粒度或至少知道需要单 clip 还是 clip chain",
    "知道当前是 previz、概念验证、广告样片，还是 downstream generation brief"
  ],
  "steps": [
    "抽取当前片段的戏剧任务、关系压力和不能丢的动作证明。",
    "尽可能保留 source span 或证据单元，让下游知道每条桥接判断来自哪段上游文本。",
    "判断当前更适合单 clip brief 还是 clip chain，并限制每个 clip 的主动作和主镜头逻辑。",
    "如果文本很长，先识别 scene / beat 边界，再决定批处理和 clip chain 组织，而不是先机械切块。",
    "区分可见人物、画外音人物、可见道具和仅在语义层存在的信息。",
    "按需要引入 visual language pack 中的术语，但只保留会改变执行的词。",
    "写出 scene residue 与 video constraints 的分层：主体、动作、镜头、灯光、音频、文字、避免项、不变量。",
    "如果涉及特定 runtime，如 Sora 或 Seedance，补模型相关的时长、连续性和控制粒度提醒，但不要退化成 CLI 教程。"
  ],
  "fallbacks": [
    "若用户真正需要的是 screenplay 本身，切回原主路由，只把 bridge 当附加说明。",
    "若用户只是缺语言词汇，不急着进入视频桥接，切到 visual-language-pack。",
    "若片段过大、动作过密，先拆 clip chain，再分别桥接。"
  ],
  "stop_conditions": [
    "brief 已保住上游场景的戏剧功能",
    "每个 clip 都只有清楚的主动作和主镜头逻辑",
    "输出没有把 screenplay、shot list 和 runtime manual 混成一份文件"
  ],
  "rubrics": ["rb.screen-to-video-brief"],
  "linked_atoms": ["ka.screenplay-to-video-boundary", "ka.video-generation-shot-economy", "ka.prompt-delegation-levels", "ka.multilingual-visual-vocabulary", "ka.source-span-traceability", "ka.long-script-batch-planning", "ka.visible-asset-grounding"]
}
---
# 剧本到视频生成桥接协议

这个协议不是让仓库去抢视频生成工具仓的活，而是解决一个越来越现实的问题：剧本 Agent 已经不只在写文本，它还要把文本交给一条更短、更脆弱、更依赖视觉约束的生成链路。

最难的地方不是“会不会写 prompt”，而是会不会翻译。好的桥接，会把 scene 里的关系压力、动作证明和视觉中心提取出来，再重新装进短时长可执行容器。差的桥接，则会把整段剧本压成一长串镜头词，或者把生成 brief 写得像技术手册。
现在这个协议还补了一层更严格的要求：桥接应尽量可追溯。也就是，关键执行判断最好能回指上游文本证据，而不是让 brief 漂成另一个故事。

所以 `screen_to_video_brief` 的核心任务，是把剧本保留在剧本那边，把生成约束保留在生成约束这边，中间只建立最小而有效的桥。

## TODOs：待回答问题

- [ ] `screen_to_video_brief` 是否需要继续区分 Sora / Seedance / 通用 T2V 三种子变体？
- [ ] 当一个项目明确要做 series of clips，而不是单一 clip 时，仓库是否应该新增 `clip_chain_blueprint`？
- [ ] 若用户要给真人拍摄团队和模型团队同时交付，是否需要双层输出而不是单份 bridge？
- [ ] 当商业广告要求强文案、强字幕、强卖点证明时，桥接协议应该如何避免画面与文字抢主次？
