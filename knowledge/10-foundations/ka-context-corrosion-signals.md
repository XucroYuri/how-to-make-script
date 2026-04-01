---
{
  "id": "ka.context-corrosion-signals",
  "type": "knowledge_atom",
  "title": "上下文腐化信号",
  "kind": "failure_mode",
  "summary": "上下文腐化不是 token 变多本身，而是上下文增量开始削弱 route 清晰度、判断一致性和生成聚焦度。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "Agent 通常在已经开始被上下文拖垮时，还以为自己只是‘参考更充分了’，结果产物变得更散、更慢、更像总结报告而不是有效创作。 ",
  "decision_rules": [
    "如果新增上下文没有改变下一步动作，却让回答更像摘要而不是决策，视为腐化信号。",
    "如果 route 在无新证据的前提下反复摇摆，先缩上下文，再重新锁定 primary route。",
    "如果回答开始混入不必要的媒介、阶段或工业条件，说明 bundle 已经失焦。"
  ],
  "anti_patterns": [
    "把 summary drift 误判为 thoroughness",
    "为了显得全面不断引入新维度",
    "一旦加载过多内容就不愿意减载"
  ],
  "prompt_primitives": [
    "新增内容是否真的改变了下一步决策",
    "当前回答是在解题还是在总结仓库",
    "现在最应该删掉哪一类上下文"
  ],
  "evaluation_checks": [
    "route 是否仍然稳定",
    "回答是否仍围绕用户请求的最小问题",
    "是否出现无必要的跨媒介或跨阶段混入"
  ],
  "links": ["ka.bounded-context-loading", "ka.reference-expansion-balance", "ka.scope-correction"],
  "source_status": "derived"
}
---
# 上下文腐化信号

上下文腐化最危险的地方，在于它一开始很像“更全面了”。Agent 会引用更多理论、更多案例、更多比较，看起来很努力，但用户真正想要的那个问题反而越来越模糊。

一个很强的腐化信号是：回答开始从“帮我做这个创作决定”滑向“给你总结一下仓库里都有什么”。另一个信号是 route 摇摆。明明没有新证据，却不断在不同媒介、不同 protocol、不同参考包之间来回跳。

高水平 Agent 必须具备减载能力。能加很重要，能停更重要，能删更重要。

## TODOs：待回答问题

- [ ] 哪些用户请求最容易让 Agent 误入 summary drift？
- [ ] 是否应该在协议层加入显式的减载动作？
- [ ] 哪些 signal 最适合自动触发“回到 core bundle”？
- [ ] 如何把上下文腐化和真正需要的 broadened comparison 区分开？
- [ ] 是否需要单独的 fixture 来回归测试 route 摇摆问题？
