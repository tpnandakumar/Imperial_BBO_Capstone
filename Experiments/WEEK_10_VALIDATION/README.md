# Week 10 Validation Experiment

## Objective

This experiment records the verified Week 10 submission and compares its returned outputs with Week 09. The purpose was to test whether the strongest known regions could be preserved or improved while gathering evidence for the final optimisation rounds.

## Verified Week 10 inputs

| Function | Input |
| --- | --- |
| Function 1 | 0.450000,0.650000 |
| Function 2 | 0.700000,0.955000 |
| Function 3 | 0.280000,0.875000,0.315000 |
| Function 4 | 0.290000,0.730000,0.690000,0.210000 |
| Function 5 | 0.120000,0.997000,0.999800,0.999800 |
| Function 6 | 0.260000,0.780000,0.260000,0.840000,0.300000 |
| Function 7 | 0.060000,0.500000,0.250000,0.220000,0.430000,0.740000 |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.470000,0.875000,0.575000,0.985000 |

## Verified Week 10 outputs

| Function | Output | Exact change from Week 09 |
| --- | ---: | ---: |
| Function 1 | 2.8950706668499033e-23 | 2.895070666849903300000000000E-23 |
| Function 2 | 0.5311818841205426 | 0.05820345572104394 |
| Function 3 | -0.08697581687486715 | 0.02869489373779095 |
| Function 4 | -13.483642655031158 | -1.694702685872613 |
| Function 5 | 4394.868042481448 | 0E-12 |
| Function 6 | -1.2283806967341901 | -0.0550776937453256 |
| Function 7 | 1.285160161342515 | -0.029147835108089 |
| Function 8 | 9.4646525 | -0.0062911 |

## Interpretation

Functions 1, 2 and 3 improved, although Function 1 remained effectively zero. Function 5 reproduced its Week 09 result exactly, confirming stability at the tested point. Functions 4, 6, 7 and 8 declined. These findings supported the move from local weekly adjustment to the more structured Strategic Optimisation Engine used for Week 11.

## Reproducibility

The complete Week 10 source files remain in `Week_10`, including the exact CSV files, analysis script, figure generation script and 15 section README. This experiment record provides a concise verified summary and does not replace those source artefacts.
