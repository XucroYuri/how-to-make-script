---
{
  "id": "ka.parallel-lane-governance",
  "type": "knowledge_atom",
  "title": "并行泳道治理",
  "kind": "heuristic",
  "summary": "并行 lane 只有在共享真相包、明确边界和定期回收的条件下才会加速，否则只会把返工提前埋好。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "outline", "scene", "rewrite", "adaptation"],
  "problem": "看起来很多 lane 同时推进，实际上事实基线分裂、风格飘移、回收成本暴涨。",
  "decision_rules": [
    "只有彼此依赖已被压缩进 handoff contract 时，任务才适合并行。",
    "每个并行 lane 都要共享一份当前真相包，包括锁定事实、未决问题、边界和版本号。",
    "并行越多，回收节奏越要明确，否则局部最优会迅速替代整体质量。"
  ],
  "anti_patterns": [
    "为了显得高效而把强耦合任务硬拆并行",
    "每个 lane 自己更新事实而不回写共享真相包",
    "没有 merge owner 就同时开很多 lane"
  ],
  "prompt_primitives": [
    "这几个 lane 之间真正共享的最小事实集是什么",
    "哪个 lane 产生的变化必须同步广播，哪个可以延迟合并",
    "如果今天只能回收一次，最该先回收哪一条 lane"
  ],
  "evaluation_checks": [
    "parallel lanes 是否建立在足够清晰的 handoff 上",
    "共享真相包是否被持续维护",
    "回收 owner 和 merge 时点是否明确"
  ],
  "links": ["ka.bounded-context-loading", "ka.reference-expansion-balance", "ka.context-corrosion-signals"],
  "source_status": "synthesized"
}
---
# 并行泳道治理

并行不是天然更快。真正能加速的是“低耦合 + 清交接 + 快回收”的并行；真正会害人的，是“高耦合 + 大家先各写各的，回头再合”的伪并行。

剧本开发尤其容易踩这个坑。因为人物、结构、语气、商业诉求、系统逻辑之间都可能互相牵连。把它们拆出去不难，难的是拆出去以后还能不能回来。没有共享真相包，没有 merge owner，没有冻结窗口，并行 lane 最终常常只是多制造几套彼此不兼容的局部正确。

所以并行治理的本质不是“分几个人做”，而是“哪些东西现在可以安全不一起思考，哪些东西必须保持同一事实面”。多智能体框架要真像一个高水平团队，这件事必须写进协议，而不能靠运气。

## TODOs：待回答问题

- [ ] 什么复杂度以上的项目才值得主动设计并行 lanes，而不是保持单线推进？
- [ ] 对长剧 writers' room 和短视频 strike team，并行 lane 的最佳粒度是否完全不同？
- [ ] 是否需要把“共享真相包”沉淀成单独产物契约，而不是只写在说明文里？
- [ ] merge owner 应该总是 room captain / showrunner 级角色，还是可以阶段性下放？
- [ ] 当某条 lane 连续产出高质量但持续偏离主路线时，系统该优先保效率还是保整体一致性？
