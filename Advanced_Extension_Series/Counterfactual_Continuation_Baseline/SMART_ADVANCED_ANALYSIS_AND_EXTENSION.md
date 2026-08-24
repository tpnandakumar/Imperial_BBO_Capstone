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

For Function 2, the strongest observed point lies between weaker neighbours at first-coordinate values `0.695000`, `0.690000` and `0.685000` while the second coordinate remains `0.950000`. A local quadratic interpolation places the estimated stationary point at approximately `0.6894136686090656`, giving the six-decimal research candidate `0.689414`.

Function 3 improved across the final local sequence and therefore supports one further controlled step to `0.860000,0.140000,0.860000`.

Function 5 remained productive near the boundary. The extension therefore reduces only the first coordinate to `0.080000` while fixing the remaining coordinates at `1.000000`.

Function 6 requires replication before directional movement because the same recorded coordinate produced different outputs across repeated evaluations.

## Stopping rule

Further querying would cease when a local bracket is resolved, successive improvements become negligible, repeated best points remain stable, response variability is characterised sufficiently to distinguish noise from movement, or the expected information value of another query falls below the value of retaining the strongest verified point.

This baseline is post-capstone evidence and is retained because it documents the reasoning that motivated the later SOC framework.