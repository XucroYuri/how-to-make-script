---
{
  "id": "ka.script-as-coordination-artifact",
  "type": "knowledge_atom",
  "title": "剧本作为协调产物",
  "kind": "principle",
  "summary": "剧本不是单纯的文学文本，它还承担开发、协作、融资、制作、交接和版本协调的作用。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "outline", "scene", "rewrite", "adaptation"],
  "problem": "把所有创作问题都压回“再写文本”，忽略当前真正需要推动的是立项、沟通、协作、版本管理还是下游执行准备。",
  "decision_rules": [
    "先判断下一位关键决策者是谁，再决定当前最应该写哪一种产物。",
    "明确区分 premise、treatment、draft、revision note、continuity-facing artifact 等不同工作表面，但保持它们之间的可追溯性。",
    "把版本状态、交付目的和使用场景当成创作信息的一部分，而不是纯行政信息。"
  ],
  "anti_patterns": [
    "无论什么阶段都只输出完整页稿",
    "把所有不同功能的文档都混成一个 script",
    "直到后期才暴露会影响写法的协作和制作约束"
  ],
  "prompt_primitives": [
    "这个阶段最需要说服或服务的是谁",
    "当前最有效的工作产物是什么，而不是默认继续写页稿",
    "哪些版本状态和交接信息会改变当前的创作决策"
  ],
  "evaluation_checks": [
    "当前产物是否匹配当下阶段与决策对象",
    "是否保留了关键的版本和交接信息",
    "是否避免把开发、改稿和制作前准备都压成一种文本形式"
  ],
  "links": ["ka.commissioning-fit", "ka.room-artifact-ladder", "ka.source-of-truth-runtime-split", "ka.handoff-contract-discipline", "ka.screenplay-to-video-boundary"],
  "source_status": "curated"
}
---
# 剧本作为协调产物

很多创作者会下意识地把剧本理解成“那份最后要写好的文本”。
但现实中的剧本工作远不止这一层。它既是叙事发动机，也是开发中的判断工具、协作中的沟通界面、版本管理对象，以及进入制作前后的协调载体。

这会直接影响 Agent 应该怎么帮你。
有时候真正需要推进项目的，并不是再多写一场戏，而是把 premise 压到能立项、把 treatment 写到能开会、把 rewrite priorities 排清、把 continuity 风险提前暴露出来。

如果 Agent 看不见这一层，就会做出一种很常见的错误勤奋：不断生成文本，但没有推动项目。

## TODOs：待回答问题

- [ ] 不同媒介和团队模式下，哪类协调产物最应该提前显式化？
- [ ] 项目从开发进入制作后，哪些原本隐性的版本信息必须升级为显性字段？
- [ ] 在 Agent 协作场景里，哪些协调信息应该始终写进 packet，哪些可以只保留在运行时？
- [ ] 对完全作者驱动的个人项目来说，协调产物的最小集合应该是什么？
