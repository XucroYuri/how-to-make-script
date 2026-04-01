---
{
  "id": "ka.source-span-traceability",
  "type": "knowledge_atom",
  "title": "源片段可追溯性",
  "kind": "heuristic",
  "summary": "当剧本要桥接到 shot、clip 或 storyboard 级容器时，最好保留能回指原始文本的 source span 或证据单元，避免下游逐步漂移成另一个故事。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video"],
  "stages": ["scene", "rewrite", "adaptation"],
  "problem": "桥接层在一轮轮转写中不断损失上游证据，最后只剩看似专业的执行语言，却已经偏离原场景意图。",
  "decision_rules": [
    "能保 source span 的地方尽量保，不要全靠摘要二次解释。",
    "下游容器改变上下文窗口，但不应该改变上游事实归属。",
    "如果某条执行说明无法说明它来自哪段剧本证据，就要警惕它可能是漂移产物。"
  ],
  "anti_patterns": [
    "桥接文件只剩重写后的总结，没有上游证据锚点",
    "多个 clip 都声称代表原场景，但谁对应哪段原文完全不清楚",
    "执行层不断补细节，最后和原戏剧任务脱钩"
  ],
  "prompt_primitives": [
    "这条桥接说明对应原场景的哪段证据",
    "如果移除这条说明，原文里是否还有依据支撑它",
    "哪些内容是上游事实，哪些只是下游执行裁决"
  ],
  "evaluation_checks": [
    "关键执行信息是否能回指上游片段",
    "桥接后是否还能辨认原场景功能",
    "摘要和裁决是否没有偷换原文事实"
  ],
  "links": ["ka.screenplay-to-video-boundary", "ka.video-generation-shot-economy", "ka.source-of-truth-runtime-split"],
  "source_status": "derived"
}
---
# 源片段可追溯性

桥接层最容易犯的错，是把“翻译”做成了“改写”，而且改着改着就不再承认自己改过。

只要下游 brief、shot unit 或 storyboard unit 还能清楚回指上游哪段剧本证据，漂移就可被发现、可被争论、可被修正。反过来，一旦所有信息都只剩二手总结，下游很快就会拥有一个看似顺畅、实际已偏题的新故事。

所以可追溯性不是官僚步骤，而是防止桥接层偷换戏剧任务的基本保险。

## TODOs：待回答问题

- [ ] source span 该精确到句子、动作单元还是 beat 单元，才最实用？
- [ ] 人类团队 handoff 和模型执行 handoff 对可追溯性的精度要求是否应不同？
- [ ] 当原剧本本身含混、跳接或依赖导演处理时，可追溯性该如何保持诚实？
