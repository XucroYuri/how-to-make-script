# Routing Policy

## Goal

Route script requests with enough structure that the selected skill, protocol, and rubric can be explained and tested.

## Required Dimensions
- `intent`
- `medium`
- `stage`
- `output`
- `constraints`

The route key is operationally anchored by `intent x medium x stage x output`.
`constraints` then refine the decision in three ways:
- they explain why a route is appropriate in this request;
- they break ties or near-ties between adjacent routes when route signals are declared;
- they govern which adjunct bundles may load after the primary route is chosen.

## Rules
- Never collapse all requests into one giant prompt.
- Prefer a single primary protocol per request.
- Select one primary rubric for the final artifact.
- Load only the atoms linked by the selected protocol unless the request explicitly asks for broader teaching or comparison.
- When multiple routes are plausible, prefer the narrower route over the generic route.
- Keep route claims honest: if constraints are only affecting loading, do not describe them as if they fully determined the route.
- After route selection, choose a bounded loading mode before expanding into adjacent references.
- Prefer `context_loading_plan` only for explicit loading-strategy, skill-design, or context-balance requests; do not use it as a generic detour before every answer.
- Prefer `pattern_reference_pack` for teaching/comparison and not as the default drafting route.
- Prefer `boundary_map` or `scope_correction` over broad craft expansion when the real question is constraint logic or claim narrowing.
- Prefer `quality_gate_report` for explicit self-check, structured audit, preflight, acceptance review, stage-specific checking, targeted recheck, or non-story artifact review instead of stretching `rewrite_report` to cover every quality problem.
- Prefer `voice_style_guide` for explicit voice, style, IP continuity, or "make it feel alive" requests instead of smearing style advice across the main draft by default.
- Prefer `visual_language_pack` for explicit multilingual shot language, culture-specific visual vocabulary, or cross-language visual handoff requests.
- Prefer `screen_to_video_brief` for explicit screenplay-to-video-generation or previz bridge requests instead of overloading scene or commercial drafting routes.
- For scene, dialogue, commercial, or adaptation drafting, keep the primary route and add the smallest expression-lens bundle only when the request or draft clearly needs it.
- For normal screenplay outputs, load multilingual visual-language assets only when downstream visual communication or cross-language execution would materially change the next decision.
- Prefer `team_workflow_blueprint` for explicit multi-agent, writers' room, or collaboration-design requests instead of burying team logic inside a normal draft answer.
- Prefer `expert_subagent_cast` for explicit “which experts / subagents / persona lenses should participate” requests instead of overloading team-workflow answers with giant role lists.
- Prefer `subagent_dispatch_plan` for explicit “how should these subagents be staged, reviewed, merged, and human-gated” requests instead of burying dispatch design inside a team mode answer.
- Prefer `project_surface_map` for explicit “what is editable truth, what is runtime state, where do packets come from, and where do review/export surfaces live” requests instead of overloading team or dispatch answers with storage architecture.
- For normal screenplay outputs, load team assets only when collaboration structure changes the next decision materially.
- For normal screenplay outputs, load expert-subagent and topology assets only when concrete cast selection or dispatch design changes the next decision materially.
- For normal screenplay outputs, load project-surface assets only when surface design changes the next decision materially by reducing wrong-edit risk, runtime drift, or handoff ambiguity.
- For normal screenplay outputs, load quality-gating assets only when a preflight or targeted audit would materially change the next decision.

## Loading Policy

Once a route is selected, use [`references/context-loading-modes.md`](./context-loading-modes.md) to decide how much additional context is justified.

Default rule:
- start at `route_kernel`;
- expand to `focus_pack` for normal execution;
- expand further only when the next layer can still change route quality, answer quality, or contrast quality;
- stop as soon as added material no longer changes the next decision materially.

## Fallbacks
- If `medium` is unknown, use a generic narrative route only when the request is clearly not commercial or interactive.
- If `output` is absent, infer the smallest useful output from stage:
  - `ideation -> premise`
  - `structure -> beat_sheet`
  - `scene -> scene_draft`
  - `dialogue -> dialogue_polish`
  - `rewrite -> rewrite_report`
