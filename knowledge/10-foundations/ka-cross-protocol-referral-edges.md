---
{
  "id": "ka.cross-protocol-referral-edges",
  "type": "knowledge_atom",
  "title": "跨协议引荐边",
  "kind": "heuristic",
  "summary": "当一个工作流协议的停止条件暗示核心问题属于另一个协议的领域时，应输出引荐而非强行在本协议内扩展范围。",
  "mediums": [
    "feature_film",
    "episodic",
    "short_drama",
    "animation",
    "commercial",
    "branded_film",
    "shortform_video",
    "game_narrative",
    "branching_interactive"
  ],
  "stages": [
    "ideation",
    "premise",
    "character",
    "structure",
    "outline",
    "scene",
    "dialogue",
    "rewrite",
    "adaptation"
  ],
  "problem": "当前协议体系内每个工作流都定义了内部纪律，但协议之间存在隐式边界——LLM需要明确知道何时应将当前请求引荐给另一个协议，而不是在本协议内强行展开不应属于本协议的维度。",
  "decision_rules": [
    "当一个协议的处理结果暗示核心问题不在本协议领域内时，输出 context_loading_plan 指向目标协议，而非在本协议内扩展范围。",
    "quality-gate → audience-proxy：当审查发现核心问题是观看体验退化（hook流失、patience崩塌）而非合同符合度时，引荐到 wp.audience-proxy-review。",
    "rewrite-doctor → quality-gate：当诊断发现问题是合同/交付物适配失败而非工艺失败时，引荐到 wp.quality-gate-report。",
    "scene-writing → session-execution-plan：当场景请求实际上横跨多个阶段时，引荐到 wp.session-execution-plan 做阶段分解。"
  ],
  "anti_patterns": [
    "在 quality-gate 内强行展开观众体验维度——gate 查规则符合，proxy 查观看体验，两者互相稀释。",
    "诊断了三层问题却还在本协议内逐个改写，而不是把合同层问题引荐给 quality-gate 做系统性审查。",
    "为每个协议边界都列出一条引荐边——只列出那些确实存在混淆风险的边，其余保持隐式路由。"
  ],
  "prompt_primitives": [
    "当前协议处理到这一步，问题的本质是否已经超出本协议的领域范围？",
    "如果换一个协议处理这个问题的核心部分，哪个协议的停止条件更接近这个问题需要的答案？",
    "引荐时应该传递的最小上下文是什么？应该丢弃的是什么？"
  ],
  "evaluation_checks": [
    "是否正确识别了协议边界而非强行越界",
    "引荐是否指向了正确的目标协议",
    "上下文传递是否最小化——没有把本协议的全部输出倾倒给下游"
  ],
  "links": [
    "ka.bounded-context-loading",
    "ka.contract-first-quality-gating",
    "ka.audience-proxy-personas"
  ],
  "source_status": "synthesized"
}
---
# 跨协议引荐边

每个协议被设计为一类问题的处理空间。当执行过程中问题的本质从一类滑向另一类时，正确的动作不是拉伸当前协议去覆盖它，而是输出引荐。协议边界的价值恰恰在于这种「不覆盖」——每个协议只做自己那件事，做到停止条件就停，然后把不属于自己的问题交给下一个协议。清晰的引荐比脏的扩展更可靠。
