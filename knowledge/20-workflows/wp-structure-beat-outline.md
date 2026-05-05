---
{
  "id": "wp.structure-beat-outline",
  "type": "workflow_protocol",
  "title": "结构 / Beat / 大纲协议",
  "goal": "把 premise 扩展为可因果推进的 beat sheet、outline 或 treatment。",
  "input_contract": [
    "premise",
    "character notes",
    "world rules"
  ],
  "output_contract": [
    "beat_sheet",
    "outline",
    "treatment"
  ],
  "preconditions": [
    "主角目标与主要阻力已明确"
  ],
  "steps": [
    "先判断项目更接近哪一类结构族，再决定主要使用哪种 beat 载体。",
    "如果项目是连续容器，先锁集数/时长/连续性强度和弧光预算，再决定 major turn 怎么分配。",
    "确定起始失衡、升级节点、危机、高潮、结局。",
    "把关键节点连成因果链。",
    "按媒介需求分配节奏波形与信息密度，并区分外部推进和内部情绪的双轨节奏。",
    "输出 beat sheet，再扩展为 outline 或 treatment。"
  ],
  "fallbacks": [
    "若中段虚弱，回退到冲突升级设计。",
    "若结构点很齐但没有戏，检查因果链、双轨节奏与场景功能。",
    "若续写安全依赖大量回读，补一个 story_memory_checkpoint，而不是继续堆 outline 细节。"
  ],
  "stop_conditions": [
    "所有关键节点存在前因后果",
    "目标媒介需要的大纲粒度已达到"
  ],
  "rubrics": [
    "rb.outline"
  ],
  "linked_atoms": [
    "ka.beat-carrier-selection",
    "ka.causality-chain",
    "ka.cross-protocol-referral-edges",
    "ka.dual-track-rhythm",
    "ka.medium-episode",
    "ka.medium-feature-film",
    "ka.medium-short-drama",
    "ka.pacing-rhythm",
    "ka.serial-arc-budgeting",
    "ka.story-goal",
    "ka.structure-family-selection"
  ],
  "budget_class": "L",
  "mandatory_atom_count": 11,
  "expansion_allowed": true
}
---
# 结构 / Beat / 大纲协议

结构工作的目标不是填模板，而是确保故事被一步步逼向不可回避的结局。

beat、outline、treatment 不是三种”格式偏好”，而是三种粒度不同的开发视角。beat 看的是大转折和推进力，outline 看的是顺序和功能，treatment 看的是整体阅读体验和戏剧连续性。
仓库不再默认所有项目都应该先写成同一种 beat sheet。不同的故事推进引擎，可能需要不同的结构族和 beat 载体来显影。对连续容器来说，还需要先锁住弧光预算，否则节拍表只会让透支写得更整齐。

专业上最值得警惕的不是”模板不标准”，而是结构点齐了却没有真正的压力递增。看起来像完整三幕式，实际中段全靠事件填空。这个协议要解决的正是这种”形式完整、戏剧无力”的问题。
同样值得警惕的是只看一条节奏线。很多 outline 不是没有转折，而是外部推进和内部情绪推进混成了一锅，所以每场都像有事发生，却没有真正被推着变。
