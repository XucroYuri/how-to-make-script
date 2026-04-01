# Agent Tiers

This repository keeps a small local fallback for delegation tiers so agent workflows do not depend on a missing external file.

## Tier Map

- `LOW`
  Use for targeted lookups, narrow edits, schema-safe additions, one-file doc changes, and fixture additions that do not affect architecture.

- `STANDARD`
  Use for normal repository work: new knowledge assets, route updates, skill-manifest changes, loading-policy edits, and verification integration across a few files.

- `THOROUGH`
  Use for architecture changes, route-family redesign, context-loading policy shifts, new asset families, or work that can create broad regression risk.

## Escalation Rules

- Escalate from `LOW` to `STANDARD` when a change crosses file families or affects routing.
- Escalate from `STANDARD` to `THOROUGH` when a change can alter multiple routes, loading behavior, or long-term repository semantics.
- Do not use `THOROUGH` for trivial edits just because the topic sounds important.

## Current Repo Guidance

- New docs only: usually `LOW`.
- New atom/protocol/rubric/skill family: usually `STANDARD`.
- Route-matrix redesign, taxonomy-axis changes, or loading-governance redesign: usually `THOROUGH`.
- Screenplay-oriented role suggestions live in [`screenplay-agent-roles.md`](./screenplay-agent-roles.md).
