---
{
  "id": "rb.subagent-dispatch-plan",
  "type": "evaluation_rubric",
  "title": "Subagent Dispatch Plan Rubric",
  "applies_to": ["subagent_dispatch_plan"],
  "dimensions": [
    {"name": "topology_fit", "question": "所选 dispatch topology 是否匹配媒介、风险结构、artifact chain 和 team mode"},
    {"name": "phase_clarity", "question": "phase ladder、lane 边界、merge 节点和 stop condition 是否清楚"},
    {"name": "packet_precision", "question": "handoff packet、truth packet 和共享字段是否明确且可操作"},
    {"name": "context_budget_control", "question": "不同 lane 的 context budget 是否有清楚上限与扩容触发"},
    {"name": "review_and_gate_design", "question": "review loop 与 human gates 是否放在真正该放的位置"},
    {"name": "collapse_and_fallback", "question": "是否说明何时裁剪 lanes、何时切换 topology、何时降级成更保守模式"}
  ],
  "scoring_bands": {
    "excellent": "调度结构贴题、阶段清楚、交接可执行、预算受控、审查位置合理，并且知道何时收缩与切换。",
    "workable": "能基本运行，但 merge、packet、gate 或 fallback 仍有模糊地带。",
    "weak": "更像抽象组织图，而不是可真正执行的调度计划。"
  },
  "hard_fail_rules": [
    "没有 merge owner 或 convergence owner",
    "所有 lanes 默认共享全部上下文",
    "并行 lanes 存在，但没有 handoff packet 或 stop condition",
    "高风险节点没有 human gate 或 review gate",
    "把 spec review 和 quality review 混成一层，导致错题也继续深化"
  ],
  "rewrite_actions": [
    "补写 topology 选择理由和备选 topology",
    "明确 phase ladder、merge 节点、handoff packet 和 stop rules",
    "为每个 lane 增加 context budget、扩容触发和 collapse trigger",
    "把 review loop 改写成 spec-first、quality-second 的两阶段结构"
  ]
}
---
# Subagent Dispatch Plan Rubric

好的调度计划，不只是“怎么多开几个 agent”，而是“怎么让系统在复杂情况下仍然不乱”。如果一份 `subagent_dispatch_plan` 看起来很酷，但没有 merge owner、没有 packet、没有 gate、没有 collapse 规则，那它只是并行幻想。

真正专业的调度，应该既能跑得快，也能在必要时收得回来。它要解释的不只是“怎么展开”，还要解释“怎么停”“怎么换模式”“怎么避免 context rot”。

## TODOs：待回答问题

- [ ] rubric 是否需要单独检查“persona lane 误伤主路由”的风险？
- [ ] 对 repo 研发型 dispatch，是否应该要求更强的 two-stage review 纪律？
- [ ] 哪些 topology 的 fallback 应该固定写进 matrix，而不是临时判断？
- [ ] human gate 过密与过稀各自的典型失败，是否值得沉淀成 fixture？
