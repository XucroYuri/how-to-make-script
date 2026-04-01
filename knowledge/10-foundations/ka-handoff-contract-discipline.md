---
{
  "id": "ka.handoff-contract-discipline",
  "type": "knowledge_atom",
  "title": "交接契约纪律",
  "kind": "heuristic",
  "summary": "多智能体协作的关键不是多找几个 specialist，而是每次交接都带着可执行的目标、边界、输入包、输出契约和未决问题。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "任务被拆出去后各写各的，结果回收时无法合并，或 specialist 在错误前提上做了高成本工作。",
  "decision_rules": [
    "每次 handoff 都必须写清目标产物、硬边界、软约束、输入包、停止条件和需要回传的问题。",
    "如果交接对象只拿到主题愿景却拿不到 artifact contract，说明 handoff 还没完成。",
    "交接包越短越好，但绝不能短到让 specialist 自己重新猜题。"
  ],
  "anti_patterns": [
    "把一个模糊愿望直接丢给 specialist",
    "交接时不标记 hard boundary 和未决问题",
    "多个 lane 使用不同事实基线却没有显式版本号"
  ],
  "prompt_primitives": [
    "这个 specialist 这一次只负责什么，不负责什么",
    "他要基于哪些共享事实工作，禁止重猜哪些前提",
    "回收时我需要他交付什么格式、什么粒度、带哪些自检"
  ],
  "evaluation_checks": [
    "handoff 是否包含输入、输出、边界和停止条件",
    "不同 lane 是否基于同一事实基线",
    "回收后的结果是否可被主 orchestrator 合并"
  ],
  "links": ["ka.bounded-context-loading", "ka.boundary-first-guidance", "ka.context-corrosion-signals"],
  "source_status": "synthesized"
}
---
# 交接契约纪律

多智能体团队真正难的地方，不是“怎么找更多专家”，而是“怎么让专家不要在错误前提上认真干活”。一旦 handoff 太松，回收阶段几乎一定会出现两种浪费：要么大家做了重复工作，要么各自产出都看起来像对的，但彼此拼不起来。

一个合格的 handoff contract 至少要解决六件事：这次为什么交给你、你基于什么材料工作、你不能碰什么、你要产出什么、做到什么程度就停、哪些问题必须带回来。只要这六件事里缺两三件，团队就会开始重新理解任务，而不是推进任务。

这对 human-in-the-loop 也一样。交给人类 reviewer 的包如果太大，他只会泛泛提意见；如果太小，又不知道自己在审什么。交接纪律说到底是在保护注意力。

## TODOs：待回答问题

- [ ] handoff contract 是否应该按研究型、创作型、诊断型、审稿型任务分不同模板？
- [ ] 当 specialist 必须访问外部材料时，source policy 和引用要求是否应进入 handoff contract 的强制字段？
- [ ] 对跨语言、跨文化或跨地区创作任务，handoff 是否要额外标注本地化风险？
- [ ] Agent 与 human 之间的交接包，是否需要和 agent-agent 的交接包采用不同结构？
- [ ] 当多个并行 lane 回收结果互相冲突时，仓库是否需要单独的 merge contract？
