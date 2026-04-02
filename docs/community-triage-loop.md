# Community Triage Loop

This playbook is for maintainers and agents who need to turn community input into repository change while preserving dissent.

It assumes screenplay guidance is heuristic, bounded, contestable, and historically situated. Triage should therefore preserve viable rival paths when they exist, not force everything toward a single truth too early.

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
6. Is the issue really a false universal warning that should weaken the claim rather than replace it?
7. Does the issue call for a scope correction, and what part of the original claim still survives?
8. Did the repo converge too early and suppress multiple still-valid paths?
9. Is there more than one viable route, and should the repo preserve that plurality instead of collapsing it?

## Maintainer Response Rules

- Acknowledge disagreement directly.
- Ask for a concrete example before debating abstractions.
- If the issue is valid, preserve the criticism even if the repo does not change immediately.
- If the issue is broad, narrow it into the smallest asset that can encode the lesson.
- If the issue is duplicated, merge it but keep the useful counterexample and link back.
- If the issue is blocked, explain what evidence would unblock it.

## Channel Conversion Rules

- Convert an issue to a discussion when the change target is still broad, comparative, or exploratory.
- Convert a discussion to an issue when the target asset, route, rubric, or governance rule becomes concrete.
- Keep Q&A public and mark answers when a clarification becomes stable enough to help future contributors.
- When a contributor brings a real field note but not yet a scoped repository change, keep it in `Show and tell` until a stable lesson emerges.

## Labeling Guidance

Default labels and transitions should be predictable:

- use `type:*` to say what kind of signal this is;
- use `status:*` to say what maintainers are doing about it;
- use `kind:*` when the real pattern is counterexample, scope correction, boundary mismatch, or premature convergence;
- use `discussion-first` when the conversation is still too open for issue scope;
- use `needs-practitioner-input`, `needs-counterexample`, `needs-route-reproduction`, or `needs-second-field-report` to say what evidence is missing next.

See the full registry in [`../references/community-label-taxonomy.json`](../references/community-label-taxonomy.json).

## Response Cadence

- Within 72 hours: classify the thread or move it to a better channel.
- Within 7 days: add the relevant `status:*` label or request the missing evidence explicitly.
- Weekly: review stalled threads and decide whether they should be converted, encoded, deferred, or closed with note.
- Monthly: review which objection patterns keep recurring and should become fixtures, docs, or governance updates.

## Turn Feedback Into Assets

- `knowledge_atom` when the community found a missing decision rule or concept boundary.
- `workflow_protocol` when the community found a missing handoff, fallback, or stop condition.
- `evaluation_rubric` when the community found a vague or miscalibrated quality gate.
- `example_fixture` when the community found a route regression or ambiguous input pattern.
- `docs` when the community found a gap in explanation or onboarding.
- `governance` when the community found a hole in contribution policy, safety, or review norms.
- `boundary map` when the issue shows that a binary answer should really be split into hard-no, soft-risk, bold-safe, and defer-to-review zones.
- `scope correction` when the issue shows a rule should be narrowed, not simply deleted or defended.

## Triage Outputs

Every triaged issue should end with one of these outcomes:

- `convert`: create or update an asset.
- `split`: break one idea into multiple assets.
- `scope-correct`: keep the surviving core but narrow the rule and encode the failure context.
- `monitor`: keep the issue open for future evidence.
- `close-with-note`: the issue is acknowledged but not actionable now.
- `escalate`: the issue needs maintainer judgment or policy review.

## What Good Maintainer Replies Look Like

- “This is a valid route failure. Please add a fixture.”
- “The objection is useful, but we need a counterexample to encode it.”
- “You are right that the rubric misses this failure mode. We will split the rule.”
- “This is a platform-specific case, so it should become a separate protocol.”
- “The feedback is real, but we need one more field report before changing governance.”
- “This is not a total rejection of the rule; it is a scope correction.”
- “The current guidance converges too early. We should preserve multiple path options here.”

## Related Docs

- [Community Feedback Loop](./community-feedback-loop.md)
- [Community Feedback Loop - Chinese](./community-feedback-loop-zh.md)
- [Community Operations](./community-operations.md)
- [Epistemic Stance](./epistemic-stance.md)
- [Exploration vs Review](./exploration-vs-review.md)
- [Content Model](./content-model.md)
- [Repository Hygiene](./repository-hygiene.md)
