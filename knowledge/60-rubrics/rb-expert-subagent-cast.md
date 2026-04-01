---
{
  "id": "rb.expert-subagent-cast",
  "type": "evaluation_rubric",
  "title": "Expert Subagent Cast Rubric",
  "applies_to": ["expert_subagent_cast"],
  "dimensions": [
    {"name": "coverage_fit", "question": "阵容是否真正覆盖了当前任务的核心创作与流程压力"},
    {"name": "role_differentiation", "question": "功能型角色、流程节点和 persona lens 是否被清楚区分"},
    {"name": "authority_clarity", "question": "谁拥有 merge / veto / review / human gate authority 是否明确"},
    {"name": "persona_governance", "question": "参考 persona 是否说明了 allowed use、blocked use、loading cap 和 non-dogma note"},
    {"name": "cast_economy", "question": "阵容是否保持克制，并给出扩容与裁剪规则"},
    {"name": "context_discipline", "question": "每个 subagent 是否有清楚的上下文预算和 handoff 方式"}
  ],
  "scoring_bands": {
    "excellent": "阵容既专业又克制，角色差异清楚，persona 使用受控，authority 与 budget 都明确，可直接进入部署讨论。",
    "workable": "基本可用，但仍有角色重叠、persona 过泛、authority 模糊或裁剪逻辑不足的问题。",
    "weak": "更像角色愿望清单或名家拼盘，无法真正指导 subagent 选型。"
  },
  "hard_fail_rules": [
    "没有 convergence owner 或 human-owned node",
    "reference persona 被写成直接 impersonation 或精确模仿名人",
    "多个 subagent 职责高度重叠却没有 trim order",
    "默认所有 subagent 共享全量上下文",
    "阵容没有 process-node，只剩 craft specialist 互相堆叠"
  ],
  "rewrite_actions": [
    "删减重叠角色，改写为最小可运行 cast",
    "补写 authority、merge owner、human gate 和 trim order",
    "把 persona 改成治理过的 craft lens，而不是模仿目标",
    "为每个 subagent 增加 mandate、context budget 和 deactivate 条件"
  ]
}
---
# Expert Subagent Cast Rubric

一份好的 `expert_subagent_cast`，不是让人看着觉得“阵容豪华”，而是让人清楚知道：这套阵容为什么值得存在、为什么不会互相打架、为什么不会把系统拖回上下文噪音。

它最怕两种失败：一种是“只有创作专家，没有流程纪律”；另一种是“只有名家气质，没有真实职责”。前者会失控，后者会变成漂亮但空的 cosplay。

## TODOs：待回答问题

- [ ] rubric 是否应按 medium 或 team mode 提供不同权重版本？
- [ ] cast_economy 是否需要和 token / latency 成本显式挂钩？
- [ ] 当阵容故意保留互相冲突的 persona lens 时，rubric 如何区分健康 tension 与无效内耗？
- [ ] 是否应该单独检查“review node 是否过早进入 ideation”？
