# Private Reference Distillation Policy

This repository may learn from private working notes during authoring, but it must not depend on them after publication.

## Rule

Private references can be used only as temporary distillation inputs.
They cannot become public requirements, hidden dependencies, or inaccessible citations.

## What Is Allowed

- extracting reusable mechanisms from private notes;
- rewriting those mechanisms as public `knowledge_atom`, `workflow_protocol`, `evaluation_rubric`, or `example_fixture` assets;
- replacing private examples with synthetic public teaching examples;
- adding public source maps when a method family has useful open references.

## What Is Not Allowed

- linking to local filesystem paths outside the repository;
- citing private notes as if they were public authorities;
- copying private prompt shells, workflow scaffolds, or workshop templates into public contracts without abstraction;
- leaving the repo in a state where an agent must read a private note to understand a public asset.

## Conversion Standard

When a private note influences the repo, the public version should do all of the following:

1. state the reusable mechanism, not the local note title;
2. separate durable rule from temporary example;
3. remove tool-bound, person-bound, or local-environment-bound details;
4. mark the asset as `derived` or `synthesized` when that is more honest than pretending it is canon;
5. add scope limits, rival paths, or anti-patterns so the note does not fossilize into false universality.

## Public Source Preference

If a method family has public references, record them in a source map.
Those links are orientation aids, not proof that one method is universally correct.

## Failure Mode To Avoid

The main risk is “secret source of truth” drift:

- the public repo looks complete;
- the real logic still lives in a private vault;
- future contributors cannot audit or extend the method honestly.

This repository should always prefer explicit public abstractions over hidden private authority.
