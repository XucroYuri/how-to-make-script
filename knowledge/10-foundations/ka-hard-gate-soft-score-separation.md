---
{
  "id": "ka.hard-gate-soft-score-separation",
  "type": "knowledge_atom",
  "title": "硬门槛与软评分分离",
  "kind": "evaluation_rule",
  "summary": "高质量质检不应把所有问题都揉成一个平均分。必须先把 hard fail 和 soft weakness 分开，避免严重违约被漂亮局部平均掉。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "如果所有问题都只变成一个总分，团队很容易忽略 contract breach、state break、delivery failure 这类‘一票否决’问题，转而只讨论可打磨的弱项。",
  "decision_rules": [
    "先判定 hard fail，再计算 weighted weakness。",
    "hard fail 不允许被平均分冲淡，必须单独列出并进入优先修复层。",
    "soft weakness 用于排序和优化，不用于掩盖契约、边界或交付级问题。"
  ],
  "anti_patterns": [
    "所有问题只有一个总分",
    "明明有明显 contract breach，却因为文风好或局部有趣给出高评价",
    "把边界风险和品味偏差混成同一种扣分项"
  ],
  "prompt_primitives": [
    "这次检查里哪些问题属于一票否决",
    "哪些问题更适合进入加权排序而不是 hard fail",
    "如果 hard fail 已存在，后续评分还起什么作用"
  ],
  "evaluation_checks": [
    "hard fail 是否被显式列出",
    "weighted weakness 是否只承担排序而非掩盖",
    "最终结论是否同时反映 gate 和 score"
  ],
  "links": ["ka.boundary-first-guidance", "ka.scope-correction", "ka.contract-first-quality-gating"],
  "source_status": "synthesized"
}
---
# 硬门槛与软评分分离

并不是所有问题都该被打成分数。有些问题是“这版先别往下走”；有些问题是“可以往下走，但这一层还不够强”。这两者必须分开。

剧本仓库里的 quality gate 也一样。`state continuity` 断裂、`target contract` 错位、`delivery handoff` 完全不可用，这些都不该被漂亮的对白、好看的句子或者部分精彩桥段平均掉。平均分是帮助排序的，不是帮助掩盖的。

所以这里借用的是专用 checker 的 gate 思维，但抽象成更通用的规则：先 gate，后 score。

## TODOs：待回答问题

- [ ] 哪些 output contract 需要更严格的 hard-fail 集，而哪些更适合宽松 gate？
- [ ] 是否需要为不同 medium 单独定义一票否决项？
- [ ] 当项目明确处于 exploration 阶段时，哪些 hard gate 仍然必须保留？
