---
{
  "id": "ka.story-memory-checkpoint",
  "type": "knowledge_atom",
  "title": "故事记忆检查点",
  "kind": "artifact_heuristic",
  "summary": "长篇、分集或多协作者写作不该每次都重新加载全量上下文；应该把当前可继续推进所需的最小故事状态压成一个可续写、可交接、可检查的检查点。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "game_narrative", "branching_interactive"],
  "stages": ["structure", "outline", "scene", "rewrite", "adaptation"],
  "problem": "长期项目、跨会话创作或多 agent / 多人 handoff 时，协作者经常靠全量回读或模糊记忆恢复上下文，导致上下文过载、连续性漂移、伏笔遗失和重写成本膨胀。",
  "decision_rules": [
    "检查点要压缩状态，不要重抄全文。",
    "至少分开记录角色/关系当前状态、未兑现承诺、连续性不变量、外部推进节奏、内部情绪节奏和下次安全切入点。",
    "把稳定事实、暂时假设和待验证推断分层，避免把 room 里的临时猜想误当 canon。",
    "在结构边界、集与集之间、重大改稿前后、跨 lane handoff 前后优先生成检查点，而不是继续堆原文上下文。"
  ],
  "anti_patterns": [
    "把检查点写成剧情复述",
    "只总结气氛，不记录未兑现承诺和状态变化",
    "把角色现状、世界规则和 room 假设混成一个层",
    "为了续写安全又把整份 outline 或 draft 全量塞回去"
  ],
  "prompt_primitives": [
    "如果下一轮只允许加载一个最小 handoff 包，哪些状态必须进检查点",
    "哪些伏笔、关系、秘密、约束如果丢了会直接写崩",
    "当前外部事件推进和内部情绪推进分别走到哪",
    "下一次恢复写作时，最安全的 entrypoint 是哪一段、哪一场、哪一个决策节点"
  ],
  "evaluation_checks": [
    "检查点是否比原始材料短得多，但仍保住续写所需的关键状态",
    "是否明确区分已兑现、未兑现和待验证的信息",
    "是否给出可执行的 next entrypoint，而不是只做回顾",
    "是否能在不重载全文的前提下支持 continuity-safe handoff"
  ],
  "links": ["ka.script-as-coordination-artifact", "ka.room-artifact-ladder", "ka.source-span-traceability"],
  "source_status": "synthesized"
}
---
# 故事记忆检查点

很多团队和很多 Agent 的默认做法，是一旦项目变长、分支变多、改稿变深，就把更多原文重新喂回去。这种做法短期看像“更稳”，长期看其实是在拿上下文过载换暂时安心。

真正更稳的做法，是把“下一轮继续推进真正需要知道什么”压成一个检查点。它不是摘要，不是大纲备份，也不是情绪笔记，而是一种最小可续写状态包。

一个合格的检查点，至少要回答六件事：

1. 现在人物和关系处在什么状态。
2. 哪些承诺已经种下但还没兑现。
3. 哪些连续性不变量不能漂。
4. 外部推进的压力波形现在走到哪。
5. 内部情绪/认知的压力波形走到哪。
6. 下一次最安全的恢复入口在哪里。

如果这一层做得好，后续写作不需要每次回读全量材料；如果这一层做得差，项目越大，模型和人都会越依赖“重新读一遍”，最后把连续性管理变成上下文堆砌。

## TODOs：待回答问题

- [ ] 什么体量的项目才值得显式建立 checkpoint cadence，而不是临时手工记要点？
- [ ] feature、episodic、interactive 三类项目的 checkpoint 字段是否应该有不同默认模板？
- [ ] 哪些信息适合进入 checkpoint，哪些信息更适合只留在 canonical source 而不进入 handoff 包？
- [ ] 一个 checkpoint 多长还算“压缩成功”，多长就已经退化成重新搬运原文？
- [ ] 是否需要单独区分 writing checkpoint、room checkpoint、review checkpoint 三种契约？
