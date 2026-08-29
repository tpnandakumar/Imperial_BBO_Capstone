# Week 06 Validation Experiment

## Objective

This experiment records the verified Week 06 submission and compares its returned outputs with Week 05. The purpose was to assess whether the current search directions improved the eight black box functions.

## Verified Week 06 inputs

| Function | Input |
| --- | --- |
| Function 1 | 0.500000,0.500000 |
| Function 2 | 0.700000,0.950000 |
| Function 3 | 0.950000,0.050000,0.950000 |
| Function 4 | 0.980000,0.020000,0.020000,0.020000 |
| Function 5 | 0.140000,0.970000,0.995000,0.995000 |
| Function 6 | 0.950000,0.050000,0.950000,0.950000,0.050000 |
| Function 7 | 0.050000,0.500000,0.250000,0.200000,0.400000,0.750000 |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.450000,0.850000,0.550000,0.950000 |

## Verified Week 06 outputs

| Function | Output | Exact change from Week 05 |
| --- | ---: | ---: |
| Function 1 | 2.6752879910742468e-09 | -0.0127796399946269479257532 |
| Function 2 | 0.5712475315739602 | 0.29107930849673504 |
| Function 3 | -0.3071823694141529 | -0.19326030563704842 |
| Function 4 | -31.20347777578016 | -3.76296281491094 |
| Function 5 | 3922.7652233497042 | 240.5541610110244 |
| Function 6 | -1.3792272680368016 | -0.3053518143412596 |
| Function 7 | 1.3529491169887171 | -0.0279808763725684 |
| Function 8 | 9.5148 | 0.0035 |

## Interpretation

Function 5 delivered the largest gain and remained the main exploitation target. Function 2 improved substantially, while Function 8 showed a small positive change. Functions 1, 3, 4, 6 and 7 declined, which indicated that the same directions should not be continued without review.

## Reproducibility

The corresponding weekly source files remain in `Week_06`. This experiment record does not replace them. It provides a concise, verified account of the submitted point, the returned outputs and the exact changes from Week 05.

