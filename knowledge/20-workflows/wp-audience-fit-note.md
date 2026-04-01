---
{
  "id": "wp.audience-fit-note",
  "type": "workflow_protocol",
  "title": "受众匹配说明协议",
  "goal": "把模糊的目标观众描述收敛成一个可执行的 audience_fit_note，用于修正 premise、结构、场景或改稿方向。",
  "input_contract": ["project concept", "draft summary", "target audience guess", "platform context", "none"],
  "output_contract": ["audience_fit_note"],
  "preconditions": [
    "至少知道目标媒介或发布场景",
    "允许从模糊 audience 假设出发"
  ],
  "steps": [
    "识别一个主受众和一个主需求状态，必要时再补一个次受众。",
    "定义观看情境、进入门槛和观众预期回报。",
    "判断当前概念或草稿在哪些地方兑现了承诺，哪些地方发生错位。",
    "输出 audience_fit_note，包含匹配点、错位风险和优先修改动作。"
  ],
  "fallbacks": [
    "若观众信息不足，先根据 medium、genre、platform 推一个基础受众假设。",
    "若项目仍处于概念期，先判断 promise 是否足以吸引目标观众进入第一层观看。"
  ],
  "stop_conditions": [
    "能清楚说明谁在看、为什么看、为什么会流失",
    "修改建议已经具体到能改变结构、场景或信息密度"
  ],
  "rubrics": ["rb.audience-fit"],
  "linked_atoms": ["ka.audience-need-state", "ka.platform-attention-economy", "ka.commissioning-fit", "ka.pacing-rhythm"]
}
---
# 受众匹配说明协议

这个协议不是做市场报告，而是把“观众为什么会看、哪里会掉线”直接翻译成创作动作。它适合用在 concept 阶段，也适合用在初稿诊断阶段。

很多项目的问题不是不好，而是不对。明明说自己写给某类观众，结果开头、节奏、回报、钩子、人物关系都没有真正服务那类人的观看动机。这个协议就是用来把这种错位显性化。

如果 audience_fit_note 做得好，后续的结构开发和改稿优先级会一下子清楚很多。因为你终于知道自己不是在抽象优化“更好看”，而是在具体优化“为什么这群人会继续看”。

## TODOs：待回答问题

- [ ] 当一个项目故意同时服务两个观看场景时，协议是否需要输出双受众版本，而不是强制压成单受众？
- [ ] audience_fit_note 是否需要区分“点开吸引力”“持续观看力”“看完后传播力”三层指标？
- [ ] 对作者电影、艺术动画、实验互动项目，这个协议该如何避免把作品误导成纯大众留存逻辑？
- [ ] 受众错位是改开头更常见，还是改 premise / genre promise 更常见，是否需要案例统计层？
- [ ] 当观众需求状态明显变化于项目中途，note 应如何标出“允许变化”与“承诺失守”的边界？
