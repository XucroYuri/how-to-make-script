---
{
  "id": "ka.genre-pack-factorization",
  "type": "knowledge_atom",
  "title": "类型包因子化",
  "kind": "framework",
  "summary": "类型知识不该只是大表格罗列，而应拆成核心承诺、关系压力、结构运动、动力学引擎和解构轴线等可复用因子。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "adaptation"],
  "problem": "类型文档越写越大，但真正可复用的判断维度越来越少。",
  "decision_rules": [
    "写类型包时先抽出它向观众承诺了什么，而不是先罗列理论名词。",
    "每种类型至少回答五件事：承诺、压力、结构运动、动力学、可被反转的旧公式。",
    "如果一个类型说明只能靠作品名单支撑，那它还不够原子化。"
  ],
  "anti_patterns": [
    "类型说明只剩代表作名单和外部理论标签",
    "把市场口味、平台热词误写成类型机制",
    "父类、子类、风格、题材、语气全部混在一张表里"
  ],
  "prompt_primitives": [
    "这个类型对观众最核心的承诺是什么",
    "它最常见的关系压力和动力学引擎是什么",
    "如果要解构它，最值得被扭转的是哪条旧公式"
  ],
  "evaluation_checks": [
    "类型包是否能脱离作品名单而独立说明机制",
    "是否区分了承诺、压力和结构运动",
    "是否给未来扩展留下可追加的因子位"
  ],
  "links": ["ka.scenario-factorization", "ka.creative-pluralism", "ka.false-universal-warning"],
  "source_status": "derived"
}
---
# 类型包因子化

类型知识最容易失控的方式，就是越写越像资料库，越写越不像可调用知识。

真正对 Agent 和创作者有用的，不是“某类型有哪些经典作品”，而是：它到底答应了观众什么、通常怎样施压、常见结构是怎么动起来的、又有哪些旧公式值得被反转。

这个原子不是为了缩减类型复杂度，而是为了让未来新增类型时有一个更稳的抽象框架。

## TODOs：待回答问题

- [ ] 类型包因子化后，哪些维度最适合进入 schema，哪些仍应留在正文说明中？
- [ ] 类型、题材、语气、世界观规模之间是否需要更明确的拆分边界？
- [ ] 是否需要为未来类型扩容建立统一的“最小因子清单”？
