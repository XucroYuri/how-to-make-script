---
{
  "id": "wp.quality-gate-report",
  "type": "workflow_protocol",
  "title": "自适应质检报告协议",
  "goal": "针对任意剧本相关 artifact 输出一份 quality_gate_report，按 target contract 选择适配的检查 lenses，分离 hard fail 与 weighted weakness，并给出 correction ladder 与 recheck plan。",
  "input_contract": ["artifact under review", "target contract or inferred artifact family", "medium", "scope mode", "constraints", "optional prior findings or diffs"],
  "output_contract": ["quality_gate_report"],
  "preconditions": [
    "存在可审查的 artifact，或至少存在一个可明确界定的 target contract",
    "用户的核心需求是审查、预检、复查、验收或 quality gate，而不是纯生成",
    "允许把 hard fail 与 soft weakness 分开表达"
  ],
  "steps": [
    "先锁定 target contract、medium、scope mode，以及这次质检是 full audit、lens-targeted、range-limited 还是 recheck。",
    "先过 target contract 对应的原生 rubric 或最接近的 contract gate，防止一开始就查错题。",
    "再从 references/check-lens-matrix.json 中选择最小有效 lens stack，并写明为什么选这些 lenses，而不是跑固定全量流程。",
    "让每个 lens 在 bounded brief 下独立检查 artifact，只接收 artifact、本 lens 定义、contract 和压缩后的 metrics。",
    "分离 hard fail、weighted weakness、open contradictions 和 confidence notes，不把所有问题揉成一个平均分。",
    "聚合成 correction ladder：哪些问题必须先停、先修、再观察，哪些只是后续优化项。",
    "如果请求包含复查或范围限定，输出 recheck plan，说明要回查哪些 lenses、哪些变更会触发升级到 full audit。"
  ],
  "fallbacks": [
    "若用户主要需要 story/text 的改稿优先级，而不是多镜头质检，返回 rewrite_report。",
    "若用户主要是在问边界或范围修正，返回 boundary_map 或 scope_correction。",
    "若用户只是在问该如何加载审查上下文，而不是直接出审查结果，返回 context_loading_plan。",
    "若 artifact 太少，保守输出 preflight risk note，不伪装成完整 quality gate。"
  ],
  "stop_conditions": [
    "报告已说明 contract、scope、selected lenses、hard fail、weighted weakness、correction ladder 和 recheck logic",
    "lens 选择理由清楚，且没有无端扩大为固定全量审查",
    "用户能据此决定是继续修改、局部复查，还是回退上游阶段"
  ],
  "rubrics": ["rb.quality-gate-report"],
  "linked_atoms": [
    "ka.contract-first-quality-gating",
    "ka.adaptive-quality-lens-selection",
    "ka.review-lens-isolation",
    "ka.metrics-handoff-compression",
    "ka.hard-gate-soft-score-separation",
    "ka.targeted-recheck-loop"
  ]
}
---
# 自适应质检报告协议

这个协议吸收的是“多层检查、隔离视角、聚合诊断、复查设计”这些高价值方法，而不是把某个专用 checker 的固定 stage 原样搬到所有场景上。

当前仓库需要的是一个更通用的审查层：
- 能审 narrative、commercial、interactive；
- 也能审 voice guide、visual pack、screen-to-video brief；
- 还能审 team workflow、subagent dispatch、project surface 这些治理型 artifact。

这意味着它不能默认采用同一套检查顺序，更不能假装所有 artifact 都要生成一个“标准化终稿”。

`quality_gate_report` 的任务，是给出一份适配当前场景的审查诊断：哪些 lens 应该启用、哪些是 hard fail、哪些只是弱项、最该先修什么、改完之后该怎么定向复查。

它的基本顺序是：
1. 先看 target contract 自己的 rubric 或 hard gate；
2. 再用共享 lens matrix 补充跨场景的质量镜头。

这样它就不会把所有检查都混成一个新大一统模式。

## TODOs：待回答问题

- [ ] 是否需要为不同 team mode 增加专门的 quality-gate bundle？
- [ ] 某些 high-pressure 场景下，quality gate 是否应自动要求 human checkpoint？
- [ ] 对纯概念级 artifact，weighted weakness 是否需要不同的表达粒度？
