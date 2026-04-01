---
{
  "id": "wp.team-workflow-blueprint",
  "type": "workflow_protocol",
  "title": "团队工作流蓝图协议",
  "goal": "根据项目媒介、开发阶段、协作约束和风险结构，输出一份 team_workflow_blueprint，明确采用哪种 team mode、有哪些角色、如何分 lane、如何交接、何时让人类拍板。",
  "input_contract": [
    "project brief",
    "medium",
    "stage",
    "commissioning context",
    "constraints",
    "human availability or approval chain"
  ],
  "output_contract": [
    "team_workflow_blueprint"
  ],
  "preconditions": [
    "已知目标媒介或主要开发容器",
    "至少知道当前任务处于哪个创作阶段",
    "允许把团队结构、交接和人工关口纳入创作设计"
  ],
  "steps": [
    "判断当前项目更适合 room、pod、cell、strike team 还是 continuity board。",
    "定义 decision owner、default roles、parallel lanes 和最小共享真相包。",
    "定义 artifact ladder、handoff contract 和 merge 节奏。",
    "定义 human checkpoints：哪些节点必须人工确认、哪些只需要补证据或范围修正。",
    "定义 failure modes、escalation path 和备用协作模式。",
    "输出 team_workflow_blueprint，明确主要 mode、为什么选它、如何运行、以及何时切换模式。"
  ],
  "fallbacks": [
    "若团队资源未知，先给最小可运行 pod，再给扩展到完整 room 或 strike team 的升级路径。",
    "若用户并不需要团队设计，而只是要单次文本产物，返回原主路由并只附最小 team note。",
    "若当前问题本质上是 audience、development 或 boundary 问题，优先调用对应输出，再把 blueprint 作为配套机制。",
    "若用户真正想知道的是‘谁进场’或‘怎么调度’，再转向 expert_subagent_cast 或 subagent_dispatch_plan。"
  ],
  "stop_conditions": [
    "蓝图已经说明 team mode、角色、lane、handoff、gate 和 owner",
    "主要失败模式和升级条件已明确",
    "蓝图既能支持并行协作，也能避免把项目锁死在唯一组织形态"
  ],
  "rubrics": [
    "rb.team-workflow-blueprint"
  ],
  "linked_atoms": [
    "ka.team-topology-selection",
    "ka.handoff-contract-discipline",
    "ka.human-checkpoint-gates",
    "ka.room-artifact-ladder",
    "ka.parallel-lane-governance",
    "ka.dissent-preservation-loop"
  ],
  "budget_class": "M",
  "mandatory_atom_count": 6,
  "expansion_allowed": true
}
---
# 团队工作流蓝图协议

如果说 `development_brief` 解决的是“项目怎么推进”，那 `team_workflow_blueprint` 解决的就是“谁和谁怎么一起推进”。它不只是列角色名，而是把团队真正会卡住的地方提前显式化：谁拍板、谁发散、谁守边界、谁做合并、谁来背 review 节点。

这个协议的重点不是追求一种“最先进”的组织方式，而是承认不同项目需要不同 team mode。有些项目要 writers' room，有些要 director-writer-producer pod，有些要 campaign strike team，有些要 interactive narrative cell。蓝图的工作，是先选对模式，再把协作成本降下来。

对 Agent Skill 来说，这也是把“多智能体”从口号变成约束的方法。没有角色、handoff、gate 和 artifact ladder，多 agent 只是多上下文噪音。
如果 blueprint 已经选好了 mode，但还需要继续回答“这次具体让哪些专家和 persona 进场”以及“这些 subagent 怎么排班和 review”，就不该继续把所有细节塞回 blueprint，而该交给 `expert_subagent_cast` 和 `subagent_dispatch_plan`。

## TODOs：待回答问题

- [ ] `team_workflow_blueprint` 是否应该拆成“模式选择版”和“执行部署版”两个层级？
- [ ] 当用户希望同时运行 agent team 和真实 human team 时，蓝图是否需要双轨角色图？
- [ ] blueprint 是否需要直接生成 meeting cadence / room agenda / async board 模板？
- [ ] 哪些项目最值得提供 primary mode + backup mode，而不是只给一条主路线？
- [ ] 当团队资源极少时，仓库应如何判断哪些角色可以折叠，哪些绝不能折叠？
