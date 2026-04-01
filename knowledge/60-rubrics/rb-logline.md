---
{
  "id": "rb.logline",
  "type": "evaluation_rubric",
  "title": "Logline / Premise Rubric",
  "applies_to": ["logline", "premise"],
  "dimensions": [
    {"name": "clarity", "question": "主角、目标、阻力、stakes 是否清楚"},
    {"name": "specificity", "question": "是否避免空泛概念词"},
    {"name": "drive", "question": "是否具备继续展开的驱动力"},
    {"name": "engine_honesty", "question": "这条 logline 是否真的在暴露故事发动机，而不是只在卖题材气味"}
  ],
  "scoring_bands": {
    "excellent": "一句话即可判断故事引擎，且具备独特性与推进力。",
    "workable": "基本要素齐全，但仍有泛化或乏力之处。",
    "weak": "更像题材描述或主题感想，而不是故事引擎。"
  },
  "hard_fail_rules": [
    "没有明确主角",
    "没有明确目标",
    "阻力或 stakes 缺失",
    "删除题材包装后，句子已无法说明真正的故事动作"
  ],
  "rewrite_actions": [
    "补足目标与代价",
    "删去空泛修饰词",
    "让题材钩子进入冲突句法",
    "区分宣传级句子和开发级句子，必要时重写而不是继续润色"
  ]
}
---
# Logline / Premise Rubric

用于判断压缩后的故事引擎是否真正成立。

这个 rubric 不是修辞评分表，而是开发判断器。它的重点不在“句子漂不漂亮”，而在“故事发动机有没有真正点火”。很多概念看起来高级，但一过这套 rubric 就会暴露出主角不清、目标不清、阻力不清的问题。
现在它还会继续追问一句：这条句子到底是在说明故事会如何推进，还是只是在说明它“看起来很有故事”。

## TODOs：待回答问题

- [ ] 群像片、程序性作品、悬念型设定片在 logline 里未必能突出单一主角，这时 hard fail 标准要不要调整？
- [ ] 某些体验型、氛围型或作者型作品的 stakes 不以外部成败呈现，如何避免 rubric 误杀这类项目？
- [ ] “具体”与“过早塞设定”之间的界线在哪里，什么程度的信息量会让 logline 从清晰变成拥挤？
- [ ] 改编作品、IP 续作、知名题材翻新在 premise 判断上能否借用观众已有认知，还是仍要独立完成引擎说明？
- [ ] 当一句话非常有钩子但目标和阻力略模糊时，应判作 workable 还是 weak，是否需要补充临界案例库？
- [ ] 什么情况下一个 premise 看似成立，但本质上只能支撑短片、广告或概念海报，不能支撑完整剧本开发？
