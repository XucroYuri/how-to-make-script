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

## References
- `wp.team-workflow-blueprint`
- `ka.team-topology-selection`
- `ka.handoff-contract-discipline`
- `ka.human-checkpoint-gates`
- `ka.room-artifact-ladder`
- `ka.parallel-lane-governance`
- `rb.team-workflow-blueprint`
