# Context Loading Policy

This policy sits between routing and generation. It does not choose the route. It controls how much context to load after the route is chosen so the model stays accurate without drowning in redundant material.

## Assessment

The current skill design is strong in three places:
- route-first selection is explicit;
- the repo already separates route packs, scenario taxonomies, boundary tools, and pattern reference packs;
- the content model favors bounded assets over one giant prompt.

The main risk is overload, not lack of knowledge. If every nearby asset is loaded whenever a request feels difficult, the model will start repeating the repo instead of using it. That causes context corrosion, weaker decision quality, and slower creative movement.

The policy below is designed to keep the repo broad enough for creative extension and narrow enough for reliable execution.

## Principles

1. Route first, load second.
2. Load the smallest context bundle that can still change the decision.
3. Expand one layer at a time. Do not jump from a route to a whole library.
4. Prefer contrastive references over bulk references.
5. Stop as soon as additional context no longer changes the route, output contract, or self-check.

## Loading Modes

Use `references/context-loading-modes.md` as the operational menu. In short:
- `route_kernel` for the minimum route-safe bundle;
- `focus_pack` for one task, one route, one rubric;
- `compare_pack` when the user wants alternatives, why-not analysis, or boundary work;
- `teaching_pack` when the user wants explanation, examples, or learning support;
- `survey_pack` only when the user explicitly wants a broad survey, and anchor it on one declared background bundle first.

## Expansion Triggers

Expand only when a new layer can still change the answer:
- the request is hybrid or multi-scenario;
- the user asks for alternatives, counterexamples, or why one path is better;
- the draft shows route mismatch, failure layers, or boundary confusion;
- the task requires audience fit, commissioning fit, learning path, or other real-world grounding;
- the task needs voice calibration, register control, continuity protection, or stronger lived-in expression;
- the task needs team-mode selection, handoff design, or review-gate design;
- the user explicitly asks for teaching, comparison, or a broader survey.
- the task is a broad theory or background-support request that needs a declared research bundle instead of ad hoc expansion.

## Stop Conditions

Stop loading when one of these is true:
- the route is stable and the output contract is fixed;
- the new material only repeats what is already loaded;
- the next asset would add detail but not change the decision;
- the context bundle already contains one route anchor, one supporting reference, and one edge-case or contrast when needed.

If the request is narrow, stop at the first bundle that can support a correct answer. If the request is broad, stop at the smallest bundle that can still explain the tradeoffs.

## Failure Signals

Treat the load as too large or too small if you see any of these symptoms:
- the answer starts summarizing docs instead of solving the request;
- multiple loaded sources conflict but the response does not resolve the conflict;
- the response becomes generic because the model spent its budget on irrelevant breadth;
- the response becomes brittle because it loaded only one favorite example and no contrast;
- the model begins treating reference fragments as templates instead of reference paths.

## Balance Rules

- Keep one primary route pack in view at all times.
- Add at most one adjacent comparison pack unless the user explicitly asks for a wider survey.
- For writing guidance, prefer one strong example plus one weak contrast over many similar examples.
- For boundary questions, prefer `boundary_map` or `scope_correction` before loading more general craft material.
- For scenario questions, prefer `docs/scenario-atlas.md` and `references/scenario-taxonomy.json` before loading many examples.
- For broad theory/support questions, prefer one background bundle from `references/background-bundles.json` before loading multiple adjacent docs.
- For pause/resume, room-handoff, or long-form continuity pressure, prefer `story_memory_checkpoint` before widening the bundle around the same draft.
- For fit or strategy questions, prefer the relevant reality-lens atoms before broad craft expansion.
- For voice or liveness questions, prefer the smallest expression-lens bundle before loading large reference packs.
- For collaboration-design questions, prefer the smallest team-mode bundle before loading broad framework comparisons.

## Recovery Rules

If the load has drifted too wide:
- drop back to the route kernel;
- reload only the primary protocol, rubric, and one supporting reference;
- ask a clarifying question if the route is still ambiguous.

If the load is too thin:
- reload the missing decision layer;
- add one contrastive reference or one boundary note;
- do not solve under-loading by loading the entire repo.

## Operating Summary

The right bundle is the smallest bundle that still lets the model explain the route, justify the decision, and generate a useful answer.
