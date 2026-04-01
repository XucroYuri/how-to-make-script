---
{
  "id": "rb.scope-correction",
  "type": "evaluation_rubric",
  "title": "Scope Correction Rubric",
  "applies_to": ["scope_correction"],
  "dimensions": [
    {"name": "surviving_core", "question": "是否保留了原说法里仍然成立的最小核心"},
    {"name": "boundary_clarity", "question": "是否把适用边界与失效条件写清楚了"},
    {"name": "counterexample_use", "question": "是否真的利用了反例，而不是只把反例当姿态摆出来"},
    {"name": "operational_impact", "question": "是否说明修正后会影响哪些 route、rubric、fixture 或 docs"}
  ],
  "scoring_bands": {
    "excellent": "修正后的说法更窄、更准，保留核心、写清边界，并明确了仓库后续应更新的地方。",
    "workable": "已经意识到原说法过宽，但 surviving core 或影响面仍不够清楚。",
    "weak": "看似在修正，实际只是把一个绝对说法换成另一个绝对说法，或根本没有写出边界。"
  },
  "hard_fail_rules": [
    "没有说明原说法中仍然成立的最小核心",
    "没有写明至少一个失效条件、反例上下文或适用边界",
    "没有说明修正后会影响哪些后续资产或路由"
  ],
  "rewrite_actions": [
    "先找 surviving core，再做边界缩窄",
    "把反例转成可操作的失效条件",
    "补写 route、rubric、fixture 或 docs 的受影响范围"
  ]
}
---
# Scope Correction Rubric

scope correction 最常见的失败，不是写得不够漂亮，而是根本没有真正缩窄任何东西。它只是把“永远如此”换成“其实也不一定”，听上去谦虚了，但仓库一点也没变准。

这个 rubric 的任务，就是防止“伪修正”。如果一条规则被挑战了，修正结果必须更清楚地回答：还剩什么成立、哪里不成立、改完之后仓库下一步该动哪里。

## TODOs：待回答问题

- [ ] scope correction 的优秀样例是否需要单独沉淀到 case study 层？
- [ ] 哪些类型的修正最容易漏掉 downstream impact？
- [ ] 当反例只来自单一地区或单一平台时，边界应该写多窄？
- [ ] rubric 是否需要单独检查“有没有把反例伪装成个人偏好”？
