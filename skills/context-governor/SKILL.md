---
name: context-governor
description: Use when the task needs a bounded context-loading plan before generation or when the current loading strategy risks context corrosion.
---

# Context Governor

Use this skill when the user asks about agent-skill design, loading strategy, context balance, reference breadth, or when the route is at risk of being drowned by too much adjacent material.

## Workflow
1. Lock the primary route first.
2. Choose one loading mode from `route_kernel`, `focus_pack`, `compare_pack`, `teaching_pack`, or `survey_pack`.
3. If the request is broad and theory-facing, pick one declared research bundle before expanding.
4. If continuity pressure is the real bottleneck, test whether a `story_memory_checkpoint` should replace broader reload.
5. Define the mandatory bundle.
6. Define the optional expansion queue and triggers.
7. Define stop conditions and corrosion signals.
8. If voice is the real bottleneck, prefer one bounded expression lens over a broad style survey.

## Output Contract
- `context_loading_plan`: primary route, loading mode, mandatory bundle, optional expansion queue, stop rules, and context-corrosion warnings.
- Do not confuse "more related material" with "better generation conditions."
- Expand only when the next asset can plausibly change route quality, answer quality, or creative extension quality.
- For broad theory/background requests, mandatory bundle should include one declared background bundle rather than a grab bag of neighboring docs.
- If the real problem is resumable continuity, prefer a checkpoint artifact over a wider bundle.
- Treat expression guidance as an adjunct bundle, not as a reason to pre-load every nearby style example.

## References
- `wp.context-loading-plan`
- `references/background-bundles.json`
- `ka.bounded-context-loading`
- `ka.reference-expansion-balance`
- `ka.context-corrosion-signals`
- `ka.story-memory-checkpoint`
- `rb.context-loading-plan`
