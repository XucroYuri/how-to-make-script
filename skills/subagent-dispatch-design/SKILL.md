---
name: subagent-dispatch-design
description: Use when the user needs a concrete multi-level dispatch plan for screenplay subagents, not just a list of roles.
---

# Subagent Dispatch Design

Use this skill when the user asks how screenplay subagents should be orchestrated across layers, lanes, reviews, and human gates.

## Workflow
1. Confirm the primary route or target artifact.
2. Confirm or infer the team mode and cast scope.
3. Select a dispatch topology and phase pattern.
4. Define packet flow, merge ownership, review loops, human gates, and context budgets.
5. Return a plan that can be executed without hidden full-context sharing.

## Output Contract
- `subagent_dispatch_plan`: control-plane order, topology, phase ladder, lane budgets, packet schema, review loops, human gates, fallback topology, and collapse triggers.
- Prefer two-stage review where under-building and over-building are both costly.
- Keep persona lanes advisory unless the plan explicitly says otherwise.

## References
- `wp.subagent-dispatch-plan`
- `ka.subagent-context-budgeting`
- `ka.convergence-owner-discipline`
- `ka.two-stage-review-loop`
- `rb.subagent-dispatch-plan`
