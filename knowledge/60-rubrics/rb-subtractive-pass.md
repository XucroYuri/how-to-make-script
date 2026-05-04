---
{
  "id": "rb.subtractive-pass",
  "type": "evaluation_rubric",
  "title": "Subtractive Pass Rubric",
  "applies_to": ["scene_draft","screenplay_draft"],
  "dimensions": [
    {"name": "declarative_removal", "question": "是否所有声明性台词（角色直接说出情感或解释情节）都已被删除或改写"},
    {"name": "stateless_removal", "question": "是否所有无状态变化的段落都已被删除"},
    {"name": "authorial_removal", "question": "是否所有'作者腔'过渡句都已被删除"},
    {"name": "coherence_preserved", "question": "删除后叙事连续性是否保持——所有角色的行动仍可追踪"},
    {"name": "necessity_proven", "question": "每一行剩余内容是否都能在'如果可以去掉，我想去掉它'的测试中存活"}
  ],
  "scoring_bands": {
    "excellent": "所有声明性、无状态段落和作者腔均已删除；剩余内容全是可执行的动作和承载信息的对白；叙事连续性完全保持。",
    "workable": "主要冗余已删除，但仍有残留声明性或功能重复的段落；连续性基本保持，但在1-2处的信息传递可能需要验证。",
    "weak": "删除幅度极小，大量冗余仍在；或删除导致连续性断裂说明前期场景设计有问题而非减法执行错误。"
  },
  "hard_fail_rules": [
    "仍有角色直接说出自己的情绪状态（'我很难过''我绝望了'）而未通过行动传达",
    "仍存在超过一段的无变化场景内容",
    "删除后叙事关键信息丢失，且丢失的信息未通过其他方式传递"
  ],
  "rewrite_actions": [
    "把声明性台词改为可拍摄的行动序列",
    "合并功能重复的场景或段落",
    "如果删除导致信息丢失但该信息确实必要，找到更早的铺设时机或更具体的承载方式重新传递"
  ]
}
---
# Subtractive Pass Rubric

这个 rubric 不评估写得好不好——它评估写的是否必要。通过结构检查和观众代理检查的剧本仍然可能过度书写。减法修改是交付前的最后一道门。

## TODOs：待回答问题

- [ ] 不同媒介（长片、剧集、短剧、动画）对"必要"的判定标准是否应不同，它们的硬边界在哪里？
- [ ] "作者腔"在特定叙事视角（如不可靠叙述者、旁白体）中的容忍度应该如何评估，何时是风格何时是缺陷？
- [ ] 如果一场戏通过了减法检查但评审反馈仍觉得"太薄"，回退路径应该是补场景还是回到 outline 检查功能设计不足？
