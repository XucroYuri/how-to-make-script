---
{
  "id": "rb.audience-fit",
  "type": "evaluation_rubric",
  "title": "Audience Fit Rubric",
  "applies_to": ["audience_fit_note"],
  "dimensions": [
    {"name": "segment_clarity", "question": "主受众是否具体到足以指导写法，而不是泛化人群标签"},
    {"name": "need_state", "question": "是否说清观众为什么会点开、继续看、看完后要得到什么"},
    {"name": "payoff_alignment", "question": "当前文本承诺和目标回报之间的吻合度是否明确"},
    {"name": "revision_utility", "question": "修改建议是否足够具体，能直接改变写作动作"}
  ],
  "scoring_bands": {
    "excellent": "主受众、需求状态、平台门槛和修改动作都具体明确，足以直接指导开发或改稿。",
    "workable": "受众方向基本清楚，但仍有概念泛化、回报模糊或修改动作偏粗的问题。",
    "weak": "更像泛泛而谈的市场想象，无法真正改变文本决策。"
  },
  "hard_fail_rules": [
    "没有明确主受众",
    "没有明确需求状态或预期回报",
    "修改建议无法映射到 premise、结构、场景或信息密度层"
  ],
  "rewrite_actions": [
    "把受众从人口标签改写成观看场景与需求状态",
    "补足承诺与回报之间的错位说明",
    "把建议改写成具体的开头、节奏、信息或角色处理动作"
  ]
}
---
# Audience Fit Rubric

这个 rubric 用来防止 audience note 滑向空泛市场话术。它要求 note 必须真正改变写作判断，而不是只给出“更贴近年轻人”“更大众”“更抓人”这种无效建议。

## TODOs：待回答问题

- [ ] 是否需要为商业脚本与叙事剧本分别设置不同的 audience fit 评分阈值？
- [ ] 当一个项目故意挑战受众预期时，这份 rubric 应如何避免误杀真正有价值的反向设计？
- [ ] audience fit 的 hard fail 是否还应加入“平台与门槛错配”这一条？
- [ ] 对互动项目而言，参与感和观看感的评价维度是否需要拆开？
