# Module 23 Reflection Preparation

## Purpose

This file preserves the preparation pathway used for Component 23.1. The Week 12 objective values have now been returned and verified.

The completed evidence based record is available in [Component 23.1 Capstone Reflection](COMPONENT_23_1_CAPSTONE_REFLECTION.md).

## Strategy maturation

The optimisation process has moved through several distinct stages:

```text
Broad exploration
        |
        v
Function specific refinement
        |
        v
Historical trajectory comparison
        |
        v
Clustering and regional recovery
        |
        v
PCA and variance structure
        |
        v
Comparison of methods
        |
        v
Function specific Week 12 selection
```

The main change is that later decisions no longer rely on a single rule across all eight functions. Each function is now assessed using the evidence most relevant to its history, dimensionality and recent behaviour.

## Drivers of variation

The PCA analysis of Functions 3 to 8 found that the recorded query trajectories were concentrated in one or two principal directions:

| Function | PC1 explained variance | PC1 plus PC2 | Components for at least 90 percent |
| --- | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9966917983027923` | 1 |
| Function 4 | `0.929457542635097` | `0.9990069305772716` | 1 |
| Function 5 | `0.9676115302998125` | `0.997726663010752` | 1 |
| Function 6 | `0.864773785020967` | `0.9866734368322968` | 2 |
| Function 7 | `0.8602299516486513` | `0.9692454132352497` | 2 |
| Function 8 | `0.9021092653998608` | `0.9666706798190747` | 1 |

These figures describe the variance of the submitted query paths. They do not prove that the hidden objective functions have the same effective dimensionality. The adaptive search process itself contributes to the concentration of the observed inputs.

The useful comparison is therefore between query variance and objective behaviour. Function 5 is the clearest example where both point in the same broad direction. Functions 6 and 7 retain meaningful variation across two principal components, which argues against reducing their immediate search to a single dominant direction.

## Exploration versus simplification

Simplification is justified where several observations provide consistent evidence and where reducing the search does not discard an important alternative explanation.

Function 5 has progressively concentrated near the upper boundary and continued to improve, so the Week 12 query tests another small refinement. Functions 1 and 8 have exact repeated best points, so their Week 12 choices prioritise reliability rather than further broad exploration. Functions 3, 4, 6 and 7 return to stronger verified historical points because those observations provide clearer immediate targets than extrapolating the PCA trajectory.

The purpose of simplification is therefore not to remove dimensions mechanically. It is to reduce attention to weak or redundant search directions while retaining uncertainty where the evidence remains mixed.

## Link to the final round

The Week 12 outputs will determine how strongly each strategy should be carried into Round 13.

The returned values will test four different choices:

1. confirmed best point repetition for Functions 1 and 8;
2. local refinement for Function 2;
3. historical best recovery for Functions 3, 4, 6 and 7;
4. PCA consistent boundary refinement for Function 5.

The final round will therefore use observed Week 12 outcomes to decide where continued exploitation is justified and where a last exploratory move still has enough information value to be worthwhile.

## PCA interpretation

The most useful lesson from PCA is not that every high dimensional search should be compressed. It is that accumulated observations can contain redundancy, and that some directions carry more information than others.

Within this capstone, PCA provides a structured way to examine how the submitted coordinates have moved together. Objective performance remains the deciding evidence. When PCA structure and performance agree, as in Function 5, the case for simplification is stronger. When they differ, the verified objective history takes priority.

## Final reflection status

The Component 23.1 reflection has been completed using the verified Week 11 and Week 12 evidence. The final record distinguishes query variance from objective behaviour, retains uncertainty and does not claim a global optimum.