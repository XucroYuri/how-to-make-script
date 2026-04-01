# 外部参考项目教训与吸收点

这份文档不是在列“致敬名单”，而是在明确：当前仓库从相邻项目里到底学到了什么，哪些值得吸收，哪些不该照搬。

## 参考项目 1：InkOS

来源：
- [Narcooo/inkos](https://github.com/Narcooo/inkos)

最有价值的设计点：
- 把长期控制文档和运行时产物拆开；
- 先编译输入，再进入写作，而不是把一坨 prompt 直接塞给模型；
- 让 runtime trace 可检查；
- 规则不是平铺成一段说明，而是有层级、有覆盖关系；
- 给人看的长期意图文档和给系统执行的状态文档明确分开。

值得仓库吸收的：
- 更强的 packet 观念；
- 长期意图与当前阶段关注点分层；
- 高价值写作 / 审查动作的输入可追溯。

不该直接照搬的：
- 小说章节级的字数治理；
- 以章节为中心的 CLI 入口形态；
- 只适合网文长篇的题材规则和 telemetry。

## 参考项目 2：Openwrite Skill

来源：
- [LiPu-jpg/Openwrite_skill](https://github.com/LiPu-jpg/Openwrite_skill)

最有价值的设计点：
- planning 和 drafting 分成不同入口；
- 资产成熟后再显式 handoff 给正文 Agent；
- `src/` 真源和 `data/` 运行态 / 派生层明确分开；
- 通过 canonical packet 组装上下文，而不是让上下文装配变成黑箱；
- 给用户看当前到底加载了什么，提升可调试性和信任。

值得仓库吸收的：
- 更清楚的阶段入口；
- 更严格的真源 / 运行态分层；
- 更明确的 planning -> drafting handoff 门槛。

不该直接照搬的：
- 小说章节和卷纲的目录结构；
- 完全面向长篇网文的风格抽取与大纲层级；
- Goethe / Dante 这种命名和命令表面本身。

## 参考项目 3：Short Drama

来源：
- [0xsline/short-drama](https://github.com/0xsline/short-drama)

最有价值的设计点：
- domain workflow 一旦把“阶段 -> 产物”写清楚，生产力会明显更强；
- quality、自检、合规、导出都应该有独立表面；
- 海外模式、格式切换、市场转换最好显式化；
- 短剧生产线需要更强的节奏、钩子、卡点、审查与批量推进意识。

值得仓库吸收的：
- 更明确的 artifact ladder；
- 更独立的 review / compliance / export surface；
- 更好的短剧工作流设计，而不是默认所有剧本都按长片逻辑组织。

不该直接照搬的：
- 把短剧的钩子配比、付费卡点比例、题材模板当成全谱系通用法则；
- 把平台或市场的合规逻辑误写成仓库的普适真理；
- 让短剧命令界面成为所有剧本创作的默认入口。

## 参考项目 4：Shanyin Screenwriting Master

来源：
- [Shanyin-ai/shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master)

最有价值的设计点：
- 明确把超短、短篇、长片、剧集拆成不同容器，而不是假设同一条 prompt 线性放大就够用；
- 把外部剧情推进和内部情绪推进当成两条相关但不同的节奏线来看；
- 用记忆检查点维护长篇连续性，而不是默认每次都重载全文；
- 在连续容器里先锁时长、集数和弧光预算，再决定 reveal 和关系跃迁怎么花。

值得仓库吸收的：
- 把 continuity compression 做成一等输出，而不是临时摘要；
- 在结构协议里补强连续容器和弧光预算逻辑；
- 用双轨节奏来诊断“外面很忙、里面没动”或“情绪很浓、外部没推”的病型。

不该直接照搬的：
- 把一整套巨型集成 prompt 当成主真源；
- 把不可见的内部自检当成可以替代 protocol / rubric / artifact 的机制；
- 使用容易漂移的打包表面，而不保留清晰的可编辑源资产。

## 这轮对本仓库的直接推动

基于这四个项目，仓库现在进一步承认并补强了这些点：
- `project_surface_map` 作为一等输出；
- `story_memory_checkpoint` 作为一等的长线连续性输出；
- source-of-truth 和 runtime-state 的明确分层；
- canonical packet 的组装和可追溯性；
- planning / drafting / review / export 的阶段入口意识；
- review 和 export surface 作为显式工作流层，而不是正文附带说明。
- 不同容器的结构放大逻辑、双轨节奏和连续剧弧光预算。

## 非教条原则

这些外部项目是“强案例”，不是“唯一答案”。

仓库的吸收方式应该永远是：
- 提取能跨项目泛化的设计思想；
- 保留只适合特定媒介 / 特定工具 / 特定市场的部分在局部范围内；
- 不把外部项目的局部成功误当成普适正确。
