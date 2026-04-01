---
{
  "id": "ka.process-node-specialization",
  "type": "knowledge_atom",
  "title": "流程节点专门化",
  "kind": "heuristic",
  "summary": "多智能体系统里的很多关键节点不是 craft 专家，而是 process node，例如 divergence、counterexample、triage、merge、review。把它们和写作专家混成一类，会让流程能力隐身。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "仓库很容易只想着‘要哪些写作专家’，却忽略了真正决定流程质量的节点型角色，导致系统会写，但不会发散、不会保留反例、不会 triage、不会收束、不会审查。",
  "decision_rules": [
    "至少把功能型 subagent 和流程节点分成两层，不要混成一个大角色表。",
    "当流程复杂、stake 高或需要强 review 纪律时，优先补 process-node，而不是盲目增加 craft specialist。",
    "process-node 的质量标准应是推进质量和错误暴露率，而不是文本华丽度。"
  ],
  "anti_patterns": [
    "把 divergence、triage、merge 都丢给同一个 story architect",
    "只有创意专家，没有任何 counterexample keeper 或 review node",
    "流程节点也被要求输出像成稿一样的长文本"
  ],
  "prompt_primitives": [
    "当前任务最缺的到底是 craft 专长，还是 process discipline",
    "这个节点的职责是扩容、缩容、审查、还是转交",
    "如果不补这个流程节点，系统最容易在哪里出错"
  ],
  "evaluation_checks": [
    "流程节点是否被独立命名并拥有清楚 mandate",
    "process-node 是否真的减少了 drift、返工或无效并行",
    "团队结构是否把写作能力和流程能力区分开来"
  ],
  "links": ["ka.parallel-lane-governance", "ka.handoff-packet-discipline", "ka.two-stage-review-loop", "ka.subagent-cast-composition"],
  "source_status": "synthesized"
}
---
# 流程节点专门化

很多人一想到多智能体，就会先想“我要一个结构专家、一个对白专家、一个世界观专家”。这当然没错，但真正让系统变专业的，往往不是再多一个 craft specialist，而是补上流程节点：谁负责保留反例，谁负责 triage，谁负责 merge，谁负责 spec review，谁负责 quality review。

流程节点的作用，是把“会写”变成“会合作”。没有这些节点，再多专家都可能只是平行写作者；有了这些节点，系统才开始像一个真正能推进复杂任务的团队。

## TODOs：待回答问题

- [ ] 哪些流程节点适合作为 repo 级固定角色，哪些应按 medium 或 stage 动态生成？
- [ ] process-node 的评估标准是否应该和 functional subagent 完全分离？
- [ ] 当任务本身很小的时候，哪些流程节点可以安全折叠，哪些绝不能折叠？
- [ ] 是否需要为 process-node 单独建立 fixture 失败案例集？
- [ ] 哪些现有技能其实本质上更像 process-node，而不是 craft skill？
