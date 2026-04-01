---
{
  "id": "rb.boundary-map",
  "type": "evaluation_rubric",
  "title": "Boundary Map Rubric",
  "applies_to": ["boundary_map"],
  "dimensions": [
    {"name": "classification", "question": "是否清楚区分了 hard boundary、soft constraint、bold-safe 和 defer-to-review"},
    {"name": "phase_awareness", "question": "是否说明哪些约束在 exploration 阶段可暂挂，哪些必须始终有效"},
    {"name": "practicality", "question": "边界划分是否足以指导下一步探索或评审"},
    {"name": "non-dogmatism", "question": "是否避免把偏好、惯例或市场口味误写成铁律"}
  ],
  "scoring_bands": {
    "excellent": "边界等级清楚、阶段分工明确、可直接指导探索与 review 的分离操作。",
    "workable": "基本有分级，但仍有一些约束混层或 review gate 说明不够清楚。",
    "weak": "更像泛泛的风险提示，无法帮助团队区分什么现在该放、什么不能放。"
  },
  "hard_fail_rules": [
    "把 soft constraint 写成 hard boundary",
    "没有保留 hard boundary 的持续有效性",
    "没有说明哪些检查要在 review 阶段重新加回"
  ],
  "rewrite_actions": [
    "先重分 hard/soft，再补 bold-safe 区域",
    "补写 exploration 与 review 的分界",
    "删去伪铁律式表述，改成边界级别说明"
  ]
}
---
# Boundary Map Rubric

boundary_map 的目标不是让团队更保守，而是让团队更分得清哪些东西真的不能碰，哪些只是别太早自我审查。这个 rubric 就是在看这件事有没有被说清。

## TODOs：待回答问题

- [ ] 哪些团队文化会系统性地把 soft constraint 误当成 hard boundary，是否需要单独案例支持？
- [ ] 某些项目若从一开始就必须满足品牌或发行要求，rubric 是否需要媒介 / 业务特化版本？
- [ ] boundary_map 是否还应加入“当前最值得探索的一块”这样的正向维度？
- [ ] 对 Agent 使用场景，是否要强制 boundary_map 标出 “not final approval” 提示？
