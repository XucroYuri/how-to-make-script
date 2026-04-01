---
{
  "id": "rb.story-memory-checkpoint",
  "type": "evaluation_rubric",
  "title": "Story Memory Checkpoint Rubric",
  "applies_to": ["story_memory_checkpoint"],
  "dimensions": [
    {"name": "compression_fidelity", "question": "是否明显压缩了原始材料，但仍保住续写和 handoff 所需的关键状态"},
    {"name": "continuity_coverage", "question": "角色状态、未兑现承诺、不变量和 canon / 假设边界是否被清楚记录"},
    {"name": "rhythm_visibility", "question": "是否区分外部推进和内部推进，而不是把节奏压成单一回顾"},
    {"name": "resume_readiness", "question": "是否给出 next safe entrypoint、优先回看面和误写风险"}
  ],
  "scoring_bands": {
    "excellent": "压缩明显、状态清楚、双轨可见、可直接续写或 handoff，且无需回灌全文。",
    "workable": "主要状态存在，但压缩不够、边界不够清或恢复入口仍偏模糊。",
    "weak": "更像剧情摘要或会议纪要，不能安全支撑下一轮写作。"
  },
  "hard_fail_rules": [
    "没有 next safe entrypoint",
    "未兑现承诺、关键不变量或主要状态变化缺失",
    "把工作假设与稳定 canon 混写",
    "检查点长度和信息组织方式接近重新搬运原始材料"
  ],
  "rewrite_actions": [
    "删掉复述性段落，改写成状态和风险清单",
    "补写未兑现承诺、关键不变量和 canon / hypothesis 边界",
    "把外部推进与内部推进拆开记录",
    "补写恢复入口、优先回看面和最容易误写的风险"
  ]
}
---
# Story Memory Checkpoint Rubric

一个好的 checkpoint 不在于“总结得很全面”，而在于“下一轮真的能继续写”。

如果它只是把故事讲了一遍，却没有告诉协作者现在到底处在哪个状态、什么东西不能漂、下一步从哪切进去最安全，那它就还不算检查点，只算复盘。

## TODOs：待回答问题

- [ ] 是否需要按 feature / episodic / interactive 分不同权重？
- [ ] compression_fidelity 是否应增加更明确的篇幅或字段上限建议？
- [ ] 对 review handoff 和 draft resume，两种 checkpoint 的 hard fail 是否应该不同？
