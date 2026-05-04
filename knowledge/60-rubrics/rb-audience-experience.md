---
{
  "id": "rb.audience-experience",
  "type": "evaluation_rubric",
  "title": "Audience Experience Rubric",
  "applies_to": ["scene_draft", "screenplay_draft", "audience_fit_note", "audience_proxy_report"],
  "dimensions": [
    {"name": "entry_pull", "question": "代理进入场景的前 30 秒内，是否产生了继续看的理由"},
    {"name": "patience_curve", "question": "patience 曲线是否持续有涨有跌，而不是单调下滑"},
    {"name": "stakes_felt", "question": "至少一个代理是否能说清楚为什么当前结果对人物来说是真实的风险"},
    {"name": "promise_honesty", "question": "开头建立的内容承诺是否在后续场景中被兑现而非悄然替换"},
    {"name": "concern_resolution", "question": "代理的 concerns 是否在合理时机内得到回应（解消或升级为更大冲突）"}
  ],
  "scoring_bands": {
    "excellent": "所有代理在末场保持 hooked=true 或 patience≥70，共识关切数量≤1，修改优先级指向非结构性打磨层。",
    "workable": "核心受众代理保持 hooked=true，但随机观众或类型老炮代理出现 2 个以上 concerns，存在断流风险点，修改优先级指向节奏或承诺一致性层。",
    "weak": "超过两个代理在中段 patience 跌至 60 以下，或存在 hooked 始终为 false，或核心关切集中在开头前两场未被解决。"
  },
  "hard_fail_rules": [
    "随机观众代理在前三场 patience 跌至 50 以下",
    "所有代理的 hooked 在末场均为 false",
    "核心受众代理存在类型承诺违背的 concern 且该 concern 在全文未被解消",
    "报告本身使用了反谄媚守卫禁止词列表中的外交包装句式",
    "修改优先级为空，或全部是无法映射到具体场景的泛化建议"
  ],
  "rewrite_actions": [
    "patience 在前三场持续下跌：压缩进入动作，把最高价值密度的信息前移至第一场的前半段",
    "hooked 未触发：检查第一场是否提供了明确的悬念钩子或代入缺口，不是靠信息铺垫，而是靠具体的处境压力",
    "类型承诺被违背：回溯开头场景，找到承诺发出点，要么修改承诺，要么修改后续不兑现的场景",
    "concerns 未解消也未升级：在后续场景中加入对应关切的明确回应节拍，或在更早位置重新处理引发关切的源头",
    "代理间高度分歧：这通常不是问题，而是信号——项目受众定位可能尚未锁定，返回前置定位步骤"
  ]
}
---
# Audience Experience Rubric

这个 rubric 不评价剧本写得好不好，它评价观看体验是否真实发生。

两件事经常被混淆：文本质量和观看体验。一个结构工整、对白无懈可击的剧本，可以产生完全无效的观看体验。而一个有明显技术粗糙的场景，也可以在受众代理身上触发真实的 hooked 状态。这个 rubric 只关心后者：代理在读完之后，他的 patience 曲线、trust 状态和 hooked 布尔值说明了什么。

## 关于 hard fail 的说明

`随机观众代理在前三场 patience 跌至 50 以下` 这条 hard fail 是最严重的信号。它意味着项目的开头设计对非主动选择型观众完全失效。这种失效在短视频时代和算法推荐场景里是致命的，在院线和剧集环境里也是高风险区。

`报告本身使用了外交包装句式` 这条规则针对的不是文本，而是评审输出本身。如果受众代理评审报告里出现了软化包装，那说明反谄媚守卫失效，整份报告的诚实性不可信，应整体重跑。

## TODOs：待回答问题

- [ ] patience 曲线的"持续有涨有跌"标准，是否需要更精确的数学定义（如：每三场至少一次涨幅 ≥5）？
- [ ] 当项目是纯氛围或纯情绪型内容（无明显冲突事件）时，hooked 触发条件是否需要重新定义？
- [ ] 四个维度是否足够覆盖系列剧的跨集留存问题，还是需要单独的跨集 patience 曲线分析？
- [ ] 当受众定位本身存在争议时，rubric 的评价对象（哪个代理是主评价人）是否应该可以显式指定？
