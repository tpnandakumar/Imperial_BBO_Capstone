# Smart Advanced Analysis and Extension

## Purpose

The thirteen-round capstone is complete, but the final results raise a useful additional question: if another optimisation opportunity were available, should the search continue?

The answer is **yes, selectively**. Round 13 still produced new overall best values for Functions 3, 5 and 6. Function 2 declined from its Week 12 peak, which suggests that its local neighbourhood remains unresolved. Functions 1, 4, 7 and 8 repeatedly retained or recovered their strongest verified values, so routine movement away from those points has a lower expected value.

This extension does not claim that a fourteenth round exists and it does not invent any further outputs. It develops a counterfactual next-step policy from the verified thirteen-round history.

## Decision rule

A further query is justified when at least one of the following is present:

1. the latest round produced a new best and the improvement direction remains unresolved;
2. a recent local move deteriorated after a stronger neighbouring observation, leaving a plausible local optimum between tested points;
3. repeated evaluation at the same coordinate gives materially different outputs, so response uncertainty remains unresolved;
4. the expected information gained from another query is greater than the value of simply repeating a stable best point.

Where none of these conditions is present, the preferred action is to stop routine optimisation and retain the strongest verified coordinate.

## Function-specific continuation decision

| Function | Continue? | Evidence | Extension action |
| --- | --- | --- | --- |
| F1 | No routine search | Best value reproduced repeatedly at `0.600000,0.600000` | Retain confirmed point |
| F2 | Yes | Week 12 peaked at `0.690000,0.950000`; Week 13 at `0.685000,0.950000` declined | Interpolate inside the local bracket |
| F3 | Yes | Week 13 produced a new best at `0.855000,0.145000,0.855000` | One small directional continuation |
| F4 | No routine search | Historical best recovered and retained at `0.600000,0.430000,0.420000,0.250000` | Retain confirmed point |
| F5 | Yes, cautiously | Week 11, 12 and 13 each strengthened the boundary trend | Continue only the first coordinate while holding the upper-bound coordinates fixed |
| F6 | Yes, but as a repeatability experiment | The same coordinate returned different values across repeated evaluations | Replicate before changing direction |
| F7 | No routine search | Historical best recovered and retained | Retain confirmed point |
| F8 | No routine search | Best value repeatedly reproduced | Retain confirmed point |

## Proposed counterfactual Round 14

If the competition required one further full submission, the following set would be the preferred **research extension**, not a claimed competition result:

```text
Function 1
0.600000-0.600000

Function 2
0.689414-0.950000

Function 3
0.860000-0.140000-0.860000

Function 4
0.600000-0.430000-0.420000-0.250000

Function 5
0.080000-1.000000-1.000000-1.000000

Function 6
0.700000-0.200000-0.700000-0.700000-0.200000

Function 7
0.040000-0.480000-0.260000-0.220000-0.420000-0.740000

Function 8
0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000
```

## Why these values were chosen

### Function 2: local interpolation rather than further extrapolation

The three most relevant observations with the second coordinate fixed at `0.950000` are:

| First coordinate | Output |
| ---: | ---: |
| `0.695000` | `0.5848554940277205` |
| `0.690000` | `0.7335252043269003` |
| `0.685000` | `0.6413430885133908` |

The strongest observed point lies between two weaker neighbours. A local quadratic interpolation through these three observations places the estimated stationary point at approximately `0.6894136686090656`. Rounded only for a hypothetical six-decimal submission, this becomes `0.689414`.

This is not evidence that `0.689414` is the true optimum. It is a disciplined interpolation inside an observed bracket, which is preferable to continuing the unsuccessful move towards `0.685000`.

### Function 3: controlled continuation

Function 3 improved from `-0.06542982421105416` at `0.840000,0.160000,0.840000` to `-0.05985127532683556` at `0.850000,0.150000,0.850000`, then to `-0.05685061601567621` at `0.855000,0.145000,0.855000`.

The improvement remained positive at the end of the experiment. A further step of `0.005000` in the same coordinate pattern gives `0.860000,0.140000,0.860000`. The step remains deliberately small because the improvement between Weeks 12 and 13 was smaller than the preceding gain.

### Function 5: boundary continuation with one free coordinate

Function 5 reached new best values in each of the final three rounds:

- Week 11: `4411.0387356061765`
- Week 12: `4427.343995806448`
- Week 13: `4440.957216598753`

The last three coordinates are already effectively at the upper boundary. The remaining practical movement is therefore concentrated in the first coordinate. The hypothetical extension reduces it from `0.090000` to `0.080000` while holding the other three coordinates at `1.000000`.

This is a continuation experiment, not evidence that the lower first coordinate must improve the objective.

### Function 6: resolve response variability before directional optimisation

The coordinate `0.700000,0.200000,0.700000,0.700000,0.200000` was evaluated more than once and did not return one fixed value. That means a further directional move would mix two questions: whether the coordinate is good and whether the response is repeatable.

The preferred extension is therefore to repeat the same coordinate first. If repeated observations continue to vary, the next analytical stage would estimate the response distribution and compare nearby points using replicated measurements rather than single observations.

## Relation to reinforcement learning and bandit reasoning

This extension uses the later course material as a decision lens rather than forcing a literal Q table onto a sparse continuous search space.

The useful reinforcement learning idea is that each additional query should have an expected value. Multi-armed bandit reasoning sharpens the exploration versus exploitation decision. Functions 1, 4, 7 and 8 have low expected information gain from routine movement, while Functions 2, 3, 5 and 6 still contain unresolved reward or uncertainty structure.

A classical tabular Q-learning implementation is not well matched to this dataset because the state and action spaces are continuous and the number of observations is small. The more defensible extension is therefore a hybrid policy: local interpolation where a bracket exists, cautious directional continuation where improvement persists, boundary testing where the trend remains active, and replication where response variability is observed.

## Stopping rule

The extension also defines when optimisation should stop. Further querying would cease when:

- a local bracket has been resolved and additional movement reduces performance;
- successive improvements fall below a meaningful threshold and no unexplored nearby direction remains justified;
- repeated best points are stable and neighbouring tests do not improve them;
- response variability is characterised sufficiently to distinguish noise from directional improvement;
- the expected information value of another query is lower than the cost of using that query.

This is the final strategic lesson from the capstone. Optimisation is not complete merely because a round limit has been reached, and it should not continue merely because another query is available. The decision to continue or stop should itself be evidence based.