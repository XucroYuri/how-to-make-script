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

## References
- `wp.team-workflow-blueprint`
- `ka.team-topology-selection`
- `ka.handoff-packet-discipline`
- `rb.team-workflow-blueprint`
