---
{
  "id": "rb.commercial-script",
  "type": "evaluation_rubric",
  "title": "Commercial Script Rubric",
  "applies_to": ["commercial_script"],
  "dimensions": [
    {"name": "message", "question": "核心信息是否单一明确"},
    {"name": "attention", "question": "开头是否具备停留力"},
    {"name": "conversion", "question": "是否存在明确行动引导"}
  ],
  "scoring_bands": {
    "excellent": "信息清楚、记忆点强、品牌与转化链路顺畅。",
    "workable": "大体可用，但信息或 CTA 仍显分散。",
    "weak": "看完热闹，却不记得卖什么也不知道做什么。"
  },
  "hard_fail_rules": [
    "没有单一核心信息",
    "没有明确 CTA",
    "品牌或产品存在感过弱"
  ],
  "rewrite_actions": [
    "压缩卖点数量",
    "前置钩子和记忆点",
    "让 CTA 从叙事逻辑中生长"
  ]
}
---
# Commercial Script Rubric

用于判断商业脚本是否真正完成传播与转化任务。

商业脚本不能只看“好不好看”，必须同时看“记不记得住、会不会行动”。这个 rubric 的价值就在于把传播链路拉回台面，避免团队在审稿时只聊审美、不聊结果。

## TODOs：待回答问题

- [ ] 当项目目标偏品牌认知而非即时转化时，“没有明确 CTA”是否仍然必须 hard fail，边界该怎么定义？
- [ ] 如果广告故意采用弱品牌露出以换取更强观看体验，什么程度仍然算品牌存在感合格，什么程度已经失去商业任务？
- [ ] 6 秒 bumper、15 秒效果片、60 秒品牌片是否应该共用同一套 scoring band，还是需要拆开版本？
- [ ] 单一核心信息和多层受众沟通之间发生冲突时，评分应优先看第一层记忆点还是完整说服链？
- [ ] 开头停留力很强但后续卖点证明偏弱，这应判为 workable 还是 weak，临界标准能否被明确量化？
- [ ] 哪些类型的商业脚本天然更依赖素材、导演执行和演员表现，导致文本 rubric 分数高也未必能成片有效？
