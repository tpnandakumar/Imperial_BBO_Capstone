# Week 08 Validation Experiment

## Objective

This experiment records the verified Week 08 submission and compares its returned outputs with Week 07. The purpose was to test whether local refinements around the newly identified productive regions could improve performance without losing the gains achieved in Week 07.

## Verified Week 08 inputs

| Function | Input |
| --- | --- |
| Function 1 | 0.350000,0.700000 |
| Function 2 | 0.720000,0.940000 |
| Function 3 | 0.260000,0.860000,0.290000 |
| Function 4 | 0.320000,0.720000,0.680000,0.220000 |
| Function 5 | 0.120000,0.995000,0.999500,0.999500 |
| Function 6 | 0.240000,0.760000,0.240000,0.820000,0.280000 |
| Function 7 | 0.060000,0.500000,0.250000,0.220000,0.420000,0.740000 |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.470000,0.870000,0.570000,0.980000 |

## Verified Week 08 outputs

| Function | Output | Exact change from Week 07 |
| --- | ---: | ---: |
| Function 1 | -1.4546199699251391e-58 | 0E-74 |
| Function 2 | 0.5672775862793291 | 0.3273484164186740 |
| Function 3 | -0.0991107637427902 | -0.00794147467902744 |
| Function 4 | -12.305008897187289 | -1.559047514052168 |
| Function 5 | 4359.384134322703 | 80.567496245717 |
| Function 6 | -1.1197178425911847 | -0.0000043427583717 |
| Function 7 | 1.3346391663186332 | 0.1803033539393350 |
| Function 8 | 9.47621 | -0.01855 |

## Interpretation

Functions 2, 5 and 7 improved. Function 5 remained the strongest objective and continued its upward trajectory. Function 1 was unchanged, while Functions 3, 4, 6 and 8 declined. The Week 08 results showed that local refinement was productive for selected functions but could not be applied uniformly across the portfolio.

## Reproducibility

The corresponding weekly source files remain in `Week_08`. This experiment record summarises the verified submission, the returned outputs and the exact changes from Week 07 while preserving the original weekly material.
