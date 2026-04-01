---
{
  "id": "rb.project-surface-map",
  "type": "evaluation_rubric",
  "title": "Project Surface Map Rubric",
  "applies_to": ["project_surface_map"],
  "dimensions": [
    {"name": "truth_runtime_split", "question": "真源与运行时表面是否清楚区分，避免误编辑和误加载"},
    {"name": "entrypoint_clarity", "question": "planning、drafting、review、compliance、export 和必要 checkpoint surface 的入口与前置条件是否明确"},
    {"name": "packet_traceability", "question": "canonical packet 是否可检查、可追溯、可解释"},
    {"name": "artifact_ladder_fit", "question": "artifact ladder 是否匹配当前媒介与工作方式"},
    {"name": "sync_governance", "question": "source 改动到 runtime state 的 sync 规则是否清楚"},
    {"name": "human_edit_policy", "question": "哪些 surface 可手改、哪些只能派生生成，是否明确"}
  ],
  "scoring_bands": {
    "excellent": "真源、运行时、入口、packet、审查面和导出面都清楚，长期协作中不容易误改或失真。",
    "workable": "大体可用，但仍有表面层混淆、sync 规则不清或 review/export 面不足的问题。",
    "weak": "更像抽象流程图，而不是可长期维护的项目表面设计。"
  },
  "hard_fail_rules": [
    "没有明确 source of truth",
    "runtime cache 或 mirror 被默认当成可长期编辑真源",
    "没有 packet 或 packet 不可追溯",
    "phase entrypoint 没有前置条件和 handoff 规则",
    "长周期项目需要 continuity checkpoint 却完全没有对应 surface",
    "review surface 和 export surface 完全缺失"
  ],
  "rewrite_actions": [
    "补写 canonical source、runtime state、review surface 和 export surface",
    "明确 phase entrypoints、handoff 条件与 sync 规则",
    "对长周期项目补一个明确的 checkpoint surface",
    "补充 canonical packet 层和 inspectability 说明",
    "明确 human-edit policy 和 wrong-edit 风险"
  ]
}
---
# Project Surface Map Rubric

项目表面图最怕“看起来很懂架构，实际上协作者一上手就会改错文件”。这份 rubric 不在评术语密度，而是在评它能不能把长期创作里的真源、运行态、交接、审查和导出表面真正分开。

如果没有这层，系统越复杂，人越容易绕过它；有了这层，复杂系统才可能长期稳定。

## TODOs：待回答问题

- [ ] rubric 是否应按 medium 分不同权重？
- [ ] packet_traceability 是否需要更细的等级标准？
- [ ] 对极简个人项目，多少 surface 才算“足够”，而不是过度设计？
- [ ] export surface 是否应该有独立的 delivery-risk 检查？
