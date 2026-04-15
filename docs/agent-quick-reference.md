# Agent Quick Reference

Use this card when you need fast, low-risk routing and loading decisions.

## 1) Route first, always

Choose route dimensions in this order:

1. `intent` (`discover`, `design`, `draft`, `polish`, `diagnose`, `adapt`)
2. `medium`
3. `stage`
4. `output`
5. `constraints`

## 2) Route selection rule

- Start from the `intent x medium x stage x output` matrix.
- Use `constraints` as a tie-breaker or loading trigger when outputs are near neighbors.
- If the request is ambiguous, map boundaries first (hard/soft) and return minimal clarifying questions that can change route/output.
- If multiple outputs remain viable, preserve plurality with `path_options` rather than forcing a single answer.

## 3) Loading mode ladder

- `route_kernel`: minimal route-safe context.
- `focus_pack`: route + primary workflow + required atoms + one rubric.
- `compare_pack`: add one rival or contrast boundary when needed.
- `teaching_pack`: route + one reference pack/atlas + one contrast aid.
- `survey_pack`: only explicit broad research/learning requests.

## 4) Stop expansion when

- route is stable and output contract is fixed;
- the next context chunk does not change route, output contract, or self-check quality;
- the response is drifting toward repo summary instead of request resolution;
- primary bundle already includes one route anchor, one primary reference, and one contrast when needed.

## 5) Lens loading shortcuts

- Reality lens: only when requested for audience, platform, industry, commissioning, business model, or writer-growth mismatch.
- Expression lens: only when output is `voice_style_guide` or constraints request explicit tonal/continuity control.
- Visual bridge: only when output is `visual_language_pack` / `screen_to_video_brief` or explicit visual handoff needs.
- Team/runtime lens: only when request is collaboration design or runtime orchestration.

## 6) Mandatory output discipline

- Keep outputs in the requested contract format.
- Attach a compact rubric-based self-check.
- If constraints change route or output contract, reload from the constrained bundle only when necessary.
