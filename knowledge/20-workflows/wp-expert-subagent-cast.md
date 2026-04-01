---
{
  "id": "wp.expert-subagent-cast",
  "type": "workflow_protocol",
  "title": "专家 Subagent 阵容协议",
  "goal": "根据项目媒介、阶段、创作压力和 team mode，输出一份 expert_subagent_cast，明确哪些功能型 subagent、流程节点和参考 persona 应进场，各自拥有哪些权责、上下文预算和退出条件。",
  "input_contract": [
    "project brief",
    "medium",
    "stage",
    "primary output need",
    "constraints",
    "optional team mode",
    "human availability",
    "optional preferred craft lineage"
  ],
  "output_contract": [
    "expert_subagent_cast"
  ],
  "preconditions": [
    "已知当前项目的主要媒介与开发阶段",
    "用户确实需要具体的 subagent 阵容，而不是只要高层 team mode",
    "允许把功能型角色、流程节点和 persona lens 区分开来"
  ],
  "steps": [
    "先判断当前问题是否真的需要 team mode；若尚未选 mode，先给最小 mode 假设或回退到 team_workflow_blueprint。",
    "选出覆盖当前主要决策压力的核心功能型 subagent。",
    "补上真正影响推进质量的 process-node，例如 divergence、triage、counterexample、merge 或 review。",
    "如有必要，再附加 0-2 个 reference_persona，并明确 persona_level、allowed_use、blocked_use 和 loading_cap。",
    "为每个 subagent 写清 mandate、输入包、输出包、authority、composes_with、deactivate 条件。",
    "输出精简阵容、扩展阵容、裁剪顺序和 human-owned nodes。"
  ],
  "fallbacks": [
    "若用户只是在问‘该用 writers' room 还是 pod’，优先返回 team_workflow_blueprint。",
    "若任务其实只需要一个主路由产物，返回原 route，并附最小 cast note。",
    "若用户要求直接模仿名人本人，改为 reference_persona 的治理版输出，保留 craft lineage 但不做无边界 roleplay。"
  ],
  "stop_conditions": [
    "阵容已经说明 core cast、optional cast、process nodes、persona lenses、human-owned nodes 和 trim order",
    "每个 subagent 都有清楚 mandate、authority 和 context budget",
    "阵容既丰富又克制，没有滑向全员上场或 persona 主导"
  ],
  "rubrics": [
    "rb.expert-subagent-cast"
  ],
  "linked_atoms": [
    "ka.subagent-cast-composition",
    "ka.process-node-specialization",
    "ka.reference-persona-governance",
    "ka.subagent-context-budgeting",
    "ka.convergence-owner-discipline",
    "ka.team-topology-selection"
  ],
  "budget_class": "M",
  "mandatory_atom_count": 6,
  "expansion_allowed": true
}
---
# 专家 Subagent 阵容协议

`team_workflow_blueprint` 回答的是“整体协作模式像什么”。`expert_subagent_cast` 回答的则是“这次到底让谁进场、谁先说、谁只负责挑错、谁拥有收束权、谁只该作为镜头而不是主导者”。

这个协议的关键，不是堆角色名，而是做阵容编排。一个靠谱的 cast，必须同时满足三件事：
- 覆盖当前最关键的创作压力；
- 不把所有压力都塞给一个万能大脑；
- 不让阵容膨胀到把系统拖回上下文腐化。

因此它天然是一份“带删减逻辑”的阵容设计，而不是“角色越多越像专家团队”的幻想清单。

## TODOs：待回答问题

- [ ] `expert_subagent_cast` 是否应该为不同 medium 提供不同的默认阵容上限？
- [ ] persona lens 是更适合写入 optional cast，还是应该单列成 pressure layer？
- [ ] trim order 是否应该按成本、风险还是信息增益排序？
- [ ] 阵容协议是否需要直接输出推荐的 handoff packet 模板？
- [ ] 当用户既要“名家风格”又要“工业可交付”时，阵容协议应如何平衡两者？
