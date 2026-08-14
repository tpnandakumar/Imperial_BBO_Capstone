# Week 12 Decision Record

## Purpose

This record explains how the verified Week 11 inputs and outputs were used to select the submitted Week 12 queries. The decision combined direct historical performance with the principal component analysis introduced in Module 23. PCA was considered as an analytical option and compared with the observed objective history for each function rather than being adopted automatically.

## Week 11 evidence

The verified Week 11 submission and returned outputs were:

| Function | Week 11 input | Week 11 output |
| --- | --- | ---: |
| Function 1 | `0.600000,0.600000` | `0.025559285339829783` |
| Function 2 | `0.695000,0.950000` | `0.5848554940277205` |
| Function 3 | `0.840000,0.160000,0.840000` | `-0.06542982421105416` |
| Function 4 | `0.620000,0.420000,0.440000,0.250000` | `-4.868852987697114` |
| Function 5 | `0.110000,0.998000,0.999900,0.999900` | `4411.0387356061765` |
| Function 6 | `0.720000,0.190000,0.700000,0.710000,0.150000` | `-0.7268715077444687` |
| Function 7 | `0.045000,0.485000,0.255000,0.220000,0.420000,0.745000` | `1.3579108517237013` |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` |

All eight functions improved relative to Week 10. Function 2 and Function 5 produced new verified best values. Function 1 and Function 8 reproduced earlier verified best values exactly.

## PCA evidence considered

The accumulated query history through Week 11 showed concentrated movement in the higher dimensional functions:

| Function | PC1 explained variance ratio | PC1 plus PC2 cumulative ratio | Components for at least 90 percent |
| --- | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9966917983027923` | 1 |
| Function 4 | `0.929457542635097` | `0.9990069305772716` | 1 |
| Function 5 | `0.9676115302998125` | `0.997726663010752` | 1 |
| Function 6 | `0.864773785020967` | `0.9866734368322968` | 2 |
| Function 7 | `0.8602299516486513` | `0.9692454132352497` | 2 |
| Function 8 | `0.9021092653998608` | `0.9666706798190747` | 1 |

These values describe the geometry of the submitted query trajectories. They do not prove that the principal directions are the directions of maximum objective improvement. The points were selected adaptively, so the principal components partly reflect the search strategy itself.

## Function by function decision

### Function 1

The Week 11 point `0.600000,0.600000` reproduced the earlier best value exactly. Direct repeatability evidence was stronger than any need for dimensional reduction in a two dimensional function.

**Submitted Week 12 query:** `0.600000-0.600000`

### Function 2

Week 11 produced a new best of `0.5848554940277205` at `0.695000,0.950000`. The strongest earlier result was `0.5712475315739602` near `0.700000,0.950000`. Reducing the first coordinate while holding the second coordinate fixed had improved the result, so a further small local test was selected.

**Submitted Week 12 query:** `0.690000-0.950000`

### Function 3

PC1 accounted for most of the recorded query variance, but the best verified output remained `-0.06037987403160633` at `0.850000,0.150000,0.850000`. Week 11 moved close to that point and recovered strongly. The direct objective evidence therefore outweighed extrapolation along PC1.

**Submitted Week 12 query:** `0.850000-0.150000-0.850000`

### Function 4

Week 11 produced a large recovery after moving back towards the stronger historical region. PCA also showed a concentrated query path, but the exact best observed point gave a clearer target than further extrapolation.

**Submitted Week 12 query:** `0.600000-0.430000-0.420000-0.250000`

### Function 5

Function 5 was the clearest case where PCA and objective history agreed. PC1 accounted for most of the recorded query variance, and the objective value had risen as the search concentrated near the upper boundary. After the Week 9 and Week 10 plateau, Week 11 improved again to `4411.0387356061765`.

A further controlled boundary refinement was therefore selected.

**Submitted Week 12 query:** `0.100000-0.999000-1.000000-1.000000`

### Function 6

The query history required two principal components to retain at least 90 percent of the recorded variance. The strongest direct evidence remained the earlier best point `0.700000,0.200000,0.700000,0.700000,0.200000`. Week 11 had already recovered after moving back towards that basin.

**Submitted Week 12 query:** `0.700000-0.200000-0.700000-0.700000-0.200000`

### Function 7

Function 7 also required two principal components for at least 90 percent of the recorded query variance. The best verified point remained `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000`, while Week 11 remained close to the same productive region.

**Submitted Week 12 query:** `0.040000-0.480000-0.260000-0.220000-0.420000-0.740000`

### Function 8

The exact Week 1 best point returned `9.58024` again when repeated in Week 11. That direct repeatability evidence was stronger than extrapolating along the principal direction.

**Submitted Week 12 query:** `0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000`

## Submitted Week 12 query set

```text
Function 1
0.600000-0.600000

Function 2
0.690000-0.950000

Function 3
0.850000-0.150000-0.850000

Function 4
0.600000-0.430000-0.420000-0.250000

Function 5
0.100000-0.999000-1.000000-1.000000

Function 6
0.700000-0.200000-0.700000-0.700000-0.200000

Function 7
0.040000-0.480000-0.260000-0.220000-0.420000-0.740000

Function 8
0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000
```

## Decision summary

The Week 12 submission was not produced by PCA alone. PCA was used to test whether the accumulated query history contained lower dimensional structure that could simplify the search without discarding useful information. The resulting principal directions were then compared with the verified objective history.

Direct historical evidence was stronger for Functions 1, 3, 4, 6, 7 and 8. Function 2 supported a small local refinement from its new Week 11 best. Function 5 provided the strongest agreement between PCA structure and observed objective improvement, so the Week 12 query continued a controlled boundary refinement.

This produced a function specific Week 12 submission in which the analytical method was selected according to the evidence available for each objective rather than applied uniformly across all eight functions.