---
{
  "id": "rb.pattern-reference-pack",
  "type": "evaluation_rubric",
  "title": "Pattern Reference Pack Rubric",
  "applies_to": ["pattern_reference_pack"],
  "dimensions": [
    {"name": "problem_fit", "question": "参考包是否真的对应当前创作问题，而不是只给了一个泛好例子"},
    {"name": "contrast_quality", "question": "成功样本与失败对照之间的差异是否清楚且有判断价值"},
    {"name": "mechanism_explanation", "question": "是否解释了为什么强样本更有效，而不是只给主观夸赞"},
    {"name": "non_dogma_guard", "question": "是否明确写出适用边界和非唯一范式声明"}
  ],
  "scoring_bands": {
    "excellent": "问题匹配准确，对照清楚，成功/失败机制解释具体，同时保留了适用边界与开放创作空间。",
    "workable": "有用，但对照或机制解释还不够硬，非教条说明偏弱。",
    "weak": "更像一个好坏判断展示，没有把为什么好、为什么坏和边界条件讲清楚。"
  },
  "hard_fail_rules": [
    "没有同时提供成功样本与失败对照",
    "没有解释为什么强样本更有效、弱样本为什么失效",
    "没有明确说明这只是参考范式而不是唯一模板"
  ],
  "rewrite_actions": [
    "把样本与当前问题重新对齐，避免泛案例滥用",
    "补强失败对照，使差异落到判断点上",
    "补写适用条件、失效边界和非唯一范式声明"
  ]
}
---
# Pattern Reference Pack Rubric

reference pack 最容易变味的地方，是它看起来很丰富，实际上只是拿一个喜欢的样本配上一段夸赞。那种写法会让人记住表皮，记不住判断。

这个 rubric 的作用，就是逼参考包把“问题-样本-对照-机制-边界”这条链条讲完整。只有这样，它才会成为真正能帮创作者和 Agent 提高判断质量的参考，而不是另一本模板手册。

## TODOs：待回答问题

- [ ] 哪些类型的问题最需要强制失败对照至少给两种？
- [ ] rubric 是否需要单独检查样本是否过度依赖文风魅力而不是结构判断？
- [ ] 当样本是对白片段时，是否需要额外检查潜台词与角色区分度？
- [ ] 对商业和互动参考包，是否需要单独的工业适配维度？
