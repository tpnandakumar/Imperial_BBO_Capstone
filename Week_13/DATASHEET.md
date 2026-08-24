# Week 13 Datasheet

## Scope

This datasheet describes the final round record for the Imperial Bayesian Black Box Optimisation capstone.

## Source data

The final round contains eight submitted vectors and eight returned objective values. The authoritative files are `week_13_inputs.csv` and `week_13_results.csv`.

## Function dimensions

| Function | Dimensions |
| --- | ---: |
| Function 1 | 2 |
| Function 2 | 2 |
| Function 3 | 3 |
| Function 4 | 4 |
| Function 5 | 4 |
| Function 6 | 5 |
| Function 7 | 6 |
| Function 8 | 8 |

All recorded coordinates are within the permitted interval from 0 to 1.

## Historical coverage

The Week 13 analysis uses the complete thirteen round history to compare the final result with previous observations. Cross function output magnitudes are not treated as directly comparable because each hidden objective operates on its own scale.

## Known limitation

Function 6 returned different values at an identical recorded coordinate across Weeks 3, 12 and 13. This means deterministic repeatability cannot be assumed for every function.

## Intended use

The dataset supports final round evaluation, strategy reflection, trajectory analysis and reproducible assessment of the capstone. It does not identify the hidden mathematical functions or prove global optimality.
