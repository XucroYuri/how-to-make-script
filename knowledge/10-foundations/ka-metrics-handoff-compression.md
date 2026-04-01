---
{
  "id": "ka.metrics-handoff-compression",
  "type": "knowledge_atom",
  "title": "质检 metrics 压缩交接",
  "kind": "workflow_rule",
  "summary": "多镜头质检中的跨层传递应以 metrics、flags 和 scope notes 为主，而不是 findings 原文堆叠，这样才能兼顾信息保留与上下文卫生。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "如果每个 lens 都把 findings 全文传给下游，最终上下文会迅速膨胀，质检层会从多角度诊断退化成‘谁先说了什么谁就赢’的串行污染。",
  "decision_rules": [
    "跨 lens 默认只传 counts、severity ratios、hard-fail flags、changed ranges、open contradictions 和 confidence notes。",
    "metrics 只保留能改变下一个 lens 判断的内容，不保留细节修辞。",
    "当 artifact 很小或只做 targeted audit 时，允许不传任何上游 metrics。"
  ],
  "anti_patterns": [
    "把 findings 原文当成 metrics",
    "为了‘信息完整’把整份报告继续向下传",
    "传了一堆数，但没有说明 scope 和 confidence"
  ],
  "prompt_primitives": [
    "哪些 summary 能改变下一个 lens 的判断",
    "哪些信息应压成 flag，而不是保留长描述",
    "这次 handoff 是否其实可以为空"
  ],
  "evaluation_checks": [
    "metrics 是否足够短且足够有用",
    "scope 和 confidence 是否被一起保留",
    "交接是否真的减少了上下文腐化"
  ],
  "links": ["ka.review-lens-isolation", "ka.handoff-packet-discipline", "ka.subagent-context-budgeting"],
  "source_status": "synthesized"
}
---
# 质检 metrics 压缩交接

通用质检不是不能传信息，而是不能乱传信息。好的做法不是“完全隔绝一切上游”，而是只传会改变下一步判断的压缩信息。

例如，对后续 `operational_feasibility` lens 来说，也许只需要知道：前一个 lens 发现了 2 个 hard fail、风险高度集中在第 3 场和第 5 场、voice 漂移属于中风险、且当前判断置信度中等。它不需要把前面的整份文字点评一并吞下去。

这层压缩交接，既继承了 packet discipline，也是在质检链里防 context corrosion 的关键手段。

## TODOs：待回答问题

- [ ] 是否需要为不同 lens 定义不同的默认 metrics 字段集？
- [ ] 哪些场景里 count 比 ratio 更重要，哪些场景相反？
- [ ] recheck 时是否需要单独的 diff metrics，而不是重复初检 metrics？
