---
{
  "id": "rb.development-brief",
  "type": "evaluation_rubric",
  "title": "Development Brief Rubric",
  "applies_to": ["development_brief"],
  "dimensions": [
    {"name": "context_clarity", "question": "是否明确委制主体、业务目标和分发窗口"},
    {"name": "creative_priorities", "question": "是否区分必须先锁定的决策与可延后探索的部分"},
    {"name": "industry_realism", "question": "是否考虑平台、交付、预算或生产逻辑，而不是只谈创作喜好"},
    {"name": "sequence", "question": "下一步开发顺序是否清楚、可执行"}
  ],
  "scoring_bands": {
    "excellent": "brief 能同时服务创作与开发决策，优先级明确，风险和下一步动作清楚。",
    "workable": "能指出方向，但仍有部分现实约束或开发顺序表达不够具体。",
    "weak": "更像概念阐述或泛泛建议，无法真正指导项目推进。"
  },
  "hard_fail_rules": [
    "没有说明项目当前所处的委制或开发语境",
    "没有明确首要目标与优先级",
    "没有具体下一步交付或验证动作"
  ],
  "rewrite_actions": [
    "补写委制主体、窗口和业务目标",
    "把建议拆成必须先锁定项、风险项、可延后项",
    "明确下一轮最该产出的开发文档或验证动作"
  ]
}
---
# Development Brief Rubric

development brief 的价值不在于“说得全面”，而在于帮助团队少走弯路。这个 rubric 的核心就是问：这份 brief 到底能不能指导下一步真实开发。

## TODOs：待回答问题

- [ ] 如果项目还没有明确委制方，这份 rubric 是否需要一个 independent baseline 模式？
- [ ] 对品牌项目和影视项目，风险项的分类维度是否应该不同？
- [ ] brief 中多大比例应该谈创作，多大比例应该谈开发与交付，是否需要更细的经验边界？
- [ ] 当项目策略必须在多个窗口并行时，rubric 应如何判断 brief 是否仍然清晰？
