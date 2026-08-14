# Week 12 Pre Result Record

## Status

The twelfth round of BBO queries has been submitted. Returned objective values are not yet available, so this folder records only the verified submitted inputs and the reasoning that led to them.

No Week 12 result file, final README, analysis summary, figure data summary, datasheet or model card is created at this stage. Those files will be prepared after the returned outputs are available and verified.

## Submitted Week 12 queries

| Function | Submitted query | Selection basis |
| --- | --- | --- |
| Function 1 | `0.600000,0.600000` | Exact repeated historical best |
| Function 2 | `0.690000,0.950000` | Small local refinement from the new Week 11 best |
| Function 3 | `0.850000,0.150000,0.850000` | Return to the strongest verified historical point |
| Function 4 | `0.600000,0.430000,0.420000,0.250000` | Return to the strongest verified historical point |
| Function 5 | `0.100000,0.999000,1.000000,1.000000` | Controlled boundary refinement supported by the observed trend and PCA structure |
| Function 6 | `0.700000,0.200000,0.700000,0.700000,0.200000` | Return to the strongest verified historical point |
| Function 7 | `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` | Return to the strongest verified historical point |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | Exact repeated historical best |

## How the decision was made

The Week 12 query set was selected after comparing three forms of evidence:

1. the complete verified input and output history through Week 11;
2. the regional and recovery patterns identified in the Week 10 and Week 11 analyses;
3. the PCA structure of the accumulated query trajectories introduced in Module 23.

PCA was treated as one analytical option rather than an automatic replacement for direct performance evidence. For Functions 3, 4, 6, 7 and 8, the strongest verified historical points provided more precise targets than extrapolation along a principal direction. Functions 1 and 2 are two dimensional, so direct geometry and local performance were clearer. Function 5 was the case where PCA structure and objective history pointed in the same broad direction, supporting one further controlled boundary refinement.

The full comparison is recorded in `../Week_11/PCA_STRATEGY_COMPARISON.md`, and the final function by function decision path is recorded in `../Week_11/WEEK_12_DECISION_RECORD.md`.

## What will be tested when outputs arrive

Week 12 will provide a direct test of several different strategic choices within the same round:

- whether repeating confirmed best points remains reliable for Functions 1 and 8;
- whether the small local refinement for Function 2 improves on its Week 11 best;
- whether returning to historical best points improves Functions 3, 4, 6 and 7;
- whether the PCA consistent boundary refinement for Function 5 produces further gain or shows diminishing returns.

These outcomes will be compared with Week 11 before the final Round 13 strategy is chosen.

## Assessment link

Component 23.1 asks for reflection on strategy maturation, drivers of variation, simplification versus continued exploration, the exploration and exploitation balance, and the relevance of PCA concepts such as variance and redundancy. The final reflection will be completed after the Week 12 outputs are available so that the discussion of the final round can be based on observed evidence rather than prediction.