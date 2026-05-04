---
name: how-to-make-script
description: Root orchestration skill for screenplay creation. Routes requests by intent, medium, stage, output, and constraints, then loads the minimum necessary protocols, rubrics, and knowledge atoms.
---

# How To Make Script

## Purpose
Use this skill when the user asks how to create, diagnose, improve, structure, or adapt a script across narrative, commercial, or interactive media.

This is the root orchestrator. It does not carry all theory inline. It resolves the request into the smallest useful route, then loads only the needed knowledge and sub-skills.

## Posture Sync

Before routing any request, perform a lightweight creative posture detection pass using the three-axis model defined in `knowledge/10-foundations/ka-creative-posture-source.md`, `ka-creative-posture-certainty.md`, and `ka-creative-posture-focus.md`.

**Three axes to detect:**
1. **Source mode** — discover / construct / generate (weighted, can mix)
2. **Certainty mode** — certain / exploring / lost (mutually exclusive)
3. **Attention focus** — character / world / event / audience / language (primary + optional secondary)

**Detection signals:**
- Discover signals: 如果 / 试试 / 也许 / 感觉 / 好像 / 说不定 / 直觉上
- Construct signals: 需要 / 应该 / 确保 / 规划 / 框架 / 设计 / 按照
- Generate signals: 碰撞 / 让他们 / 看看会发生 / 放进去 / 不管结果
- Lost signals: 卡住了 / 不知道从哪 / 脑子空 / 没有思路 / 写不下去 / 没感觉
- Exploring signals: 也可以 / 或者 / 两个方向 / 哪个更好 / 不确定哪个

**Posture influence on loading:**
- `lost` certainty mode: suppress rubric hard-fail output; lead with one minimal executable action or nucleation question
- `discover` source mode: load possibility-expanding atoms first; delay hard structural constraints
- `construct` source mode: apply full protocol steps and rubric evaluation
- Attention focus determines which atom category loads as primary

**Constraint signal:** Store detected posture as `posture_mode` constraint for downstream route signals.

## Non-Negotiables
- Route by `intent x medium x stage x output`, then use `constraints` as route signals, tie-breakers, and loading triggers.
- Do not rely on loose keyword matching alone.
- Do not duplicate theory from `knowledge/` into sub-skills.
- Prefer the smallest protocol that can satisfy the request.
- Ask only for missing information that changes the route or output contract.
- Always attach a brief rubric-based self-check to the final result.
- Load reality-lens atoms only when they change routing or output quality.
- Do not collapse to one path when multiple viable options remain during `discover` and `design`.
- Separate hard boundaries from soft constraints before recommending convergence.
- Prefer scope correction over false certainty flips when a rule is challenged but not fully broken.

## Posture-Adaptive Response Rules
- When `posture_certainty = lost`: respond with one minimal executable action or one nucleation question only; do not apply rubric hard-fails; do not output rule checklists; use inviting rather than prescriptive language.
- When `posture_certainty = exploring`: provide comparison with judgment criteria; do not force convergence to a single path; do not withhold valid alternatives.
- When `posture_certainty = certain`: execute the most precise protocol step directly; do not add unnecessary alternative options.
- When `posture_source = discover`: load possibility-expanding atoms first; prefer `path_options` and `idea-discovery` routes; avoid pushing hard structural constraints.
- When `posture_source = construct`: load structural-constraint atoms first; apply full protocol and rubric.
- When `posture_source = generate`: provide collision experiment conditions; do not predict or pre-plan outcomes; leave space for unexpected results.
- When `posture_focus = character`: load character psychology atoms as primary; deprioritize structure-beat and world-building atoms.
- When `posture_focus = audience`: load audience-experience atoms as primary; deprioritize internal world-consistency atoms.
- When `posture_focus = language`: load dialogue and voice-calibration atoms as primary; deprioritize high-level structure atoms.

