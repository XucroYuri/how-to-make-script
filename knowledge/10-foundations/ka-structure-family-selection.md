---
{
  "id": "ka.structure-family-selection",
  "type": "knowledge_atom",
  "title": "结构族选择",
  "kind": "framework",
  "summary": "结构不是先选模板再装剧情，而是先识别故事的推进引擎，再决定它更接近 quest、mystery、lie-to-truth、parallel-thread、loop 或其他结构族。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "outline", "adaptation"],
  "problem": "项目被默认塞进单一结构模板，结果形式完整但推进逻辑和题材承诺并不匹配。",
  "decision_rules": [
    "先看故事主要靠什么推进：目标追逐、真相拼图、人物误判瓦解、群像并行、循环变体，还是分支选择。",
    "结构族应该服务冲突引擎，而不是反过来强迫项目为模板表演。",
    "如果多个结构族都能成立，先明确主结构，再标记副结构，而不是全部混写。"
  ],
  "anti_patterns": [
    "所有项目默认三幕式 + 15 beat，不问题材差异",
    "侦探、群像、互动项目被强塞成单主角线性推进",
    "结构语言很完整，但回答不了为什么这个项目必须这样推进"
  ],
  "prompt_primitives": [
    "这个故事的主要推进引擎是什么",
    "如果把项目换成另一种结构族，最先坏掉的是什么",
    "主结构和副结构分别承担什么功能"
  ],
  "evaluation_checks": [
    "所选结构族是否贴合题材和观看承诺",
    "是否明确了主结构与副结构的边界",
    "模板语言是否没有覆盖掉真正的推进机制"
  ],
  "links": ["ka.causality-chain", "ka.theme-pressure", "ka.creative-pluralism"],
  "source_status": "derived"
}
---
# 结构族选择

很多结构问题不是“不会写 beat”，而是从一开始就选错了要用哪一套结构视角看项目。

比如谜案驱动的故事，本质上更接近线索梯子的组织问题；群像戏更接近线程协同和交汇设计；角色谎言瓦解型故事则更依赖错误信念被一步步逼破。它们都可以借用三幕式语言，但如果只剩三幕式语言，就很容易把真正的推进引擎抹平。

这个原子的作用，是让仓库先问“这个故事靠什么往前走”，再决定用什么结构族来组织它。

## TODOs：待回答问题

- [ ] 仓库是否需要为常见结构族形成更明确的对照表和失败征候表？
- [ ] 季播剧、单元剧、互动分支项目的结构族是否应该在媒介层进一步细拆？
- [ ] 当平台留存逻辑与故事本体结构族冲突时，协议应如何裁决优先级？
