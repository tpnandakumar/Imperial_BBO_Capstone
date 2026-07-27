# PGC Experiment 008BA: Data-Family-Specific Autonomic Regulation

## Status

Completed cross-domain family-adaptive validation. This is not a final confirmatory result.

## Purpose

Test whether recognising the data family first and then applying a specialised autonomic policy improves on one universal microcirculation controller.

## Data coverage

Twelve heterogeneous datasets were tested across three new seeds, giving 36 dataset-seed units.

Data families included:

- real tabular
- image-derived
- nonlinear geometry
- imbalanced
- high-dimensional
- noisy
- mixed multiclass
- sequential

## Systems compared

- static 5-stack
- static 10-stack
- universal microcirculation
- family-adaptive autonomic regulation

## Family-adaptive variables

The controller selected these variables using development data only:

- confidence threshold
- disagreement quantile
- entropy threshold
- specialist blend
- activation penalty

## Main results

| System | Mean accuracy | Worst unit | Macro-F1 | Balanced accuracy | Log loss | Models activated | Inference ratio vs static 10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Universal microcirculation | **0.873200** | 0.388889 | **0.799105** | **0.798404** | 0.349350 | 7.645 | 0.584 |
| Static 5-stack | 0.873106 | **0.394444** | 0.797886 | 0.797477 | **0.345642** | **5.000** | **0.196** |
| Family-adaptive autonomic | 0.873026 | 0.388889 | 0.798925 | 0.798231 | 0.348387 | 7.574 | 0.561 |
| Static 10-stack | 0.870538 | 0.391667 | 0.796451 | 0.795839 | 0.376287 | 10.000 | 1.000 |

## Statistical evidence

The Friedman comparison across all four systems was not significant:

- statistic: 2.286713
- p value: 0.515071

Pairwise results after Holm correction:

- family-adaptive versus universal microcirculation: mean difference -0.000174, Holm p = 0.359425
- family-adaptive versus static 5-stack: mean difference -0.000080, Holm p = 0.797513
- family-adaptive versus static 10-stack: mean difference 0.002488, Holm p = 0.252164

## Efficiency findings

The family-adaptive controller used 7.574 models per sample on average, which is a 24.3% reduction from the static 10-stack.

Its measured inference-time ratio was 0.561 relative to the static 10-stack, corresponding to approximately 43.9% lower inference time.

The static 5-stack remained the most efficient system and also produced the best mean log loss and strongest worst-unit accuracy.

## Interpretation

The family-specific controller did not outperform the universal controller overall. The first family-policy grid was too coarse to produce a reliable cross-domain gain.

However, it remained more accurate than the static 10-stack while reducing model activation and inference time. This supports the cardiovascular architecture as an efficiency mechanism, but not yet as a universal accuracy mechanism.

The evidence indicates that simple family labels are not sufficient. The next regulator should use continuous dataset-state measurements rather than broad categories alone, including class imbalance, dimensionality-to-sample ratio, local nonlinearity, noise, sparsity and model disagreement.

## Evidence boundary

All policy selection used development folds only. Holdout labels were not used to choose policy thresholds. The experiment remains exploratory because only three seeds and twelve datasets were used.
