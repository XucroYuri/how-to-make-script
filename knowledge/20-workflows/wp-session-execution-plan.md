---
{
  "id": "wp.session-execution-plan",
  "type": "workflow_protocol",
  "title": "会话执行规划协议",
  "goal": "当一个用户请求横跨两个以上阶段或输出合同时，把它分解为有序的段落序列，为每个段落指定协议、停止条件和交接合同，避免 Agent 在跨阶段任务中丢失方向或过度加载。",
  "input_contract": ["logline", "premise", "outline", "beat_sheet", "scene_card"],
  "output_contract": ["session_execution_plan"],
  "preconditions": ["用户请求明确横跨两个或以上阶段", "至少可以锁定两个连续的 output 目标"],
  "steps": [
    "判断请求是否真的跨越两个以上阶段——如果不是，退出本协议，用常规单路由处理。",
    "把任务分解为有序段落列表，每段包含：stage（阶段）、output（输出合同）、protocol_id（使用的协议）、stop_condition（完成标准）。",
    "为每个段落之间的接缝指定一个交接合同：下一段必须接收什么，必须忽略什么。",
    "为每个段落标注 budget_class（S/M/L），标出哪些段落可以延后。",
    "在任何跨越 `structure→scene` 或 `scene→rewrite` 边界的两个段落之间插入一次 `wp.story-memory-checkpoint` 调用。",
    "输出计划；**只执行第一段**；在每个后续段落前重新评估计划是否仍然有效。"
  ],
  "fallbacks": [
    "若请求跨越超过5个阶段，要求用户缩小范围，不要生成超过5段的计划。",
    "若段落间的交接合同无法明确（前段产物不确定），先完成前段，再重新规划后续段落。"
  ],
  "stop_conditions": [
    "所有段落均已有明确的 output 合同和 stop_condition",
    "每个段落间的交接合同已写清楚",
    "计划段落数 ≤ 5"
  ],
  "rubrics": ["rb.session-execution-plan"],
  "linked_atoms": ["ka.creative-posture-certainty", "ka.bounded-context-loading", "ka.story-memory-checkpoint"],
  "budget_class": "M",
  "mandatory_atom_count": 3,
  "expansion_allowed": false
}
---
# 会话执行规划协议

会话计划不是项目路线图。它只覆盖当前这一次工作窗口。它的任务是告诉 Agent 下一步做什么，而不是预测项目最终会变成什么样子。

当一个请求横跨多个阶段时，最常见的失败模式不是方向错误，而是 Agent 试图在同一段上下文里完成所有工作，导致后段的产出被前段的噪声污染。这个协议的核心机制是段落间的交接合同：它强制 Agent 明确说清楚哪些内容必须带入下一段、哪些内容必须被搁置，而不是默认把整个上下文一起传递下去。

计划一旦超过 5 段，它就不再是会话计划，而是项目计划。项目计划属于 `wp.project-surface-map` 的职责范围，不应在这里生成。跨越 `structure→scene` 或 `scene→rewrite` 边界时，必须在两段之间显式插入一次 `wp.story-memory-checkpoint`，以防故事状态在边界处静默漂移。

## TODOs：待回答问题

- [ ] 当用户在会话中途修改了其中一个段落的目标，后续段落的交接合同应如何重新校验？
- [ ] budget_class 为 L 的段落是否应该强制拆分，还是允许在用户确认后作为单段执行？
- [ ] 若两个相邻段落使用同一个 protocol_id，是否需要合并为一段，还是保留独立的 stop_condition？
