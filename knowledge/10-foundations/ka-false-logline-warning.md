---
{
  "id": "ka.false-logline-warning",
  "type": "knowledge_atom",
  "title": "伪 Logline 预警",
  "kind": "heuristic",
  "summary": "很多句子听起来像 logline，但实际上只在贩卖题材气味、设定新奇感或主题姿态，并没有暴露故事发动机。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "adaptation"],
  "problem": "项目看似有一句话概念，但真正进入开发时，主角动作、阻力来源和持续推进力都不清楚。",
  "decision_rules": [
    "先判断当前句子是在描述故事发动机，还是只是在卖设定气味。",
    "如果拿掉风格形容词和世界观名词后句子立即塌掉，说明它多半还是伪 logline。",
    "一句好 logline 不一定要解释完整世界，但必须让人看见谁会被迫做什么、为什么难、为什么失败有代价。"
  ],
  "anti_patterns": [
    "只有高概念设定，没有明确行动方向",
    "只有主题判断，没有主角决策压力",
    "只有反转感或谜面感，没有可持续推进的冲突"
  ],
  "prompt_primitives": [
    "如果删掉题材包装，这句里还剩下什么真正的故事动作",
    "主角被迫采取的核心行动是什么",
    "这句是在说明故事会如何推进，还是只是在说明它看起来像什么"
  ],
  "evaluation_checks": [
    "是否有可辨认的主角行动线",
    "阻力和 stakes 是否不是靠读者脑补补完",
    "句子是否具有开发级判断价值，而不是只适合市场宣传"
  ],
  "links": ["ka.story-goal", "ka.conflict-pressure", "ka.reference-expansion-balance"],
  "source_status": "derived"
}
---
# 伪 Logline 预警

最常见的问题不是“不会压缩”，而是把还没形成故事发动机的概念，过早压成一句听起来很像样的话。

伪 logline 往往有三个特点：它很像宣传语，它很像题材标签，它也可能很像作者的主题宣言。但它不一定真的回答了开发最关心的问题：谁会被迫行动、为什么现在必须行动、到底是什么在阻碍他、失败会损失什么。

对 Agent 来说，这个预警尤其重要。因为模型天然擅长把模糊概念润色得很顺，顺到让人误以为结构已经成立。这个原子就是用来阻止“句子先漂亮，发动机后补票”。

## TODOs：待回答问题

- [ ] 群像片、观察型项目、程序性作品在“伪 logline”识别上是否需要单独边界？
- [ ] 对 IP 续作或世界观强项目，哪些信息可以借用既有认知，哪些仍必须独立说明？
- [ ] 仓库是否需要形成一组“伪 logline 临界案例”，帮助区分 workable 与 weak？
