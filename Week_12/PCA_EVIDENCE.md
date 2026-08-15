# Week 12 PCA Evidence Record

## Purpose

Week 11 introduced centred principal component analysis as a comparison method before the Week 12 submission. Week 12 repeats the same calculation after adding the new query. This provides an auditable comparison between the variance structure through Week 11 and the structure through Week 12.

## Code pathway

Run from the repository root:

```bash
python Week_12/week_12_analysis.py
python Week_12/generate_week_12_figures.py
```

The first script validates all eight Week 12 inputs and outputs against the locked source values. It then loads the verified Weeks 1 to 11 history from `Week_11/week_11_analysis.py`, adds the Week 12 coordinates and performs centred PCA by singular value decomposition for Functions 3 to 8.

The analysis records:

- the PC1 explained variance ratio through Week 11;
- the revised PC1 ratio through Week 12;
- cumulative variance from PC1 and PC2;
- the number of components needed to retain at least 90 per cent of observed query variance;
- the coordinate with the largest absolute PC1 loading;
- the maximum absolute correlation between observed coordinates.

## Interpretation

PCA is used here to describe the search trajectory. It can show whether submitted coordinates moved mainly along one direction, whether two directions remained important, and whether some coordinates moved together.

It cannot reveal the hidden objective function directly. High explained variance does not prove that a function has only one effective dimension. Strong coordinate correlation may indicate redundancy in the sampled path, but it does not prove that either coordinate is irrelevant to the objective.

The returned objective values remain the outcome test. Each function is compared with its own history because the eight functions use different numerical scales.

## Week 13 boundary

This analysis does not create Week 13 inputs. It prepares an evidence base that can be compared with any new strategy introduced in the next course material. The final submission will remain open until that requirement is known.
