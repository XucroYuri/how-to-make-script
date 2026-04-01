---
{
  "id": "rb.team-workflow-blueprint",
  "type": "evaluation_rubric",
  "title": "Team Workflow Blueprint Rubric",
  "applies_to": ["team_workflow_blueprint"],
  "dimensions": [
    {"name": "mode_fit", "question": "所选 team mode 是否匹配媒介、阶段、IP/商业压力和风险结构"},
    {"name": "role_clarity", "question": "角色分工、decision owner 和 merge owner 是否明确"},
    {"name": "handoff_precision", "question": "lane 之间的 handoff 和共享真相包是否足够清楚"},
    {"name": "checkpoint_design", "question": "人工关口是否放在真正高风险节点而不是泛化打断"},
    {"name": "pluralism_control", "question": "是否既保留 dissent 和 alternative，又有明确收敛机制"}
  ],
  "scoring_bands": {
    "excellent": "模式贴合、角色清楚、交接可执行、人工关口到位，并且能并行而不失控。",
    "workable": "能大致运行，但仍有角色模糊、gate 过泛或 merge 机制不足的问题。",
    "weak": "更像组织口号或角色清单，无法真正指导团队协作。"
  },
  "hard_fail_rules": [
    "没有明确的 decision owner 或 merge owner",
    "没有具体 handoff 机制却要求多 lane 并行",
    "人工 checkpoint 过泛，无法知道何时需要谁来拍板",
    "只给一种组织形态但没有解释为什么适配当前项目"
  ],
  "rewrite_actions": [
    "补写 team mode 选择理由和替代模式",
    "明确 roles、owner、lane 和共享真相包",
    "把 checkpoint 改写成具体 gate、权限和问题",
    "补充 dissent 保留和 convergence 机制"
  ]
}
---
# Team Workflow Blueprint Rubric

团队蓝图最怕“看起来很完整，实际上没法跑”。这份 rubric 不是在评组织想象力，而是在评这份 blueprint 到底能不能让一个真实团队或 agent team 少走弯路。

好的蓝图应该回答清楚：为什么是这个模式、谁拍板、怎么并行、怎么交接、哪里必须让人类回来。差的蓝图通常只是把许多好听角色放进一张图里，却没有真正的推进机制。

## TODOs：待回答问题

- [ ] rubric 是否需要按 writers' room、story trust、campaign strike team、interactive cell 拆成不同权重版本？
- [ ] 对极小团队或单人 + agent 的场景，`role_clarity` 该如何定义才不显得虚假繁复？
- [ ] 当 blueprint 故意保留多个备选模式时，rubric 如何区分“健康分歧”与“没有拍板能力”？
- [ ] 是否需要增加一项“现实资源匹配度”，避免蓝图过度理想化？
