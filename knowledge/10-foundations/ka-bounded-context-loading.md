---
{
  "id": "ka.bounded-context-loading",
  "type": "knowledge_atom",
  "title": "有界上下文加载",
  "kind": "framework",
  "summary": "Agent Skill 不应靠无限加上下文来换取正确率，而应先锁定 route，再按层级扩容到刚好足够解决当前问题的 bundle。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "没有加载边界的 Agent 很容易把相关知识、邻近知识和可选参考全部一次性装进上下文，导致 route 漂移、注意力稀释和生成质量下滑。",
  "decision_rules": [
    "先锁定 primary route，再决定需要什么加载模式，而不是边看边无限加料。",
    "默认只加载 core bundle；只有当额外材料会改变 route、判断或创意延伸质量时才扩容。",
    "优先加载近邻高价值参考，而不是广撒式把所有看似相关内容塞进上下文。"
  ],
  "anti_patterns": [
    "把整个 repo 当一个大 prompt 读入",
    "在 route 未锁定前就开始堆参考样本",
    "为了求稳把所有邻近媒介和邻近类型都一起加载"
  ],
  "prompt_primitives": [
    "这个请求当前最小足够 bundle 是什么",
    "如果再加一个参考，哪一个最可能改变答案质量",
    "继续扩容会带来真实收益还是只会稀释注意力"
  ],
  "evaluation_checks": [
    "是否先锁定了 route 再开始加载",
    "加载出来的每项内容是否都能解释为什么值得进入上下文",
    "是否避免了无差别扩容"
  ],
  "links": ["ka.scenario-factorization", "ka.reference-pattern-usage", "ka.creative-pluralism"],
  "source_status": "derived"
}
---
# 有界上下文加载

很多 Agent 看起来“很努力”，其实只是不断往上下文里堆东西。短期内它可能显得更全面，长期看却更容易路由漂移、答非所问、创意发散无焦点。

有界上下文加载要解决的，就是这个问题。它要求 Agent 先回答：“为了这次请求，最小足够 bundle 是什么？”只有先把这个问题答对，后面的扩容才有意义。

所谓“有界”，不是让 Agent 变保守，而是让它知道什么时候该停。真正高水平的创意延伸，不是无限找资料，而是在正确的主路线上，补少量但高价值的邻近参考。

## TODOs：待回答问题

- [ ] 对不同模型规模，core bundle 的默认上限是否应该不同？
- [ ] 哪些类型的请求最容易因为 fear of missing out 而过载？
- [ ] 哪些参考类型最容易看似相关、实际只会稀释注意力？
- [ ] 是否需要把 bundle 大小做成可显式声明的 constraint？
- [ ] 当用户显式要求“尽可能多参考”时，仓库应如何避免失控扩容？
