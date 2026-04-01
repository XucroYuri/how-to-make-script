[中文说明](./README_zh.md)

# how-to-make-script

`how-to-make-script` is a research-first, agent-ready monorepo for screenplay creation.

It serves two audiences at once:
- humans who want a rigorous, expandable map of screenplay craft;
- LLM and agent systems that need structured, routable, testable knowledge assets.

It now includes a real-world grounding layer so output quality is not detached from:
- audience demand signals;
- commissioning and business context;
- platform and release logic;
- writer development maturity;
- historical evolution of screenwriting practice.

The repository does not start from a web app. It starts from durable creative infrastructure:
- a screenplay knowledge ontology;
- reusable knowledge atoms;
- workflow protocols;
- evaluation rubrics;
- a root orchestration skill plus thin sub-skills;
- examples, fixtures, validation scripts, and CI.

It is also intentionally human-in-the-loop:
- contributors are expected to challenge claims, routes, and rubrics;
- issues are treated as structured feedback inputs, not just bug bins;
- disagreement is supposed to produce better atoms, protocols, rubrics, fixtures, and docs.

## Agent Use

The intended loop is:
1. classify the request by `intent x medium x stage x output x constraints`;
2. load the smallest matching protocol and rubric set;
3. generate the requested artifact;
4. run a rubric-based self-check;
5. expand only if the user asks for broader teaching or comparison.

This is the repository's main capability claim: help an agent stay correctly routed, context-bounded, and output-disciplined.

For requests involving market fit, development strategy, or writer training, constraints should explicitly include:
- audience segment and audience need state;
- commissioning context and business model;
- release window and platform logic;
- writer maturity and reference bar.

## V1 Focus

V1 uses a full-spectrum taxonomy with focused depth:
- narrative screenwriting;
- commercial / branded scripting;
- interactive / branching narrative.
- real-world screenplay grounding (audience, industry, training, history).

## Repository Layout

```text
how-to-make-script/
├── SKILL.md
├── knowledge/
├── schemas/
├── skills/
├── references/
├── examples/
├── scripts/
└── tests/
```

## Asset Model

The repository treats four structured asset types as first-class:
- `knowledge_atom`
- `workflow_protocol`
- `evaluation_rubric`
- `example_fixture`

Structured Markdown assets use JSON frontmatter between `---` fences. That keeps content readable in GitHub while staying easy to validate with standard-library tooling.

For agent use, the working split is:
- atoms hold reusable craft logic;
- protocols define the execution path;
- rubrics constrain final output quality;
- fixtures make routing behavior regression-testable.

Additional output contracts for real-world grounding:
- `audience_fit_note`
- `development_brief`
- `learning_path`

## Quick Start

```bash
python3 scripts/validate_assets.py
python3 scripts/check_routes.py
python3 scripts/check_forbidden_paths.py
python3 scripts/check_question_todos.py
python3 scripts/run_fixture_suite.py
python3 -m unittest discover -s tests -v
```

## Install As A Skill

Use the same repository as both a human-readable reference and an agent-installable skill package.

### Codex

```toml
[[skills.config]]
path = "/absolute/path/to/how-to-make-script"
enabled = true
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s /absolute/path/to/how-to-make-script ~/.claude/skills/how-to-make-script
```

### OpenCode

```bash
mkdir -p ~/.config/opencode/skills
ln -s /absolute/path/to/how-to-make-script ~/.config/opencode/skills/how-to-make-script
```

### Gemini CLI

Install as a local extension or clone it under a shared skills directory recognized by your setup.

## Design Rules
- IDs are stable once published.
- Skills are thin wrappers around repository knowledge, not duplicate prompt silos.
- Routing is explicit: `intent x medium x stage x output x constraints`.
- Reality lenses are loaded only when they change route quality or output quality.
- New knowledge is additive by default.
- If a request is underspecified, ask only for the missing detail that changes the route or output contract.
- Prefer one primary protocol and one primary rubric per request.
- Treat commercial and interactive work as first-class routes, not narrative edge cases.

## Key Docs
- [Architecture](./docs/architecture.md)
- [Content Model](./docs/content-model.md)
- [Reality Lenses](./docs/reality-lenses.md)
- [Real-World Source Map](./docs/source-map-real-world.md)
- [Roadmap](./docs/roadmap.md)
- [Bilingual Authoring Policy](./docs/bilingual-authoring.md)
- [Socratic Question Backlog](./docs/socratic-question-backlog-en.md)
- [Repository Hygiene](./docs/repository-hygiene.md)
- [Taxonomy](./references/taxonomy.md)
- [Routing Policy](./references/routing-policy.md)

## Verification

CI runs:
- schema and asset validation;
- route resolution checks;
- forbidden-path governance checks;
- Socratic-question TODO coverage checks;
- fixture suite checks;
- unit tests;
- internal link checks.

## Community Loop

If you want to improve this repository, the highest-value contribution is often not a new file. It is a precise objection.

Open an issue when you can say one of these clearly:
- "This claim breaks in real production."
- "This route chooses the wrong protocol."
- "This rubric misses a professional failure mode."
- "This audience or industry assumption is outdated."
- "This learning path sounds right but fails in teaching practice."

Start here:
- [Community Feedback Loop](./docs/community-feedback-loop.md)
- [Community Triage Loop](./docs/community-triage-loop.md)
- [Contributing Guide](./CONTRIBUTING.md)
