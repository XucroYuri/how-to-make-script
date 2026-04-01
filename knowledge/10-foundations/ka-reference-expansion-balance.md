---
{
  "id": "ka.reference-expansion-balance",
  "type": "knowledge_atom",
  "title": "参考扩展平衡",
  "kind": "decision_heuristic",
  "summary": "找到更多参考并不等于一次性装入更多参考；更好的做法是按距离和价值排序，只追加最能改变当前判断的少量邻近参考。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "Agent 在想提高准确率时，很容易把 reference breadth 当成 reference quality，导致参考越来越多但真正可用的判断越来越少。",
  "decision_rules": [
    "优先追加与当前 medium、stage、creative problem 最近的参考，再考虑跨媒介对照。",
    "每次扩展只补最有可能改变当前判断的 1-2 个 reference source。",
    "当额外参考只会重复已知结论时，停止扩展。"
  ],
  "anti_patterns": [
    "相关就全加",
    "把跨媒介对照默认视为更高级的参考",
    "参考越多越稳"
  ],
  "prompt_primitives": [
    "下一份最值得加载的参考是什么",
    "这份参考会改变 route、判断还是只会重复",
    "有没有更近邻的参考比远距离参考更值钱"
  ],
  "evaluation_checks": [
    "扩展是否保持近邻优先",
    "每次扩展是否有明确收益说明",
    "是否控制了跨媒介/跨类型的噪声"
  ],
  "links": ["ka.bounded-context-loading", "ka.reference-pattern-usage", "ka.false-universal-warning"],
  "source_status": "derived"
}
---
# 参考扩展平衡

“多找一些参考”这件事，本身没有错。错的是把它理解成“能加多少就加多少”。真正有效的参考扩展，是有顺序的：先近后远，先核心问题后外围比较，先能改变判断的再加只能重复结论的。

如果一个 feature drama 的结构问题，已经有当前媒介下的强 protocol、rubric 和 reference pack 了，下一步未必该跳到互动叙事或品牌片找灵感。除非用户明确要跨媒介改写，或者当前路径已经解释不动问题。

所以参考扩展的本质，不是 breadth 最大化，而是 marginal value 最大化。

## TODOs：待回答问题

- [ ] 哪些场景下跨媒介参考的增益最大？
- [ ] reference pack、scenario card、reality lens 之间的默认优先级是否应固定？
- [ ] 何时一个远距离参考反而比近邻参考更能打开创意？
- [ ] 是否需要单独记录“高噪声参考类型”？
- [ ] 当用户追求创意突破时，参考扩展应如何兼顾新奇和聚焦？
