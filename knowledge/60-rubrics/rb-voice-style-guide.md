---
{
  "id": "rb.voice-style-guide",
  "type": "evaluation_rubric",
  "title": "Voice Style Guide Rubric",
  "applies_to": ["voice_style_guide", "dialogue_polish", "scene_draft", "commercial_script"],
  "dimensions": [
    {"name": "identity_fidelity", "question": "是否写出了角色 / IP / 品牌人格真正稳定的表达锚点"},
    {"name": "lived_pressure", "question": "是否把处境压力、身体感和关系风险转进了语言机制"},
    {"name": "register_fit", "question": "语域是否适配媒介、平台、品牌或互动任务"},
    {"name": "creative_range", "question": "是否保留了可变区间，而不是把风格冻结成模板"}
  ],
  "scoring_bands": {
    "excellent": "锚点清晰，压力真实，语域贴合，既能守住身份又保留变化空间。",
    "workable": "大方向可用，但仍有抽象标签过多、边界不清或活人感不足的问题。",
    "weak": "只有风格形容词，没有可执行锚点；要么太泛，要么太僵。"
  },
  "hard_fail_rules": [
    "把角色或 IP 声音简化成口头禅、腔调标签或漂亮形容词",
    "没有写出明显的 drift warning 或禁行区",
    "文本只讲“自然一点 / 高级一点”，却没有说明为什么、怎么做、什么不能做",
    "把 guide 写成唯一模板，几乎不允许场景变化"
  ],
  "rewrite_actions": [
    "补世界观、关系策略、羞耻点和表达禁区等 voice anchors",
    "把情绪标签改写成处境压力和具身反应",
    "明确允许区间、禁行区和 off-model 红旗",
    "把模板式示例降级为参考片段，并补 variability budget"
  ]
}
---
# Voice Style Guide Rubric

这份 rubric 不是在评“风格词够不够漂亮”，而是在评这份 guide 有没有真的帮后续写作降低漂移风险。

好的 `voice_style_guide` 应该让人一眼知道：这个角色 / 这个 IP / 这个品牌为什么会这么说，不会怎么说，哪些变化是合理的，哪些一写就会出戏。差的 guide 往往只有调性形容词，看起来很会说，实际上对写作没有真正约束力。

## TODOs：待回答问题

- [ ] 当项目故意追求强风格化统一口吻时，`creative_range` 该如何重新评分？
- [ ] 商业内容里的品牌人格，与叙事角色的人物声纹，是否需要两套不同权重的 rubric？
- [ ] 对互动叙事，是否应增加“玩家可读性”维度，防止真实感压垮信息清晰度？
- [ ] 当 IP 官方设定本身互相冲突时，rubric 应如何处理 continuity 判断的不确定性？
- [ ] 如果 guide 很强，但执行文本仍然失败，仓库是否需要单独增加“guide-to-draft consistency”检查？
