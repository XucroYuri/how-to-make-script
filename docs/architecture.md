# Architecture

## Core Idea

This repository separates reusable screenplay intelligence into four layers:

1. `knowledge/` stores durable theory and craft fragments.
2. `schemas/` define the machine-checked contracts for structured assets.
3. `skills/` provide thin orchestration entrypoints for agents.
4. `scripts/` and `tests/` keep the repository verifiable.

The repo is intentionally opinionated:
- the knowledge layer is the source of truth;
- skills are routing and composition wrappers;
- fixtures and tests enforce that routes stay stable;
- additive growth is preferred over reorganizing published IDs.

The orchestration layer now carries a bounded reality-grounding rule:
- audience lens;
- industry and commissioning lens;
- platform and release lens;
- writer development lens;
- historical evolution lens.

These lenses are loaded only when they change route choice or output quality.

The consequence is that agents should not read the whole repository by default. They should enter through a route, then load one protocol, its linked atoms, and one rubric.

## Why A Monorepo

A single repository makes it possible to evolve:
- shared taxonomies;
- routing rules;
- linked knowledge atoms;
- cross-skill fixtures;
- validation tooling;
- open source documentation

without version drift between separate repositories.

This also keeps narrative, commercial, and interactive logic from drifting into separate prompt silos.
It also prevents pure craft outputs from drifting away from audience demand and production constraints.

## Design Constraints
- Research-first, not UI-first.
- Human-readable first, but machine-validated.
- Stable IDs and additive evolution.
- Explicit routing over ad-hoc prompt accumulation.
- A route should be explainable as `intent x medium x stage x output x constraints`.
- Constraints must support real-world parameters such as audience need state, commissioning context, business model, release logic, and writer maturity.
- Every asset type should be independently lintable.
- Thin skills should stay operational while theory stays centralized in `knowledge/`.

## Build Philosophy

The repository should be able to expand indefinitely by appending:
- new atoms;
- new protocols;
- new rubrics;
- new fixtures;
- new skills;
- new media and genre packs

without breaking existing consumers.
