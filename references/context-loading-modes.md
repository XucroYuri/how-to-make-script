# Context Loading Modes

This file defines the bounded loading menu used after routing. It is not a routing table. It assumes a route has already been selected and only answers how much surrounding context should be loaded.

## Mode Map

| Mode | Tier | Use When | Required Load | Optional Load | Stop Condition | Common Failure Signal |
| --- | --- | --- | --- | --- | --- | --- |
| `route_kernel` | 0 | Any request that needs a correct route | Root skill, routing policy, selected output contract, selected route entry | None | Route and output are fixed | Model starts explaining the repo instead of the request |
| `focus_pack` | 1 | Single artifact generation or narrow rewrite | Primary protocol, primary rubric, linked atoms, one scenario card or case note | One reality lens if the request depends on audience / industry / history / training, or one expression lens if the request depends on voice / register / continuity | Additional context would only restate the same decision | Generic output because the load was too thin |
| `compare_pack` | 2 | Alternatives, counter-paths, boundary questions, why-not analysis | Focus pack plus one rival route or one boundary reference | `path_options`, `boundary_map`, `scope_correction`, one contrastive reference pack | The added material changes the tradeoff analysis or confirms the chosen route | Too many near-duplicates that blur the choice |
| `teaching_pack` | 3 | Explanation, learning, comparison, reference guidance | Scenario atlas, one primary reference pack, one contrastive example, one relevant case note | Reality lenses, backlog question, adjacent scenario family | The explanation can name the pattern, the failure mode, and the boundary | The model quotes the repo instead of teaching from it |
| `survey_pack` | 4 | Explicit broad survey or research-style request | One declared background bundle, scenario atlas when relevant, multiple representative packs, relevant case studies | Additional family cards and cross-links | The survey has enough breadth to map the space, but not enough to become a literature dump | Context saturation, repetition, and route drift |

## Loading Rules

1. Start at `route_kernel`.
2. Expand only if the request or the draft proves that more context changes the answer.
3. Expand one mode at a time.
4. Prefer one contrasting source over many similar sources.
5. Never load a broad mode just because the repo contains it.

## Trigger Cheatsheet

- `compare`, `alternative`, `counter-path`, `why not`, `boundary`, `scope` -> `compare_pack`
- `teach`, `explain`, `why this works`, `show me examples` -> `teaching_pack`
- `survey`, `all known`, `full taxonomy`, `deep mapping` -> `survey_pack`
- `how to create a screenplay`, `theory support`, `research baseline`, `background map` -> `research_background_map` or `survey_pack` anchored on one declared background bundle
- `rewrite`, `diagnose`, `fix this draft` -> usually `focus_pack`, sometimes `compare_pack`
- `resume later`, `story handoff`, `continuity checkpoint`, `compress current state`, `don't reload the whole draft` -> `story_memory_checkpoint` or `focus_pack` plus the smallest checkpoint bundle
- `audience fit`, `development brief`, `learning path` -> `focus_pack` plus the relevant reality lens
- `voice style`, `character voice`, `IP continuity`, `make it feel alive` -> `voice_style_guide` or `focus_pack` plus the relevant expression lens
- `multilingual shot language`, `Japanese / Korean / Russian / Spanish / Chinese film vocabulary`, `cross-language visual handoff` -> `visual_language_pack` or `focus_pack` plus the smallest visual-language bundle
- `turn this scene into a video brief`, `previz bridge`, `Sora / Seedance handoff`, `clip-ready adaptation` -> `screen_to_video_brief` or `focus_pack` plus the smallest bridge bundle
- `multi-agent workflow`, `writers' room design`, `team topology`, `handoff design` -> `team_workflow_blueprint` or `focus_pack` plus the relevant team lens
- `which experts should join`, `subagent cast`, `writer/director-inspired personas`, `specialist roster` -> `expert_subagent_cast` or `focus_pack` plus the smallest subagent-library bundle
- `dispatch plan`, `multi-level scheduler`, `review order`, `subagent handoff topology`, `subagent-driven-development loop` -> `subagent_dispatch_plan` or `focus_pack` plus the smallest topology bundle
- `source of truth vs runtime`, `project surface`, `packet assembly`, `review surface`, `export surface`, `planning-to-drafting handoff` -> `project_surface_map` or `focus_pack` plus the smallest project-surface bundle
- `self-check`, `quality gate`, `preflight`, `acceptance review`, `recheck`, `stage-specific audit`, `lens-targeted review` -> `quality_gate_report` or `focus_pack` plus the smallest quality-gating bundle

## Recovery

- If the bundle feels bloated, drop back to `route_kernel`.
- If continuity pressure is the only reason the bundle keeps growing, create or refresh a `story_memory_checkpoint` instead of widening again.
- If the bundle is too narrow, add one contrastive or boundary reference, not a whole new library.
- If route choice is still unclear after one expansion step, ask a clarifying question instead of widening again.
