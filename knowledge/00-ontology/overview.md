# Ontology Overview

`knowledge/` is organized by function, not by chronology.

- `00-ontology`: shared conceptual maps and repository-wide taxonomies.
- `10-foundations`: universal storytelling and screenplay foundations.
- `20-workflows`: composable protocols that turn atoms into outputs.
- `30-craft`: scene-level and line-level craft decisions.
- `40-media`: medium-specific constraints and affordances.
- `50-genre`: reusable genre mechanics.
- `60-rubrics`: quality review frameworks.
- `70-case-studies`: worked examples and interpretation notes.

Structured assets in this repository are machine-checked. Narrative explanation and discussion live in Markdown bodies; reusable metadata lives in JSON frontmatter.

从中文使用者角度看，这一层最重要的价值不是“分类整齐”，而是降低后续扩写时的混乱成本。剧本知识一旦不分层，很快就会出现三种常见问题：同一概念在不同文件里反复改写、流程协议和理论正文互相污染、以及新加内容不知道该挂在哪个层级。这个 ontology 的作用，就是先把“概念层”“流程层”“评分层”“案例层”分开，再允许每一层持续生长。

## TODOs：待回答问题

- [ ] 现有 ontology 是否还缺少一个专门容纳“反模式 / 误诊 / 反例”的层级，而不只是把它们散落在各个 atom 中？
- [ ] 对于同时兼具 narrative、commercial、interactive 属性的混合项目，当前分层是否足够表达，还是需要中间层？
- [ ] 哪些内容现在名义上属于 `knowledge/`，实际上更应该提升为 `references/` 里的稳定规则文档？
- [ ] 当前 ontology 是否缺少“研究证据层”，用于收纳行业经验、方法论出处、争议理论与适用边界？
- [ ] 当一个知识单元同时影响 taxonomy、workflow、rubric 时，应该由哪一层持有主定义，哪几层只保留引用？
- [ ] 仓库扩展到更细粒度后，如何防止出现名称不同但语义重复的知识原子？
- [ ] 中文创作者阅读友好性与 Agent 可路由性发生冲突时，ontology 规则应该优先约束哪一侧？
