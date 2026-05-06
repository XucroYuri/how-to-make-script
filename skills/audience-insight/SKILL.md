---
name: audience-insight
description: Use when the user needs a concrete audience-fit diagnosis or target-segment note before drafting.
---

# Audience Insight

Use this skill to convert broad audience assumptions into a testable audience-fit note.

## Workflow
1. Identify the primary audience segment and consumption context.
2. Translate audience need state into narrative, commercial, or interactive demand signals.
3. Surface mismatch risks between intent and expected audience payoff.
4. Return one actionable audience fit note with revision priorities.

## Output Contract
- `audience_fit_note`: a compact note with audience segment, need state, expected payoff, and fit risks.
- Include one primary segment and no more than one secondary segment.
- Make revision actions specific enough to change structure, scene design, or message strategy.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask one activating question only: "Who are you most afraid of losing in the first five minutes — and why?" Do not output a full audience framework. Let one concrete answer lead.

**When `source = discover`:**
Surface the gap between who the writer *thinks* the audience is and who the story is actually calling to. Offer two contrasting audience frames; do not converge to one.

**When `source = construct`:**
Apply the full audience-fit workflow: segment → need state → payoff alignment → mismatch risks. Make revision actions specific enough to change structure or scene sequence.

**When `focus = audience`:**
This is the primary activation context. Load `ka.audience-need-state` and `ka.platform-attention-economy` as the first priority bundle.

**When `focus = character`:**
Translate character-layer work into audience-perception questions: "When this character withholds information, does the audience track the gap or feel confused?"

## References
- `wp.audience-fit-note`
- `rb.audience-fit`
- `ka.audience-need-state`
- `ka.commissioning-fit`
- `ka.cross-protocol-referral-edges`
- `ka.pacing-rhythm`
- `ka.platform-attention-economy`
- `ka.platform-douyin`
- `ka.platform-reels`
