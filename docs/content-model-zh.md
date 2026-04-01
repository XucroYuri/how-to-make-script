# 内容模型

## 结构化 Markdown

可复用知识以 Markdown 文件形式存在，并带 JSON frontmatter：

```markdown
---
{
  "id": "ka.story-goal",
  "type": "knowledge_atom",
  "title": "故事目标",
  "...": "..."
}
---
# Human-readable body
```

这种形式让文件同时具备以下特点：

- 在 GitHub 中可直接阅读；
- 人类易于编辑；
- 对 Python 工具链依赖很轻；
- agent 可以按需选择性加载。

JSON frontmatter 是机器契约，Markdown 正文是人类解释。两者必须保持一致。

## 资产类型

### `knowledge_atom`

- 最小可复用的 craft 单元。
- 表达一个理论、策略、规则、失败模式或决策启发。
- 它应足够具体，能够驱动一次明确判断，而不是一团松散主题。
- 它也应足够窄，避免一加载就把无关 craft 包袱带进答案。

### `workflow_protocol`

- 稳定的创作工作流契约。
- 定义多个 atom 如何组合成一个目标输出。
- 它应该回答：输入是什么、输出是什么、经过哪些步骤、何时停止。
- 一旦 route 被选中，它就是 agent 行为的主要驱动层。

### `evaluation_rubric`

- 把定性的口味判断转成可执行的审查维度和 hard-fail 规则。
- 它应该让 rewrite 决策更具体，而不是停留在模糊评价。
- 在回答阶段，它应该可以直接作为紧凑的 self-check 使用。

### `example_fixture`

- 编码示例请求及其预期 route，供回归检查使用。
- 它的重点应该是 route selection，而不只是内容生成。
- 它应代表真实用户请求，而不是只服务 schema 的玩具样本。

真实世界锚定类输出也是一等契约：

- `audience_fit_note`
- `development_brief`
- `learning_path`
- `path_options`
- `boundary_map`
- `scope_correction`
- `pattern_reference_pack`
- `context_loading_plan`
- `voice_style_guide`
- `visual_language_pack`
- `screen_to_video_brief`
- `team_workflow_blueprint`
- `expert_subagent_cast`
- `subagent_dispatch_plan`
- `project_surface_map`
- `quality_gate_report`

这些契约存在的目的，是让 agent 可以显式推理受众需求、委托语境与作者成长，而不是把这些因素藏进泛化 prose。
它们也让仓库能够直接表达多路径并存、边界逻辑、claim 收窄行为、对照式参考教学以及 bounded loading 控制，而不是假装所有好答案都能塌缩成一个规范工件。
新的 expression 契约让 voice、register、continuity 与“活人感”成为显式质量维度，而不把所有起草任务都塞进 style-template 工作流。
新的 visual-language 契约让跨语言镜头词汇与文化绑定的视觉锚点显式化，而不把所有剧本请求都强行拖进 multilingual 模式。
新的 screen-to-video bridge 契约让下游视觉转译成为显式层，而不把剧本写作和供应商 prompt 语法混在一起。
新的 team 契约让多智能体与人机协作成为显式对象，而不是假设一种 workflow 适用于所有媒介和制作环境。
新的 expert-cast 契约允许选择有边界的专家 subagent 与 reference persona lens，而不是把所有 route 膨胀成永久团队。
新的 dispatch-plan 契约让排期、handoff、review 顺序和上下文预算显式可见，而不是把 orchestration 留在隐形 prompt 经验里。
新的 project-surface 契约让 canonical truth、runtime mirror、packet assembly、review surface 和 export surface 显式化，而不是把长周期项目设计交给隐含的 repo 习惯。
新的 quality-gate 契约让自适应、按 lens 叠加的 self-check 显式化，这样仓库才能审查文本、bridge、治理工件和 recheck 范围，而不把一切压平成一个 rewrite note。

## 资产规则

- 每个资产都必须有稳定的 `id`。
- 每个被链接的 `id` 都必须可解析。
- 每个 protocol 都必须声明其 rubrics 与 linked atoms。
- 每个 fixture 都必须声明预期 route。
- 如果某个资产无法自动验证，就应继续拆分，直到可以验证。
- 如果某个输出依赖受众/行业/历史/作者成长约束，应把这种依赖编码进 protocol 与 fixture constraint，而不是写成临时 prompt 文字。
- 如果某条规则不是普遍真理，应编码它的前提、边界条件或 rival route，而不是把限制藏在 prose 里。
- 如果一次挑战削弱了一条 claim，但没有摧毁其核心，应优先做 scope correction，而不是删除 claim 或翻成新的绝对论。
- 如果一个参考样本被用于教学，应同时配一个 failure contrast 和一个 non-dogma 注记，避免仓库把样本悄悄当成模板。
- 如果请求很复杂，应显式决定要加载多少周边上下文，而不是无声扩大上下文包。

## 问题积压表

在新增资产之前，先查看苏格拉底式问题积压表：

- [`docs/socratic-question-backlog-en.md`](./socratic-question-backlog-en.md) 用于 agent-facing intake；
- [`docs/socratic-question-backlog.md`](./socratic-question-backlog.md) 用于 practitioner-facing intake。

这个 backlog 是 discovery layer，不是 source-of-truth layer。它的作用是把缺口导向四种明确结果之一：

- 新 atom；
- 新 protocol；
- 新 rubric；
- 新 fixture 或案例说明。

因此，这个内容模型优化的是 bounded loading、route stability 和可重复的输出行为，而不是一次性概述整个仓库。
它也应保留高质量分歧，为仓库提供存放 rival path、延后边界和由 counterexample 驱动的修正的位置。

关于当前的现实锚定层，请把本文与以下文档配套阅读：

- [`docs/reality-lenses-zh.md`](./reality-lenses-zh.md)
- [`docs/source-map-real-world.md`](./source-map-real-world.md)
- [`docs/epistemic-stance-zh.md`](./epistemic-stance-zh.md)
- [`docs/exploration-vs-review.md`](./exploration-vs-review.md)
- [`docs/scenario-atlas-zh.md`](./scenario-atlas-zh.md)
- [`docs/context-loading-policy-zh.md`](./context-loading-policy-zh.md)
- [`docs/semantic-governance-zh.md`](./semantic-governance-zh.md)
- [`docs/progressive-disclosure-policy-zh.md`](./progressive-disclosure-policy-zh.md)
- [`docs/private-reference-distillation-policy-zh.md`](./private-reference-distillation-policy-zh.md)
- [`docs/source-map-screenplay-methods-zh.md`](./source-map-screenplay-methods-zh.md)
