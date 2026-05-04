---
{
  "id": "rb.session-execution-plan",
  "type": "evaluation_rubric",
  "title": "Session Execution Plan Rubric",
  "applies_to": ["session_execution_plan"],
  "dimensions": [
    {"name": "sequence_validity", "question": "每个段落的阶段顺序是否合理，前段产物是否是后段的有效输入"},
    {"name": "handoff_completeness", "question": "每个段落间的交接合同是否明确写出了必须传递和必须忽略的内容"},
    {"name": "posture_consistency", "question": "计划是否与当前创作态势一致——lost 态势不应生成多段计划"},
    {"name": "budget_realism", "question": "每个段落的 budget_class 标注是否反映了真实的加载复杂度"},
    {"name": "checkpoint_placement", "question": "是否在需要的接缝处插入了 story-memory-checkpoint 调用"}
  ],
  "scoring_bands": {
    "excellent": "段落序列合理，每个交接合同清晰，态势一致，预算标注真实，检查点位置正确。",
    "workable": "主要段落有效，但交接合同有省略，或预算标注偏乐观，或检查点位置需要调整。",
    "weak": "段落超过5个，或交接合同缺失，或计划与当前 lost 态势矛盾——应退回单段处理。"
  },
  "hard_fail_rules": [
    "计划段落数超过5个",
    "存在交接合同完全缺失的段落接缝",
    "用户处于 lost 态势但计划仍然输出了多段序列",
    "某个段落的 protocol_id 在仓库中不存在"
  ],
  "rewrite_actions": [
    "超过5段：要求用户缩小当前会话范围，把后续段落推入下一个会话",
    "交接合同缺失：明确写出前段产出的最小必要内容和下段可以安全忽略的部分",
    "态势矛盾：退出本协议，用单路由处理用户的第一个请求"
  ]
}
---
# Session Execution Plan Rubric

这个 rubric 的核心关切是范围边界。

会话计划写得越长，不代表越完善——段落堆叠通常意味着它已悄悄变成项目计划，只借用了会话计划的格式。五段硬失败规则就是为了防止这种漂移。段落间的交接合同必须显式写出，省略交接内容等于把上下文管理负担甩给下一个协议。检查点不是装饰，是会话记忆安全续接的关键接缝。

## TODOs：待回答问题

- [ ] 当某个段落本身 budget_class 很低，但其产出会被后续高预算段落大量引用时，标注是否应该向后看而不是只反映当前段落的加载量？
- [ ] 交接合同中"必须忽略"的内容，是否需要区分"可以忽略"和"必须删除"——后者涉及上下文污染风险，处理方式不同？
- [ ] 如果会话途中创作态势从 active 滑入 lost，已经生成的多段计划是否需要立即作废并触发重新路由，还是允许完成当前段落后再退出？
