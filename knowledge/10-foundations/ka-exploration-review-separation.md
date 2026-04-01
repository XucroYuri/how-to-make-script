---
{
  "id": "ka.exploration-review-separation",
  "type": "knowledge_atom",
  "title": "探索-审查分离",
  "kind": "framework",
  "summary": "创意探索阶段与后续审查阶段应被明确区分，避免把发散期和放行期混为一谈。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "rewrite", "adaptation"],
  "problem": "系统要么在 ideation 阶段过早自我审查，要么反过来把探索当成最终批准，导致两边都失真。",
  "decision_rules": [
    "探索阶段可暂缓 soft conformity checks，但不能撤下 hard safety boundaries。",
    "review 阶段必须把 audience、production、platform、release、brand 与 safety 等约束重新加回。",
    "任何看起来大胆的探索结论，在进入最终产物前都必须经过 review gate。"
  ],
  "anti_patterns": [
    "把 ideation 当成最终批准",
    "把软约束前置成创意阶段的道德审查",
    "把硬边界后移到最后才想起"
  ],
  "prompt_primitives": [
    "当前是在探索还是在审查",
    "哪些约束此刻可以暂缓，哪些必须保持",
    "进入最终交付前还需要经过哪些 gate"
  ],
  "evaluation_checks": [
    "探索和审查是否明确分层",
    "hard boundary 是否在所有阶段持续可见",
    "review gate 是否足以拦住不该进入最终交付的内容"
  ],
  "links": ["ka.boundary-first-guidance", "ka.creative-pluralism", "ka.audience-need-state", "ka.commissioning-fit"],
  "source_status": "derived"
}
---
# 探索-审查分离

创作里很常见的一种混乱，是把“我现在只是想看看还有什么可能”与“这东西已经可以拿去交付”混成一件事。前者需要空间，后者需要约束。两者不分，系统就会要么太保守，要么太冒险。

探索-审查分离的核心不是取消约束，而是改变它们进场的时机。比如品牌风格、平台优化、市场熟悉度这些 soft constraint，很多时候可以后置；但安全、伤害、隐私、非法剥削这类 hard boundary 不能离场。

这条原则尤其适合 Agent，因为系统天生倾向于把每一次输出都伪装成最终答案。仓库需要显式告诉它：不是每次都要立刻“放行”，很多时候先发散，后 review，才是更成熟的工作方式。

## TODOs：待回答问题

- [ ] 哪些用户请求应该默认被判定为 exploration，而不是 review？
- [ ] 对高风险商业发布项目，探索阶段可放松的 soft constraint 会不会更少？
- [ ] 互动叙事的 exploration 与 review 是否需要额外的 state / player impact gate？
- [ ] 哪些团队流程最容易把“探索性草案”误拿去当最终交付？
- [ ] 如何让 Agent 在输出里显式标注“这是 exploration candidate，不是 final approval”？
