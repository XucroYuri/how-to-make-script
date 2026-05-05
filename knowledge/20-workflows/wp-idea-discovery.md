---
{
  "id": "wp.idea-discovery",
  "type": "workflow_protocol",
  "title": "创意发现协议",
  "goal": "把模糊想法收敛为可进入剧本开发的 premise。",
  "input_contract": [
    "raw idea",
    "theme fragment",
    "image prompt",
    "market brief",
    "none"
  ],
  "output_contract": [
    "premise"
  ],
  "preconditions": [
    "允许先从模糊灵感开始",
    "至少能说明目标媒介或应用场景"
  ],
  "steps": [
    "识别主角、欲望、阻力、代价的最小组合。",
    "判断更适合 narrative、commercial 还是 interactive 路径。",
    "把题材兴趣翻译为可测试的冲突命题。",
    "输出一个可扩展 premise，并附带 2-3 个后续展开方向。"
  ],
  "fallbacks": [
    "若媒介未知，先按 narrative generic 路径收敛 premise。",
    "若用户只给情绪或主题，先补故事目标。"
  ],
  "stop_conditions": [
    "premise 已能说明角色、目标、阻力、代价",
    "下一步最适合进入 logline、character 或 commercial 开发"
  ],
  "rubrics": [
    "rb.logline"
  ],
  "linked_atoms": [
    "ka.conflict-pressure",
    "ka.cross-protocol-referral-edges",
    "ka.screenplay-lens-stacking",
    "ka.story-goal",
    "ka.theme-pressure"
  ],
  "budget_class": "M",
  "mandatory_atom_count": 5,
  "expansion_allowed": true
}
---
# 创意发现协议

先找驱动力，再找形式。模糊灵感只有进入角色目标与冲突之后，才值得继续开发。

这个协议最适合”我有一个感觉/题材/画面，但还不是故事”的阶段。目标不是马上把 idea 放大，而是先判断它有没有真正的叙事发动机。

实践中，创意发现最容易犯的错是过早沉迷于世界观、类型氛围或营销包装，却没有先把主角的目标和阻力压出来。这个协议就是用来拦截这种虚胖开发。
