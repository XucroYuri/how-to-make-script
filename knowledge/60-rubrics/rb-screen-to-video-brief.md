---
{
  "id": "rb.screen-to-video-brief",
  "type": "evaluation_rubric",
  "title": "Screen To Video Brief Rubric",
  "applies_to": ["screen_to_video_brief", "commercial_script", "scene_draft"],
  "dimensions": [
    {"name": "dramatic_fidelity", "question": "桥接后是否仍保住了原场景的戏剧任务和关系压力"},
    {"name": "clip_economy", "question": "每个 clip 是否只有明确的主动作和主镜头逻辑"},
    {"name": "constraint_clarity", "question": "不变量、避免项、时长和执行边界是否清楚分层"},
    {"name": "container_honesty", "question": "输出是否诚实地区分了 screenplay residue 与 video-generation constraints"},
    {"name": "source_traceability", "question": "关键执行判断是否仍能回指上游文本证据"},
    {"name": "chain_continuity", "question": "如果拆成 clip chain，跨 clip 的连续性和分工是否清楚"}
  ],
  "scoring_bands": {
    "excellent": "既保住原场景核心，又把生成约束压缩得清楚、干净、可执行，没有容器混乱。",
    "workable": "大方向可用，但仍有动作过密、容器混写或约束不够清楚的问题。",
    "weak": "不是剧本就是提示词垃圾堆；要么戏剧丢失，要么执行完全失焦。"
  },
  "hard_fail_rules": [
    "整段剧本几乎原样复制进 brief",
    "一个 clip 同时承载多个主动作或多个互相竞争的镜头逻辑",
    "没有写清不变量、避免项或时长边界",
    "把工具运行细节写成了主要内容，反而没有保住上游戏剧目的",
    "关键桥接判断无法说明来自哪段上游文本",
    "clip chain 已被拆开，但连续性和职责分工不清"
  ],
  "rewrite_actions": [
    "重新抽取场景的戏剧任务和最小动作证明",
    "把过密的片段拆成 clip chain 或删减主意图",
    "把 invariants、avoid、audio、text 等层单独列出，减少正文拥堵",
    "删除与当前执行无关的工具说明和 screenplay 残留解释",
    "为关键桥接说明补 source span 或证据锚点",
    "明确 clip chain 的跨段连续性说明与每段职责"
  ]
}
---
# Screen To Video Brief Rubric

`screen_to_video_brief` 最容易失败在两个极端：一个是太像剧本，一个是太像堆词的提示词清单。

好的 bridge 会让你看得出原 scene 的戏剧作用，也看得出这份 brief 为什么更适合进入视频生成或 previz 链路。
现在这套 rubric 还要求它尽量可追溯。否则一旦下游执行偏掉，就很难知道偏差是来自上游、来自桥接裁决，还是来自执行层。

## TODOs：待回答问题

- [ ] 当 bridge 明确是给真人拍摄前的 previz 用，而不是给生成模型用，`clip_economy` 权重是否需要调整？
- [ ] 商业广告与叙事情绪戏在 `dramatic_fidelity` 的判断上，是否需要不同的基准？
- [ ] 对长场景拆链后，这份 rubric 是否需要新增“chain continuity”维度？
