# Project Surface Architecture

This repository now models one more layer that earlier versions only implied:

- not just what to write;
- not just how to route;
- not just who collaborates;
- but where creative truth lives and how work moves across surfaces.

## Why This Matters

The repo was already strong on:
- route selection;
- bounded loading;
- output contracts;
- team modes;
- subagent casts and dispatch plans.

What it was still weaker on was long-horizon project surfaces:
- where humans should edit;
- what runtime artifacts should be compiled;
- how packets should be assembled and inspected;
- where review and export should live.

The external reference projects made this gap obvious.

## Surface Layers

### Canonical Source

Artifacts that humans or planning agents are allowed to edit directly:
- story core;
- world anchors;
- outline truth;
- character anchors;
- brand or commissioning anchors;
- continuity anchors.

### Runtime State

Derived artifacts used to run the current phase:
- local workflow state;
- scene or chapter state mirrors;
- packet compilation outputs;
- lane summaries;
- telemetry and traces.

These should be regenerable by default.

### Packet Layer

The bounded packet that feeds one concrete action:
- selected truth sources;
- selected local state;
- rules stack;
- handoff summary;
- current task intent;
- stop condition.

### Review Surfaces

Artifacts used for checking drift before delivery:
- craft review;
- continuity review;
- compliance review;
- downstream-surface review;
- release or export readiness.

### Export Surfaces

Artifacts prepared for downstream humans or tools:
- readable treatment or script packets;
- production-facing scene or sequence bundles;
- video-bridge or previz bundles;
- archive or sync-safe packets.

## Design Rule

Project surfaces should stay explicit, not implicit.

If the repo eventually grows a runtime planner, it should not invent these layers later.
It should inherit them from the project-surface layer defined here.

## Linked Contracts

- [`wp.project-surface-map`](../knowledge/20-workflows/wp-project-surface-map.md)
- [`rb.project-surface-map`](../knowledge/60-rubrics/rb-project-surface-map.md)
- [`docs/reference-project-lessons.md`](./reference-project-lessons.md)
