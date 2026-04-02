---
{
  "id": "ka.targeted-recheck-loop",
  "type": "knowledge_atom",
  "title": "定向复查回路",
  "kind": "workflow_rule",
  "summary": "复查不应默认重跑所有检查层。应优先重跑被修改范围直接影响的 lens，再补一个相邻 lens 检查副作用，只有当 contract 或 invariants 大变时才升级成 full audit。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "很多复查不是因为改动很大，而是因为系统不会限缩范围，只能把整个审查链重跑一遍，既浪费资源，也让团队更难看清这次到底修掉了什么。",
  "decision_rules": [
    "先标记 changed range、changed contract 和 changed invariants。",
    "默认只重跑受直接影响的 lens，再补一个最可能被牵连的邻接 lens。",
    "只有当主 contract、核心 state、关键 handoff 或 boundary 条件发生大变化时，才升级成 full audit。"
  ],
  "anti_patterns": [
    "任何修改都全量复查",
    "复查只看修改点，不看邻接副作用",
    "明明 contract 已大幅变化却还假装 targeted recheck 足够"
  ],
  "prompt_primitives": [
    "这次变更直接影响哪些 lens",
    "最可能被副作用波及的邻接 lens 是什么",
    "当前是否已经越过 targeted recheck 的边界"
  ],
  "evaluation_checks": [
    "recheck scope 是否被明确限定",
    "是否补了至少一个副作用 lens",
    "是否在需要时诚实升级成 full audit"
  ],
  "links": ["ka.metrics-handoff-compression", "ka.review-lens-isolation", "ka.command-artifact-mapping"],
  "source_status": "synthesized"
}
---
# 定向复查回路

复查的目标不是再证明一遍系统很认真，而是最快确认“这次改动是否真的修到了该修的层，而且有没有带来新副作用”。

这要求复查默认是 range-limited 的。你修的是对白口吻，就优先回查 `expression_integrity`，再补一个最容易被牵连的 `contract_fit` 或 `continuity_invariants`；你改的是 branch map 收束逻辑，就回查 `mechanics_pressure` 和 `continuity_invariants`；只有当主 contract 被改了，才升级成 full audit。

这样质检层才不会变成另一个拖慢开发的重型流程。

## TODOs：待回答问题

- [ ] 哪些变更最容易伪装成小修，实际已经应该升级 full audit？
- [ ] 对 team workflow 和 project surface 这类治理型 artifact，邻接 lens 应如何选？
- [ ] 是否需要把 `changed range` 标准化成 machine-readable 字段？
