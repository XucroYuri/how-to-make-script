---
{
  "id": "ka.review-lens-isolation",
  "type": "knowledge_atom",
  "title": "审查镜头隔离",
  "kind": "principle",
  "summary": "多镜头质检时，每个 lens 都应在 bounded brief 下独立判断，避免前一个 lens 的原始 findings 污染后一个 lens。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "一旦前一个审查层的大段结论被直接喂给后一个审查层，后面的 lens 很容易开始重复前面的判断，或者被某个早期偏见拖着跑，失去独立诊断价值。",
  "decision_rules": [
    "每个 lens 只接收 artifact、本 lens 定义、target contract 和压缩后的上游 metrics。",
    "不要把上一个 lens 的原始 findings 全文传给下一个 lens。",
    "如果不同 lens 结论冲突，应在聚合层处理，而不是提前在 lens 层互相说服。"
  ],
  "anti_patterns": [
    "多个 lens 共享同一大段 findings 上下文",
    "第二个 lens 只是复述第一个 lens 的判断",
    "还没聚合就把一个 lens 的结论伪装成总结论"
  ],
  "prompt_primitives": [
    "这个 lens 仅凭当前 artifact 和压缩 state，应该独立回答什么",
    "哪些信息必须保留为 metrics，哪些不能直接传 findings",
    "如果 lens 之间冲突，应该在哪里裁决"
  ],
  "evaluation_checks": [
    "lens brief 是否足够小且独立",
    "metrics 是否替代了原始 findings 的大段传递",
    "聚合层是否保留了 lens 间分歧"
  ],
  "links": ["ka.handoff-packet-discipline", "ka.bounded-context-loading", "ka.context-corrosion-signals"],
  "source_status": "synthesized"
}
---
# 审查镜头隔离

专用 checker 工作流里最值得借的，不是固定几层，而是“每层只看自己该看的东西”。这条原则对通用剧本仓库更重要，因为当前 repo 要处理的 artifact 比单一 AI 可执行剧本复杂得多。

如果 `contract_fit`、`voice`、`execution_feasibility`、`delivery_handoff` 全都共享同一大段 findings，上下文只会越来越脏。最后得到的不是多镜头质检，而是一个长上下文自我强化回路。

所以这个仓库的通用质检层要借的是“镜头隔离”，不是“固定 stage 数”。

## TODOs：待回答问题

- [ ] 对哪些 high-risk lens，是否应完全禁止接收任何上游 metrics，只看原 artifact？
- [ ] lens 间冲突是否需要单独的 conflict summary schema？
- [ ] 某些 targeted audit 是否可以退化成单 lens，不必走聚合层？
