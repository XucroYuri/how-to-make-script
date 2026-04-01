---
{
  "id": "rb.quality-gate-report",
  "type": "evaluation_rubric",
  "title": "Quality Gate Report Rubric",
  "applies_to": ["quality_gate_report"],
  "dimensions": [
    {"name": "scope_fit", "question": "是否先锁定了 target contract、scope mode 和 medium，而不是泛泛审稿"},
    {"name": "lens_selection", "question": "selected lenses 是否与当前 artifact family 和风险压力匹配"},
    {"name": "isolation_discipline", "question": "是否保持 lens 独立判断，而不是让各层互相污染"},
    {"name": "hard_gate_clarity", "question": "hard fail、weighted weakness、open contradictions 是否清楚分开"},
    {"name": "correction_ladder", "question": "修改优先级是否清楚，能帮助团队决定先停、先修、再观察"},
    {"name": "recheck_design", "question": "当任务涉及复查或范围限定时，recheck plan 是否足够精确"}
  ],
  "scoring_bands": {
    "excellent": "scope、lens、gate、排序和复查设计都清楚，既能发现问题，也能指导下一步行动。",
    "workable": "能给出有用诊断，但 lens 选择、gate 分离或复查设计仍略粗。",
    "weak": "更像泛泛点评或统一 checklist，缺少 contract 适配和真正可执行的 gate 逻辑。"
  },
  "hard_fail_rules": [
    "没有明确 target contract 或 scope mode",
    "没有说明为什么选这些 lenses",
    "hard fail 和 soft weakness 混成一个总评价",
    "没有 correction ladder",
    "在用户明确要求 recheck 时没有给出复查范围"
  ],
  "rewrite_actions": [
    "先补 target contract、scope mode 和 medium",
    "重选 lens stack，并说明不启用其他 lenses 的原因",
    "把 hard fail 与 weighted weakness 拆开",
    "补写 correction ladder 与 recheck plan"
  ]
}
---
# Quality Gate Report Rubric

这份 rubric 不是在鼓励“审得越细越好”，而是在防止一种更常见的失败：看起来查得很认真，实际上既没对题，也没告诉团队下一步该怎么动。

一个好的 `quality_gate_report` 必须做到三件事：
1. 查对题；
2. 查分层；
3. 查完之后能推动下一步，而不是制造更多模糊争论。

它的价值不在“像不像一个全面报告”，而在“有没有把场景适配、gate 逻辑和复查路径做实”。

## TODOs：待回答问题

- [ ] 对只做 lens-targeted audit 的报告，rubric 是否应单独降低 full coverage 要求？
- [ ] 某些 exploratory artifact 是否需要更宽松的 hard-fail 集？
- [ ] 是否需要为 commercial / interactive / governance artifact 加不同权重模板？
