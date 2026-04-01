---
{
  "id": "ka.beat-carrier-selection",
  "type": "knowledge_atom",
  "title": "Beat 载体选择",
  "kind": "framework",
  "summary": "不是每个项目都适合用同一种 beat 载体；有的适合 beat sheet，有的更适合 sequence ladder、clue ladder、thread map、scene chain 或分支状态图。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "game_narrative", "branching_interactive"],
  "stages": ["structure", "outline", "adaptation"],
  "problem": "项目明明需要别的组织视角，却被强行写成同一种 beat sheet，导致信息层级混乱或关键机制缺席。",
  "decision_rules": [
    "先判断当前最需要被看见的是转折、线索、线程、场景功能，还是状态变化。",
    "beat 载体的职责是让关键推进机制可见，而不是满足格式统一。",
    "当一个载体已经掩盖问题而不是暴露问题时，立刻换载体，而不是继续填。"
  ],
  "anti_patterns": [
    "侦探项目没有 clue ladder，只有泛泛 beats",
    "群像项目没有 thread map，只有一条假主线",
    "互动项目没有状态和分支视图，只有线性 outline"
  ],
  "prompt_primitives": [
    "当前最应该被显化的推进单位是什么",
    "如果继续用现在的载体，哪些问题会被隐藏起来",
    "换成另一种载体后，最容易暴露的结构病是什么"
  ],
  "evaluation_checks": [
    "当前载体是否让关键推进机制变清楚",
    "是否存在更小、更诚实的结构载体",
    "载体是否没有被格式惯性绑架"
  ],
  "links": ["ka.structure-family-selection", "ka.causality-chain", "ka.command-artifact-mapping"],
  "source_status": "derived"
}
---
# Beat 载体选择

结构工作经常失败，不是因为作者不知道“应该有转折”，而是因为他用错了承载这些转折的容器。

有些故事最适合用 sequence 看，有些最适合用 clue 看，有些最适合用 thread 看。把所有项目都写成同一种 beat sheet，会让真正应该被看见的东西被压扁。

所以这里的重点不是发明更多表格，而是承认不同项目需要不同的结构显像方式。

## TODOs：待回答问题

- [ ] 仓库是否要正式列出常见 beat 载体与适用场景的映射表？
- [ ] 一个项目在开发中何时应该切换载体，切换后如何保持旧资产不失效？
- [ ] 是否需要为短剧、广告、互动叙事单独定义最小有效载体？
