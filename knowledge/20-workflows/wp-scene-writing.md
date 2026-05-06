---
{
  "id": "wp.scene-writing",
  "type": "workflow_protocol",
  "title": "场景写作协议",
  "goal": "把 outline 转成具备明确功能、变化和可执行表演承载的 scene card、scene draft 或 screenplay draft。",
  "input_contract": [
    "outline",
    "beat_sheet",
    "scene goal"
  ],
  "output_contract": [
    "scene_card",
    "scene_draft",
    "screenplay_draft"
  ],
  "preconditions": [
    "大纲中已有场景前后关系"
  ],
  "steps": [
    "写明本场的主功能、冲突方和变化点。",
    "如果这是开场戏，先决定它最主要承担的开场工作，而不是默认同时完成所有工作。",
    "设计进入、冲突升级和离开点。",
    "按媒介调整篇幅、动作密度与镜头可执行性，并把角色声音、具身压力和影像语体显式带进动作与对白。",
    "为每个对白回合补齐表演承载：要么 inline performance，要么紧邻动作拍点，不允许裸对白直接裸露在剧本块里。",
    "只有在确实存在视听设计时才输出 `VFX`、`SFX`、`BGM`，但一旦输出就必须保持固定标签。",
    "输出 scene card、scene draft 或 screenplay draft，并在 handoff 前自检机械语症、对白-表演耦合和场景变化是否成立。"
  ],
  "fallbacks": [
    "若场景无变化，合并或删除。",
    "若台词承担过多解释，回退信息揭示控制。",
    "若多个角色开始同声同气，回退角色声音与具身压力，而不是只换词。"
  ],
  "stop_conditions": [
    "场景功能明确",
    "场景结束后的局面已不同于开始",
    "对白回合都有表演承载，且不触发中文机械语症硬失败"
  ],
  "rubrics": [
    "rb.scene-draft",
    "rb.screenplay-draft"
  ],
  "linked_atoms": [
    "ka.character-voice-consistency",
    "ka.cinematic-prose-register",
    "ka.conflict-pressure",
    "ka.cross-protocol-referral-edges",
    "ka.embodied-text-pressure",
    "ka.exposition-control",
    "ka.medium-animation",
    "ka.reactive-comedy-loop",
    "ka.scene-function",
    "ka.setup-and-payoff",
    "ka.verbal-rhythm"
  ],
  "budget_class": "L",
  "mandatory_atom_count": 11,
  "expansion_allowed": true
}
---
# 场景写作协议

场景就是结构的执行单元。每写一场戏，都得让某个系统状态发生变化，不能白写。

这个协议适合这种情况：我知道这场戏大概要干什么，但就是不知道怎么把它写成立。它要求你先想清楚本场功能、冲突方和变化点，再考虑怎么进入、怎么升级、怎么离开，而不是一上来就铺陈台词和氛围。如果当前场景是项目开场，还要额外问一层：这一段最主要的开场工作是什么。否则很容易一上来就想把人物、世界、冲突、主题、基调全塞进第一页。

这个协议默认把 `scene_draft` 当成场景级剧本块，把 `screenplay_draft` 当成多场景页稿级剧本块。两者都不再接受"只有对白功能、没有表演承载"的松散文本。对白不是独立漂浮的句子，每个回合都得靠括注、动作拍点、节奏断裂或空间行为把表演信息带出来。

如果一场戏删掉以后，人物关系、信息状态、行动条件都没什么变化，那它通常不是"写得还不够好"，而是从功能上就还没有被设计出来。
