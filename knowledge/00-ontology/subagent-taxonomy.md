# Subagent Taxonomy

`subagent taxonomy` is the repository layer that turns multi-agent screenplay work from a vague aspiration into an addressable system.

The repo already had a team-mode layer. This new layer sits below it and answers a more operational question:

- which specialist subagents should enter the job;
- what kind of subagent each one is;
- how many should run at once;
- who owns convergence;
- what packet each subagent gets instead of a full-context dump.

## Why This Layer Exists

High-end screenplay work is rarely improved by “just add more agents.”

The failure usually comes from one of four mistakes:

- every agent gets the whole repo and starts hallucinating authority;
- functional specialists and review nodes are mixed together;
- real-person-inspired lenses are treated like universal truth or direct impersonation;
- parallelism expands faster than merge discipline.

The subagent layer exists so the repository can say:

- route first;
- choose team mode second;
- choose a bounded cast third;
- choose a dispatch topology fourth.

## Core Terms

- `functional subagent`: owns one craft problem, such as premise pressure, scene execution, dialogue, brand message, continuity, or branch logic.
- `process-node subagent`: owns one workflow position, such as divergence, counterexample retention, rewrite triage, convergence, or review.
- `reference_persona`: a bounded craft lens inspired by real creators, companies, or schools of practice. It is a calibration aid, not final authority.
- `convergence owner`: the role that decides when the system stops branching and what survives into the next artifact.
- `dispatch topology`: the shape of coordination, such as supervisor tree, specialist ring, debate board, dual-track loop, or two-stage review loop.
- `handoff packet`: the bounded context one node passes to another instead of forwarding the whole workspace.

## Design Rules

1. Do not let every expert become a new route.
2. Separate craft specialists from process nodes.
3. Let reference personas pressure decisions, not replace protocol contracts.
4. Give every cast one clear convergence owner.
5. Keep persona loading smaller than functional loading.
6. Prefer a smaller cast with explicit composition rules over a huge cast with implicit overlaps.
7. Keep human authority explicit at high-risk gates.

## Relation To Existing Layers

- `team_workflow_blueprint` answers which collaboration mode fits the job.
- `expert_subagent_cast` answers which concrete specialists and persona lenses should participate.
- `subagent_dispatch_plan` answers how those specialists should be scheduled, merged, reviewed, and trimmed.

The subagent layer therefore extends the team layer. It does not replace it.

## What This Layer Should Prevent

- turning every screenplay job into a giant “all experts at once” room;
- treating a famous creator's public craft signature like a license for exact mimicry;
- letting review personas draft first-pass material by default;
- letting every lane read every artifact;
- expanding the cast without naming who can merge, veto, or stop.

## TODOs: Questions To Keep Open

- [ ] Which screenplay problems still need first-class subagent families not yet represented in the library?
- [ ] When should a small project skip team mode entirely and instantiate only one focused subagent plus one reviewer?
- [ ] Which persona families are useful enough to keep, and which will create more mythology than signal?
- [ ] How should the library distinguish “reference lineage” from “direct style pressure” when users ask for real-person-inspired help?
- [ ] Which dispatch topologies should be reserved for repo-development tasks versus screenplay-generation tasks?