## Route Selection Heuristics
- Prefer exact medium matches over generic narrative reuse.
- Prefer diagnostic routing when the user brings existing text and asks what is wrong with it.
- Prefer `quality_gate_report` when the user asks for structured checking, self-audit, preflight, acceptance gating, stage-specific review, targeted recheck, or non-story artifact quality control.
- Prefer `path_options` when the user asks for alternatives, counter-paths, or challenge-driven exploration.
- Prefer `boundary_map` when the user asks what is absolutely disallowed versus flexibly negotiable.
- Prefer `scope_correction` when the user challenges a rule, route, or rubric and the right response is to narrow its scope rather than replace it wholesale.
- Prefer `audience_proxy_report` when the user asks for scene- or draft-level viewing experience simulation, multi-persona reading, attention curve diagnosis, or anti-sycophancy honest feedback on a specific scene or script passage.
- Prefer `session_execution_plan` when the user's request spans two or more stages (e.g., "from logline to scene draft tonight"), needs multi-stage decomposition, explicit handoff contracts between stages, or the user asks for a session-level work plan rather than a single output.
- Prefer subtractive editing (wp.subtractive-pass) when the user asks to cut, trim, remove redundancy, or "make it shorter/tighter" from an existing scene or screenplay draft.
- Prefer `research_background_map` for broad theory or background requests; use a `survey_pack` only if breadth remains materially necessary after that route is selected.
- Prefer one narrow protocol over a broad mixed-context answer.

## Boundary Rule
Treat constraints in two classes:
- hard boundaries: safety, legal, and non-negotiable constraints that stay active in every phase;
- soft constraints: taste, market, brand, or format preferences that may be relaxed in exploration and reintroduced during review.

When route certainty is low, map boundaries first and then generate path options.

## Domain-Specific Loading Rule
Load domain-specific assets (reality-lens, expression-lens, visual-bridge, team-collaboration, subagent-library, project-surface, story-memory, audience-proxy, quality-gating, research-bundle) only when:
- (a) the requested output belongs to that domain, OR
- (b) constraints signal that domain, OR
- (c) a current draft failure can only be diagnosed using that domain's lens.

When the primary output is a screenplay artifact, keep the original route and add only what materially changes the next decision. Do not load domain assets speculatively.

## Context Loading Ladder
After route selection, choose one loading mode from [`references/context-loading-modes.md`](references/context-loading-modes.md):
- `route_kernel`: route anchor only.
- `focus_pack`: primary protocol, primary rubric, linked atoms, and one scenario or case anchor when needed.
- `compare_pack`: focus pack plus one rival route or one boundary/contrast layer.
- `teaching_pack`: scenario atlas plus one primary reference pack and one contrastive aid.
- `survey_pack`: only for explicit broad mapping requests; anchor on [`docs/how-to-create-a-screenplay-research.md`](docs/how-to-create-a-screenplay-research.md) and [`docs/source-map-screenplay-creation-research.md`](docs/source-map-screenplay-creation-research.md) before adding narrower craft or medium packs.

Default rule: start narrow, expand one layer at a time, and stop when the next asset would no longer change the answer materially.

## Context Stop Rules
Stop expansion when one of these is true:
- the route is stable and the output contract is fixed;
- the next asset only repeats what is already loaded;
- the answer is drifting toward repo summary instead of task resolution;
- the bundle already contains one route anchor, one execution pack, and one contrastive layer when contrast is needed.

## Routing Steps
1. Classify the request:
   - `intent`: discover, design, draft, polish, diagnose, adapt
   - `medium`: feature_film, episodic, short_drama, animation, commercial, branded_film, shortform_video, game_narrative, branching_interactive
   - `stage`: ideation, premise, character, structure, outline, scene, dialogue, rewrite, adaptation
   - `output`: one of the public contracts in [`references/supported-outputs.md`](references/supported-outputs.md)
    - `constraints`: genre, tone, format, duration, audience segment, audience need state, platform, release window, commissioning context, business model, campaign goal, source medium, draft stage, participation mode, rating, budget, interactivity, franchise/IP limits, writer maturity, research scope, reference bar, creative problem, scenario family, loading mode, reference depth, comparison mode, route certainty, hard boundaries, soft constraints, voice target, language register, aesthetic register, IP continuity, experiential depth, visual vocab locale, prompt runtime, shot granularity, aspect ratio, reference asset mode, continuity invariants, audio mode, text mode, team mode, coordination model, parallelism budget, human gate level, artifact chain, subagent family, persona policy, selection strategy, dispatch topology, convergence owner, context budget, project horizon, phase focus, truth surface policy, runtime surface policy, packet strategy, traceability level, edit policy, target contract, audit scope, check depth, lens focus, recheck mode, acceptance bar, posture mode (source: discover/construct/generate; certainty: certain/exploring/lost; focus: character/world/event/audience/language)
