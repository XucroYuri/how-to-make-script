---
name: expert-subagent-casting
description: Use when the user needs a concrete cast of screenplay subagents, including functional specialists, process nodes, and optional reference-persona lenses.
---

# Expert Subagent Casting

Use this skill when the user is not just asking for a team mode, but for the actual specialist cast that should participate in the work.

## Workflow
1. Identify the primary screenplay problem, medium, stage, and delivery pressure.
2. Select the smallest viable core cast of functional specialists.
3. Add process-node subagents only where they materially improve divergence, triage, review, or convergence.
4. Add reference-persona lenses only when they change judgment quality materially and can be governed safely.
5. Return a cast with authority, budget, handoff expectations, and trim order.

## Output Contract
- `expert_subagent_cast`: core cast, optional cast, process nodes, persona lenses, authority map, context budgets, handoff notes, human-owned nodes, and trim order.
- Keep persona lenses bounded. They pressure decisions; they do not replace route, protocol, rubric, or hard boundaries.
- Prefer smaller casts with explicit composition rules over bigger casts with overlapping mandates.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the one thing you cannot decide without another perspective?" A single capability gap is enough to seed the cast. Do not produce a full roster.

**When `certainty = exploring`:**
Offer two cast options: minimum viable (2-3 roles) and expanded (4-5 roles). State what each cast can and cannot cover. Let the user select.

**When `certainty = certain`:**
Apply the full workflow: primary problem → smallest viable core cast → process nodes → persona lenses → authority map → trim order. Persona lenses are advisory only unless explicitly scoped otherwise.

**When `focus = character`:**
Character-layer problems benefit from a character-authenticity specialist and an audience-proxy lens. Suppres heavy infrastructure roles (context budget manager, convergence owner) unless the project scale demands them.

**When `focus = event`:**
Structure-layer problems benefit from a structure specialist and a causality checker. Audience-response simulation is a useful secondary lens, not a primary one.

## References
- `wp.expert-subagent-cast`
- `rb.expert-subagent-cast`
- `ka.convergence-owner-discipline`
- `ka.cross-protocol-referral-edges`
- `ka.process-node-specialization`
- `ka.reference-persona-governance`
- `ka.subagent-cast-composition`
- `ka.subagent-context-budgeting`
- `ka.team-topology-selection`
