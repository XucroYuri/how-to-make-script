---
{
  "id": "ka.feature-development-pod",
  "type": "knowledge_atom",
  "title": "电影开发小组模式",
  "kind": "pattern",
  "summary": "电影开发更像受控串行开发加阶段性评审，而不是持续开放式 writers' room。",
  "mediums": ["feature_film"],
  "stages": ["ideation", "premise", "structure", "outline", "rewrite", "adaptation"],
  "problem": "把电影开发误当成 TV room，会导致前期发散过多、角色责任混乱、rewrite mandate 不清。",
  "decision_rules": [
    "先锁概念、rights/mandate、开发目标，再进入 draft 与 rewrite lanes。",
    "feature 模式通常需要较强的 producer/director/showrunner-like synthesis，而不是长期多人平权发散。",
    "每轮 rewrite 前要明确 page-one mandate、不可动核心和 note response 目标。"
  ],
  "anti_patterns": [
    "像 room 一样无限发散但无人负责收束",
    "没有 rewrite mandate 就直接进入大改",
    "把 rights、credit、producer pass 风险留到后面才处理"
  ],
  "prompt_primitives": [
    "这个 feature 的开发责任链是谁到谁",
    "当前轮次最需要锁定的是概念、结构、人物还是 production note",
    "哪些 note 属于必须执行，哪些只是 alternative pressure"
  ],
  "evaluation_checks": [
    "开发顺序是否清楚",
    "rewrite mandate 是否明确",
    "高成本决策是否留给了合适的 review gate"
  ],
  "links": ["ka.team-topology-selection", "ka.commissioning-fit", "ka.boundary-first-guidance"],
  "source_status": "curated"
}
---
# 电影开发小组模式

电影开发通常不是常态化 writers' room。它更常见的是一个相对窄的责任链：编剧、制片、导演、公司开发或 exec，在不同阶段以不同密度介入。它的重点不在于“多少人一起想”，而在于“谁有权定义这一轮到底要改什么”。

因此 feature 的团队模式应该优先强调：
- 清晰的开发 mandate；
- 有限但高价值的 specialist lane；
- 强收束的 synthesis 角色；
- 阶段性人工 gate。

如果把它做成无限并行 brainstorm，很容易看起来热闹，实则没有任何人对一版可落地的 draft 负责。

## TODOs：待回答问题

- [ ] 独立电影、流媒体平台片和传统 studio feature 是否需要三套不同 pod 变体？
- [ ] 当导演尚未加入时，feature pod 的最终收束角色应该是谁？
- [ ] 哪些 feature 开发阶段最适合 parallel lanes，哪些阶段反而应极度收窄？
