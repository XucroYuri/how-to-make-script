# Screenplay To Video Bridge

This repository is still screenplay-first. It is not turning into a general video-generation toolbox.

But screenplay work increasingly has to travel downstream into:
- previz;
- text-to-video generation;
- concept clips;
- ad prototypes;
- visual proof-of-concept material.

That creates a real translation problem.

## The Problem

A screenplay scene and a video-generation brief are not the same container.

The screenplay carries:
- dramatic purpose;
- character pressure;
- narrative context;
- scene function.

The video-generation brief carries:
- clip-scale action;
- shot logic;
- timing;
- invariants;
- avoid rules;
- runtime-facing execution constraints.

If the repo ignores this distinction, agents either overfit to screenplay logic and produce unusable visual briefs, or overfit to prompt-writing habits and destroy the dramatic purpose of the scene.

## What The Bridge Must Preserve

- the dramatic function of the source scene;
- the minimum non-negotiable beat or action proof;
- a bounded control level;
- explicit invariants and avoid rules;
- honesty about what belongs to the screenplay and what belongs to the downstream visual container.

## What The Bridge Must Avoid

- copying whole scene text into a prompt-shaped blob;
- treating a short clip like a whole dramatic scene;
- adding every camera, sound, and aesthetic idea at once;
- turning model CLI details into the main artifact.

## Related Assets

- `screen_to_video_brief`
- `ka.screenplay-to-video-boundary`
- `ka.video-generation-shot-economy`
- `ka.prompt-delegation-levels`
- `wp.screen-to-video-brief`
- `rb.screen-to-video-brief`

