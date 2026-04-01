# Constraint Taxonomy

`constraints` 不是零散备注，而是会改变 route 和输出质量的路由信号。当前仓库需要把现实世界约束显式分类，否则系统容易把所有问题都误判成纯 craft 问题。

建议统一使用以下约束簇：

## Audience Constraints

- `audience_segment`：核心人群是谁，不只写年龄，也包括观看位置和内容关系。
- `audience_need_state`：观众来找的是释放、代偿、刺激、安慰、共鸣、身份认同、参与感还是讨论价值。
- `taste_floor`：观众能接受的复杂度、慢热程度、信息密度下限。
- `taste_ceiling`：观众对套路感、说教感、低密度的容忍上限。

## Industry Constraints

- `commissioning_context`：独立开发、平台命题、品牌 brief、导演驱动、IP 改编、游戏任务等。
- `business_model`：票房、订阅留存、广告转化、品牌好感、互动留存、IP 孵化。
- `release_window`：院线、长视频平台、社交平台、游戏内叙事、节展、内部提案。
- `deliverable_mode`：pitch、development note、outline、production-facing draft、writers' room packet。

## Production Constraints

- `budget_band`：小体量、中体量、大体量。
- `episode_count` / `duration_seconds` / `episode_minutes`：时长容器。
- `rating`：分级边界。
- `franchise_ip_limits`：是否可改写核心世界观与角色设定。

## Platform Constraints

- `platform`：院线、流媒体、短视频平台、品牌自媒体、游戏客户端等。
- `retention_window`：前 3 秒、前 30 秒、首场戏、首幕、前两集等关键留存窗口。
- `interaction_model`：线性观看、分支选择、循环参与、UGC 评论传播。

## Writer Constraints

- `writer_maturity`：新手、进阶、职业化、showrunner / head writer 预备。
- `failure_layer`：概念、结构、场景、对白、返修、行业理解。
- `reference_bar`：目标参照是练习级、投递级、开发级还是生产级。

## Routing Rule

当这些约束只影响表达细节时，不要切换协议；当它们会改变输出目标、优先级或加载知识包时，必须参与路由。

例如：

- 只是用户补了“偏女性向”，但仍然只是要 `logline`，不一定要切 route。
- 用户要求“先判断这部短剧到底适不适合 18-24 岁刷手机用户”，就该切到 `audience_fit_note`。
- 用户要“先搞清楚这个项目在平台委制语境里该怎么开发”，就该切到 `development_brief`。
- 用户问“我从广告文案转叙事编剧应该怎么练”，就该切到 `learning_path`。

## TODOs：待回答问题

- [ ] 约束字段是否还需要加入地域文化、审查风险、演员资源、制作周期等更外层因素？
- [ ] `audience_segment` 与 `audience_need_state` 在什么情况下会相互矛盾，路由应如何处理？
- [ ] 哪些 constraint 更适合在 fixture 中固化，哪些只适合在文档说明层保留？
- [ ] 对一个项目同时存在平台目标、品牌目标、作者目标时，root skill 应优先锁哪个约束？
- [ ] `writer_maturity` 是否需要更细的行为定义，而不是只给抽象等级标签？
- [ ] 当用户完全不提供约束时，系统默认推断的边界应该写到哪里才不容易失控？
