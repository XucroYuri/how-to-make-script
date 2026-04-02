---
name: how-to-make-script
description: Root orchestration skill for screenplay creation. Routes requests by intent, medium, stage, output, and constraints, then loads the minimum necessary protocols, rubrics, and knowledge atoms.
---

# How To Make Script

## Purpose
Use this skill when the user asks how to create, diagnose, improve, structure, or adapt a script across narrative, commercial, or interactive media.

This is the root orchestrator. It does not carry all theory inline. It resolves the request into the smallest useful route, then loads only the needed knowledge and sub-skills.

## Preflight Sync

Before routing any request, perform a lightweight sync check against the upstream repository to ensure knowledge assets are current.

**Remote**: `https://github.com/XucroYuri/how-to-make-script` (public)

**Steps**:
1. Query `https://api.github.com/repos/XucroYuri/how-to-make-script/commits/main` to get the latest remote commit SHA.
2. Compare with the local commit SHA (`git rev-parse HEAD` in the repository root). If they match, skip sync.
3. If the remote is ahead, download changed files from `https://raw.githubusercontent.com/XucroYuri/how-to-make-script/main/{relative_path}` and overwrite local copies. Priority sync targets:
   - `SKILL.md` (this file)
   - `references/router-matrix.json`
   - `references/expression-lens-triggers.md`
   - Any protocol, rubric, or knowledge-atom file referenced by the current route
4. After sync, re-read the routing matrix and re-validate the route before proceeding.
5. If the GitHub API or raw content URLs are unreachable, proceed with local assets and note the sync failure in the response.

**Constraints**:
- Do not attempt a full `git pull`; download only the files that have changed.
- Do not block the user's request if sync fails; degradation is acceptable.
- Do not sync on every single request within the same session; cache the last-checked SHA and re-check only if the session has been idle or the user requests a refresh.

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

## Route Selection Heuristics
- Prefer exact medium matches over generic narrative reuse.
- Prefer exact output-contract matches over broad stage matches.
- Prefer diagnostic routing when the user brings existing text and asks what is wrong with it.
- Prefer `quality_gate_report` when the user asks for structured checking, self-audit, preflight, acceptance gating, stage-specific review, targeted recheck, or non-story artifact quality control.
- Prefer one narrow protocol over a broad mixed-context answer.
- Prefer reality-grounded routes when the user asks for audience fit, commissioning fit, or writer growth strategy.
- Prefer `path_options` when the user asks for alternatives, counter-paths, or challenge-driven exploration.
- Prefer `boundary_map` when the user asks what is absolutely disallowed versus flexibly negotiable.
- Prefer `scope_correction` when the user challenges a rule, route, or rubric and the right response is to narrow its scope rather than replace it wholesale.
- Prefer `pattern_reference_pack` when the user asks for strong/weak screenplay examples, success-pattern comparisons, or "why this works better than that" guidance.
- Prefer `context_loading_plan` when the user asks how the skill should load context, balance reference breadth, or avoid context corruption.
- Prefer `story_memory_checkpoint` when the user asks to pause and resume long-form work, compress current story state, preserve continuity across sessions, or hand current state to another human or agent without reloading the whole draft.
- Prefer `voice_style_guide` when the user asks for language-style calibration, character/IP voice continuity, or stronger "alive" expression before drafting.
- Prefer `visual_language_pack` when the user asks for multilingual shot language, cross-language visual vocabulary, or culture-specific film-language calibration.
- Prefer `screen_to_video_brief` when the user asks to bridge screenplay material into a video-generation or previz-ready visual brief.
- Prefer `team_workflow_blueprint` when the user asks for multi-agent collaboration, writers' room design, team workflow design, specialist handoffs, or human-in-the-loop screenplay process design.
- Prefer `expert_subagent_cast` when the user asks which experts, roles, subagents, or reference-persona lenses should participate in a screenplay task.
- Prefer `subagent_dispatch_plan` when the user asks how those subagents should be scheduled, layered, reviewed, or merged.
- Prefer `project_surface_map` when the user asks how a long-running screenplay project should separate source-of-truth assets, runtime state, packet assembly, review surfaces, export surfaces, or phase entrypoints.
- Prefer `research_background_map` when the user asks broad questions such as “how to create a screenplay,” asks for theory support, asks for the repo’s background rationale, or needs a many-angle screenplay research baseline before choosing a narrower route. After that route is selected, use a `survey_pack` only if the breadth is still materially necessary.

