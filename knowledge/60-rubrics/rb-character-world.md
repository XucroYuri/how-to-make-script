---
{
  "id": "rb.character-world",
  "type": "evaluation_rubric",
  "title": "Character / World Rubric",
  "applies_to": ["premise", "synopsis"],
  "dimensions": [
    {"name": "drive_pressure", "question": "角色欲望、恐惧、价值排序和内在矛盾是否真的会推动选择"},
    {"name": "world_pressure", "question": "世界规则是否会给主线冲突施压，而不是停留在设定说明"},
    {"name": "relation_network", "question": "关键关系是否形成持续压力，而不是只提供身份信息"},
    {"name": "development_readiness", "question": "这份输出是否已经能作为后续结构设计的可用输入"}
  ],
  "scoring_bands": {
    "excellent": "人物驱动清楚，世界施压有效，关系网络可直接进入结构开发。",
    "workable": "已有明确压力方向，但仍存在标签化或设定展示倾向。",
    "weak": "更像角色档案或世界观简介，还不足以支撑真正的结构推进。"
  },
  "hard_fail_rules": [
    "角色只剩标签，没有选择驱动力",
    "世界规则与主线冲突无直接压力关系",
    "关系网络无法说明谁在持续施压",
    "这份输出无法直接支撑后续结构工作"
  ],
  "rewrite_actions": [
    "补齐角色驱动四联体",
    "把世界规则改写成限制、代价或风险",
    "重写关键关系的压力方向",
    "删去与结构推进无关的档案式设定"
  ]
}
---
# Character / World Rubric

用于判断人物与世界观材料是否已经从“设定”变成“可开发的压力系统”。

这套 rubric 不奖励履历丰富、名词密集或世界观宏大。它只关心一件事：这些材料能不能直接进入后续结构工作，并持续给故事施压。

## TODOs：待回答问题

- [ ] 群像项目里，relation network 的判断标准是否需要和单主角项目分开？
- [ ] 现实题材里世界规则更弱时，world_pressure 维度是否需要不同阈值？
- [ ] 当人物非常鲜活但世界压力尚弱时，development_readiness 应如何判分才不误导后续结构工作？
