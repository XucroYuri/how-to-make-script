# Multi-Agent Screenplay Architecture

This repository now treats screenplay creation as a possible **team problem**, not only a routing problem.

That does not mean every request should become a multi-agent run. It means the repo now has a designated place to describe when screenplay work should be handled by:
- one orchestrator plus specialists;
- parallel exploration lanes;
- bounded handoffs;
- explicit review boards;
- human approval gates.

## Design Position

The repository does **not** adopt one universal “writer super-agent” model.
Public multi-agent systems and real-world screenplay teams both point the other way:
- use a central orchestrator when ownership and synthesis matter;
- use specialists when different decisions need different bundles;
- use handoffs instead of full-context sharing;
- use human intervention at the costly or ambiguous gates.

## New Layer

The new layer sits above ordinary route selection:

1. Root route selection still decides the primary screenplay problem.
2. Team-mode selection decides whether the work should run as a pod, room, trust loop, studio workflow, or branch lab.
3. Expert-cast selection decides which functional specialists, process nodes, and persona lenses should actually enter.
4. Dispatch-topology selection decides how those specialists run, merge, review, and shrink again.
5. Specialist lanes get only the minimum bundle relevant to their job.
6. Handoff packets carry state between lanes.
7. Review boards and humans absorb the high-risk decisions.

## Default Team Modes

### `feature_dev_pod`
- Best for: feature development, adaptation-heavy rewrite, pitch-to-outline planning.
- Shape: hybrid room.
- Why: feature work needs strong synthesis, rewrite mandates, and producer/director alignment.

### `showrunner_room`
- Best for: season-engine work, episode breaking, room-based television development.
- Shape: supervisor tree.
- Why: the room can parallelize, but showrunner synthesis must remain central.

### `animation_story_trust`
- Best for: animation development where story and visual iteration must co-evolve.
- Shape: hybrid room.
- Why: story logic, visual storytelling, and production feasibility all need explicit loops.

### `brand_content_studio`
- Best for: commercial, branded film, and shortform campaign work.
- Shape: hybrid room.
- Why: creative, brand, and distribution concerns must run in parallel without collapsing into hard-sell copy.

### `interactive_branch_lab`
- Best for: game narrative and branching interactive design.
- Shape: supervisor tree.
- Why: narrative, state, and QA loops must stay distinct while a narrative director controls scope.

### `franchise_continuity_board`
- Best for: existing IP, canon-sensitive adaptation, persona continuity risk.
- Shape: review board.
- Why: canon anchors and identity risks need explicit guardianship before innovation expands.

## Handoff Rule

Every specialist should return a bounded handoff packet, not an essay dump.

Minimum fields:
- `working_hypothesis`
- `loaded_bundle_ids`
- `open_questions`
- `confidence`
- `recommended_next_agent`
- `needs_human_review`

This is the team-level extension of bounded loading.

## Subagent Rule

Not every team-mode question needs a concrete subagent deployment.

Use:
- `team_workflow_blueprint` when the repo should choose the collaboration family;
- `expert_subagent_cast` when the repo should choose the participating specialists;
- `subagent_dispatch_plan` when the repo should specify live scheduling, review order, and merge logic.

This keeps mode, cast, and topology from collapsing into one overstuffed answer.

## Human-In-The-Loop Rule

Human review should not be everywhere.
It should appear at the points where the cost of silent drift is high:
- IP continuity and franchise identity;
- audience-fit disputes;
- commissioning or brand-boundary conflict;
- scope correction at major strategic claims;
- final delivery approval.

## Why This Fits The Repo

This design extends what already exists:
- route-first orchestration remains intact;
- bounded loading remains per role and per step;
- anti-dogma outputs remain important because not all team modes converge the same way;
- team mode becomes another explicit layer instead of an invisible assumption.

## Public Sources Behind This Layer

- WGA room and feature-development guidance:
  [Showrunners’ Guide to 2023 MBA Writers’ Room Provisions](https://www.wga.org/contracts/contracts/mba/showrunners-guide-to-2023-mba-writers-room-provisions)
  [Screenwriters Handbook](https://www.wga.org/members/employment-resources/screenwriters-handbook)
- Animation workflow references:
  [Disney Animation Story Artist](https://www.disneyanimation.com/team/story-artist/)
  [Pixar - Pete Docter](https://www.pixar.com/docter)
- Branded-content workflow references:
  [Digitas branded content arm](https://www.digitas.com/en-us/pressroom/newfront-founder-digitas-unveils-branded-content-arm)
- Interactive narrative workflow references:
  [inklewriter](https://www.inklestudios.com/inklewriter/)
  [ChoiceScript automated testing](https://www.choiceofgames.com/make-your-own-games/testing-choicescript-games-automatically/)
- Multi-agent orchestration references:
  [OpenAI Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
  [LangGraph Supervisor](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html)
  [OpenAI Swarm](https://github.com/openai/swarm)
  [CrewAI human-in-the-loop](https://docs.crewai.com/en/learn/human-in-the-loop)
  [oh-my-openagent](https://github.com/code-yeongyu/oh-my-opencode)
