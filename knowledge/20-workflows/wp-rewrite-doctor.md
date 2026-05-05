---
{
  "id": "wp.rewrite-doctor",
  "type": "workflow_protocol",
  "title": "改稿诊断协议",
  "goal": "输出按层级排序、可执行的 rewrite report。",
  "input_contract": [
    "draft",
    "outline",
    "scene set",
    "dialogue excerpt"
  ],
  "output_contract": [
    "rewrite_report"
  ],
  "preconditions": [
    "存在至少一个可诊断的已有文本"
  ],
  "steps": [
    "先判定主要问题发生在概念、结构、场景还是对白层。",
    "列出高杠杆病灶与症状对应关系。",
    "给出按优先级排序的修改动作。",
    "区分必须重构、建议改进和可观察风险。"
  ],
  "fallbacks": [
    "若文本过少，只输出风险预判，不伪造定论。",
    "若用户需要的是 multi-lens quality gate、preflight、acceptance 或 recheck，返回 quality_gate_report。"
  ],
  "stop_conditions": [
    "报告已包含层级诊断、优先级和具体动作"
  ],
  "rubrics": [
    "rb.rewrite-report"
  ],
  "linked_atoms": [
    "ka.causality-chain",
    "ka.cross-protocol-referral-edges",
    "ka.dialogue-subtext",
    "ka.dual-track-rhythm",
    "ka.feedback-subjectivity-management",
    "ka.pacing-rhythm",
    "ka.rewrite-diagnosis",
    "ka.scene-function",
    "ka.setup-and-payoff",
    "ka.weak-opening-diagnosis"
  ],
  "budget_class": "L",
  "mandatory_atom_count": 10,
  "expansion_allowed": true
}
---
# 改稿诊断协议

先诊断，再动刀。在错误层级上勤奋只会把坏结构抛光。

这个协议对标的是剧本医生或开发会上的工作方式：先判断病灶在哪一层。它不是泛泛点评，也不是"我觉得这里可以更精彩"，而是明确区分概念病、结构病、场景病、对白病，并给出优先级。

项目越成熟，越需要这种分层诊断。因为局部越多，错误修补的代价越高。不先做层级判断，团队很容易在低杠杆位置上反复用力。
