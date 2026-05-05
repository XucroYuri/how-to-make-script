---
name: project-surface-design
description: Use when the user needs a long-running screenplay project surface design with source-of-truth, runtime state, packet assembly, review surfaces, and export surfaces.
---

# Project Surface Design

Use this skill when the user asks how a screenplay project should persist state, separate editable truth from runtime artifacts, expose phase entrypoints, or assemble inspectable packets for writing and review.

## Workflow
1. Identify the medium, phase pressure, and collaboration shape.
2. Separate canonical source from runtime state.
3. Define entrypoints, handoffs, packet assembly, review surfaces, export surfaces, and checkpoint surfaces when long-horizon continuity matters.
4. State sync rules and human-edit policy explicitly.
5. Return a map that can support long-running work without silent drift.

## Output Contract
- `project_surface_map`: source-of-truth artifacts, runtime surfaces, phase entrypoints, canonical packet layers, review surfaces, export surfaces, sync rules, drift risks, and future runtime hooks.
- Keep the map medium-aware. A short-drama production line is not the same as a feature development workspace.
- Prefer explicit human-edit policy over silent assumptions.
- If resumable continuity matters, place checkpoint surfaces explicitly instead of leaving them as implicit notes.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "Where are you most afraid of accidentally overwriting something important?" The answer usually locates the source-of-truth gap. Do not produce a full surface map until that fear is named.

**When `source = construct`:**
Primary activation context. Apply the full workflow: canonical source → runtime state → entrypoints → handoffs → packet assembly → review surfaces → export surfaces → sync rules → drift risks.

**When `certainty = exploring`:**
Offer two surface architectures: one optimised for solo long-form work, one optimised for team handoffs. State the critical difference in edit policy and drift risk.

**When `focus = world`:**
Long-form world-consistency problems are often project-surface problems in disguise: canonical world rules are being silently overwritten in runtime drafts. Locate the drift source before fixing the rules.

**When `focus = event`:**
Episodic and serial projects often suffer from arc-budget drift between surface layers. Checkpoint surfaces and canon-vs-hypothesis boundaries are the highest-value elements of the map.

## References
- `wp.project-surface-map`
- `rb.project-surface-map`
- `ka.archive-literacy`
- `ka.canonical-packet-assembly`
- `ka.command-artifact-mapping`
- `ka.cross-protocol-referral-edges`
- `ka.phase-entrypoint-handoff`
- `ka.script-as-coordination-artifact`
- `ka.source-of-truth-runtime-split`
- `ka.story-memory-checkpoint`
- `ka.subagent-context-budgeting`
