---
{
  "id": "ka.project-surface-taxonomy",
  "type": "knowledge_atom",
  "title": "项目表面层 taxonomy",
  "kind": "ontology",
  "summary": "定义长期剧本项目里 canonical source、runtime state、canonical packet、phase entrypoint、review surface、export surface 和 sync rule 的关系，避免真源与运行时混淆。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "如果长期项目没有显式的表面层设计，协作者会误改 derived files、把 mirror 当真源，并让 handoff、review 和 export 逐渐失去可追溯性。",
  "decision_rules": [
    "把 human-editable canonical source 和 derived runtime state 明确分开。",
    "让每个主要 phase 都有 entrypoint、handoff 条件和 sync rule。",
    "让 canonical packet 对单次 action 可检查、可解释，而不是隐式拼接。",
    "让 review surface 与 export surface 成为命名层，而不是正文尾部的副产品。"
  ],
  "anti_patterns": [
    "把 runtime mirror 默认当成真源",
    "让 packet 组装不可见",
    "planning、review、export 混在同一表面层"
  ],
  "prompt_primitives": [
    "哪些 artifacts 属于可编辑真源，哪些只是运行态派生物",
    "这次 phase 的 entrypoint、handoff 条件和 sync rule 分别是什么",
    "如果 review 或 export 出问题，能否追溯到产生它的 packet"
  ],
  "evaluation_checks": [
    "truth/runtime split 是否清楚",
    "entrypoint 与 handoff 是否明确",
    "review/export surfaces 是否独立可辨"
  ],
  "links": ["ka.source-of-truth-runtime-split", "ka.canonical-packet-assembly", "ka.phase-entrypoint-handoff", "ka.command-artifact-mapping"],
  "source_status": "synthesized"
}
---

# Project Surface Taxonomy

`project surface taxonomy` is the repository layer for designing how a long-running screenplay project should persist state, expose entrypoints, assemble packets, and separate editable truth from runtime artifacts.

It exists because a strong screenplay agent system is not only a routing problem. It is also a persistence and workflow-surface problem.

## Why This Layer Exists

Once a project runs beyond one reply, three questions become unavoidable:

- what files or artifacts are the editable source of truth;
- what files are only runtime state, caches, mirrors, or telemetry;
- how planning, drafting, review, compliance, and export surfaces hand off to each other.

If those layers are collapsed together, creative systems drift silently:
- people edit the wrong files;
- agents re-ingest stale mirrors as truth;
- handoffs become opaque;
- review outputs stop being traceable back to the packet that produced them.

## Core Terms

- `source_of_truth`: human-editable canonical artifacts that should be changed directly.
- `runtime_state`: derived artifacts, packet compilations, workflow state, caches, and telemetry.
- `canonical_packet`: the bounded assembled input for one concrete writing or review action.
- `entrypoint`: the named workflow surface that starts a phase, such as planning, drafting, reviewing, or exporting.
- `review_surface`: the checkpoint artifact where quality, compliance, continuity, or delivery concerns are evaluated.
- `export_surface`: the delivery artifact for downstream human teams, platforms, or tools.
- `sync_rule`: the rule that says how changes in canonical source must propagate to derived runtime state.

## Design Rules

1. Keep canonical truth editable and visible.
2. Keep runtime artifacts derived and disposable by default.
3. Make packet assembly inspectable.
4. Give each workflow phase a clear entrypoint and handoff.
5. Let review and export surfaces be explicit rather than hidden side effects.
6. Never let mirrors or caches quietly become the real source of truth.

## What This Layer Should Prevent

- editing derived files because they look easier to reach;
- turning long-horizon collaboration into a pile of unnamed state blobs;
- hiding what context actually went into a generation or review step;
- mixing planning artifacts with delivery artifacts until neither is trustworthy;
- forcing every screenplay medium to use the same artifact ladder without adaptation.

## Relation To Other Layers

- `team_workflow_blueprint` chooses the collaboration family.
- `expert_subagent_cast` chooses who participates.
- `subagent_dispatch_plan` chooses how they run.
- `project_surface_map` chooses where truth lives, what runtime produces, and how packets and exports are assembled.

## TODOs: Questions To Keep Open

- [ ] Which screenplay media need their own default project-surface template first?
- [ ] How should short-drama, feature, episodic, and branching projects differ in review and export surfaces?
- [ ] Which runtime artifacts are worth preserving long-term, and which should always be disposable?
- [ ] When should a packet be inspectable by default, and when is a lighter trace enough?
- [ ] How should the repo distinguish human-editable mirrors from machine-only caches?
