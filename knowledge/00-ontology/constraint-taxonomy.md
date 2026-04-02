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

## Expression Constraints

- `voice_target`：当前文本要靠近哪种表达重心，例如压抑愤怒、装轻松的自保、冷幽默式防御、可信赖的专业感。
- `language_register`：语言语域落在哪个区间，例如现实主义、诗性、平台化短句、premium brand、青少年口语、制度性冷感。
- `aesthetic_register`：当前视觉或文化气质更接近哪种美学锚点，例如侘寂、han、toska、realismo mágico、国风写意、MV 节拍感。
- `ip_continuity`：是否要严格守住既有角色 / IP / 品牌人格的表达连续性。
- `experiential_depth`：是否要求文本更强地体现具身化压力、活人感、处境重量。

## Visual Surface Constraints

- `visual_vocab_locale`：这次视觉语言包主要使用哪种工作语，例如 zh、ja、ko、ru、es 或 hybrid。
- `prompt_runtime`：下游是 Sora、Seedance、generic_t2v、previz，还是纯 human handoff。
- `shot_granularity`：当前 bridge 是按 scene、beat、single clip，还是 clip chain 切分。
- `aspect_ratio`：最终容器的画幅，例如 16:9、9:16、1:1。
- `reference_asset_mode`：是否需要 image anchor、video anchor、multimodal anchor，还是纯文本。
- `continuity_invariants`：哪些人物、道具、镜头、色调或关系要素不能漂移。
- `audio_mode`：无声、环境声、音乐、对白、口播、lip-sync 对齐等。
- `text_mode`：无屏幕字、字幕主导、画中文字、品牌文案上屏等。

## Team Constraints

- `team_mode`：当前任务更适合 feature development pod、showrunner room、animation story trust、brand content studio、interactive branch lab，还是 hybrid。
- `coordination_model`：是 supervisor tree、swarm parallel、handoff chain、review board，还是 hybrid。
- `parallelism_budget`：允许多少并行 lanes 同时存在而不失控。
- `human_gate_level`：人类是只做最终审批、关键节点审批，还是全程高频介入。
- `artifact_chain`：团队需要串联哪些产物，例如 premise -> outline -> rewrite report -> production handoff。

## Subagent Constraints

- `subagent_family`：当前最需要的是功能型专家、流程节点，还是参考 persona。
- `persona_policy`：参考 persona 应采用 inspired_by、calibrated_reference，还是明确禁止 roleplay。
- `selection_strategy`：是最小可运行阵容、最大覆盖阵容，还是先小后扩的 staged cast。
- `dispatch_topology`：是 specialist ring、writers room tree、debate board、dual track，还是 two-stage review loop。
- `convergence_owner`：谁拥有 merge / lock / reopen 的最终权责。
- `context_budget`：每条 lane 可以加载多大 bundle，以及何时允许扩容。

## Project Surface Constraints

- `project_horizon`：这是一次性短任务、一个阶段性开发包，还是要长期滚动推进的项目。
- `phase_focus`：当前最关键的是 planning、drafting、review、compliance 还是 export。
- `truth_surface_policy`：哪些文件或表面层被视为 canonical source，谁能直接编辑。
- `runtime_surface_policy`：哪些内容只允许作为 mirror、cache、packet、trace 或 lane summary 存在。
- `packet_strategy`：当前 action 的 canonical packet 如何组装、是否必须可检查、是否允许导出。
- `traceability_level`：这次流程需要多强的可追溯性，是轻量说明、review-ready，还是 audit-ready。
- `edit_policy`：哪些 surface 人可以直接改，哪些 surface 只能通过 sync / compile / export 生成。

## Quality Gate Constraints

- `target_contract`：这次到底在审什么 artifact，例如 `scene_draft`、`commercial_script`、`interactive_branch_map`、`voice_style_guide`、`story_memory_checkpoint`、`project_surface_map`。
- `audit_scope`：是 full audit、lens-targeted、range-limited，还是 recheck。
- `check_depth`：是 preflight、development-room、delivery-ready，还是 acceptance 级检查。
- `lens_focus`：这次是否明确指定要优先看哪些 lenses，例如 continuity、voice、delivery、boundary。
- `recheck_mode`：这是初检、修改后复查，还是只检查变更范围和邻接副作用。
- `acceptance_bar`：当前质量门槛是可继续开发、可进下一工序、可对外提案，还是可直接交付。

