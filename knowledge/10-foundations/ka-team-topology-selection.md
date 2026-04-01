---
{
  "id": "ka.team-topology-selection",
  "type": "knowledge_atom",
  "title": "团队拓扑选择",
  "kind": "heuristic",
  "summary": "不同剧本项目需要不同协作拓扑，showrunner room、story trust、campaign strike team、interactive cell 和 continuity board 不能互相替代。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "rewrite", "adaptation"],
  "problem": "团队设计过于单一，导致要么决策过慢、要么并行失控、要么所有项目都被错误地套进同一种 room 模式。",
  "decision_rules": [
    "先判断项目真正需要的是集中决策、并行发散、跨部门耦合，还是 IP 连续性保护。",
    "让 team mode 服从媒介容器、开发阶段、委制语境和风险结构，而不是服从流行组织话术。",
    "只有当 artifact ladder 和 decision owner 清楚时，团队拓扑才算选对。"
  ],
  "anti_patterns": [
    "把所有项目都做成同一种 writers' room",
    "并行太早但没有共享真相包和收口机制",
    "需要 IP 守门时却只配发散型创意团队"
  ],
  "prompt_primitives": [
    "当前项目最需要集中锁定的东西是什么，最需要并行探索的东西又是什么",
    "谁拥有最终决策权，谁只拥有建议权",
    "这个项目更像 room、pod、cell、board 还是 strike team"
  ],
  "evaluation_checks": [
    "team mode 是否匹配媒介和开发阶段",
    "并行 lanes 是否建立在清晰 handoff 上",
    "决策 owner 和 review gate 是否清楚"
  ],
  "links": ["ka.commissioning-fit", "ka.scenario-factorization", "ka.parallel-lane-governance"],
  "source_status": "synthesized"
}
---
# 团队拓扑选择

多智能体或多人团队协作最容易犯的错，不是“人太少”，而是“组织方式错了”。明明是一个需要强中心收敛的 IP 改编项目，却上来就做开放式发散；明明是一个需要多端实验的短视频 campaign，却还沿用长周期线性开发。

所谓 team topology，说白了就是：谁负责发散，谁负责收口，谁负责守边界，谁负责把不同 lane 汇总成一个可继续推进的版本。不同项目天然需要不同形状。有的更像 writers' room，有的更像 director-writer-producer pod，有的更像 story trust，有的更像 campaign strike team。

对 Agent 来说，团队拓扑不是运营名词，而是路由后的第二层决策。它决定后面应该怎么切 role、怎么分工、怎么交接、怎么避免集体把时间浪费在不该同步的环节上。

## TODOs：待回答问题

- [ ] 团队拓扑是否应该进一步按“强作者中心”“showrunner 中心”“品牌客户中心”“系统设计中心”再细分？
- [ ] 同一个项目在不同阶段切换 team mode 的最佳时机，是否可以沉淀成更明确的规则？
- [ ] 多智能体条件下，什么情况下单一 orchestrator 反而会成为瓶颈？
- [ ] 当用户没有明确团队资源和 human availability 时，系统默认该选最小 pod 还是 room 结构？
- [ ] 如果项目同时具有平台委制、品牌露出和 IP 连续性三种高压约束，仓库应如何选择主拓扑？
