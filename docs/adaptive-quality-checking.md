# Adaptive Quality Checking

This repository now treats screenplay self-checking as an adaptive system rather than a single universal checklist.

## Why This Layer Exists

Specialized checker workflows can be extremely strong inside a narrow domain.
Their most transferable strengths are:
- layered checking instead of vague “overall feedback”;
- bounded review perspectives instead of one bloated critic voice;
- compact handoff metrics instead of full-context chaining;
- hard gates separated from weighted scoring;
- explicit recheck logic after revisions.

What does not transfer cleanly is a fixed linear stage stack for every artifact.

This repo covers:
- narrative artifacts;
- commercial and branded scripts;
- interactive structures;
- voice guides;
- visual-language packs;
- screen-to-video briefs;
- team and subagent governance artifacts;
- project-surface design.

Those artifacts do not fail in the same way, so they should not be checked through one frozen pipeline.

## Core Design

The repo now uses `quality_gate_report` as a generic audit output.

Its logic is:
1. lock the target contract first;
2. apply the target artifact's native rubric or closest contract gate;
3. select a small lens stack from [`references/check-lens-matrix.json`](../references/check-lens-matrix.json);
4. run each lens with bounded context;
5. separate hard fails from weighted weaknesses;
6. synthesize a correction ladder;
7. define a limited recheck plan when appropriate.

## Lens Set

The current reusable lenses are:
- `contract_fit`
- `mechanics_pressure`
- `continuity_invariants`
- `expression_integrity`
- `operational_feasibility`
- `delivery_handoff`
- `boundary_risk`

These are not mandatory in every case.
They are a reusable vocabulary for selecting the right audit surface.

## Scope Modes

The repo currently supports four review scopes:
- `full_audit`
- `lens_targeted`
- `range_limited`
- `recheck`

That prevents the quality layer from becoming unnecessarily heavy.

## Boundary With Rewrite Report

`rewrite_report` still exists and remains useful.

Use `rewrite_report` when the main job is:
- identify the failing craft layer;
- prioritize rewrite moves inside story/text development;
- tell the team what to rewrite first.

Use `quality_gate_report` when the main job is:
- run a structured audit;
- preflight an artifact before handoff or delivery;
- inspect non-story artifacts such as voice guides, screen-to-video briefs, team plans, or project surfaces;
- run targeted recheck after changes;
- separate hard gate failure from weighted weakness.

The intended stack is:
- route-native rubric first;
- shared lens matrix second.

## Linked Assets

- [`wp.quality-gate-report`](../knowledge/20-workflows/wp-quality-gate-report.md)
- [`rb.quality-gate-report`](../knowledge/60-rubrics/rb-quality-gate-report.md)
- [`references/check-lens-matrix.json`](../references/check-lens-matrix.json)
