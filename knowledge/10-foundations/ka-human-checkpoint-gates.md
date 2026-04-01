---
{
  "id": "ka.human-checkpoint-gates",
  "type": "knowledge_atom",
  "title": "人工检查关口",
  "kind": "heuristic",
  "summary": "human-in-the-loop 不是随时来一句“你觉得呢”，而是要在关键风险点设置有明确权限和明确问题的人工关口。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "character", "structure", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "人工参与过早会拖慢探索，过晚会放大返工；没有明确 gate 的 human review 往往只会制造泛化意见。",
  "decision_rules": [
    "只在会改变方向、边界、IP 连续性、商业风险或最终批准权的节点上设置人类关口。",
    "每个 gate 都要写清是批准、反驳、补充证据，还是只做范围修正。",
    "human review 问题必须具体到当前 artifact，而不是把所有判断重新打开。"
  ],
  "anti_patterns": [
    "每一步都要求人类确认，导致团队失去并行速度",
    "直到成稿才让人类第一次看到核心方向",
    "把人类 reviewer 当成没有明确任务的总裁判"
  ],
  "prompt_primitives": [
    "这个节点的人类到底有 veto 权、建议权还是补证据权",
    "如果不在这里过 gate，后面最贵的返工会发生在哪里",
    "这次 review 最多只允许重新打开哪几个决策"
  ],
  "evaluation_checks": [
    "checkpoint 是否放在真正高风险节点",
    "每个 gate 的权限和问题是否明确",
    "人类输入是否被结构化吸收，而不是重新把任务打散"
  ],
  "links": ["ka.boundary-first-guidance", "ka.scope-correction", "ka.ip-voice-continuity"],
  "source_status": "synthesized"
}
---
# 人工检查关口

很多所谓 human-in-the-loop，其实只是“人时不时来插一句”。这不是真正的协作机制，而是一种不稳定的打断。真正有效的人工关口应该像制作流程里的检查点：过不过、谁能拍板、拍板依据是什么，都得清楚。

好关口有两个效果。第一，它能保护发散阶段，不让所有探索都被过早保守化。第二，它能在高成本节点前把真正该由人类承担的判断收回来，比如 IP 连续性、审美方向、客户或平台底线、最终 greenlight。

如果关口位置错了，团队要么会被 review 拖死，要么会在错误方向上越跑越快。Agent Skill 要做的不是“让人多参与”，而是“让人只在该参与的时候参与”。

## TODOs：待回答问题

- [ ] 不同 team mode 下，人类关口的密度和权限是否应该显著不同？
- [ ] 当人类 stakeholder 不只一个，且意见可能互相冲突时，gate 机制该如何设主审和次审？
- [ ] 对品牌、平台、IP 三类高约束项目，哪些关口必须提前，哪些可以延后？
- [ ] 是否需要把 human checkpoint 分成“创意判断 gate”和“生产/合规 gate”两套？
- [ ] 当人类无法及时反馈时，系统是否需要自动降级到更保守的 team mode？
