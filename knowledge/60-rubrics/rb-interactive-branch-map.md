---
{
  "id": "rb.interactive-branch-map",
  "type": "evaluation_rubric",
  "title": "Interactive Branch Map Rubric",
  "applies_to": ["interactive_branch_map"],
  "dimensions": [
    {"name": "choice_meaning", "question": "关键选择是否真正造成差异"},
    {"name": "state_tracking", "question": "状态与后果是否可追踪"},
    {"name": "convergence", "question": "结构是否具备合理收束"}
  ],
  "scoring_bands": {
    "excellent": "选择有意义、状态清楚、结构能扩展且可收束。",
    "workable": "基本成型，但部分选择差异或收束策略不够强。",
    "weak": "分支多而空，或者很快塌成伪选择。"
  },
  "hard_fail_rules": [
    "关键选择没有差异后果",
    "没有状态追踪逻辑",
    "完全没有收束计划"
  ],
  "rewrite_actions": [
    "减少无意义分支",
    "补状态变量和后果回显",
    "增加合流节点"
  ]
}
---
# Interactive Branch Map Rubric

用于判断互动分支设计是否既有意义又可持续。

互动项目里很容易出现“设计时觉得很丰富，落地时发现根本维护不了”的情况。这个 rubric 除了看选择有没有意义，也在看结构有没有控制力。分支如果只会增长，不会收束，后面基本一定出问题。

## TODOs：待回答问题

- [ ] 如果多个关键选择最终只改变关系、资源或文本语气，不改变主线节点，这种差异是否足以拿到 excellent？
- [ ] 状态追踪最少需要细到什么程度才不算“名义上有变量，实际上无后果”？
- [ ] 某些互动作品故意做开放型无收束结构时，“完全没有收束计划”是否仍然应 hard fail，还是要区分体验目标？
- [ ] 当制作预算不支持所有分支等量展开时，评分应如何处理“主干强、侧枝弱”的现实约束？
- [ ] 选择意义是应以作者设计意图评判，还是必须以玩家可感知差异评判，二者冲突时谁优先？
- [ ] 哪些 branch map 在纸面上成立，但一进入 UI、节奏、数值系统或存档逻辑就会崩溃，rubric 该如何提前暴露这种风险？
