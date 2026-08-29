# Week 07 Validation Experiment

## Objective

This experiment records the verified Week 07 submission and compares its returned outputs with Week 06. The aim was to determine whether the revised search directions recovered performance after the mixed Week 06 results.

## Verified Week 07 inputs

| Function | Input |
| --- | --- |
| Function 1 | 0.350000,0.700000 |
| Function 2 | 0.760000,0.985000 |
| Function 3 | 0.250000,0.850000,0.300000 |
| Function 4 | 0.300000,0.700000,0.650000,0.250000 |
| Function 5 | 0.120000,0.990000,0.999000,0.999000 |
| Function 6 | 0.250000,0.750000,0.250000,0.800000,0.300000 |
| Function 7 | 0.050000,0.520000,0.240000,0.180000,0.410000,0.770000 |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.460000,0.860000,0.560000,0.980000 |

## Verified Week 07 outputs

| Function | Output | Exact change from Week 06 |
| --- | ---: | ---: |
| Function 1 | -1.4546199699251391e-58 | -2.675287991074246800000000000E-9 |
| Function 2 | 0.2399291698606551 | -0.3313183617133051 |
| Function 3 | -0.09116928906376276 | 0.21601308035039014 |
| Function 4 | -10.745961383135121 | 20.457516392645039 |
| Function 5 | 4278.816638076986 | 356.0514147272818 |
| Function 6 | -1.119713499832813 | 0.2595137682039886 |
| Function 7 | 1.1543358123792982 | -0.1986133046094189 |
| Function 8 | 9.49476 | -0.02004 |

## Interpretation

Week 07 produced major recoveries in Functions 3, 4, 5 and 6. Function 5 again delivered the largest gain and strengthened the evidence for boundary directed exploitation. Functions 1, 2, 7 and 8 declined, showing that the recovery was function specific rather than universal.

## Reproducibility

The corresponding weekly source files remain in `Week_07 `. The folder name includes the trailing space already present in the repository. This experiment record preserves the exact submission, returned outputs and Decimal changes without altering the historical weekly folder.

