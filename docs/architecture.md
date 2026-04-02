# Architecture

## Core Idea

This repository separates reusable screenplay intelligence into four layers:

1. `knowledge/` stores durable theory and craft fragments.
2. `schemas/` define the machine-checked contracts for structured assets.
3. `skills/` provide thin orchestration entrypoints for agents.
4. `scripts/` and `tests/` keep the repository verifiable.

The repo is intentionally opinionated:
- the knowledge layer is the source of truth;
- skills are routing and composition wrappers;
- fixtures and tests enforce that routes stay stable;
- additive growth is preferred over reorganizing published IDs.

The orchestration layer now carries a bounded reality-grounding rule:
- audience lens;
- industry and commissioning lens;
- platform and release lens;
- writer development lens;
- historical evolution lens.

These lenses are loaded only when they change route choice or output quality.

The orchestration layer includes bounded loading rules for five extension domains:

**Team collaboration.** Ordinary screenplay requests should still stay single-route by default; multi-agent or hybrid-team logic should load only when team structure changes the next decision materially; specialist roles should exchange bounded handoff packets instead of full shared context.

**Subagent library.** `team_workflow_blueprint` chooses the collaboration shape; `expert_subagent_cast` chooses the bounded specialist roster; `subagent_dispatch_plan` chooses the live scheduling and review structure; reference personas remain bounded lenses instead of replacing route logic or convergence ownership.

**Project surface.** `project_surface_map` chooses where canonical truth lives; runtime mirrors, caches, and traces stay derived by default; packet assembly stays inspectable instead of invisible; review and export surfaces stay named instead of being mixed into editing truth.

**Quality gating.** `quality_gate_report` chooses a lens stack rather than a universal checklist; hard gates are separated from weighted weaknesses; targeted recheck is preferred over automatic full re-audit; specialized checker logic can inform the design without becoming repo-wide law.

**Visual translation.** Multilingual visual-language assets should load only when cross-language shot/staging communication changes answer quality materially; screenplay-to-video bridge assets should stay vendor-neutral and clip-bounded; downstream model or tool choice should sit after bridge construction, not inside screenplay routing.

The repository also applies a clear anti-dogma stance:
- screenplay guidance is heuristic, not absolute;
- multiple viable paths may coexist before convergence;
- hard boundaries and soft constraints must not be conflated;
- exploration and review are separate phases, not one blended act.
- challenged claims should narrow through scope correction instead of toggling between opposite absolutes.
- reference patterns should teach contrastive success/failure logic without becoming a hidden canon.

The consequence is that agents should not read the whole repository by default. They should enter through a route, then load one protocol, its linked atoms, and one rubric.
When the task is teaching, comparison, or scenario diagnosis, they should also use the scenario atlas as a factorization layer rather than jumping straight from medium label to sample choice.
Between route selection and generation, they should choose a bounded loading mode so the system can widen references without drifting into context degradation.
When the work genuinely needs multiple roles, they should also choose a team mode so collaboration structure stays clear instead of becoming an invisible prompt habit.
When the work genuinely needs long-horizon project design, they should also choose a project surface so editable truth, runtime state, handoff packets, and delivery surfaces do not collapse into one folder-shaped blur.
When the work genuinely needs structured checking, they should choose a quality gate so contract fit, execution risk, delivery readiness, and recheck scope stay clear instead of being buried inside generic rewrite advice.

## Why A Monorepo

A single repository makes it possible to evolve:
- shared taxonomies;
- routing rules;
- linked knowledge atoms;
- cross-skill fixtures;
- validation tooling;
- open source documentation

without version drift between separate repositories.

This also keeps narrative, commercial, and interactive logic from drifting into separate prompt silos.
It also prevents pure craft outputs from drifting away from audience demand and production constraints.

## Design Constraints
- Research-first, not UI-first.
- Human-readable first, but machine-validated.
- Stable IDs and additive evolution.
- Clear routing over ad-hoc prompt accumulation.
- A route should be explainable as `intent x medium x stage x output x constraints`.
- Constraints must support real-world parameters such as audience need state, commissioning context, business model, release logic, and writer maturity.
- The system must resist false universals by making assumptions, boundaries, and convergence triggers clear.
- The system must resist context degradation by separating route selection from bounded reference expansion.
- The system must resist fake collaboration by separating real specialist lanes, handoff contracts, and human gates from mere parallelism theater.
- The system must resist persona worship by separating craft-lineage pressure from direct impersonation or hidden canon.
- The system must resist prompt-first drift by separating screenplay reasoning from downstream visual-bridge containers.
- The system must resist repo-surface drift by separating canonical source, runtime state, and delivery surfaces instead of letting them emerge accidentally.
- The system must resist checker overgeneralization by separating reusable audit abstractions from any one domain-specific checking pipeline.
- Every asset type should be independently lintable.
- Thin skills should stay operational while theory stays centralized in `knowledge/`.

## Build Philosophy

The repository should be able to expand indefinitely by appending:
- new atoms;
- new protocols;
- new rubrics;
- new fixtures;
- new skills;
- new media and genre packs

without breaking existing consumers.
