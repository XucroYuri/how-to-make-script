---
{
  "id": "wp.writer-development-path",
  "type": "workflow_protocol",
  "title": "编剧成长路径协议",
  "goal": "根据学习者当前失败层、目标媒介和目标水平，输出一条可执行的 learning_path。",
  "input_contract": ["writer maturity", "sample weakness", "target medium", "target level", "available time"],
  "output_contract": ["learning_path"],
  "preconditions": [
    "至少能描述当前阶段和目标方向",
    "允许用阶段性训练替代一次性全面提升"
  ],
  "steps": [
    "诊断学习者最稳定的失败层和当前成熟度。",
    "按从最短板到可迁移能力的顺序安排训练阶段。",
    "为每一阶段绑定真实产物、反馈渠道和返修节奏。",
    "输出 learning_path，说明阶段目标、练习方式、里程碑与升级条件。"
  ],
  "fallbacks": [
    "若成熟度未知，先输出一轮 1-2 周诊断冲刺，用来判定短板层。",
    "若目标太大，先把长目标拆成一个近期媒介目标和一个长期职业目标。"
  ],
  "stop_conditions": [
    "每个阶段都有具体产物与反馈方式",
    "下一轮训练的优先级已经清楚，不再停留在泛化建议"
  ],
  "rubrics": ["rb.learning-path"],
  "linked_atoms": ["ka.writer-development-loop", "ka.screenwriting-history-shift", "ka.scene-function", "ka.rewrite-diagnosis", "ka.screenwriting-deliberate-practice", "ka.archive-literacy"]
}
---
# 编剧成长路径协议

这个协议处理的不是某个剧本该怎么改，而是写剧本的人下一步该怎么练。它的核心是假定：编剧成长必须被拆成阶段、产物、反馈和返修，而不是靠“多写多看”四个字概括。

最常见的问题是把学习路径写成阅读清单，或者把训练建议写成抽象美德。这样看起来很完整，但几乎不能真正改变一个学习者的写作习惯。成长路径必须具体到：这周写什么、谁来反馈、改几轮、过关标准是什么。

它不是职业生涯咨询，也不是鸡汤文，而是一条围绕真实写作产物组织出来的训练路径。只有这样，仓库才能同时服务专业编剧培养和 Agent 辅助教学。

## TODOs：待回答问题

- [ ] learning_path 是否需要按新手、转行者、职业编剧、showrunner 预备分别输出不同骨架？
- [ ] 学习路径里应如何平衡“模仿经典”与“原创输出”，避免任何一端过重？
- [ ] 当学习者目标媒介不止一种时，系统应如何判断先训练哪一种最有迁移价值？
- [ ] 某些学习者的瓶颈来自生活经验、观察力或协作能力，这些非文本问题该如何纳入路径？
- [ ] 成长路径是否需要显式建议何时参加 writers' room、工作坊、比赛、提案或行业实习？
