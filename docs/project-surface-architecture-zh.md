# 项目表面层架构

仓库现在正式把一个过去只隐含存在的层补出来了：

- 不只是“写什么”；
- 不只是“怎么路由”；
- 不只是“谁来协作”；
- 还包括“长期真源放哪、运行态放哪、packet 怎么组、review 和 export 表面放哪”。

## 为什么这层重要

当前仓库在这些地方已经很强：
- route 选择；
- bounded loading；
- output contract；
- team mode；
- subagent cast 与 dispatch。

但它之前还欠一块长期项目能力：
- 人到底该改哪些表面层；
- 哪些运行态应该由系统派生而不是人工维护；
- packet 应该如何被组装和检查；
- 审查和导出应该落在哪一层。

外部参考项目把这个缺口照得很清楚。

## 表面层分法

### Canonical Source

这是可以直接改的真源。

例如：
- 故事核心设定；
- 世界规则锚点；
- 大纲真源；
- 角色锚点；
- 品牌 / 委制锚点；
- continuity anchors。

### Runtime State

这是为了跑当前阶段而生成的派生层。

例如：
- workflow state；
- 当前场景 / 当前集状态镜像；
- packet 编译结果；
- lane 摘要；
- trace 和 telemetry。

它们默认应可再生，不应该默默升级成真源。

### Packet Layer

这是一次具体动作真正读取的那一包输入。

它至少要能说明：
- 读了哪些真源；
- 读了哪些局部状态；
- 规则层是什么；
- 上游 handoff 是什么；
- 当前任务意图是什么；
- 什么时候该停。

### Review Surfaces

这是在交付前暴露问题的表面层。

例如：
- craft review；
- continuity review；
- compliance review；
- downstream surface review；
- delivery readiness review。

### Export Surfaces

这是给下游 human 或 tool 的交付表面层。

例如：
- 可阅读的剧本包；
- 制片 / 分镜 / 视频桥接包；
- 可归档的 packet；
- 供同步和交接的导出层。

## 设计原则

不要把项目表面层做成“隐式存在”。

如果未来仓库继续长成 runtime planner，这一层不应该到那时再临时发明，而应该从现在就作为知识与协议层被清楚定义。

## 关联文件

- [`wp.project-surface-map`](../knowledge/20-workflows/wp-project-surface-map.md)
- [`rb.project-surface-map`](../knowledge/60-rubrics/rb-project-surface-map.md)
- [`docs/reference-project-lessons-zh.md`](./reference-project-lessons-zh.md)