2. Look up the preferred route in [`references/router-matrix.json`](references/router-matrix.json).
   - Use declared `constraint_signals` to explain why the route is appropriate and to break ties between otherwise-equal adjacent routes.
3. Choose the loading mode.
4. Load:
   - one primary workflow protocol;
   - one primary skill wrapper;
   - the linked atoms required by the protocol;
   - the rubric that governs the requested output;
   - only the smallest adjacent references justified by the loading mode.
5. If the request is underspecified, ask only for the minimum missing information that changes the route or output contract.
6. Produce the requested artifact and a compact self-check using the selected rubric.

## Output Pattern
- Return the requested artifact in the requested format.
- Add a brief rubric-based self-check or revision note when useful.
- If the user asks for teaching or explanation, anchor the answer in the relevant protocol and atom references.
- For reference-pattern outputs, use original synthetic fragments and say explicitly that they are reference paths, not the only valid creative route.
- For loading-plan outputs, explain why each expansion step is justified and what should not be loaded yet.
- For specialized domain outputs, return the artifact-specific required fields only; see the relevant protocol for the field list.
- For session-execution outputs, return ordered segment list with per-segment protocol/stop-condition/handoff-contract, not a project roadmap.

## What This Skill Should Prevent
- loading unrelated theory just because it exists in the repo;
- answering a commercial brief as if it were a feature outline;
- flattening interactive branching into ordinary linear plotting;
- giving rewrite advice without identifying the failure layer first;
- giving craft advice detached from audience demand and production context.
- treating one method as a universal truth across mediums, audiences, and eras.
- enforcing soft preferences as if they were hard boundaries during ideation.
- replacing one overbroad rule with its mirror-image overbroad rule after a challenge.
- presenting memorized or quote-like script passages as if they were the repository's own reference patterns.
- expanding context because assets exist, rather than because they change the next decision.
- reloading full drafts, season packets, or room notes when a bounded continuity checkpoint would preserve the needed state.
- flattening all checking into one generic rewrite note, even when the artifact under review is operational, governance-oriented, or contract-heavy.
- running the same fixed audit stack for every medium, artifact family, and delivery surface.
- defaulting every character, IP, or brand to the same neutral authorial language.
- confusing voice guidance with a fixed template that erases scene-specific variation.
- turning multilingual visual language into decorative jargon instead of executable communication.
- flattening screenplay scenes into vendor-specific prompt soup before preserving dramatic function.
- flattening feature, TV room, animation, brand, and interactive workflows into one generic "writer team."
- treating multi-agent collaboration as full-context sharing instead of bounded handoffs.
- treating real-creator-inspired personas as permission for direct impersonation or exact mimicry.
- stuffing every expert, reviewer, and persona into one cast instead of composing a minimal viable subagent team.
- using one vague multi-agent answer where the task really needs separate mode selection, cast selection, and dispatch design.

## Default Output Contracts
- `logline`
- `premise`
- `synopsis`
- `treatment`
- `beat_sheet`
- `outline`
- `scene_card`
- `scene_draft`
- `screenplay_draft`
- `dialogue_polish`
- `rewrite_report`
- `commercial_script`
- `interactive_branch_map`
- `audience_fit_note`
- `development_brief`
- `learning_path`
- `research_background_map`
- `path_options`
- `boundary_map`
- `scope_correction`
- `pattern_reference_pack`
- `context_loading_plan`
- `story_memory_checkpoint`
- `voice_style_guide`
- `visual_language_pack`
- `screen_to_video_brief`
- `team_workflow_blueprint`
- `expert_subagent_cast`
- `subagent_dispatch_plan`
- `project_surface_map`
- `quality_gate_report`
- `audience_proxy_report`
- `session_execution_plan`

## Sub-Skills & References

See [`references/skill-directory.md`](references/skill-directory.md) for the complete sub-skill and reference directory.

For runtime route lookup, see the generated execution index (`python scripts/generate_index.py --mode runtime`).

## Operating Principle
Posture-sync first. Resolve the route second. Load the minimum context third (posture-weighted). Generate fourth. Self-check last.
