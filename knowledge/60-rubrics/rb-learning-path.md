---
{
  "id": "rb.learning-path",
  "type": "evaluation_rubric",
  "title": "Learning Path Rubric",
  "applies_to": ["learning_path"],
  "dimensions": [
    {"name": "diagnosis", "question": "是否真正定位了学习者的失败层与当前成熟度"},
    {"name": "sequencing", "question": "训练顺序是否合理，而不是把所有建议平铺"},
    {"name": "practice_design", "question": "是否有真实写作产物、练习方式和升级条件"},
    {"name": "feedback_loop", "question": "是否说明反馈来源、返修节奏和复盘机制"}
  ],
  "scoring_bands": {
    "excellent": "路径分阶段、可执行、与真实写作产物绑定，能清楚说明为什么先练什么。",
    "workable": "有基本阶段感，但诊断或练习设计仍偏粗，反馈机制不够具体。",
    "weak": "更像阅读清单或励志建议，无法形成稳定成长循环。"
  },
  "hard_fail_rules": [
    "没有说明当前失败层或学习阶段",
    "没有绑定具体写作产物或练习任务",
    "没有反馈与返修机制"
  ],
  "rewrite_actions": [
    "先补诊断，再安排顺序",
    "把抽象建议改成具体练习和里程碑",
    "为每一阶段补上反馈与返修方式"
  ]
}
---
# Learning Path Rubric

学习路径最容易失效的原因，是它听起来很完整，却不改变任何写作行为。这个 rubric 的重点就是逼路径落到真实训练动作，而不是落在“多看、多想、多练”这种空话上。

## TODOs：待回答问题

- [ ] 不同职业阶段的 learning path 是否需要不同的 minimum viable detail？
- [ ] 对自学者和有导师者，反馈机制的合格标准是否应不同？
- [ ] 某些成长路径需要团队协作训练时，当前 rubric 是否需要单独的协作维度？
- [ ] 什么时候一条 learning path 已经过长、过满，反而降低执行概率？
