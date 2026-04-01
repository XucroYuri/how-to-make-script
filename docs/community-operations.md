# Community Operations

This repository does not want a quiet issue tracker. It wants a high-signal disagreement machine.

The goal is not to collect praise. The goal is to turn objections, counterexamples, and field evidence into better screenplay knowledge, better routing, and better human-in-the-loop habits.

## Operating Targets

- Increase the share of community inputs that contain a concrete challenge, counterexample, or field report.
- Keep open-ended disagreement in Discussions until it is scoped enough to change the repository.
- Convert repeated objections into assets, fixtures, or governance changes instead of re-litigating them forever.
- Make it easy for non-code contributors to improve the project without pretending they need to submit code first.

## Feedback Surface Ladder

Use the lightest surface that still fits the problem:

1. `Q&A` discussion:
   Use when the person is still trying to understand a claim, route, or asset before challenging it.
2. `General` discussion:
   Use when the disagreement is real but still broad, comparative, or exploratory.
3. `Ideas` discussion:
   Use when the person sees a missing path, new workflow, or better community process but the change is not issue-shaped yet.
4. `Show and tell` discussion:
   Use when someone has a field report, case study, or "we tried this and here is what happened" contribution.
5. Issue form:
   Use when the change target is concrete enough to name a file, claim, route, rubric, or governance rule.
6. Pull request:
   Use when the contributor can already encode the lesson into repository assets.

This follows GitHub's own recommendation: use Discussions for brainstorming and broader feedback, then move the conversation to an issue when the work is ready to be scoped.

## Maintainer Cadence

These are targets, not hard promises:

- Within 72 hours:
  add a `type:*` label or `discussion-first`, and decide whether the surface is correct.
- Within 7 days:
  add a `status:*` label, request missing evidence, or convert the thread to a better surface.
- Weekly:
  review open `needs-triage`, `needs-practitioner-input`, and `needs-counterexample` threads.
- Monthly:
  publish one short community digest or announcement that summarizes what objections changed the repo.
- Quarterly:
  review labels, forms, unanswered discussions, and moderation load.

## Maintainer Roles

- `maintainer`: owns policy, merges changes, and makes final scope calls.
- `triage steward`: classifies feedback, requests missing evidence, and keeps threads moving.
- `field-note curator`: looks for real-world reports that should become atoms, fixtures, or case notes.
- `fixture shepherd`: turns repeated failures into regression fixtures.
- `discussion moderator`: keeps conversation constructive and converts early-stage issues into discussions when needed.

GitHub Discussions supports promoting trusted contributors to higher moderation responsibility. Use that path when a contributor repeatedly improves the repo through high-signal answers, respectful disagreement, or disciplined triage help.

## Default Conversation Moves

Encourage maintainers and contributors to make these moves explicit:

- ask for the exact claim or route being challenged;
- ask for one concrete counterexample before debating abstractions;
- label a thread `discussion-first` if the lesson is real but not scoped;
- convert a discussion into an issue once the asset target is clear;
- convert an issue into a discussion if the work is still exploratory;
- mark answered Q&A threads so useful clarifications become easier to browse;
- close only after the lesson is encoded, deferred with reason, or rejected with scope rationale.

## Seeded Community Rituals

- Keep one standing thread for open counterexamples and field notes.
- Keep one standing thread for rival routes or missing workflow families.
- In PR review, ask reviewers what assumption or field context should be used to break the change.
- When merging a scope correction, link back to the discussion or issue that forced the narrowing.

## Useful Metrics

- discussion-to-issue conversion count;
- issue-to-asset conversion count;
- open `needs-practitioner-input` threads;
- open `needs-second-field-report` threads;
- median time to first maintainer classification;
- count of merged PRs that reference an originating objection.

## Related Files

- [Community Feedback Loop](./community-feedback-loop.md)
- [Community Triage Loop](./community-triage-loop.md)
- [Contributing](../CONTRIBUTING.md)
- [Discussion Surface Map](../references/discussion-surface-map.json)
- [Community Label Taxonomy](../references/community-label-taxonomy.json)
