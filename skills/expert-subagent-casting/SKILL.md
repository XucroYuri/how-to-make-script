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

## References
- `wp.expert-subagent-cast`
- `ka.subagent-cast-composition`
- `ka.process-node-specialization`
- `ka.reference-persona-governance`
- `ka.subagent-context-budgeting`
- `rb.expert-subagent-cast`
