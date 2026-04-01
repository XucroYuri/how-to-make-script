---
{
  "id": "wp.path-options",
  "type": "workflow_protocol",
  "title": "多路径方案协议",
  "goal": "在还不该过早收敛的阶段，为同一 brief 输出多条真正不同且可比较的 path_options。",
  "input_contract": ["brief", "concept fragment", "current direction", "known constraints", "none"],
  "output_contract": ["path_options"],
  "preconditions": [
    "用户处于 discover 或 design 阶段，且仍需要探索多个 viable path",
    "至少存在一个可描述的核心 brief、问题或创作目标"
  ],
  "steps": [
    "锁定当前 brief 中真正不可动的部分，避免伪差异。",
    "根据任务宽度生成 2-5 条彼此不同的可行路径，而不是同一路径的轻微改写。",
    "为每条路径标注其优化目标、主要代价、适配条件与收敛触发点。",
    "输出 path_options，并说明此刻为什么不应过早收敛到单一路径。"
  ],
  "fallbacks": [
    "若 brief 过于模糊，先锁定一个最小核心问题，再生成路径。",
    "若路径差异不明显，回退并改从结构、受众、媒介或约束切分。"
  ],
  "stop_conditions": [
    "窄问题至少有 2 条、宽问题至少有 3 条路径具有清楚差异和 tradeoff",
    "收敛条件足够明确，后续可以转入单路径开发"
  ],
  "rubrics": ["rb.path-options"],
  "linked_atoms": ["ka.creative-pluralism", "ka.divergence-convergence-loop", "ka.false-universal-warning", "ka.boundary-first-guidance"]
}
---
# 多路径方案协议

这个协议不是为了拖延决定，而是为了避免在该发散的时候假装已经知道唯一正确答案。它适合用于 ideation、premise 和部分结构阶段，尤其适合那些“看起来已经有一个方案了，但其实还有别的 viable path”的项目。

真正有用的多路径，不是列三版同义改写，而是让每条路径都改变押注点。比如一条路径押人物关系，一条押高概念引擎，一条押平台留存，一条押互动参与。只有这样，比较才有意义。对窄问题，2 条真正不同的路径也可能已经比 4 条假多样更有价值。

一旦 path_options 做对了，后续收敛就不再是凭感觉，而是基于 tradeoff 的选择。

## TODOs：待回答问题

- [ ] 什么时候 path_options 最适合只给 3 条，什么时候应扩到 5 条？
- [ ] 对高约束 brief，仓库如何防止 path_options 变成形式上的多样性？
- [ ] 不同媒介下，路径差异最应该落在 premise、structure 还是 audience payoff 层？
- [ ] 哪些用户其实并不需要 path_options，而需要直接进入 boundary_map 或 development_brief？
- [ ] path_options 是否需要一个轻量版，用于时间极紧的探索会话？
