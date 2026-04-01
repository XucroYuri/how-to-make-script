---
{
  "id": "ka.creative-pluralism",
  "type": "knowledge_atom",
  "title": "创作多路径",
  "kind": "principle",
  "summary": "同一个剧本问题经常存在多条有效路径，仓库应优先呈现 tradeoff，而不是伪装成只有一个正确答案。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "rewrite", "adaptation"],
  "problem": "系统过早把一个局部有效的方案写成全局最优，压缩了创意空间，也掩盖了真实 tradeoff。",
  "decision_rules": [
    "当至少两条路径都满足当前 brief 时，先呈现差异与代价，再考虑是否收敛。",
    "多路径不等于无判断，每条路径都要说明自己在优化什么、牺牲什么。",
    "如果一个建议只有在特定媒介、平台或受众条件下成立，必须把条件显式写出。"
  ],
  "anti_patterns": [
    "用单一路径冒充唯一真值",
    "把多样性误写成选择困难",
    "只给方案，不给 tradeoff"
  ],
  "prompt_primitives": [
    "这个问题至少还有哪两条不同但成立的路径",
    "每条路径分别在优化什么、牺牲什么",
    "在什么条件下应该从多路径收敛成单路径"
  ],
  "evaluation_checks": [
    "是否真的给出了彼此不同的路径",
    "每条路径的 tradeoff 是否清楚",
    "收敛条件是否可判断"
  ],
  "links": ["ka.false-universal-warning", "ka.divergence-convergence-loop", "ka.audience-need-state", "ka.commissioning-fit"],
  "source_status": "synthesized"
}
---
# 创作多路径

很多创作问题不是“谁对谁错”，而是“哪条路更适合当前条件”。一旦系统太早给出单一路径，它看起来更果断，实际上却更容易偷换前提，把一个局部解说成普遍解。

创作多路径的价值，不是把所有方案都列出来，而是承认：同一个 premise、同一个结构问题、同一个角色设计，常常至少有两到三种都成立的走法。它们真正不同的地方，不是优劣本身，而是各自在押注什么。

仓库因此不该把“多条路径并存”理解成噪音，而应理解成必要的信息密度。只有在 tradeoff 被说清楚以后，收敛才是有根据的，而不是拍脑袋的。

## TODOs：待回答问题

- [ ] 哪些阶段最适合默认给多路径，哪些阶段更适合快速收敛？
- [ ] 多路径输出到什么数量最有用，超过多少就会降低判断效率？
- [ ] 当用户明确只想要一个可执行方向时，系统应如何保留 pluralism 而不显得啰嗦？
- [ ] 哪些项目天然更适合单路径推进，例如高约束商业项目或 tight brief 项目？
- [ ] 多路径之间如果共享同一底层引擎，仓库应如何避免把“换皮方案”误写成新路径？
