---
{
  "id": "wp.logline-premise",
  "type": "workflow_protocol",
  "title": "Logline / Premise 协议",
  "goal": "把故事引擎压缩成高可读、高判断力的 logline 或 premise。",
  "input_contract": [
    "story concept",
    "premise",
    "character idea"
  ],
  "output_contract": [
    "logline",
    "premise"
  ],
  "preconditions": [
    "已具备主角与核心冲突轮廓"
  ],
  "steps": [
    "锁定主角、目标、主要阻力、 stakes。",
    "检查当前句子是在暴露故事发动机，还是只是在贩卖题材气味与设定新奇感。",
    "判断题材钩子是否真正进入冲突，而非仅作装饰。",
    "生成 1 句 logline 和 1 段 premise。",
    "用 rubric 清理空泛、高概念噪声和重复信息。"
  ],
  "fallbacks": [
    "若 stakes 不清楚，先退回目标与代价澄清。",
    "若题材很强但人物很弱，优先补主角视角。"
  ],
  "stop_conditions": [
    "logline 可独立成立",
    "premise 能明确后续结构开发方向"
  ],
  "rubrics": [
    "rb.logline"
  ],
  "linked_atoms": [
    "ka.causality-chain",
    "ka.conflict-pressure",
    "ka.cross-protocol-referral-edges",
    "ka.false-logline-warning",
    "ka.genre-pack-factorization",
    "ka.story-goal",
    "ka.viewer-inference-guidance"
  ],
  "budget_class": "L",
  "mandatory_atom_count": 7,
  "expansion_allowed": true
}
---
# Logline / Premise 协议

压缩不是删词，而是把真正驱动故事的核心关系留下来。

logline 和 premise 在开发流程里的角色不是宣传语，而是判断工具。一条好的 logline 能让你很快看清：这个故事有没有主角、有没有动作方向、有没有足够的冲突压力、有没有可持续展开的空间。

如果一条 logline 听起来"很有气质""很有世界观"，但听不出谁在做什么、为什么必须做，那它还不是开发级 logline，只是概念气氛。这里还要提防一种常见误判：句子写顺了，作者和 Agent 就以为开发工作已经完成。其实很多 logline 只是漂亮的题材陈述，还不是故事发动机。
