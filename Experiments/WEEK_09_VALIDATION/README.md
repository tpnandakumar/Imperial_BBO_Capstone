# Week 09 Validation Experiment

## Objective

This experiment records the verified Week 09 submission and compares its returned outputs with Week 08. The aim was to test whether the established high performing regions could be refined further while retaining enough exploration for the weaker functions.

## Verified Week 09 inputs

| Function | Input |
| --- | --- |
| Function 1 | 0.350000,0.700000 |
| Function 2 | 0.725000,0.945000 |
| Function 3 | 0.255000,0.855000,0.295000 |
| Function 4 | 0.310000,0.710000,0.670000,0.230000 |
| Function 5 | 0.120000,0.997000,0.999800,0.999800 |
| Function 6 | 0.240000,0.760000,0.240000,0.820000,0.280000 |
| Function 7 | 0.058000,0.495000,0.248000,0.218000,0.425000,0.742000 |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.468000,0.872000,0.572000,0.982000 |

## Verified Week 09 outputs

| Function | Output | Exact change from Week 08 |
| --- | ---: | ---: |
| Function 1 | -1.4546199699251391e-58 | 0E-74 |
| Function 2 | 0.47297842839949866 | -0.09429915787983044 |
| Function 3 | -0.1156707106126581 | -0.0165599468698679 |
| Function 4 | -11.788939969158545 | 0.516068928028744 |
| Function 5 | 4394.868042481448 | 35.483908158745 |
| Function 6 | -1.1733030029888645 | -0.0535851603976798 |
| Function 7 | 1.314307996450604 | -0.0203311698680292 |
| Function 8 | 9.4709436 | -0.0052664 |

## Interpretation

Function 5 improved again and established a new best output. Function 4 also improved, although it remained the lowest ranked objective. Function 1 was unchanged. Functions 2, 3, 6, 7 and 8 declined, which led to the Week 09 strategy of exploiting Function 5, refining Functions 2, 4, 7 and 8, reassessing Functions 3 and 6, and exploring Function 1.

## Reproducibility

The corresponding weekly source files remain in `Week_09`. This experiment record retains the exact submission, outputs and Decimal comparisons and does not replace the fuller weekly analysis.
