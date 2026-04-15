# Agent 快速参考卡

用于快速做决策的执行卡，帮助 Agent 在处理请求时避免加载过多上下文。

## 1) 先路由，再生成

按固定顺序确定路由维度：

1. `intent`（`discover` / `design` / `draft` / `polish` / `diagnose` / `adapt`）
2. `medium`
3. `stage`
4. `output`
5. `constraints`

## 2) 路由选择规则

- 先以 `intent x medium x stage x output` 为主；
- 当输出候选过于接近时，用 `constraints` 做冲突拆解和优先级补位；
- 不确定时先明确边界（硬边界/软边界），再只问一个会改变路由/产物的澄清问题；
- 若存在多条可行输出，不强行压缩为单一路径，优先保留 `path_options`。

## 3) 加载层级

- `route_kernel`：最小路由安全包；
- `focus_pack`：路由 + 主 protocol + 必要 atoms + 1 个 rubric；
- `compare_pack`：当需要对照/否定分析时再补一条对照层；
- `teaching_pack`：教学/解释/示例场景；
- `survey_pack`：仅在明确要求做宽域调研时使用。

## 4) 停止扩展的条件

- 路由稳定，输出契约已固定；
- 继续加载不再改变路由、契约或自检结论；
- 回答开始偏向“仓库目录总结”而不是“任务解决”；
- 主包已具备 1 个 route anchor、1 个主参考、1 个对照/边界。

## 5) 镜像加载触发（最小化）

- 现实镜像（现实透镜）：仅在需要受众、平台、制片约束、商业模型、委约上下文、成长性矫正时加载；
- 表达镜像：仅在需要 `voice_style_guide`，或明确提出语气/角色连续性约束时加载；
- 视觉桥接：仅在 `visual_language_pack` / `screen_to_video_brief` 或明确跨端交付约束时加载；
- 团队执行镜像：仅在协作设计 / 执行编排任务时加载。

## 6) 输出纪律

- 按请求产物格式输出；
- 末尾附上简短 rubric 式自检；
- `constraints` 触发约束变化时，才补充重载对应包，否则保持最小上下文。