## Boundary Rule
Treat constraints in two classes:
- hard boundaries: safety, legal, and non-negotiable constraints that stay active in every phase;
- soft constraints: taste, market, brand, or format preferences that may be relaxed in exploration and reintroduced during review.

When route certainty is low, map boundaries first and then generate path options.

## Reality-Lens Loading Rule
Load audience, industry, history, writer-development, and platform-attention lenses only when one of these is true:
- the requested output is `audience_fit_note`, `development_brief`, or `learning_path`;
- constraints include audience segment, audience need state, commissioning context, business model, release window, platform logic, writer maturity, or reference bar;
- the current draft fails because audience promise and delivery are misaligned.

Keep lens loading bounded: select only the linked atoms required by the chosen protocol.

## Expression-Lens Loading Rule
Load expression-lens assets only when one of these is true:
- the requested output is `voice_style_guide`;
- constraints include `voice_target`, `language_register`, `ip_continuity`, or `experiential_depth`;
- the draft fails because characters sound writerly, samey, fake-premium, NPC-like, or off-model for the target IP;
- adaptation or continuity work cannot proceed safely without a voice anchor first.

When the primary output is still `scene_draft`, `dialogue_polish`, `commercial_script`, or an adaptation artifact, keep the original route and load only the smallest adjunct bundle from [`references/expression-lens-triggers.md`](references/expression-lens-triggers.md).

## Visual-Bridge Loading Rule
Load visual-language or screen-to-video assets only when one of these is true:
- the requested output is `visual_language_pack` or `screen_to_video_brief`;
- constraints include `visual_vocab_locale`, `prompt_runtime`, `shot_granularity`, `reference_asset_mode`, or `continuity_invariants`;
- the user explicitly needs cross-language shot/staging communication, on-screen text strategy, or downstream previz / video-generation handoff;
- a normal screenplay draft cannot proceed safely because downstream visual execution requirements would materially change the next writing decision.

When the primary output is still a screenplay artifact, keep the original route and add only the smallest visual bundle that changes execution quality materially.

## Team-Lens Loading Rule
Load team-collaboration assets only when one of these is true:
- the requested output is `team_workflow_blueprint`;
- constraints include `team_mode`, `coordination_model`, `parallelism_budget`, `human_gate_level`, or `artifact_chain`;
- the task spans multiple deliverables, specialist lanes, or review gates and cannot be modeled well as one undifferentiated writer pass;
- the user explicitly asks for a writers' room, development pod, story trust, brand studio, branch lab, or multi-agent screenplay process.

When the primary output is still a normal screenplay artifact, keep the original route and load team assets only if the collaboration design would materially change role boundaries, review cadence, or handoff safety.

## Subagent-Library Loading Rule
Load subagent-library assets only when one of these is true:
- the requested output is `expert_subagent_cast` or `subagent_dispatch_plan`;
- constraints include `subagent_family`, `persona_policy`, `selection_strategy`, `dispatch_topology`, `convergence_owner`, or `context_budget`;
- the user explicitly asks for named expert roles, real-creator-inspired lenses, process-node design, or multi-level dispatch architecture;
- a normal team blueprint is insufficient because the next decision depends on concrete cast composition or review-order design.

When the primary output is still `team_workflow_blueprint`, keep the original route and load subagent-library assets only if the user needs a concrete cast or a live orchestration plan.

## Project-Surface Loading Rule
Load project-surface assets only when one of these is true:
- the requested output is `project_surface_map`;
- constraints include `project_horizon`, `phase_focus`, `truth_surface_policy`, `runtime_surface_policy`, `packet_strategy`, `traceability_level`, or `edit_policy`;
- the user explicitly asks where humans should edit, where runtime artifacts should live, how packets should be assembled, or how review/export surfaces should be separated;
- a normal screenplay or team-workflow answer would be unsafe because source-of-truth, mirrors, or handoff surfaces are still ambiguous.

When the primary output is still a normal screenplay artifact, keep the original route and load project-surface assets only if surface design would materially change handoff safety, review discipline, or runtime drift risk.

## Continuity-Checkpoint Loading Rule
Load story-memory-checkpoint assets only when one of these is true:
- the requested output is `story_memory_checkpoint`;
- constraints include `phase_focus`, `continuity_invariants`, `traceability_level`, or `context_budget` in a resume or handoff context;
- the user explicitly asks to compress current story state, preserve unresolved lines, or resume later without reloading a large packet;
- broad reloading would otherwise be used only as a continuity crutch rather than because the user truly needs a wider survey.

