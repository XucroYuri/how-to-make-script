---
{
  "id": "wp.subagent-dispatch-plan",
  "type": "workflow_protocol",
  "title": "Subagent 调度计划协议",
  "goal": "根据当前项目和所选阵容，输出一份 subagent_dispatch_plan，明确多层级调度结构、phase ladder、dispatch topology、handoff packet、review loop、human gates 和 context budget。",
  "input_contract": ["project brief", "medium", "stage", "selected output or workflow", "constraints", "optional team mode", "optional expert cast", "human gate assumptions"],
  "output_contract": ["subagent_dispatch_plan"],
  "preconditions": [
    "已知主路由或至少已知当前主要产物",
    "任务确实需要说明如何调度 subagent，而不只是说明谁在场",
    "允许把 phase、lane、review loop 和 handoff 机制显式化"
  ],
  "steps": [
    "确认 control plane 顺序：route -> team mode -> cast -> dispatch topology。",
    "根据 medium、risk profile 和 artifact chain 选择合适的 topology 与 phase pattern。",
    "为每一层写清 owner、parallel lanes、merge 节点、truth packet 和 stop condition。",
    "规定每个 lane 的 context budget，以及哪些信息只能通过 handoff packet 共享。",
    "如果任务需要 review loop，优先拆成 spec compliance 与 quality review 两阶段。",
    "标出 human gates、fallback topology、collapse trigger 和 mode-switch trigger。"
  ],
  "fallbacks": [
    "若任务只需要 team mode 说明，回退到 team_workflow_blueprint。",
    "若任务只需要阵容说明，回退到 expert_subagent_cast。",
    "若团队规模极小，输出最小 dispatch：one owner + one specialist + one review gate。"
  ],
  "stop_conditions": [
    "计划已经说明 topology、phase ladder、lane budget、handoff packet、merge owner、review loop 和 human gates",
    "系统知道何时扩容、何时裁剪、何时切换模式",
    "没有任何关键节点默认共享全量上下文"
  ],
  "rubrics": ["rb.subagent-dispatch-plan"],
  "linked_atoms": ["ka.subagent-context-budgeting", "ka.convergence-owner-discipline", "ka.two-stage-review-loop", "ka.handoff-packet-discipline", "ka.parallel-lane-governance", "ka.team-topology-selection"]
}
---
# Subagent 调度计划协议

如果说 `expert_subagent_cast` 解决的是“谁进场”，那 `subagent_dispatch_plan` 解决的就是“这些 subagent 到底怎么跑”。这是多智能体系统最容易被口号化的部分，因为很多方案喜欢展示“很多专家同时参与”，却不展示谁合并、谁裁决、谁复核、谁决定什么时候停。

在这个仓库里，调度计划必须是可执行的。它不只是拓扑图，而是包括：
- 哪一层是 control plane；
- 哪些 lane 可以并行；
- 哪些 review 必须后置；
- 什么信息通过 packet 传；
- 哪些节点必须交给人类；
- 哪些情况下要缩回更保守的模式。

真正的高水平调度，不是让所有人都说上话，而是让每个人在对的时间、拿着对的上下文、说对的问题。

## TODOs：待回答问题

- [ ] `subagent_dispatch_plan` 是否需要区分“repo 开发型调度”和“剧本创作型调度”两大类？
- [ ] 哪些 topology 最适合长周期 feature development，哪些更适合高频短周期品牌内容？
- [ ] handoff packet 是否应针对 persona lane、functional lane、review lane 采用不同字段集？
- [ ] 调度计划是否应该显式给出 token / latency / merge-cost 预算？
- [ ] 在没有稳定 human feedback 的环境里，哪些 topology 最安全？
