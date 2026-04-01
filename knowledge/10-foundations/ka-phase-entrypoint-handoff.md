---
{
  "id": "ka.phase-entrypoint-handoff",
  "type": "knowledge_atom",
  "title": "阶段入口与显式交接",
  "kind": "workflow_rule",
  "summary": "长期创作系统应区分 planning、drafting、review、compliance、export 等 phase 的入口，并显式 handoff，而不是让一个通用入口对所有阶段一把梭。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "当所有阶段都靠一个模糊入口推进时，系统很难知道什么时候该先补资产，什么时候该先写正文，什么时候该先审查，最后会把 planning 和 drafting 混在一起。",
  "decision_rules": [
    "为不同 phase 提供不同 entrypoint，并写清它们的前置条件与交接条件。",
    "planning entrypoint 产出的是可写资产，不是直接成稿；drafting entrypoint 产出的是局部文本，不是重新定义世界规则。",
    "handoff 必须包含‘现在为什么可以切到下一阶段’以及‘下一阶段不该重新打开什么’。"
  ],
  "anti_patterns": [
    "从 idea 直接跳到完整场景成稿",
    "drafting agent 持续回改基础设定却没有明确 handoff",
    "review 入口既做规划又做写作又做定稿"
  ],
  "prompt_primitives": [
    "当前应该先走 planning 入口还是 drafting 入口",
    "进入下一阶段前，哪些资产必须满足门槛",
    "handoff 包里要写清哪些 survive / freeze / reopen 条件"
  ],
  "evaluation_checks": [
    "phase entrypoint 是否清楚且相互区分",
    "handoff 是否说明了前置门槛和禁 reopen 区",
    "系统是否避免了 planning 与 drafting 的职责混淆"
  ],
  "links": ["ka.canonical-packet-assembly", "ka.team-topology-selection", "ka.two-stage-review-loop"],
  "source_status": "synthesized"
}
---
# 阶段入口与显式交接

很多长周期创作系统真正稳定的原因，不是模型更强，而是阶段边界更清楚。规划入口先把灵感整理成资产；写作入口再基于资产推进正文；审查入口单独做质量检查；导出入口只负责交付，不重新发明内容。

这种分层对剧本项目同样重要。尤其是在多智能体或 human-in-the-loop 条件下，如果阶段入口不清楚，就很容易让每个 Agent 都觉得自己可以顺手改动更上游的东西，最后整条链都失去门槛和秩序。

## TODOs：待回答问题

- [ ] 当前仓库最需要哪些一等入口，而哪些入口不该过早产品化？
- [ ] planning 与 drafting 之间的 handoff 门槛，是否应按 medium 有不同标准？
- [ ] 什么时候 review 入口应该允许回退上游资产，什么时候只应生成问题清单？
- [ ] 是否需要为 export 单独设计一组 entrypoint，而不是并入 review 或 drafting？
