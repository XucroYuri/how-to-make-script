---
{
  "id": "ka.scenario-factorization",
  "type": "knowledge_atom",
  "title": "场景因子化",
  "kind": "decision_heuristic",
  "summary": "剧本创作场景应被拆成多个可组合因子来理解，而不是被一个单一标签或单一成功范式压扁。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "If the repo starts from one dominant label, it will overfit to genre slogans or platform slogans and lose the ability to route real screenplay work, especially in mixed-scenario briefs.",
  "decision_rules": [
    "Classify the scenario by a stack of factors, not by a single headline label.",
    "Use the smallest factor set that changes the route or the evaluation.",
    "Keep rival routes visible when multiple scenario signatures are still viable.",
    "Treat scenario references as guidance, not canon."
  ],
  "anti_patterns": [
    "genre first, everything else later",
    "one sample becomes the whole rule",
    "route choice is made before the scenario is factorized",
    "creative exploration is forced to obey a final-review rule set"
  ],
  "prompt_primitives": [
    "What kind of scenario is this really?",
    "Which factors matter most here?",
    "What must stay fixed, and what can still vary?",
    "Which success pattern is being referenced, and which rival pattern still exists?"
  ],
  "evaluation_checks": [
    "Can the classification distinguish two superficially similar but operationally different briefs?",
    "Does the factorization explain why one route is better for this request?",
    "Does it preserve at least one viable alternative when the brief is still open?",
    "Does it avoid turning a reference pattern into a universal law?"
  ],
  "links": ["ka.creative-pluralism", "ka.false-universal-warning", "ka.scope-correction", "ka.boundary-first-guidance"],
  "source_status": "derived"
}
---
# 场景因子化

剧本创作场景最容易出错的地方，不是分类太少，而是分类太粗。

如果只用“电影 / 剧集 / 短剧 / 广告”去看一个任务，很多真正影响写法的东西会被吞掉，比如：

- 是要写 `premise` 还是 `rewrite_report`
- 是在做 `brand_campaign` 还是 `spec`
- 观众要的是 `curiosity` 还是 `conversion`
- 故事靠 `goal_obstacle` 还是 `choice_consequence`
- 最后的情绪承诺是 `warmth`、`thrill` 还是 `clarity`

这就是场景因子化要解决的问题。它不是要把创意写死，而是先把问题看清。

## 因子化的原则

1. 先看容器，再看机制。
2. 先看受众要什么，再看故事怎么动。
3. 先看工业条件，再看审美偏好。
4. 先区分探索和审查，再决定要不要收敛。
5. 一条规则被质疑时，先想它是否需要 `scope correction`，而不是立刻推翻或硬保。

## 为什么不能只看一种分类

- 只看媒介，容易把不同工业任务写成同一种方法。
- 只看类型，容易把类型当成万能钥匙。
- 只看平台，容易把平台要求误写成创作真理。
- 只看情绪，容易忽略结构和执行。
- 只看成功案例，容易把局部经验误写成全局规律。

## 场景参考

`scenario-taxonomy.json` 里列出的卡片可以当成参考场景。比如：

- 长片原创开发更像 `goal_obstacle` + `release`
- 短剧更像 `escalation_chain` + `thrill`
- 商业片更像 `conversion` + `single_message`
- 互动叙事更像 `choice_consequence` + `stateful_progression`
- 范围修正更像 `boundary_map` + `surviving_core`

这些都不是唯一正确答案，只是更容易成功的参考范式。真正的任务是根据项目条件选择合适的因子组合，而不是把任何一种范式神化。

## 失败模式

- 把一个成功案例直接升格成所有场景都适用的规则。
- 把“好看”当成“可路由”。
- 把“有风格”当成“有机制”。
- 把探索阶段的开放性误当成最终交付的放行。
- 把反例当成应该直接否定原规则的理由，而不是先做范围修正。

## TODOs: Questions To Keep Open

- [ ] 哪些新场景还需要单独的 factorization card?
- [ ] 哪些因素在中文创作语境里比英文语境更常改变 route?
- [ ] 哪些 scenario families 适合先做参考卡片, 哪些适合先做 workflow?
- [ ] 当两个 scenario cards 同时成立时, 何时应该保留并行路径?
- [ ] 场景因子化是否还需要一个专门的 counterexample registry?
