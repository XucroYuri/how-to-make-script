---
name: context-governor
description: Use when the task needs a bounded context-loading plan before generation or when the current loading strategy risks context corrosion.
---

# Context Governor

Use this skill when the user asks about agent-skill design, loading strategy, context balance, reference breadth, or when the route is at risk of being drowned by too much adjacent material.

## Workflow
1. Lock the primary route first.
2. Choose one loading mode from `route_kernel`, `focus_pack`, `compare_pack`, `teaching_pack`, or `survey_pack`.
3. Define the mandatory bundle.
4. Define the optional expansion queue and triggers.
5. Define stop conditions and corrosion signals.
6. If voice or continuity is the real bottleneck, prefer one bounded expression lens over a broad style survey.

## Output Contract
- `context_loading_plan`: primary route, loading mode, mandatory bundle, optional expansion queue, stop rules, and context-corrosion warnings.
- Do not confuse "more related material" with "better generation conditions."
- Expand only when the next asset can plausibly change route quality, answer quality, or creative extension quality.
- Treat expression guidance as an adjunct bundle, not as a reason to pre-load every nearby style example.

## References
- `wp.context-loading-plan`
- `ka.bounded-context-loading`
- `ka.reference-expansion-balance`
- `ka.context-corrosion-signals`
- `rb.context-loading-plan`
