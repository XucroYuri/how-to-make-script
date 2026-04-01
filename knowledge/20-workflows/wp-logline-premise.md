---
{
  "id": "wp.logline-premise",
  "type": "workflow_protocol",
  "title": "Logline / Premise 协议",
  "goal": "把故事引擎压缩成高可读、高判断力的 logline 或 premise。",
  "input_contract": ["story concept", "premise", "character idea"],
  "output_contract": ["logline", "premise"],
  "preconditions": [
    "已具备主角与核心冲突轮廓"
  ],
  "steps": [
    "锁定主角、目标、主要阻力、 stakes。",
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
  "rubrics": ["rb.logline"],
  "linked_atoms": ["ka.story-goal", "ka.conflict-pressure", "ka.causality-chain"]
}
---
# Logline / Premise 协议

压缩不是删词，而是把真正驱动故事的核心关系留下来。

logline 和 premise 在开发流程里不是宣传语，而是判断工具。一个好的 logline 能让你很快看出：这个故事有没有主角、有没有动作方向、有没有足够的冲突压力、有没有可持续展开的空间。

如果一条 logline 听起来“很有气质”“很有世界观”，但听不出谁在做什么、为什么必须做，那它还不是开发级 logline，只是概念气氛。

## TODOs：待回答问题

- [ ] 不同媒介对 logline / premise 的压缩强度要求是否应该分开定义？
- [ ] 群像剧、双主角剧、反英雄项目的 logline 该如何写，才不会被单主角句法强行扭曲？
- [ ] 当项目卖点明显强于人物时，仓库应如何处理“先卖设定还是先卖人物”的取舍？
- [ ] 面向内部开发、面向投资人、面向平台、面向观众的 logline 是否应允许不同版本并存？
- [ ] premise 需要透露到什么程度才足够判断潜力，又不会提前消耗悬念和阅读兴趣？
- [ ] 当项目核心魅力在语气、形式或结构实验而非情节钩子时，logline 该如何避免失真？
- [ ] 体系是否需要加入“反 logline 检查”，专门识别那些句子顺但没有开发价值的伪概念？
