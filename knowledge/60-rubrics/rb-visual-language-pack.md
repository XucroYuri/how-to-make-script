---
{
  "id": "rb.visual-language-pack",
  "type": "evaluation_rubric",
  "title": "Visual Language Pack Rubric",
  "applies_to": ["visual_language_pack", "screen_to_video_brief", "scene_draft"],
  "dimensions": [
    {"name": "task_fit", "question": "这份语言包是否服务于明确任务，而不是泛泛展示多语种词汇"},
    {"name": "term_selectivity", "question": "是否只选了会改变当前镜头和表达决策的术语"},
    {"name": "cultural_fidelity", "question": "文化美学锚点是否被正确落到可执行决策，而不是标签化装饰"},
    {"name": "misread_control", "question": "是否写明了 hybrid 使用方式、误读风险或禁忌点"},
    {"name": "bridge_readiness", "question": "若此包服务 bridge 或 previz handoff，是否说明了哪些词负责精度、哪些词负责气质锚定"}
  ],
  "scoring_bands": {
    "excellent": "任务目标清楚，术语精简而准，文化锚点可执行，且明确说明了误用风险。",
    "workable": "大方向可用，但词类仍偏多、任务指向不够聚焦，或文化词与执行层连接不够稳。",
    "weak": "像词典摘录或风格秀，既不选词，也不解释为什么这些词对当前任务有用。"
  },
  "hard_fail_rules": [
    "把多语种词汇包写成大而全词典，没有任务筛选",
    "使用文化概念却没有说明它如何改变镜头、节奏或质感",
    "混用多种术语体系但没有说明哪一层负责技术精度、哪一层负责气质锚定",
    "输出中没有任何误读或误用警报"
  ],
  "rewrite_actions": [
    "重新锁定当前语言包服务的任务类型和接收方",
    "删掉不会改变当前结果的词类，只保留高影响词",
    "把抽象文化词改写成镜头、构图、灯光、节奏或动作层面的具体约束",
    "补充 hybrid 规则、禁忌词和误读风险",
    "如果它会进入 bridge 层，明确精度词和气质锚词的分工"
  ]
}
---
# Visual Language Pack Rubric

这份 rubric 判断的不是“会不会多语种”，而是这份多语种包有没有真的帮助下游少走弯路。

好的 `visual_language_pack` 会显著降低歧义。差的则只是把问题翻译成另一种语言继续模糊。
当它继续服务 bridge 或 previz handoff 时，还要额外防止一种错：所有术语都很好听，但没人知道哪个词在管精度，哪个词只是在管气质。

## TODOs：待回答问题

- [ ] 不同语种之间是否需要不同的评分偏重，例如中文偏信息密度、日语偏美学锚点、韩语偏流行影视节奏？
- [ ] 当语言包只服务人类协作、并不服务模型时，`misread_control` 的定义是否需要调整？
- [ ] 是否应给文化美学词单独加入“刻板化风险”维度，避免它们被过度消费？
