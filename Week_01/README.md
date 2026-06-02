# Week 01

Initial Bayesian Black-Box Optimisation submission.

## Objectives

- Analyse starter datasets
- Identify promising regions of the search space
- Select one query point for each function
- Apply Bayesian optimisation principles
- Balance exploration and exploitation

## Functions

- Function 1 (2D)
- Function 2 (2D)
- Function 3 (3D)
- Function 4 (4D)
- Function 5 (4D)
- Function 6 (5D)
- Function 7 (6D)
- Function 8 (8D)

## Submitted Queries

| Function | Query |
|----------|----------|
| 1 | 0.740000-0.740000 |
| 2 | 0.720000-0.940000 |
| 3 | 0.530000-0.640000-0.250000 |
| 4 | 0.600000-0.430000-0.420000-0.250000 |
| 5 | 0.210000-0.870000-0.900000-0.900000 |
| 6 | 0.750000-0.180000-0.700000-0.720000-0.040000 |
| 7 | 0.050000-0.500000-0.250000-0.220000-0.420000-0.740000 |
| 8 | 0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000 |

## Strategy Summary

The initial submission used local refinement around the strongest observed regions while maintaining awareness of uncertainty, local maxima and increasing dimensionality. Functions with smoother behaviour were approached using exploitation, whereas higher-dimensional functions required more cautious exploration.

## Contents

This folder will contain:
data/
queries/
reflection/
figures/
notebooks/
results/
analysis/
