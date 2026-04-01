# Contributing

## Principles
- Keep the repository research-first: prefer stable knowledge assets over ad-hoc prompt dumps.
- Do not duplicate theory text across skills. Add or update knowledge atoms instead.
- Preserve stable IDs. Never rename a published ID; deprecate or supersede it.
- Prefer additive changes. New media, genres, or protocols should extend registries rather than rewrite existing contracts.
- Treat disagreement as a contribution type. Strong rebuttals, counterexamples, and field corrections are welcome when they are specific and evidence-based.
- Avoid universal claims unless you can defend their scope limits. Most screenplay guidance should be framed as context-bounded heuristics.

## Contribution Types
- New `knowledge_atom`
- New `workflow_protocol`
- New `evaluation_rubric`
- New `example_fixture`
- New or revised skill manifest / skill wrapper
- Validation tooling and test improvements
- Documentation, translation, and example improvements
- Theory rebuttals and counterexamples
- Route-failure reports and prompt-to-output mismatch reports
- Professional field reports from production, platform, brand, or writers' room practice
- Learning-friction reports from actual use of the repository

## Good First Contributions

If you are new to the repository, start with one narrow move:

- challenge one claim that feels too broad or too absolute;
- add one counterexample, field note, or regional caveat;
- improve one example, one README path, or one rubric explanation;
- reproduce one route mismatch and turn it into a fixture candidate;
- improve one translation or bilingual wording problem that affects usability.

Newcomers do not need to start by adding a full new workflow. Small, concrete corrections are preferred over grand rewrites.

## Human-In-The-Loop Feedback

This repository is designed to improve through challenge, not through passive praise.

High-value issues include:
- a claim in the repo that fails under real production conditions;
- a protocol that routes correctly but produces the wrong artifact shape;
- a rubric that misses an obvious professional failure mode;
- an industry or audience assumption that is outdated, regional, or too generic;
- a learning path that sounds correct but fails in actual training use.

When opening an issue or pull request, try to make one of these moves explicit:
- `challenge`: "This claim is too broad / wrong / unstable."
- `counterexample`: "This breaks on this project, medium, audience, or market."
- `field evidence`: "Here is what happened in actual practice."
- `route failure`: "The system loaded the wrong protocol or output contract."
- `learning friction`: "This was theoretically clear but failed as a teaching or writing tool."
- `premature convergence`: "Multiple viable paths existed, but guidance forced one too early."
- `boundary mismatch`: "A soft preference was treated as a hard boundary (or vice versa)."
- `scope correction`: "This claim still has a useful core, but its current scope is too broad."

The project prefers structured dissent over vague approval. If you disagree, say what you disagree with, where it breaks, what evidence you have, and what asset should change as a result.

## Feedback Surface Ladder

Use the lightest surface that fits the current state of your thought:

- `Q&A` discussion when you are still clarifying a claim, route, or contribution path.
- `General` discussion when the disagreement is real but still exploratory or comparative.
- `Ideas` discussion when you see a missing workflow, rival path, or community-process improvement that is not issue-shaped yet.
- `Show and tell` discussion when you have field notes, case studies, or usage evidence from real practice.
- Issue forms when you can point to the exact file, claim, route, rubric, or governance rule that should change.
- Pull requests when you already know how to encode the lesson into repository assets.

The repository intentionally uses Discussions to keep open-ended disagreement public and searchable before it is narrowed into an issue.

## Issue Quality Standard

A strong issue usually includes:
- the exact claim, route, rubric, or file being challenged;
- the context where it failed;
- one concrete example or counterexample;
- if applicable, what part of the original claim still survives after correction;
- the proposed correction scope: atom, protocol, rubric, fixture, docs, or governance;
- confidence level and uncertainty if the evidence is partial.

Low-signal reports are still useful, but maintainers may ask for narrowing before acting on them.

## Maintainer Response Targets

These are targets, not guarantees:

- Within 72 hours:
  classify new issues or discussions with a `type:*` label or `discussion-first`.
- Within 7 days:
  add a `status:*` label, request missing evidence, or move the thread to a better surface.
- Weekly:
  review open `needs-triage`, `needs-practitioner-input`, and `needs-counterexample` threads.
- Monthly:
  summarize which objections, counterexamples, or field reports changed the repository.

If a report is still too broad, maintainers should narrow it rather than let it stall silently.

## Content Requirements
- Every structured asset must satisfy its schema in [`schemas/`](schemas).
- Every new ID must be unique and follow the policy in [`references/id-policy.md`](references/id-policy.md).
- Every cross-link must resolve to a real asset ID.
- Every protocol must declare input and output contracts.
- Every rubric must include hard-fail rules and rewrite actions.
- Reference-pattern examples must be original synthetic teaching samples, not quoted or close-imitation script passages.
- Reference-pattern contributions must include a failure contrast and a non-dogma note, not just a preferred sample.

## Local Verification

Run all of the following before opening a pull request:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_assets.py
python3 scripts/check_routes.py
python3 scripts/check_route_overlaps.py
python3 scripts/check_community_surfaces.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_paths.py
python3 scripts/check_question_todos.py
python3 scripts/run_fixture_suite.py
```

## Review Expectations

Maintainers and contributors should review with these defaults:
- challenge the claim, not the person;
- prefer "show me where this fails" over "I don't like this";
- treat unresolved uncertainty as a valid review outcome;
- turn repeated objections into fixtures, rubrics, or docs instead of repeating them forever in comments.
- when a claim is weakened but not destroyed, ask whether a scope correction would be more accurate than deletion.
- if a thread is still exploratory, move it to Discussions instead of forcing premature issue scope.
- if a contributor repeatedly provides high-signal evidence or answers, consider inviting them into broader triage or moderation help.

If your pull request changes a claim, route, or rubric, explicitly state what kind of disagreement you want from reviewers.

## Forbidden Local Workspace State
- Never commit `.obsidian/` into the repository.
- The repository treats `.obsidian/` as forbidden both in the current index and in Git history.
- If a branch ever contains accidental `.obsidian/` commits before publication, rewrite the branch history before pushing.


## Style
- Chinese is the primary repository language for knowledge content.
- English summaries are encouraged for top-level docs and outward-facing metadata.
- Keep Markdown concise, structured, and reusable by both humans and agents.
- Use JSON frontmatter blocks for structured Markdown assets so the tooling stays dependency-light.
