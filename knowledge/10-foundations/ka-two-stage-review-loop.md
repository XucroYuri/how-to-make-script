---
{
  "id": "ka.two-stage-review-loop",
  "type": "knowledge_atom",
  "title": "两阶段审查回路",
  "kind": "workflow_rule",
  "summary": "复杂 subagent 工作不应只有一个笼统 review。先做 spec compliance，再做 quality review，能显著降低‘做错方向但写得很漂亮’或‘方向对但实现很脏’的问题。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "多智能体协作里最常见的返工，不是完全不会做，而是 spec 没对齐就开始谈 quality，或者 quality 很强却根本没做对题。",
  "decision_rules": [
    "当任务有明确 contract 时，先过 spec compliance，再过 quality review。",
    "spec reviewer 关注有没有漏做、做多、做偏；quality reviewer 关注实现质量、组合合理性、表达与治理风险。",
    "在 spec 未通过前，不要进入 quality review，也不要让漂亮实现掩盖错题。"
  ],
  "anti_patterns": [
    "一个 reviewer 同时模糊地看方向和细节",
    "implementer 自评就算 review 完成",
    "质量很好但已经偏离 output contract 还继续往前推进"
  ],
  "prompt_primitives": [
    "这次交付的 spec 到底是什么，哪些属于额外发挥",
    "如果只看 contract，这份结果有没有漏项、越权或错位",
    "在 spec 通过后，质量层面最可能出的问题是什么"
  ],
  "evaluation_checks": [
    "spec review 与 quality review 是否明确分开",
    "review loop 是否在发现问题后真正回流 implementer",
    "最终结果是否同时满足 contract 和质量要求"
  ],
  "links": ["ka.process-node-specialization", "ka.convergence-owner-discipline", "ka.subagent-context-budgeting"],
  "source_status": "synthesized"
}
---
# 两阶段审查回路

多智能体系统里，最贵的错误往往不是“写得烂”，而是“根本写错了方向，还花了很多 token 把它写得很像那么回事”。这就是为什么 spec compliance 和 quality review 必须拆开。

第一阶段解决的是：有没有按题目做、有没有越界、有没有漏项、有没有把一个 mode 误当另一个 mode。第二阶段才去看：做得够不够稳、结构是否优雅、组合是否合理、表达是否会在真实流程里出事。

这条原则对 repo 本身的知识资产开发也成立。只要任务是“新增协议 / 新增 skill / 新增 route / 新增拓扑”，就不该把“看起来写得不错”和“真的符合设计目标”混成一个 review。

## TODOs：待回答问题

- [ ] 哪些任务必须强制两阶段 review，哪些任务可以降级成单 review？
- [ ] spec reviewer 是否需要独立于 quality reviewer 的默认角色池？
- [ ] 当任务主要是 docs / knowledge 资产时，quality review 的重点应该如何定义？
- [ ] 两阶段 review 的结果是否应进入 future fixture 或 case-study 层？
- [ ] 某些 high-risk route 是否还需要第三阶段的 final convergence audit？
