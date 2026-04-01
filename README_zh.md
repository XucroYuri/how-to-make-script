[English](./README.md)

# how-to-make-script

`how-to-make-script` 是一个“研究库优先”的开源 Agent Skill Monorepo，用来把“如何创作剧本”这件事拆成可持续累积、可精确调用、可机器校验、可长期升级的知识资产系统。

它同时面向两类对象：
- 人类创作者：系统学习剧本创作知识、方法、判断规则、改稿逻辑；
- LLM / Agent：在不同媒介、不同阶段、不同目标产物下调用最小必要知识包完成创作任务。

当前版本额外加入了“现实世界 grounding”能力，避免产出只在纸面上成立，却和真实需求脱节。核心会显式考虑：
- 受众细分与需求状态；
- 行业委托场景与商业模型；
- 平台分发与档期逻辑；
- 编剧能力成熟度与训练路径；
- 编剧实践的历史演进与当下约束。

这不是把一堆“提示词模板”堆在一起的仓库。它更像一套剧本研发基础设施：上层是 skill 和协议，底层是可复用的知识原子、评估标准、路由规则和样例夹具。人来读，可以系统学习；Agent 来调，可以按契约拿料，不用每次从一大坨说明文里硬猜。

它也明确是一个 `human-in-the-loop` 项目：
- 不把 issue 区当报错回收站，而把它当知识修正入口；
- 不把质疑当添乱，而把高质量反驳当升级信号；
- 不追求“大家都说好”，而追求“有人指出哪里不对、为什么不对、该怎么修”。

## V1 的定位

V1 不先做 Web App，也不先做重型数据库，而是先把基础设施打稳：
- 剧本创作知识本体与 taxonomy；
- 高细粒度 `knowledge_atom`；
- 可编排的 `workflow_protocol`；
- 可自检的 `evaluation_rubric`；
- 总控 skill 与薄编排子 skill；
- 示例、fixture、校验脚本、测试与 CI。

## 首批重点深挖

仓库整体 taxonomy 覆盖全谱系，但首轮高密度沉淀优先三大簇：
- 叙事剧本
- 商业 / 品牌脚本
- 互动 / 分支叙事

对应的人类工作场景也很明确：
- 编剧或策划先用它把 premise、人物关系、结构、场景功能、对白策略拆清楚；
- 剧本医生用它定位概念病、结构病、场景病、对白病分别出在哪里；
- Agent 用它根据 `intent x medium x stage x output x constraints` 走最短路径，而不是每次都重新“理解一下你想要什么”。
- 当任务涉及市场定位、开发策略或编剧培养时，Agent 会额外调用现实维度镜头，不再只给纯 craft 建议。

## 仓库结构

```text
how-to-make-script/
├── SKILL.md
├── knowledge/
├── schemas/
├── skills/
├── references/
├── examples/
├── scripts/
└── tests/
```

## 四类一等资产

- `knowledge_atom`：最小知识单元，表达单一理论、技巧、规则、失败模式或创作策略。
- `workflow_protocol`：把知识单元编排成稳定工作流。
- `evaluation_rubric`：把“好不好”变成可执行的质量判断。
- `example_fixture`：把“理论可调用”变成“行为可验证”。

这四层的关系可以理解成：
- `knowledge_atom` 负责回答“这里到底在讲哪一个专业判断点”；
- `workflow_protocol` 负责回答“先做什么，再做什么”；
- `evaluation_rubric` 负责回答“现在这版到底行不行、差在哪”；
- `example_fixture` 负责回答“这套东西是不是能被稳定调用，而不是看心情发挥”。

新加入的三类现实向目标产物：
- `audience_fit_note`：受众匹配说明，回答“给谁看、为什么会看、哪里不匹配”；
- `development_brief`：开发策略简报，回答“在什么行业语境里怎么推进最稳”；
- `learning_path`：编剧成长路径，回答“当前能力到目标能力应该怎么练”。

## 中文内容怎么写

这个仓库的中文内容不是英文说明的逐句翻译版，而是偏向剧本专业人员阅读体验的版本。它会优先追求三件事：
- 术语像行业里会说的话，不写翻译腔；
- 解释落到创作动作上，不停留在空泛理念；
- 复杂概念尽量说人话，但不牺牲专业判断力。

如果你是编剧、策划、导演、文学策划、短剧开发、品牌内容负责人或剧本医生，中文正文应该更接近你实际会拿来讨论和返修的语言层级。

## 快速验证

```bash
python3 scripts/validate_assets.py
python3 scripts/check_routes.py
python3 scripts/check_forbidden_paths.py
python3 scripts/check_question_todos.py
python3 scripts/run_fixture_suite.py
python3 -m unittest discover -s tests -v
```

## 安装为 Skill

### Codex

在 `~/.codex/config.toml` 中加入：

```toml
[[skills.config]]
path = "/absolute/path/to/how-to-make-script"
enabled = true
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s /absolute/path/to/how-to-make-script ~/.claude/skills/how-to-make-script
```

### OpenCode

```bash
mkdir -p ~/.config/opencode/skills
ln -s /absolute/path/to/how-to-make-script ~/.config/opencode/skills/how-to-make-script
```

## 关键原则
- 路由必须显式基于 `intent x medium x stage x output x constraints`。
- 当现实维度会改变结论时，必须加载 audience / industry / history / writer-development / platform 相关镜头。
- 子 skill 必须是薄编排层，不复制知识正文。
- 已发布 ID 不可重命名，只能废弃或 supersede。
- 新理论、新媒介、新案例优先采用追加式扩展。
- `.obsidian/` 属于禁止进入 Git 的本地工作区状态，当前索引和历史都不允许包含它。
- 英文层优先服务 Agent 调度与执行，中文层优先服务专业创作者阅读与判断。

## 推荐先读
- [架构说明](./docs/architecture.md)
- [内容模型](./docs/content-model.md)
- [现实镜头说明](./docs/reality-lenses-zh.md)
- [现实世界来源地图](./docs/source-map-real-world.md)
- [社区反馈回路](./docs/community-feedback-loop-zh.md)
- [社区分诊机制](./docs/community-triage-loop.md)
- [路线图](./docs/roadmap.md)
- [双语写作策略](./docs/bilingual-authoring.md)
- [苏格拉底式问题总表](./docs/socratic-question-backlog.md)
- [仓库治理](./docs/repository-hygiene.md)
- [taxonomy 说明](./references/taxonomy.md)
- [路由策略](./references/routing-policy.md)

## 社区协作方式

如果你想真正帮助这个仓库变强，最有价值的往往不是一句“不错”，而是下面这些具体反馈：
- “这个判断在真实项目里会失效。”
- “这个 route 选错协议了。”
- “这个 rubric 没抓到真正的专业失败点。”
- “这个行业 / 受众假设已经过时或过宽。”
- “这个学习路径看起来对，但实际教不会。”

欢迎你直接开 issue 来反驳、举反例、给一线经验、指出漏判。这个项目希望把这种质疑变成默认协作方式，而不是例外。
