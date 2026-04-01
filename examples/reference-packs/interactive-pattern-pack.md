# Interactive Pattern Pack

This pack is synthetic and callable. It is meant to help an agent recognize branching and game-narrative situations, not to define the only good way to write interactive content.

## Classification Axes

- `choice_consequence`: cosmetic, stateful, irreversible, or mixed.
- `branch_shape`: shallow fork, braid, loop, hub-and-spoke, or delayed merge.
- `player_need`: agency, deduction, romance, mastery, status, or exploration.
- `state_model`: relationship, resource, reputation, time, memory, or faction control.
- `replay_behavior`: single run, repeat run, route contrast, or puzzle revisit.
- `integration_pressure`: UI, save system, quest flow, pacing, or content budget.

## Scenario I01: Branching Mystery With Irreversible Evidence

When to use: the player is solving a mystery and each choice should change what can still be known later.

Creative problem: make every branch alter evidence, not just flavor text.

Strong fragment:

```text
CHOICE:
1. Open the evidence locker now.
2. Leave it sealed and tail the witness.

STATE:
If locker is opened, the witness loses trust.
If the witness is tailed, the locker remains a later risk.
```

Why this works: the choice changes access, trust, and future information, so the branch has material weight.

Weaker fragment:

```text
CHOICE:
1. Investigate the locker.
2. Investigate the hallway.

RESULT:
Both paths reveal the same clue with different adjectives.
```

Why the weaker version fails: it changes presentation, not possibility.

Non-dogma note: some mysteries should braid back faster if the format values pacing over branching depth.

## Scenario I02: Moral Survival Under Pressure

When to use: the story asks the player to choose under scarcity, and the point is consequence, not optimization.

Creative problem: make both options carry a cost that matters in the fiction.

Strong fragment:

```text
CHOICE:
1. Share the last battery with the injured scout.
2. Keep the battery and risk the scout's loss.

STATE:
Sharing raises trust but lowers escape capacity.
Keeping it preserves mobility but fractures the group.
```

Why this works: the decision is not moral wallpaper; it changes survival math and group dynamics.

Weaker fragment:

```text
CHOICE:
1. Be kind.
2. Be smart.

RESULT:
Either way, the next scene plays the same.
```

Why the weaker version fails: the labels are moral, but the system is not reactive.

Non-dogma note: not every interactive choice needs tragedy; some should reward competence or curiosity instead.

## Scenario I03: Relationship-Driven Visual Novel

When to use: the main pleasure is emotional alignment, and the branches should change intimacy, trust, or confession timing.

Creative problem: make dialogue choice alter tone and closeness, not just route selection.

Strong fragment:

```text
CHOICE:
1. "I was wrong, and I know why."
2. "You overreacted, but I can stay."

STATE:
Path 1 unlocks honest follow-up scenes.
Path 2 keeps the route open, but the other character stays guarded.
```

Why this works: the branch changes relationship temperature and future access to vulnerability.

Weaker fragment:

```text
CHOICE:
1. Nice reply.
2. Slightly colder reply.

RESULT:
Same affection score, same next scene.
```

Why the weaker version fails: the choice is cosmetic and the emotional engine stays flat.

Non-dogma note: some visual novels benefit from subtle rather than dramatic divergence, as long as the emotional state still moves.

## Scenario I04: Quest With Gating and Backtracking

When to use: the player explores a world where progress is controlled by tools, knowledge, or unlocked access.

Creative problem: make traversal teach something, not just consume time.

Strong fragment:

```text
BEAT 1: The player reaches the locked transit door.
BEAT 2: A side route reveals the maintenance code.
BEAT 3: Returning to the door opens a larger route and a new faction question.
```

Why this works: the backtrack is not dead time; it recontextualizes the hub and changes the next decision.

Weaker fragment:

```text
BEAT 1: The player is blocked.
BEAT 2: The player is blocked again.
BEAT 3: The player finally proceeds with no new meaning.
```

Why the weaker version fails: gating becomes delay instead of transformation.

Non-dogma note: some quest structures should be linear if the budget or platform cannot support meaningful re-entry.

## Scenario I05: Faction Reputation and Political Alignment

When to use: the interactive system needs more than branch choice; it needs long-horizon social consequences.

Creative problem: show that alliances shift future available scenes, not just end-state scores.

Strong fragment:

```text
CHOICE:
1. Hide the raid from the council.
2. Expose the raid and risk retaliation.

STATE:
Hiding preserves access to one ally.
Exposing unlocks a new investigative branch but closes a safe harbor.
```

Why this works: reputation becomes a route manager, not a decorative counter.

Weaker fragment:

```text
CHOICE:
1. Council +10
2. Council -10

RESULT:
The number changes, but nothing else does.
```

Why the weaker version fails: a score without route impact is not narrative state.

Non-dogma note: reputation is only useful if the player can feel it, not merely inspect it.

## Scenario I06: Replay Loop With Delayed Revelation

When to use: the design wants repeat play, route contrast, or a story that gets meaning from second-run knowledge.

Creative problem: make the first run incomplete in a productive way.

Strong fragment:

```text
RUN 1:
The player saves the engineer and never learns who sabotaged the gate.

RUN 2:
With the engineer gone, a hidden log appears in the evac tunnel.
The same scene now reads as concealment, not failure.
```

Why this works: replay is rewarded with new interpretation, not just extra scenes.

Weaker fragment:

```text
RUN 1:
You missed content.

RUN 2:
You see the same content with a different label.
```

Why the weaker version fails: it punishes the first run without adding interpretive payoff.

Non-dogma note: replay loops should be intentional, not a workaround for underwritten branching.