## Routing Rule

当这些约束只影响表达细节时，不要切换协议；当它们会改变输出目标、优先级或加载知识包时，必须参与路由。

例如：

- 只是用户补了“偏女性向”，但仍然只是要 `logline`，不一定要切 route。
- 用户要求“先判断这部短剧到底适不适合 18-24 岁刷手机用户”，就该切到 `audience_fit_note`。
- 用户要“先搞清楚这个项目在平台委制语境里该怎么开发”，就该切到 `development_brief`。
- 用户问“我从广告文案转叙事编剧应该怎么练”，就该切到 `learning_path`。
- 用户说“先别写，先把角色 / IP / 品牌的说话方式锁住”，就该优先切到 `voice_style_guide`。
- 用户仍然要 `scene_draft` 或 `dialogue_polish`，但明确要求“别像作者腔 / 要有活人感 / 要守住 IP 角色声音”，就保持原 route，同时追加表达校准包。
- 用户说“先别直接写生成 brief，先给我一套日语 / 韩语 / 俄语 / 西语 / 中文镜头词和视觉表达包”，就该切到 `visual_language_pack`。
- 用户说“把这场戏桥接成一个给 Sora / Seedance / previz 用的可执行 brief”，就该切到 `screen_to_video_brief`。
- 用户问“这个项目应该怎么组织 writers' room / agent team / review board”，就该优先切到 `team_workflow_blueprint`。
- 用户问“这次具体该让哪些 subagent / 专家 / 流程节点 / 名家参考 persona 进场”，就该优先切到 `expert_subagent_cast`。
- 用户问“这些 subagent 应该怎么调度、怎么 review、怎么合并、怎么控制上下文”，就该优先切到 `subagent_dispatch_plan`。
- 用户问“这个项目里哪些是真源、哪些只是运行时镜像、planning / review / export 分别在哪些 surface 上发生”，就该优先切到 `project_surface_map`。
- 用户问“先把当前故事状态压成一个以后能继续写、能 handoff、又不用重新加载全文的检查点”，就该优先切到 `story_memory_checkpoint`。
- 用户问“帮我做自检 / 预检 / 复查 / 验收 / stage-specific audit”，或者正在审的对象本身不是纯故事文本，就该优先切到 `quality_gate_report`。
- 用户仍然要正常产物，但任务明显跨多个 specialist lane 和审查 gate，就保持主 route，同时追加 team lens。
- 用户仍然要正常产物，但如果表面层混乱已经会直接导致误改、漂移或错误 handoff，就保持主 route，同时追加 project-surface lens。
- 用户仍然要正常产物，但如果交付前的 preflight 结果会直接改变下一步行动，就保持主 route，同时追加 quality-gating lens。

## TODOs：待回答问题

- [ ] 约束字段是否还需要加入地域文化、审查风险、演员资源、制作周期等更外层因素？
- [ ] `audience_segment` 与 `audience_need_state` 在什么情况下会相互矛盾，路由应如何处理？
- [ ] 哪些 constraint 更适合在 fixture 中固化，哪些只适合在文档说明层保留？
- [ ] 对一个项目同时存在平台目标、品牌目标、作者目标时，root skill 应优先锁哪个约束？
- [ ] `writer_maturity` 是否需要更细的行为定义，而不是只给抽象等级标签？
- [ ] 当用户完全不提供约束时，系统默认推断的边界应该写到哪里才不容易失控？
- [ ] project surface 约束是否还需要单独拆出 `review_surface_set` 与 `export_surface_set`？
- [ ] 什么级别的项目才值得显式建 `traceability_level`，避免过度流程化？
- [ ] `quality_gate_report` 的 `target_contract` 是否需要与 root output contract 共用同一注册表？
- [ ] `audit_scope` 与 `check_depth` 哪些情况下会互相冲突，谁优先？
