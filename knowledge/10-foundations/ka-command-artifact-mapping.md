---
{
  "id": "ka.command-artifact-mapping",
  "type": "knowledge_atom",
  "title": "阶段到产物的显式映射",
  "kind": "heuristic",
  "summary": "强 domain workflow 往往不是靠一句‘开始写’，而是靠阶段入口与产物面的清晰映射。清楚知道每一步输出什么，会显著降低漂移和返工。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "如果 workflow 只描述抽象阶段，却不说明‘这一步到底会落成什么 artifact’，系统就会越来越依赖口头记忆和隐式上下文，难以交接、复查和批量推进。",
  "decision_rules": [
    "让每个 phase 或入口都映射到一个或一组明确产物，而不是只写‘继续推进’。",
    "产物不仅要说明名称，还要说明其服务对象：给 human 看、给 agent 路由、给下游执行，还是给审查和导出。",
    "不同 media 可以有不同 artifact ladder，但每条 ladder 都应清楚哪些是 planning artifact、runtime artifact、review artifact 和 export artifact。"
  ],
  "anti_patterns": [
    "只有动作，没有产物",
    "所有阶段都在生成同一种大文档",
    "review 和 export 只是正文末尾附加说明，没有独立产物面"
  ],
  "prompt_primitives": [
    "这一步最该产出什么 artifact，谁会消费它",
    "如果要批量推进，这个 artifact 是否足够稳定可复用",
    "下一阶段真正需要读取的，是正文、摘要、packet 还是 review note"
  ],
  "evaluation_checks": [
    "阶段与产物之间是否有清晰映射",
    "artifact ladder 是否能支持交接与批量推进",
    "是否避免了所有事情都挤进一份大文档"
  ],
  "links": ["ka.phase-entrypoint-handoff", "ka.source-of-truth-runtime-split", "ka.project-surface-taxonomy"],
  "source_status": "synthesized"
}
---
# 阶段到产物的显式映射

外部项目给当前仓库的一个直接提醒是：优秀的创作 Agent 系统，往往会把“这一步做什么”和“这一步产出什么”绑得很紧。不是因为命令多，而是因为产物面清楚。

对剧本项目来说，这种清楚非常值钱。你知道 `/创作方案` 产出的是故事骨架，`/目录` 产出的是分集目录，`/自检` 产出的是质量审查，那么交接、批量推进和返工优先级就会自然清晰很多。

仓库不一定要复制命令行形态，但应该学习这种“阶段 -> artifact surface”的思维。

## TODOs：待回答问题

- [ ] 当前仓库有哪些 workflow 还缺少清楚的 artifact ladder？
- [ ] 哪些 output contract 其实适合作为 phase artifact，而不是直接给最终用户的终局产物？
- [ ] 不同媒介的 artifact ladder 差异，是否值得沉淀为 machine-readable registry？
- [ ] 对未来 runtime planner 来说，哪些 artifact 应优先拥有 export surface？
