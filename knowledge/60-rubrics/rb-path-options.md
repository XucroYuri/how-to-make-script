---
{
  "id": "rb.path-options",
  "type": "evaluation_rubric",
  "title": "Path Options Rubric",
  "applies_to": ["path_options"],
  "dimensions": [
    {"name": "difference", "question": "各路径是否真的不同，而不是同一路线的轻微改写"},
    {"name": "tradeoff", "question": "每条路径的收益、代价与适配条件是否清楚"},
    {"name": "constraint_awareness", "question": "路径是否回应了关键约束而非纯脑洞堆叠"},
    {"name": "convergence_utility", "question": "是否说明何时该从多路径收敛到单路径"}
  ],
  "scoring_bands": {
    "excellent": "路径之间差异清楚、tradeoff 具体、收敛条件明确，足以指导下一步决策。",
    "workable": "有多路径意识，但差异或 tradeoff 还不够硬，收敛依据仍偏模糊；对窄问题，2 条高差异路径也可成立。",
    "weak": "更像一个方案的多种表述，无法真正支持探索阶段的判断。"
  },
  "hard_fail_rules": [
    "宽问题没有至少三条真正不同的路径，或窄问题没有至少两条真正不同的路径",
    "没有说明每条路径的主要 tradeoff",
    "没有任何收敛触发点或选择依据"
  ],
  "rewrite_actions": [
    "扩大路径差异，而不是只改措辞",
    "给每条路径补收益、代价和适配条件",
    "补写从多路径收敛到单路径的触发条件"
  ]
}
---
# Path Options Rubric

path_options 最容易假的地方，是看起来给了多个方案，实际上只是同一个方案换了几种包装。这个 rubric 的作用，就是逼多路径真正变成多路径，而不是机械追求条数。

## TODOs：待回答问题

- [ ] 对短时探索会话，是否应允许 path_options 只有 2 条，但要求更高差异度？
- [ ] 哪些 tradeoff 维度最应该标准化，例如 audience、production、platform、style、budget？
- [ ] 当用户其实早就偏向某条路径时，rubric 应如何防止另外几条路径沦为陪衬？
- [ ] 是否需要为跨媒介 path_options 增加额外维度来检查容器转换质量？
