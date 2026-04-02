# Roadmap

## Current Position

The repository is past the bootstrap stage. It already has:

- a root skill with clear routing and bounded-loading rules;
- a multi-asset knowledge model;
- broad coverage across narrative, commercial, and interactive screenplay work;
- review artifacts, research-background artifacts, continuity artifacts, and team-orchestration artifacts;
- CI checks for routes, registries, semantic consistency, forbidden local-tool leakage, and fixture coverage;
- bilingual entry surfaces for practitioners and agent builders.

## Highest-Priority Gaps

- The repo can describe multi-agent screenplay teams, but it still cannot instantiate a live runtime planner that turns blueprints into bounded execution.
- Bounded loading is well documented, but bundle selection and expansion control are still only partly machine-enforced.
- Registry validation is uneven: some registries have schema/checkers, others still rely on convention and review discipline.
- Route coverage is broad, but edge-case fixture depth is still thin compared to the number of similar outputs now in the system.
- Knowledge breadth is strong, but several genre, medium, case-study, and dialogue/character knowledge areas are still shallow.
- Community intake exists, but the path from discussion to triage to asset change still relies too much on manual effort.
- Bilingual entrypoints are much better, but parity is still incomplete at the deeper documentation layer.

## Next-Stage Phases

### Phase 5: Runtime Execution Layer

- [ ] Define a runtime-planner contract that turns `team_workflow_blueprint`, `expert_subagent_cast`, and `subagent_dispatch_plan` into executable lanes.
- [ ] Introduce a machine-checkable handoff-packet schema for writer lane handoff, review handoff, research handoff, and adaptation handoff.
- [ ] Add a resumable runtime ledger format so long-running screenplay jobs can pause, resume, and branch safely.
- [ ] Add bounded context-budget accounting to runtime planning so every expansion step has a stated reason and stop condition.
- [ ] Add a dry-run mode that simulates lane sequencing and handoff order before any live multi-agent execution.
- [ ] Add clear human-gate insertion points for approval, challenge, scope correction, and final sign-off.
- [ ] Add runtime failure policies for dead-end routes, handoff loss, contradiction discovery, and over-budget context expansion.
- [ ] Add end-to-end fixtures for at least one feature pod, one showrunner room, and one branded-content flow.

### Phase 6: Router And Retrieval Hardening

- [ ] Add a route-priority register for cases where multiple outputs can plausibly match the same request.
- [ ] Add adversarial fixtures for near-neighbor outputs such as `path_options`, `boundary_map`, `scope_correction`, `pattern_reference_pack`, and `quality_gate_report`.
- [ ] Add machine-checkable bundle-planner rules so `route_kernel`, `focus_pack`, `compare_pack`, `teaching_pack`, and `survey_pack` are not only documented but enforced.
- [ ] Add schema/checkers for more registries, starting with scenario taxonomy, check-lens matrix, expression-lens triggers, and context-loading-mode surfaces.
- [ ] Add contradiction lint for linked atoms, protocols, rubrics, and reference packs that use overlapping terms differently.
- [ ] Add a controlled vocabulary / alias registry for terms that drift across craft, production, review, and agent-design contexts.
- [ ] Add coverage reports that show fixture density by medium, stage, output, and route family.
- [ ] Add tests that fail when a new route silently widens loading requirements without updating docs or fixtures.

### Phase 7: Knowledge Depth And Reference Power

- [ ] Expand genre packs beyond the current backbone into thriller, mystery, horror, comedy, romance, action, family, and speculative-fiction problem families.
- [ ] Add medium-specific constraint packs for feature, episodic, short drama, animation, branded film, shortform video, and game narrative delivery contexts.
- [ ] Deepen dialogue-stage knowledge atoms around subtext pressure, information asymmetry, verbal rhythm, exposition avoidance, and character-specific speech behavior.
- [ ] Deepen character-stage knowledge atoms around sympathy design, contradiction design, relationship pressure, and transformation tracking.
- [ ] Split broad research scopes into narrower callable slices for audience cognition, scene escalation, character inference, dialogue perception, and rewrite psychology.
- [ ] Add success/failure case studies that explain not only “what worked” but also “what looked promising and still failed.”
- [ ] Add reference packs for stage-specific problems such as weak openings, flat reveals, limp midpoint turns, collapsed endings, and generic dialogue.
- [ ] Add more screenplay-to-video bridge examples that preserve screenplay logic without turning the repo into a vendor prompt library.

### Phase 8: Quality, Evaluation, And Regression Depth

- [ ] Add output-specific quality-gate presets for premise, outline, scene, dialogue, commercial, branch map, research map, and checkpoint artifacts.
- [ ] Add more golden flows so every high-value output family has at least one end-to-end example chain.
- [ ] Add targeted recheck fixtures for “after revision” scenarios rather than only first-pass diagnosis.
- [ ] Add cross-artifact consistency checks, especially premise ↔ outline, outline ↔ scene, scene ↔ dialogue, and script ↔ bridge artifacts.
- [ ] Add regression fixtures for semantic drift in terms like `premise`, `beat`, `scene function`, `voice`, `continuity`, and `canon`.
- [ ] Add review-depth presets that distinguish teaching feedback, development-room feedback, preflight checks, and launch-ready acceptance gates.
- [ ] Add compact evaluation summaries that can be safely handed off between agents without reloading the full artifact history.
- [ ] Add stronger tests for background-bundle scope discipline and checkpoint-vs-reload decision quality.

### Phase 9: Human-In-The-Loop Community Operations

- [ ] Operationalize the existing discussion-to-asset workflow with clearer ownership, timing, and handoff expectations.
- [ ] Turn the existing triage categories into a clearer maintainer decision tree for claim narrowing, route fixes, fixture additions, and governance changes.
- [ ] Add contributor-facing templates for field notes, failed routes, successful overrides, and practitioner disagreement reports where current intake is still too free-form.
- [ ] Add periodic backlog review rituals that convert high-signal discussions into roadmap items or closed-scope decisions.
- [ ] Add intake metrics: how many discussions became fixtures, how many route bugs became tests, and how many objections narrowed claims.
- [ ] Add moderation playbooks that make existing community guidance easier to apply consistently at higher scale.
- [ ] Add onboarding material for contributors who want to move from “issue reporter” to “triage steward” to “knowledge curator.”
- [ ] Add automation support for recurring triage and follow-up reporting only where it reduces manual drift instead of creating meta-work.

### Phase 10: Bilingual And Packaging Maturity

- [ ] Complete parity for deep docs where English is still ahead of Chinese or vice versa.
- [ ] Add glossary pages for key screenplay, production, and agent-design terms that easily drift across languages.
- [ ] Add doc-level parity checks so core linked docs are not updated in one language and forgotten in the other.
- [ ] Add clearer install and invocation examples for Codex, Claude Code, OpenCode, Gemini CLI, OpenClaw, and future compatible runtimes.
- [ ] Add a compact “choose your route” onboarding surface for new human users who do not yet understand the output vocabulary.
- [ ] Add an agent-facing quick-reference card for loading modes, route selection, and escalation rules.
- [ ] Add publish-ready repo surfaces such as generated indexes or overview pages only when they reduce onboarding cost without duplicating source truth.
- [ ] Keep the README short enough for discovery while pushing deeper operational detail into linked docs.

## Maintainer Rule

The next stage should increase routing precision, runtime executability, and regression resistance.

It should not:

- turn the repo into a single giant runtime framework;
- turn every new insight into a new taxonomy axis;
- turn every useful example into a hidden template mandate;
- turn bilingual coverage into duplicate context stuffing.
