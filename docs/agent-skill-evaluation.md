# Agent Skill Evaluation

## Verdict

The current design is now strong as both an agent routing system and a bounded retrieval system, with governance risks remaining at the edges rather than in the core.

It now has the right ingredients for a professional screenplay agent: route-first orchestration, layered knowledge assets, explicit pluralism, scenario factorization, contrastive reference packs, a formal context-loading policy, and a repo-local tier fallback. The remaining work is mostly discipline and regression control: keeping nearby routes distinct, keeping scenario axes stable, and preventing reference breadth from silently becoming template pressure.

## What Is Working

- The `intent x medium x stage x output x constraints` route key is concrete enough for a real agent to explain its decision.
- `knowledge_atom`, `workflow_protocol`, and `evaluation_rubric` keep theory, procedure, and evaluation separable.
- `scenario taxonomy` and the scenario atlas prevent the repo from collapsing everything into genre slogans.
- `path_options`, `boundary_map`, `scope_correction`, and `pattern_reference_pack` give the agent explicit outputs for divergence, limits, claim narrowing, and contrastive teaching.
- `context_loading_plan` and the bounded loading modes give the agent a formal way to decide how much context is justified before generation.
- `voice_style_guide` plus the expression-lens triggers now let the repo model style, continuity, and lived-in expression explicitly without forcing every draft through a template route.
- `team_workflow_blueprint` plus the team-mode matrix now let the repo model real collaboration structures instead of flattening all high-end screenplay work into one writer-agent.
- The community loop and Socratic backlog make disagreement a structured input instead of an afterthought.
- The repo now includes a local [`docs/shared/agent-tiers.md`](./shared/agent-tiers.md) fallback, so tiered agent work no longer points at a missing local contract.
- Route-overlap checking is now explicit in CI, which reduces the risk of adjacent “smart answer” modes collapsing into one another silently.

## Where The Design Is Still Fragile

### 1. Load governance must stay real, not ceremonial

The repo now has a loading ladder, but the real risk is operational drift: contributors may keep adding assets while quietly ignoring the bounded-loading rules.

That would recreate the same failure modes in softer form:
- under-loading: the agent never leaves `route_kernel` or `focus_pack` and answers too generically;
- over-loading: the agent escalates to `teaching_pack` or `survey_pack` for ordinary tasks and corrodes context anyway.

### 2. Route overlap risk

Several outputs live close together in concept space:
- `path_options`
- `boundary_map`
- `scope_correction`
- `pattern_reference_pack`
- `team_workflow_blueprint`

Each one is useful, but the repo still needs careful fixture design so they do not become interchangeable "smart answer" modes. The overlap checker reduces silent ambiguity, but it does not replace judgment.

### 3. Retrieval inflation risk

The repo now has enough supporting material that the agent can easily over-collect:
- scenario atlas
- reality lenses
- reference packs
- case notes
- pluralism docs

That is good for teaching and diagnosis, but not every request needs that much scaffolding. If maintainers start normalizing broad packs as the default, the model will again import more context than the task can benefit from.

### 4. Scenario-axis creep

The scenario atlas is now a strong factorization layer, but it can still bloat into a second canon if new axes are added casually. Scenario cards should grow faster than scenario axes.

## What To Change

1. Keep the loading modes strict in practice.
   - `route_kernel`
   - `focus_pack`
   - `compare_pack`
   - `teaching_pack`
   - `survey_pack`
   The modes now exist. The next job is to keep new routes and docs from bypassing them.

2. Keep route priority and overlap tests current.
   - If two routes can match the same request, the router must know which one wins.
   - If a new route creates ambiguity, it should fail CI before it reaches users.

3. Freeze the core scenario axes.
   - New scenario cards should be append-only.
   - New axes should require review, because axis creep is how a scenario system turns into a second ontology.

4. Gate reference packs by request type.
   - Use them for teaching, comparison, diagnosis, or explicit "why this is better" requests.
   - Do not load them by default for ordinary drafting.

5. Add a budget check before expansion.
   - If additional context does not change the route, the rubric, or the next decision, do not load it.
   - If the agent cannot state why a new reference changes the answer, the reference is probably redundant.

6. Keep the repo-owned tier fallback minimal.
   - The fallback now exists.
   - Do not let it grow into a complicated second workflow framework.

7. Keep expression guidance constrained.
   - Style assets should load when they change line-level decisions.
   - They should not become a pretext for loading flavor docs into every draft.

8. Keep team modes explicit and bounded.
   - Team mode should activate when workflow structure changes the next decision.
   - It should not turn ordinary writing requests into performative multi-agent theater.

## Balanced Retrieval Rule

The right balance is not "load as much as possible" and not "load as little as possible".

The better rule is:
- load the smallest set that changes the route;
- expand only when the task is comparative, diagnostic, or teaching-oriented;
- stop as soon as the next asset no longer changes the answer materially.

That is the point at which the agent stays creative without becoming context-saturated.

## Why The Design Still Has High Extension Capacity

The architecture is still very extensible because new knowledge is mostly additive:
- new media or genre packs can be appended;
- new scenario cards can be added without renaming old IDs;
- new pattern packs can be created for new problem families;
- new protocols and rubrics can be introduced as long as they stay routeable.

The only real constraint is governance: extension should add routing precision, not just add more text.

## Short List Of Priorities

- Keep bounded loading modes operational.
- Keep the repo-local tier guide small and sufficient.
- Keep overlap tests for route selection current.
- Keep the scenario taxonomy frozen at the axis level unless there is a strong justification.
- Treat reference packs as contrastive teaching artifacts, not as canonical templates.
- Treat voice guides as calibration tools, not as substitute drafts or canonized speaking templates.
- Treat team blueprints as workflow selectors, not as a default wrapper around every request.
