---
{
  "id": "wp.idea-discovery",
  "type": "workflow_protocol",
  "title": "创意发现协议",
  "goal": "把模糊想法收敛为可进入剧本开发的 premise。",
  "input_contract": ["raw idea", "theme fragment", "image prompt", "market brief", "none"],
  "output_contract": ["premise"],
  "preconditions": [
    "允许先从模糊灵感开始",
    "至少能说明目标媒介或应用场景"
  ],
  "steps": [
    "识别主角、欲望、阻力、代价的最小组合。",
    "判断更适合 narrative、commercial 还是 interactive 路径。",
    "把题材兴趣翻译为可测试的冲突命题。",
    "输出一个可扩展 premise，并附带 2-3 个后续展开方向。"
  ],
  "fallbacks": [
    "若媒介未知，先按 narrative generic 路径收敛 premise。",
    "若用户只给情绪或主题，先补故事目标。"
  ],
  "stop_conditions": [
    "premise 已能说明角色、目标、阻力、代价",
    "下一步最适合进入 logline、character 或 commercial 开发"
  ],
  "rubrics": ["rb.logline"],
  "linked_atoms": ["ka.story-goal", "ka.conflict-pressure", "ka.theme-pressure", "ka.screenplay-lens-stacking"],
  "budget_class": "M",
  "mandatory_atom_count": 4,
  "expansion_allowed": true
}
---
# 创意发现协议

先找驱动力，再找形式。模糊灵感只有在进入角色目标与冲突后，才值得进入后续开发。

这个协议最适合处理“我有一个感觉/题材/画面，但还不是故事”的阶段。它的目标不是立刻把 idea 写大，而是先判断这个想法有没有真正的叙事发动机。

实务上，创意发现最容易犯的错是过早沉迷世界观、类型氛围或营销包装，却没有先把主角的目标和阻力压出来。这个协议就是用来拦截这种虚胖开发的。

## TODOs：待回答问题

- [ ] 对于“先有市场任务、后找故事”的项目，idea discovery 是否需要单独的商业化入口协议？
- [ ] 当用户只给 mood、reference、海报感、AI 生成图时，仓库应如何从视觉灵感里提炼叙事引擎？
- [ ] 哪些创意其实不该被继续开发，而应该被及时判定为“只有包装没有故事”？
- [ ] 创意发现阶段是否需要一套“淘汰标准”，明确哪些想法值得继续、哪些应果断放弃？
- [ ] 面对高度相似的流行题材，协议应如何追问差异化，而不是默认接受陈词滥调？
- [ ] 如果用户同时给出个人表达欲、平台任务、商业诉求三种方向，哪一种应该先主导创意收敛？
- [ ] 当前协议是否需要引入更细的访谈问题模板，帮助用户从模糊感受过渡到可开发 premise？
