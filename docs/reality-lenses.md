# Reality Lenses

This repository does not only model screenplay craft. It also needs to model the real-world conditions that shape what scripts get developed, trained, commissioned, purchased, scheduled, rewritten, and ultimately watched.

Use these lenses when a request is not just "write the story" but "write a story that can survive contact with audiences, training pipelines, and production reality."

## Lenses

### Audience and Attention
Load this lens when the request involves audience fit, hook strength, retention, platform behavior, or "who is this really for?"

What it changes:
- premise framing;
- opening pressure;
- scene density;
- emotional pacing;
- whether the script should optimize for streaming, social, broadcast, theatrical, or interactive use.

What it prevents:
- writing for a generic viewer who does not exist;
- assuming attention is stable across platforms;
- treating pace, hook, and payoff as medium-neutral.

### Industry and Commissioning
Load this lens when the request involves staffing, development rooms, writer-producer constraints, platform briefs, deliverables, or "what will actually get made?"

What it changes:
- format choice;
- episode sizing;
- room-aware outline depth;
- rewrite priorities;
- whether the output needs to be production-friendly or pitch-friendly.

What it prevents:
- generating elegant text that ignores commissioning logic;
- hiding labor assumptions inside the story layer;
- treating AI output as if it were already industry-ready.

### Writer Development
Load this lens when the request is about learning screenwriting, teaching screenwriting, onboarding a junior writer, building skill progression, or diagnosing a writer's growth bottleneck.

What it changes:
- lesson order;
- practice sequencing;
- feedback structure;
- exercise design;
- the difference between concept understanding and repeatable craft.

What it prevents:
- flattening screenwriting into a single "prompt and output" event;
- teaching structure before the learner can observe scene function;
- confusing taste with trainable skill.

### History and Archive
Load this lens when the request needs historical comparison, lineage, archival research, or "how did this form evolve?"

What it changes:
- reference selection;
- analog choice;
- period-specific expectations;
- how the system treats old models, old formats, and old production assumptions.

What it prevents:
- treating current practice as timeless;
- copying classic structures without noticing what industrial conditions made them work;
- using history as decoration instead of evidence.

### Platform Attention Ecology
Load this lens when the script is meant for social video, short drama, branded content, trailers, or any format where attention is fragmented and distribution is platform-shaped.

What it changes:
- opening speed;
- message singularity;
- visual clarity;
- compression ratio;
- CTA or next-step pressure.

What it prevents:
- writing a feature-film opening for a 15-second slot;
- assuming one script shape works across every surface;
- burying the core message under extra plot.

## When To Load

Use a reality lens whenever the user asks for one of the following:
- audience research;
- genre positioning;
- platform adaptation;
- industry-facing development notes;
- curriculum or training design;
- rewrite diagnosis that mentions market fit, fatigue, or "this does not feel current";
- historical comparison or research.

If the user request is purely internal craft generation, load only the lenses that change the route. Do not attach all of them by default.

## Decisions These Lenses Influence

- whether a premise is good enough for development;
- which medium is the right container;
- how much information should appear in the first scene;
- whether the story should optimize for retention, prestige, conversion, or participation;
- how much room the format allows for character work versus forward motion;
- whether a rewrite should focus on craft, audience fit, or production fit first;
- whether a learning path should train concept, scene, or rewrite skill first.

## Failure Modes Prevented

- writing against the wrong audience model;
- confusing current platform habit with permanent audience desire;
- using industry language without understanding real commissioning constraints;
- overfitting training advice to one writer's personality;
- treating history as trivia;
- assuming AI can replace the development process instead of supporting it;
- confusing "good prose" with "shippable screenplay."

## Inference Policy

Some claims in this repository are direct source signals. Others are inferences from those signals.

Examples:
- "Streaming and social platforms now dominate attention" is a source-backed signal.
- "Scripts need stronger opening compression on short-form surfaces" is an inference from that signal.
- "Writers need staged practice loops" is an inference from the education sources, not a verbatim claim.

When this skill uses a reality lens, it should be able to say which part is source-backed and which part is an operational inference.
