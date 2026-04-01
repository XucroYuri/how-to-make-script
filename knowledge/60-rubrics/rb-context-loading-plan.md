---
{
  "id": "rb.context-loading-plan",
  "type": "evaluation_rubric",
  "title": "Context Loading Plan Rubric",
  "applies_to": ["context_loading_plan"],
  "dimensions": [
    {"name": "route_stability", "question": "plan 是否先锁定了 route，而不是边加载边漂移"},
    {"name": "bundle_discipline", "question": "mandatory bundle 是否足够小、足够清楚、足够解释当前任务"},
    {"name": "expansion_logic", "question": "optional expansions 是否真的有 trigger，而不是为了显得全面"},
    {"name": "corrosion_defense", "question": "是否写出了明确的 stop conditions 与腐化信号"}
  ],
  "scoring_bands": {
    "excellent": "route 稳、bundle 清、扩容有因、停止有据，既防过载又保留创造性扩展空间。",
    "workable": "总体方向对，但 bundle 或 expansion logic 仍偏松，停止条件不够硬。",
    "weak": "更像加载愿望清单，没有真正控制上下文增长，也没有防 summary drift。"
  },
  "hard_fail_rules": [
    "没有明确 primary route 或 route certainty",
    "没有区分 mandatory bundle 和 optional expansion queue",
    "没有写出 stop conditions 或 context-corrosion signals"
  ],
  "rewrite_actions": [
    "先锁 route，再重写 bundle",
    "删掉没有明确 trigger 的扩展项",
    "补写 stop rules 和腐化信号"
  ]
}
---
# Context Loading Plan Rubric

好的 loading plan 应该像一个控制台，而不是一个购物清单。它不是把想看的都列进来，而是把最该先看的、可以后看的、根本不该看的分开。

如果一个 plan 只会说“这些也相关、那些也可能有用”，却不能告诉 Agent 什么时候应该停，那它本质上还是在鼓励上下文腐化。

## TODOs：待回答问题

- [ ] rubric 是否需要显式检查 compare_pack、teaching_pack 和 survey_pack 的边界？
- [ ] 是否应要求每个 loading mode 都给一个典型 bundle 大小示例？
- [ ] 对 rewrite / diagnose 场景，rubric 是否应更严格惩罚过度扩容？
- [ ] 哪些 stop condition 最适合转成 fixture 里的 key check？
