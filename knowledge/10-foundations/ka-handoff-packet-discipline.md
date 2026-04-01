---
{
  "id": "ka.handoff-packet-discipline",
  "type": "knowledge_atom",
  "title": "交接包纪律",
  "kind": "principle",
  "summary": "优秀的多智能体协作依赖小而准的 handoff packet，而不是把整段上下文原样甩给下一个角色。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "角色之间交接时上下文过量、目标不清、责任模糊，导致信息漂移和上下文腐化。",
  "decision_rules": [
    "handoff packet 只保留能改变下一步决策的状态，不保留整段历史复述。",
    "每次交接至少写明 working hypothesis、loaded bundle ids、open questions、confidence、recommended next agent、needs human review。",
    "如果下游角色需要的不是状态而是重新判断，就不要假装 handoff 足够，应显式回退到 route 或 human gate。"
  ],
  "anti_patterns": [
    "把所有上游讨论全文贴给下游",
    "交接只说“你接着写”却没有假设和风险说明",
    "把未解决争议伪装成已确定结论传下去"
  ],
  "prompt_primitives": [
    "下一个角色真正需要知道哪些状态",
    "哪些未决问题必须保留为开放问题而不是被偷渡成结论",
    "这次交接是否需要 human review 标记"
  ],
  "evaluation_checks": [
    "handoff 是否足够小而不失关键状态",
    "open questions 和 confidence 是否明确",
    "交接是否减少了漂移而不是扩大了漂移"
  ],
  "links": ["ka.bounded-context-loading", "ka.context-corrosion-signals", "ka.team-topology-selection"],
  "source_status": "synthesized"
}
---
# 交接包纪律

很多多智能体系统失败，不是因为没有 specialist，而是因为 specialist 之间交接得太差。上游把一大段历史、风格要求、争议、无关注释一股脑塞给下游，下游看起来拿到了“更多信息”，实际上拿到的是更多噪音。

对这个仓库来说，handoff packet 应该是 bounded loading 在团队协作层的延伸。它的作用不是记录一切，而是保护下一步决策的清晰度。一个好的交接包会告诉下游：当前假设是什么、已经加载了哪些 bundle、还有哪些开放问题、置信度如何、推荐交给谁、是否必须让人看一眼。

这样多角色协作才不会越来越像仓库摘要竞赛，而是像真实的专业分工。

## TODOs：待回答问题

- [ ] handoff packet 是否需要按不同 team mode 允许不同字段集？
- [ ] 对高并行场景，是否应加入 conflict summary 字段来显式记录 lane 间冲突？
- [ ] 什么时候 handoff 最好改成 review-board 汇总，而不是继续多站串行传递？
- [ ] 是否需要把 token budget 或 bundle budget 纳入 handoff packet 本身？
