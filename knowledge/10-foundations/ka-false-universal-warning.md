---
{
  "id": "ka.false-universal-warning",
  "type": "knowledge_atom",
  "title": "伪普遍规律预警",
  "kind": "failure_mode",
  "summary": "剧本知识最常见的错误之一，是把局部成功经验误写成跨媒介、跨时代、跨受众的普遍定律。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "rewrite", "adaptation"],
  "problem": "知识条目表面上很有把握，但真实成立范围比写出来的窄得多，导致误导后续创作与路由。",
  "decision_rules": [
    "当一个规则听起来过于稳定时，先追问它依赖的媒介、平台、产业和历史条件。",
    "任何强规则都应优先寻找反例，而不是只找成功案例。",
    "如果一条规则只能在有限条件下成立，应缩窄表述，而不是保留宏大说法。"
  ],
  "anti_patterns": [
    "成功案例即普遍规律",
    "忽略反例",
    "适用范围未写出却使用强断言"
  ],
  "prompt_primitives": [
    "这条规则在哪些条件下会失效",
    "有哪些反例能迫使它缩窄",
    "如果保留这条规则，它的适用边界应该怎么写"
  ],
  "evaluation_checks": [
    "是否明确了适用边界",
    "是否考虑了至少一种反例或失效条件",
    "规则强度是否与证据强度匹配"
  ],
  "links": ["ka.screenwriting-history-shift", "ka.creative-pluralism", "ka.commissioning-fit", "ka.audience-need-state"],
  "source_status": "synthesized"
}
---
# 伪普遍规律预警

“伪普遍规律”是很多剧本教学和经验总结里最常见的病。它看上去像在给清晰判断，实际是在偷换适用范围，把某种局部有效经验包装成到处适用的准则。

这类错误尤其容易出现在三种地方：经典案例总结、平台爆款复盘、以及维护者过度自信的经验陈述。它们不一定全错，但往往比写出来的范围更窄。

仓库如果不主动建立这种预警机制，很快就会从“帮助决策”滑向“制造教条”。所以任何强规则都应该默认接受一个追问：它在哪些地方会坏？

## TODOs：待回答问题

- [ ] 哪些现有 atom 或 docs 最可能含有伪普遍化风险？
- [ ] 反例应该如何进入 repo，才能真正压缩伪普遍规律的表达空间？
- [ ] 是否需要单独的“counterexample registry”来收纳这些失效条件？
- [ ] 哪些强规则值得保留，即使反例存在，只是必须写清适用范围？
- [ ] 当社区对一条规则的适用范围持续争论时，何时该拆成两个并行规则？
