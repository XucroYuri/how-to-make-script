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

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "Which part of the work cannot proceed until someone else finishes — and who is that someone?" One dependency bottleneck is the seed of a dispatch plan. Do not produce a full topology yet.

**When `certainty = certain`:**
Apply the full workflow: confirm route and cast → select topology → define packet flow and merge ownership → define review loops, human gates, and context budgets → return plan with collapse triggers.

**When `certainty = exploring`:**
Offer two topology options: a tighter sequential chain (lower parallelism, lower merge risk) and a wider parallel ring (higher throughput, higher convergence complexity). State the deciding factor.

**When `source = construct`:**
Primary activation context for this skill. Dispatch design is fundamentally a construct-mode activity: every topology decision is a structural choice with explicit cost and benefit.

**When `focus = event`:**
For event-layer screenplay work, the dispatch plan should reflect the narrative sequence: earlier structural decisions constrain later scene decisions. Topology should respect this dependency order.

## References
- `wp.subagent-dispatch-plan`
- `rb.subagent-dispatch-plan`
- `ka.convergence-owner-discipline`
- `ka.cross-protocol-referral-edges`
- `ka.handoff-packet-discipline`
- `ka.parallel-lane-governance`
- `ka.subagent-context-budgeting`
- `ka.team-topology-selection`
- `ka.two-stage-review-loop`
