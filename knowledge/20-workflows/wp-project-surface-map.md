---
{
  "id": "wp.project-surface-map",
  "type": "workflow_protocol",
  "title": "项目工作流表面图协议",
  "goal": "根据媒介、阶段、协作方式和长期创作压力，输出一份 project_surface_map，明确 source of truth、runtime state、canonical packet、phase entrypoints、review surfaces、export surfaces 和 sync rules。",
  "input_contract": ["project brief", "medium", "stage", "team mode or subagent need", "constraints", "human editing assumptions", "downstream execution assumptions"],
  "output_contract": ["project_surface_map"],
  "preconditions": [
    "用户需要设计长期创作工作流或持久化表面层，而不是只要一次性文本产物",
    "已知项目主要媒介或工作容器",
    "允许把真源、运行时、审查和导出显式区分"
  ],
  "steps": [
    "先判断项目最核心的 phase 是 planning、drafting、review、compliance 还是 export。",
    "定义 canonical source artifacts、derived runtime artifacts、review surfaces 和 export surfaces。",
    "定义每个 phase 的 entrypoint、前置条件、handoff 条件和 sync rules。",
    "如果项目具有长周期或多 lane handoff，明确是否需要 story memory checkpoint surface 以及它属于哪一层。",
    "定义 canonical packet 的组装层次与 inspectability 要求。",
    "定义 human-edit policy：哪些 surface 能手改，哪些只能 sync/compile 生成。",
    "输出 project_surface_map，并标出 drift risks、wrong-edit risks 和 future runtime hooks。"
  ],
  "fallbacks": [
    "若用户只需要 team mode，返回 team_workflow_blueprint。",
    "若用户只需要具体 subagent 阵容，返回 expert_subagent_cast。",
    "若用户只需要 live orchestration，返回 subagent_dispatch_plan。",
    "若任务只是一轮文本生成，不进入 project surface 设计。"
  ],
  "stop_conditions": [
    "已经说明 source of truth、runtime state、entrypoints、packet、review surfaces、export surfaces 与 sync rules",
    "human-edit policy 和 drift risks 已明确",
    "surface map 能支撑长期推进，而不是只解释一次性操作"
  ],
  "rubrics": ["rb.project-surface-map"],
  "linked_atoms": ["ka.source-of-truth-runtime-split", "ka.canonical-packet-assembly", "ka.phase-entrypoint-handoff", "ka.command-artifact-mapping", "ka.subagent-context-budgeting", "ka.script-as-coordination-artifact", "ka.archive-literacy", "ka.story-memory-checkpoint"]
}
---
# 项目工作流表面图协议

当前仓库已经很会回答“写什么”“怎么评”“怎么协作”，但外部参考项目提醒我们，还需要更明确地回答“这些东西长期放在哪、怎么流动、谁能改什么、哪些只是运行态”。

`project_surface_map` 就是解决这个问题的。它不是在设计 UI，也不是在设计 CLI，而是在设计一个长期可运转的创作表面层：人和 Agent 该看什么、改什么、导出什么、审查什么。对长周期项目来说，这里面还应该包含“检查点放在哪”：什么时候要产出 resumable state，而不是让下一轮继续靠全量回读。

如果未来仓库要继续往 runtime planner 走，这一层会变成必要基础，而不是可有可无的附录。

## TODOs：待回答问题

- [ ] 不同 medium 是否需要不同默认 surface template？
- [ ] canonical packet 默认是否需要可导出，还是只在 debug / review 模式下导出？
- [ ] review surface 是否应该进一步拆成 craft、continuity、compliance、delivery 四类？
- [ ] export surface 是否应把 human-facing 与 tool-facing 交付分开？
