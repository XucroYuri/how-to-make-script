# Community Triage Loop

This playbook is for maintainers and agents who need to turn community input into repository change without flattening dissent.

## Triage States

- `new`: the issue has not been classified yet.
- `needs-evidence`: the claim is plausible but not yet grounded.
- `reproducing`: a route, failure, or counterexample is being tested.
- `routed`: the feedback has been mapped to an asset type.
- `encoded`: the repository has been updated.
- `deferred`: the issue is valid but blocked by scope, evidence, or timing.
- `rejected`: the issue is not actionable, unsupported, or out of scope.

## Classification Questions

1. Is this a route failure, a theory rebuttal, a field report, a missing case, or a governance issue?
2. Does the feedback change a route, a contract, a rubric, or a taxonomy entry?
3. Can the issue be reproduced with an example, fixture, or source reference?
4. Is the right fix a new asset, a split asset, or a policy update?
5. Does the issue expose a stable gap or only a one-off preference conflict?

## Maintainer Response Rules

- Acknowledge disagreement directly.
- Ask for a concrete example before debating abstractions.
- If the issue is valid, preserve the criticism even if the repo does not change immediately.
- If the issue is broad, narrow it into the smallest asset that can encode the lesson.
- If the issue is duplicated, merge it but keep the useful counterexample and link back.
- If the issue is blocked, explain what evidence would unblock it.

## Turn Feedback Into Assets

- `knowledge_atom` when the community found a missing decision rule or concept boundary.
- `workflow_protocol` when the community found a missing handoff, fallback, or stop condition.
- `evaluation_rubric` when the community found a vague or miscalibrated quality gate.
- `example_fixture` when the community found a route regression or ambiguous input pattern.
- `docs` when the community found a gap in explanation or onboarding.
- `governance` when the community found a hole in contribution policy, safety, or review norms.

## Triage Outputs

Every triaged issue should end with one of these outcomes:

- `convert`: create or update an asset.
- `split`: break one idea into multiple assets.
- `monitor`: keep the issue open for future evidence.
- `close-with-note`: the issue is acknowledged but not actionable now.
- `escalate`: the issue needs maintainer judgment or policy review.

## What Good Maintainer Replies Look Like

- “This is a valid route failure. Please add a fixture.”
- “The objection is useful, but we need a counterexample to encode it.”
- “You are right that the rubric misses this failure mode. We will split the rule.”
- “This is a platform-specific case, so it should become a separate protocol.”
- “The feedback is real, but we need one more field report before changing governance.”

## Related Docs

- [Community Feedback Loop](./community-feedback-loop.md)
- [Community Feedback Loop - Chinese](./community-feedback-loop-zh.md)
- [Content Model](./content-model.md)
- [Repository Hygiene](./repository-hygiene.md)

