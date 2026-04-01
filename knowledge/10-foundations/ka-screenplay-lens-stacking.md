---
{
  "id": "ka.screenplay-lens-stacking",
  "type": "knowledge_atom",
  "title": "剧本问题的多镜头拆解",
  "kind": "framework",
  "summary": "“如何创作剧本”这类宽问题不能被一个方法流派吃掉，而应拆成故事发动机、观众认知、媒介容器、开发流程、工业现实、历史边界等多个镜头。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "outline", "rewrite", "adaptation"],
  "problem": "把“如何创作剧本”错误压缩成单一结构模型、单一格式规则或单一审美路径，导致回答看似完整，实则漏掉真正改变下一步决策的层面。",
  "decision_rules": [
    "先把宽问题拆成故事引擎、观众理解、媒介容器、开发协作、工业环境和历史边界等镜头，再判断哪一层当前最关键。",
    "不要让某一种方法流派独占整个问题，只在它真正改变当下决策时才提升为主镜头。",
    "当多个镜头都成立时，优先返回主镜头加对比镜头，而不是假装只有一个正确答案。"
  ],
  "anti_patterns": [
    "用一个 beat sheet 回答全部编剧问题",
    "把格式习惯误当成创作本体",
    "在需要拆问题时过早给唯一结论"
  ],
  "prompt_primitives": [
    "当前真正卡住的是故事发动机、观众理解、媒介容器还是开发流程",
    "哪一个镜头如果不先处理，后续所有建议都会失真",
    "哪些镜头现在只需要做背景提示，不需要主导当前路线"
  ],
  "evaluation_checks": [
    "是否显式区分了多个有效镜头",
    "是否说清了当前主镜头为什么最重要",
    "是否避免把单一方法包装成普遍真理"
  ],
  "links": ["ka.audience-need-state", "ka.commissioning-fit", "ka.screenwriting-history-shift", "ka.script-as-coordination-artifact", "ka.viewer-inference-guidance", "ka.screenwriting-deliberate-practice"],
  "source_status": "curated"
}
---
# 剧本问题的多镜头拆解

很多关于编剧的争论，本质上都是因为大家在回答不同问题，却以为自己在回答同一个问题。

有人在说结构，有人在说观众理解，有人在说行业开发，有人在说媒介差异，有人在说作者表达。每个人讲的都可能有局部真值，但一旦把局部真值抬成“剧本就是这样写”，就开始失真。

这个原子的作用，就是提醒 Agent 和协作者：当问题宽到“如何创作剧本”这个级别时，先拆镜头比先给答案更重要。

如果当前其实卡在 audience promise，却直接套结构表；或者其实卡在 development artifact，却直接开始写场景；或者其实卡在媒介容器，却继续按 feature film 习惯给建议，最后都会让建议看起来专业、用起来失效。

## TODOs：待回答问题

- [ ] 这套镜头拆解是否还缺少 performance、sound design、editing anticipation 等更下游镜头？
- [ ] 不同 level 的用户是否需要不同默认镜头顺序，例如新手先从 engine 开始，职业用户先从 commissioning 开始？
- [ ] 哪些剧本问题最容易因为镜头错位而被误诊？
- [ ] 在实际运行里，系统应如何判断某个镜头只该做背景提示，而不该扩大为主路线？
