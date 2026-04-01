---
{
  "id": "wp.context-loading-plan",
  "type": "workflow_protocol",
  "title": "上下文加载计划协议",
  "goal": "在正式生成前，输出一份 context_loading_plan，明确当前请求应加载哪些核心资产、哪些候选扩展、为何扩展，以及何时必须停止扩容。",
  "input_contract": ["request", "route candidate", "output target", "constraints", "explicit depth ask", "none"],
  "output_contract": ["context_loading_plan"],
  "preconditions": [
    "用户请求涉及 Agent Skill 设计、加载策略、复杂教学、比较性创作，或当前 route 存在明显不确定性",
    "至少可以锁定一个候选 output 或 creative problem"
  ],
  "steps": [
    "先锁定 primary route 和当前 route certainty，避免在未分类前扩容。",
    "在 `route_kernel`、`focus_pack`、`compare_pack`、`teaching_pack`、`survey_pack` 中选一个 loading mode。",
    "如果当前请求属于宽理论或背景支持问题，先从 background bundle registry 里选一个 research anchor。",
    "如果连续性压力是主要扩容原因，优先评估是否应该产出 story_memory_checkpoint，而不是继续扩大 bundle。",
    "列出 mandatory bundle：一个 primary protocol、一个 primary rubric、必要 linked atoms，以及在需要时最多一个背景包或场景分类入口。",
    "列出 optional expansion queue，并说明每一项只有在什么 trigger 下才值得加载。",
    "写明 explicit stop conditions 和 context-corrosion checks，防止 bundle 无限膨胀。"
  ],
  "fallbacks": [
    "若 route certainty 过低，先返回需要补充的最小信息，而不是假装能制定稳定 loading plan。",
    "若用户只要直接产物，不需要系统设计或教学比较，则回退到 focus_pack，不单独展开 loading plan。"
  ],
  "stop_conditions": [
    "loading mode 已明确，mandatory bundle 足以解释当前 primary answer",
    "每个 optional reference 都带有清楚的 expansion trigger",
    "至少写出两个 context-corrosion signals 或 stop rules"
  ],
  "rubrics": ["rb.context-loading-plan"],
  "linked_atoms": ["ka.bounded-context-loading", "ka.reference-expansion-balance", "ka.context-corrosion-signals", "ka.scenario-factorization", "ka.story-memory-checkpoint"],
  "budget_class": "M",
  "mandatory_atom_count": 5,
  "expansion_allowed": true
}
---
# 上下文加载计划协议

这个协议的核心，不是把加载策略写得多复杂，而是把“为什么现在只加载这些”和“为什么现在不该再加更多”都说清楚。

对当前仓库来说，最大的系统风险不是知识不够，而是加载没有分级。只要没有 loading plan，Agent 很容易在 route 已经够清楚的情况下继续加 scenario atlas、reference pack、reality lens、background docs、邻近 protocol，最后把自己拖进 summary 模式。

所以这个协议其实是在保护生成质量。它把“路由”“扩容”“停止”三个动作分开，让 Agent 有机会保持一个专业但不僵化的 balance。
当问题只是“下次继续写时别丢状态”，最好的答案经常不是再加载五份相邻资产，而是先产出一个可恢复的检查点。

## TODOs：待回答问题

- [ ] 默认 loading modes 是否还需要再细分为 narrative/commercial/interactive 三套？
- [ ] context_loading_plan 是否应该支持显式的 token budget 或 bundle budget？
- [ ] 对创意延伸型请求，何时该从 compare_pack 升到 teaching_pack 或 survey_pack？
- [ ] 是否需要单独记录“必须禁止同时加载”的冲突资产组合？
- [ ] 什么时候 route certainty 足够低，应该先追问而不是制定 loading plan？
