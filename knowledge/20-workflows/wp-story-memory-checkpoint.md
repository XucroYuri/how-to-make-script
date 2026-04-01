---
{
  "id": "wp.story-memory-checkpoint",
  "type": "workflow_protocol",
  "title": "故事记忆检查点协议",
  "goal": "输出一份 story_memory_checkpoint，把当前故事推进所需的最小状态压缩成可续写、可交接、可检查的 continuity-safe 包，而不是重新搬运全文。",
  "input_contract": ["current draft span or outline span", "medium", "current phase", "active continuity concerns", "handoff or resume reason", "constraints"],
  "output_contract": ["story_memory_checkpoint"],
  "budget_class": "M",
  "mandatory_atom_count": 5,
  "expansion_allowed": true,
  "preconditions": [
    "任务具有长篇、分集、多轮改稿、多协作者或跨会话继续写作的压力",
    "至少能识别一个当前阶段边界、handoff 场景或恢复写作场景"
  ],
  "steps": [
    "先锁定检查点覆盖的 span 和目的：resume、room handoff、review handoff、lane handoff 还是 adaptation bridge。",
    "压缩当前角色/关系状态、进行中的目标与阻力、未兑现承诺、连续性不变量和稳定 canon。",
    "分开写外部推进节奏和内部情绪/认知节奏，避免把节奏压扁成一条线。",
    "如果项目具有连续容器，写出当前 arc budget 消耗情况：哪些 reveal、turn、payoff 已花掉，哪些仍保留。",
    "给出 next safe entrypoint、最该优先回看的 source surfaces，以及不该误当 canon 的临时假设。",
    "输出 story_memory_checkpoint，并说明它取代了哪些不必要的全量重载。"
  ],
  "fallbacks": [
    "若用户实际需要的是项目表面设计，返回 project_surface_map。",
    "若用户实际需要的是加载策略而不是故事状态压缩，返回 context_loading_plan。",
    "若当前材料太少，不足以形成状态压缩，先要求最小必要 span，而不是编造检查点。"
  ],
  "stop_conditions": [
    "检查点已经覆盖状态、未兑现承诺、不变量、双轨节奏、arc budget 和 next entrypoint",
    "内容足以支撑下一轮安全续写或 handoff，但明显短于原始材料",
    "已经明确哪些只是临时工作假设，不可误写成 canon"
  ],
  "rubrics": ["rb.story-memory-checkpoint"],
  "linked_atoms": ["ka.story-memory-checkpoint", "ka.dual-track-rhythm", "ka.serial-arc-budgeting", "ka.room-artifact-ladder", "ka.script-as-coordination-artifact"]
}
---
# 故事记忆检查点协议

这个协议的用途，不是重新解释故事，而是把“继续写下去真正不能丢的东西”压缩出来。

它最适合三类时刻：

- 写到一半要暂停，未来要恢复；
- 一条 lane 要把当前状态交给另一条 lane；
- room 已经讨论出很多东西，但不值得每次都重读所有原始材料。

对当前仓库来说，这个协议还有额外价值：它提供了一种比“继续加载更多文档”更健康的连续性管理手段。也就是说，当真正的问题是 continuity-safe handoff 时，最优解往往不是扩 context，而是产出 checkpoint。

## TODOs：待回答问题

- [ ] checkpoint 是否需要区分“作者自己恢复写作”和“交给别的 Agent / 人”的两种模板？
- [ ] 在互动叙事里，状态变量和剧情记忆是否应分成两个层？
- [ ] 哪些项目需要每一集都有 checkpoint，哪些项目只在 major turn 后做 checkpoint 即可？
- [ ] checkpoint 是否要显式标注“若只回看一处 source，优先回看哪里”？
