---
{
  "id": "ka.source-of-truth-runtime-split",
  "type": "knowledge_atom",
  "title": "真源与运行时分层",
  "kind": "heuristic",
  "summary": "长周期创作项目必须区分 source of truth 与 runtime state；否则 human 和 agent 会不断编辑错误的表面层，最终把缓存当真相。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "一旦把可编辑真源、派生缓存、工作流状态和运行时 packet 混在一起，系统就会开始从错误文件继续写作或审查，导致长期漂移和不可追溯。",
  "decision_rules": [
    "为每个项目显式标注哪些文件是 canonical source，哪些只是 runtime state、mirror、cache 或 telemetry。",
    "默认只允许人和长期规划 agent 直接编辑真源；运行时产物应由编译或 sync 生成。",
    "如果 derived artifact 看起来像真源，也要在 surface map 中明确它的从属关系和刷新规则。"
  ],
  "anti_patterns": [
    "把 outline draft、workflow cache、runtime packet 当成长期可手改真相",
    "多个文件都宣称自己是世界观或大纲真源",
    "review 结果回写到了派生缓存，却没有回到 canonical source"
  ],
  "prompt_primitives": [
    "这个项目里哪些文件能直接改，哪些文件只能由 sync 或 compile 生成",
    "如果 human 改了真源，哪些 runtime 状态必须刷新",
    "哪些 artifact 只是为了可见性存在，不能被误当真相"
  ],
  "evaluation_checks": [
    "真源与运行时状态是否明确分层",
    "每个 derived artifact 是否有清楚的上游来源",
    "人类协作者是否不容易误编辑 runtime surface"
  ],
  "links": ["ka.canonical-packet-assembly", "ka.phase-entrypoint-handoff", "ka.command-artifact-mapping"],
  "source_status": "synthesized"
}
---
# 真源与运行时分层

外部项目里最值得借鉴的一条，不是它们用了多少命令，而是它们都在试图解决同一个底层问题：长期创作过程中，什么才是真正应该被编辑和维护的“真相”，什么只是为了运行、调试、可视化和审查而生成的衍生产物。

如果没有这层分离，系统很快就会出现两个问题。第一，人会去改那些“看起来最顺手”的文件，而不是该改的文件。第二，Agent 会拿看起来更新但其实只是缓存的文件继续推演，最后越写越偏。

所以这个 atom 不是在讨论文件组织习惯，而是在讨论创作系统的记忆纪律。

## TODOs：待回答问题

- [ ] 不同媒介下，source-of-truth 的最小集合是否应该不同？
- [ ] 哪些 runtime mirror 需要允许人工修正，哪些应完全禁止？
- [ ] 当 canonical source 与 runtime state 冲突时，系统应如何暴露并处理？
- [ ] 是否需要为“编辑错误表面层”的问题建立专门 regression fixture？
