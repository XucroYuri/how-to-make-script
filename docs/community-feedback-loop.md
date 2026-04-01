# Community Feedback Loop

This repository wants more than bug reports. It wants challenge.

The best community contribution here is a well-argued disagreement: a theory rebuttal, a field report that breaks an assumption, a route failure with a reproducible example, or a professional objection that says “this looks elegant, but it will fail in practice.”

## What We Want

Useful feedback includes:

- issue reports with concrete reproduction steps;
- theory rebuttals with counterexamples;
- field reports from real writing, development, or production work;
- route failures where the current `intent x medium x stage x output x constraints` mapping is wrong;
- missing cases that are not covered by the current taxonomy or workflows;
- professional objections that explain why a rule is too weak, too broad, or too naive;
- counterexamples that show where the repository’s guidance stops working.

## What Feedback Becomes

Every good challenge should be converted into one of these repository assets:

- a new `knowledge_atom` when the issue is a missing judgment point;
- a new `workflow_protocol` when the issue is a missing decision sequence;
- a new `evaluation_rubric` when the issue is a vague or miscalibrated quality check;
- a new `example_fixture` when the issue is route stability or regression behavior;
- a docs update when the issue is explanation, framing, or onboarding;
- a governance update when the issue changes contribution rules, routing policy, or safety boundaries.

## Feedback Loop

1. A contributor opens an issue, PR, or discussion with evidence.
2. Maintainers classify it as a knowledge gap, route failure, rubric gap, fixture gap, or governance gap.
3. The team confirms whether the problem is real, ambiguous, or already covered elsewhere.
4. The gap is encoded into the smallest asset type that can hold it.
5. The new asset gets links, tests, or fixtures so the same problem does not reappear silently.
6. The original issue is closed only after the repository has absorbed the lesson.

## Maintainer Response Rules

- Treat disagreement as a contribution unless it is hostile or unsupported.
- Ask for evidence before asking for elegance.
- Prefer “show me where this fails” over “I feel this is wrong.”
- If the feedback is correct but too broad, narrow it into a concrete asset.
- If the feedback is useful but incomplete, keep the issue open and label the missing evidence.
- If the feedback is a counterexample, preserve it even when the main rule stays unchanged.

## Community Signals To Encourage

- “This route is wrong because the output contract does not match the medium.”
- “This rubric misses a failure mode I see in actual development work.”
- “This rule is correct for feature films but breaks in short drama.”
- “This example is strong, but it hides the real tradeoff.”
- “This theory should be split into two atoms because the decisions are different.”

## Related Docs

- [Community Triage Loop](./community-triage-loop.md)
- [Socratic Question Backlog](./socratic-question-backlog.md)
- [Content Model](./content-model.md)
- [Community Feedback Loop](./community-feedback-loop-zh.md)

