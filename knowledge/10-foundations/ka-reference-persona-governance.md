---
{
  "id": "ka.reference-persona-governance",
  "type": "knowledge_atom",
  "title": "参考人物型 Subagent 治理",
  "kind": "boundary_rule",
  "summary": "真实人物、公司或创作流派可以作为参考 persona 的灵感来源，但在仓库中应以 craft lens 和 workflow lineage 的方式出现，而不是无边界的直接 impersonation。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "一旦把名编剧 / 名导演直接塞进 subagent 机制，系统很容易从‘借鉴决策逻辑’滑向‘假装这个人本人在说话’，进而把创作参考误做成教条模仿。",
  "decision_rules": [
    "默认用 inspired_by 或 calibrated_reference 两级，不把参考 persona 写成绝对权威。",
    "reference persona 的职责是施加特定 craft 压力、审美偏置或 workflow 习惯，而不是接管 route、rubric 和 hard boundary。",
    "任何 persona profile 都必须声明 strengths、misuse_risks、loading_cap 和 blocked_use。"
  ],
  "anti_patterns": [
    "要求 persona 精确模仿某位在世创作者本人",
    "把 famous creator 的气质当成跨场景的万能正确答案",
    "让 persona lens 覆盖掉 medium、audience 或 production 约束"
  ],
  "prompt_primitives": [
    "这个 persona 的价值到底是 workflow 形状、判断倾向，还是语体压力",
    "它允许影响哪些决策，不允许影响哪些决策",
    "如果不用真实人物名，只保留 craft lineage，这个 subagent 是否仍然成立"
  ],
  "evaluation_checks": [
    "persona profile 是否说明了允许借用的部分与禁止借用的部分",
    "persona 是否只作为 lens，而非最终 merge owner",
    "non-dogma note 是否清楚说明它只是参考路径之一"
  ],
  "links": ["ka.creative-pluralism", "ka.false-universal-warning", "ka.scope-correction", "ka.subagent-cast-composition"],
  "source_status": "synthesized"
}
---
# 参考人物型 Subagent 治理

真实人物、真实公司、真实流派，本身就是剧本创作知识的重要来源。问题不在于能不能参考，而在于怎么参考。如果仓库只是说“不要碰真实人物”，那会损失大量有价值的 workflow 经验和 craft lineage。如果仓库反过来说“那就直接扮演他们”，系统又会滑向僵化模仿。

更稳的做法，是把参考 persona 设计成一种“受限的压力镜头”。它不是替代 route 的大脑，而是给当前任务施加某种额外的创作偏置：更强调 moral collision、更强调 visual humanity、更强调 verbal combat、更强调 systemic choice。这种偏置可以帮助系统接近高水平团队的工作方式，但不能把它变成唯一审美法院。

参考 persona 的价值，应该主要体现在：
- 它让某些取舍更鲜明；
- 它让某些 failure mode 更早暴露；
- 它让某些创作语言更接近真实业内思考；
- 但它不会凌驾于协议、边界、媒介容器和人类关口之上。

## TODOs：待回答问题

- [ ] inspired_by 与 calibrated_reference 的分界线，是否需要更明确的操作标准？
- [ ] 对已经形成强公共人格的在世创作者，仓库是否需要更严格的 persona loading cap？
- [ ] 哪些真实公司 / studio workflow 更适合抽成团队 persona，而不是个人 persona？
- [ ] persona profile 是否需要单独记录“哪些常见误读最容易被新手拿去模仿”？
- [ ] 当 persona lens 和 audience / production reality 明显冲突时，系统应该如何排序？
