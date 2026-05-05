---
name: team-workflow-design
description: Use when the user needs a screenplay collaboration blueprint across humans, agents, or hybrid teams.
---

# Team Workflow Design

Use this skill when the user asks how a writing room, story team, director-writer pod, campaign strike team, interactive narrative cell, or hybrid human-agent team should actually operate.

## Workflow
1. Identify the project container, stage, and core pressure.
2. Select the closest team mode.
3. Define roles, lanes, handoffs, and checkpoints.
4. Return a blueprint that can run without pretending one team shape fits everything.

## Output Contract
- `team_workflow_blueprint`: team mode, role map, artifact ladder, handoff rules, human checkpoints, failure modes, and mode-switch triggers.
- The blueprint should preserve creative dissent long enough to be useful, then converge deliberately.
- Parallelism is only a benefit when the blueprint also defines merge control.
- If the question shifts from mode choice to exact subagent composition, hand off to `expert_subagent_cast`.
- If the question shifts from mode choice to scheduling, review order, or packet flow, hand off to `subagent_dispatch_plan`.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "Who is responsible when something goes wrong in the current process — and do they know it?" One accountability gap is the right entry point for a workflow design conversation. Do not produce a blueprint yet.

**When `certainty = certain`:**
Apply the full workflow: project container and stage → team mode → roles, lanes, handoffs, checkpoints → return a blueprint with merge control and failure modes explicit.

**When `certainty = exploring`:**
Offer two workflow shapes: one that preserves creative dissent until a deliberate convergence gate, one that converges at every stage. State when each is appropriate.

**When `source = construct`:**
Primary activation context. Workflow design is inherently a construct-mode activity. Parallelism is a liability if the blueprint does not also define merge control.

**When `focus = audience`:**
Audience-response feedback loops should be explicit in the workflow design. If audience proxies or test readers are part of the process, name when they enter and what their gate authority is.

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
