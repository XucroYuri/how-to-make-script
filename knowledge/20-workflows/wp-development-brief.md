---
{
  "id": "wp.development-brief",
  "type": "workflow_protocol",
  "title": "开发策略简报协议",
  "goal": "在真实委制、平台、发行和业务约束下，为项目产出一个 development_brief，明确创作优先级与开发顺序。",
  "input_contract": ["concept", "current draft", "commissioning context", "platform/release assumptions", "business objective"],
  "output_contract": ["development_brief"],
  "preconditions": [
    "项目至少已有一个概念或草稿方向",
    "允许把现实约束与创作方向一起纳入判断"
  ],
  "steps": [
    "锁定委制主体、业务目标、发行或分发窗口。",
    "判断目标受众、平台注意力逻辑与媒介容器是否一致。",
    "把创作建议拆成必须先锁定的非谈判项、可延后探索项和高风险项。",
    "输出 development_brief，明确下一轮开发应先产出什么、验证什么、暂缓什么。"
  ],
  "fallbacks": [
    "若委制方未明确，先给出一版 baseline independent strategy，再给一版平台或品牌化替代路径。",
    "若商业目标模糊，先按最可能的分发窗口推导最低限度开发逻辑。"
  ],
  "stop_conditions": [
    "brief 已说明当前项目最该解决的开发问题",
    "创作建议已经与平台、业务、交付现实对齐"
  ],
  "rubrics": ["rb.development-brief"],
  "linked_atoms": ["ka.commissioning-fit", "ka.platform-attention-economy", "ka.audience-need-state", "ka.screenwriting-history-shift"]
}
---
# 开发策略简报协议

这个协议面对的是“作品怎么往前推进最稳”这个问题，而不是“作品是不是已经写好了”。它把创作和开发放在同一个桌面上看，目的是避免项目一开始就走歪。

很多项目真正缺的不是更多剧情细节，而是一张清晰的开发地图：当前阶段最关键的决策是什么、哪些因素必须先锁、哪些问题还可以保留开放、下一轮交付物最该是什么。没有这张地图，团队就很容易把大量时间花在错误的细化上。

development_brief 的价值，在于让“写什么”和“怎么推进”被同时回答。这样 Agent 才不会只会帮你生成文本，而是能帮你降低开发上的盲打。

## TODOs：待回答问题

- [ ] development_brief 是否需要针对 narrative、commercial、interactive 三类项目拆成不同模版？
- [ ] 在品牌短片或平台命题项目里，brief 应该多大程度直接写业务目标，而不损伤创作可读性？
- [ ] 若项目同时考虑院线、流媒体、短视频切条、IP 延展，brief 应如何排序主窗口与副窗口？
- [ ] “先锁定什么”这件事是否可以进一步沉淀成决策树，而不是依赖文字说明？
- [ ] 哪些项目其实不该继续写 brief，而应该先回到 premise 层重构引擎？