When the primary output is still a normal screenplay artifact, keep the original route and add a checkpoint only if resumable continuity materially changes the next decision.

## Quality-Gating Loading Rule
Load quality-gating assets only when one of these is true:
- the requested output is `quality_gate_report`;
- constraints include `target_contract`, `audit_scope`, `check_depth`, `lens_focus`, `recheck_mode`, or `acceptance_bar`;
- the user explicitly asks for self-check, stage-specific audit, preflight, acceptance review, lens-targeted review, or recheck after edits;
- the artifact under review is not well served by `rewrite_report` because the real issue is contract fit, delivery readiness, operational feasibility, or cross-artifact quality control.

When the primary output is still a normal screenplay artifact, keep the original route and add the smallest quality-gating bundle only if a preflight or targeted check would materially change the next decision.

## Research-Bundle Loading Rule
Load research-background assets only when one of these is true:
- the requested output is `research_background_map`;
- constraints include `research_scope`, `reference_depth`, or `route_certainty` for an explicitly broad question;
- the user explicitly asks for theory support, background rationale, or a many-angle screenplay-creation research baseline;
- a broad survey would otherwise expand without one declared background anchor.

When the primary output is still a normal screenplay artifact, do not auto-load research bundles just because they exist. Exit the bundle as soon as the user’s next need becomes a narrower route.

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
    - `constraints`: genre, tone, format, duration, audience segment, audience need state, platform, release window, commissioning context, business model, campaign goal, source medium, draft stage, participation mode, rating, budget, interactivity, franchise/IP limits, writer maturity, research scope, reference bar, creative problem, scenario family, loading mode, reference depth, comparison mode, route certainty, hard boundaries, soft constraints, voice target, language register, aesthetic register, IP continuity, experiential depth, visual vocab locale, prompt runtime, shot granularity, aspect ratio, reference asset mode, continuity invariants, audio mode, text mode, team mode, coordination model, parallelism budget, human gate level, artifact chain, subagent family, persona policy, selection strategy, dispatch topology, convergence owner, context budget, project horizon, phase focus, truth surface policy, runtime surface policy, packet strategy, traceability level, edit policy, target contract, audit scope, check depth, lens focus, recheck mode, acceptance bar
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
- For voice-style outputs, return anchors, register guardrails, drift warnings, and variability budget rather than a rigid tone template.
- For visual-language outputs, return a task-bounded term set, cultural or hybrid anchors, prompt-ready phrases, and misuse warnings rather than a full dictionary dump.
- For screen-to-video outputs, return source-scene intent, clip mode, main action, camera logic, invariants, avoid rules, and runtime-facing notes without pretending the bridge replaces the screenplay.
- For team-workflow outputs, return mode rationale, roles, handoff packets, review cadence, and human gates rather than vague org-chart prose.
- For expert-cast outputs, return core cast, optional cast, process nodes, persona lenses, authority map, context budgets, and trim order rather than a maximalist wishlist.
- For subagent-dispatch outputs, return control-plane order, topology, phase ladder, packet flow, review loops, human gates, and collapse triggers rather than generic orchestration slogans.
- For project-surface outputs, return canonical sources, runtime surfaces, packet layers, phase entrypoints, sync rules, edit permissions, review surfaces, export surfaces, and drift risks rather than abstract architecture prose.
- For story-memory outputs, return current state, unresolved promises, invariants, dual-track rhythm, and next safe entrypoint rather than a broad story recap.
- For quality-gate outputs, return target contract, scope mode, selected lenses, hard fails, weighted weaknesses, correction ladder, open contradictions, and recheck logic rather than one blended review paragraph.
- For broad screenplay-theory or research-background requests, return the lens decomposition first, then the strongest stable inferences, then the most relevant callable atoms rather than collapsing the answer into one method summary.

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
- flattening feature, TV room, animation, brand, and interactive workflows into one generic “writer team.”
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

## Sub-Skills & References

See [`references/skill-directory.md`](references/skill-directory.md) for the complete sub-skill and reference directory.

For runtime route lookup, see the generated execution index (`python scripts/generate_index.py --mode runtime`).

## Operating Principle
Sync first. Resolve the route second. Load the minimum context third. Generate fourth. Self-check last.
