---
{
  "id": "rb.research-background-map",
  "type": "evaluation_rubric",
  "title": "Research Background Map Rubric",
  "applies_to": ["research_background_map"],
  "dimensions": [
    {"name": "lens_coverage", "question": "是否把宽问题拆成了足够有判断力的研究镜头，而不是继续停留在单方法总结"},
    {"name": "stability_honesty", "question": "是否区分了稳定发现、局部经验、历史条件和争议点，而不是把一切都说成定论"},
    {"name": "callability", "question": "是否把研究背景落回到可调用 atom、source map 和后续 route，而不是只做阅读摘要"},
    {"name": "loading_discipline", "question": "是否避免把背景图写成仓库全量 dump，并且说明下一步该走哪条更窄路线"}
  ],
  "scoring_bands": {
    "excellent": "镜头拆解清楚，稳定发现与局部条件区分明确，可调用资产和后续路线清晰，同时保持了加载克制和反教条边界。",
    "workable": "能用，但研究镜头、资产回落或边界说明还不够硬，仍有摘要化倾向。",
    "weak": "更像一篇泛泛研究综述，没有形成可调用结构，也没有把宽问题拆成真正可操作的判断单元。"
  },
  "hard_fail_rules": [
    "没有明确拆出多个研究镜头",
    "没有列出可调用的 atom、source map 或后续 route",
    "把局部经验或单一流派包装成普适结论",
    "把答案写成仓库全量摘要而没有加载边界"
  ],
  "rewrite_actions": [
    "把宽问题重新拆成 3-6 个高价值研究镜头",
    "补写稳定发现、局部条件和争议点之间的边界",
    "把背景层落回到具体 atom、docs 和下一步 route",
    "删除不会改变下一步决策的摘要噪音"
  ]
}
---
# Research Background Map Rubric

研究背景图最容易退化成两种东西：一种是“仓库导览”，另一种是“方法论讲稿”。两者都不够好。

前者的问题是材料很多，但调用价值很低。后者的问题是判断很强，但经常把单一流派误写成普遍真理。

这个 rubric 的工作，就是逼 `research_background_map` 在“有结构、有边界、有调用价值”这三件事上同时成立。

## TODOs：待回答问题

- [ ] rubric 是否需要单独检查“后续 route 建议是否过宽”？
- [ ] 对面向 Agent Skill 设计的背景图，是否应增加 machine-callability 的专门维度？
- [ ] 对面向人类学习者的背景图，是否应增加教学可读性的维度而不是只看结构硬度？
