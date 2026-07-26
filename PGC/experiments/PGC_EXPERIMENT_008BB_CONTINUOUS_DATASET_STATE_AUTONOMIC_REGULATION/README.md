# PGC Experiment 008BB: Continuous Dataset-State Autonomic Regulation

## Status

Completed cross-domain continuous-state validation. This is not a final confirmatory result.

## Purpose

Replace broad data-family labels with continuous development-state measurements that regulate specialist activation, stack depth and microcirculation.

## Continuous state variables

- class-imbalance severity
- dimensionality-to-sample ratio
- sparsity
- noise proxy
- nonlinearity proxy
- model disagreement
- confidence
- entropy
- calibration gap

## Design

- 12 heterogeneous datasets
- 3 new seeds: 601, 619 and 641
- 36 dataset-seed units
- three-fold cross-fitting
- development-only state estimation
- identical holdouts for all systems

## Systems compared

- static 5-stack
- static 10-stack
- universal microcirculation
- continuous-state autonomic regulation

## Main results

| System | Mean accuracy | Worst unit | Macro-F1 | Balanced accuracy | Log loss | Models activated | Inference ratio vs static 10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Continuous-state autonomic | **0.872592** | **0.419444** | **0.799406** | **0.798062** | 0.351761 | 7.496 | 0.520 |
| Universal microcirculation | 0.872495 | 0.419444 | 0.799287 | 0.797916 | 0.351974 | 7.547 | 0.524 |
| Static 5-stack | 0.872391 | 0.416667 | 0.798208 | 0.797464 | **0.348852** | **5.000** | **0.214** |
| Static 10-stack | 0.870981 | 0.419444 | 0.797685 | 0.796841 | 0.379812 | 10.000 | 1.000 |

## Statistical evidence

The Friedman comparison across all four systems was not significant:

- statistic: 0.545455
- p value: 0.908798

Pairwise comparisons after Holm correction:

- continuous-state versus universal microcirculation: mean difference 0.000096, Holm p = 1.000000
- continuous-state versus static 5-stack: mean difference 0.000200, Holm p = 1.000000
- continuous-state versus static 10-stack: mean difference 0.001611, Holm p = 0.660647

## Efficiency findings

The continuous-state controller activated 7.496 models per sample on average, representing approximately 25.0% fewer model activations than the static 10-stack.

Its measured inference-time ratio was 0.520 relative to the static 10-stack, corresponding to approximately 48.0% lower inference time.

The static 5-stack remained the most efficient and produced the best mean log loss.

## Interpretation

Continuous measured state improved the ranking of the autonomic controller. It achieved the highest mean accuracy, macro-F1 and balanced accuracy in this experiment, while reducing model activation and inference time relative to the static 10-stack.

However, the differences were extremely small and not statistically significant. This supports continuous-state regulation as a promising control architecture, but not yet as evidence of a general accuracy advantage.

The next stage should learn the mapping from development-state measurements to control actions across datasets, rather than using a fixed hand-designed formula. That learner must be trained only on development units and evaluated on unseen datasets or dataset groups.

## Evidence boundary

No holdout labels were used to estimate state or define control actions. Electrical energy and monetary cost were not measured.
