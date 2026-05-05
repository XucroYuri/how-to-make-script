---
name: team-orchestration
description: Use when the user needs a multi-agent or hybrid screenplay collaboration blueprint rather than a single drafting pass.
---

# Team Orchestration

Use this skill when the request is about designing a screenplay team workflow, agent-room structure, handoff model, specialist-lane setup, or human review gates.

## Workflow
1. Identify the real-world workflow family the task most resembles.
2. Choose a team mode and coordination model.
3. Define roles, lane boundaries, synthesis cadence, and handoff packets.
4. Mark human gates and high-risk review points.
5. Return a blueprint that is executable, not just inspirational.

## Output Contract
- `team_workflow_blueprint`: mode rationale, role map, coordination model, artifact chain, handoff packet rules, human gates, failure modes, and fallback path.
- Keep the root skill as orchestrator; do not make every worker a mini-root.
- Prefer bounded per-role bundles over shared full-repo context.
- If the user needs a concrete expert roster, route onward to `expert_subagent_cast`.
- If the user needs live scheduling or review-order design, route onward to `subagent_dispatch_plan`.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the one handoff in this project you are most worried about dropping?" One critical handoff point is the seed of a team design. Do not produce a full team blueprint yet.

**When `certainty = certain`:**
Apply the full workflow: identify real-world workflow family → choose team mode and coordination model → define roles, lane boundaries, synthesis cadence, and handoff packets → mark human gates → return executable blueprint.

**When `certainty = exploring`:**
Present two team configurations: one optimised for creative divergence (keeps dissent alive longer), one optimised for convergence speed. State what each costs.

**When `source = construct`:**
Primary activation context. A team blueprint is a construct-mode deliverable: roles, lanes, and handoffs must be specific enough to execute, not inspirational enough to admire.

**When `focus = character` or `focus = language`:**
Creative specialisation at the character or language layer often benefits from a bounded specialist lane, not from full-room collaboration. Suggest a smaller team with a defined character/language expert role rather than a full writers' room.

## References
- `wp.team-workflow-blueprint`
- `rb.team-workflow-blueprint`
- `ka.cross-protocol-referral-edges`
- `ka.dissent-preservation-loop`
- `ka.handoff-contract-discipline`
- `ka.human-checkpoint-gates`
- `ka.parallel-lane-governance`
- `ka.room-artifact-ladder`
- `ka.team-mode-recipes`
- `ka.team-topology-selection`
