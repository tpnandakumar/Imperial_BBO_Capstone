# PGC Experiment 008U: Cross-Fitted Maximum-Accuracy Stack

## Status

Completed three-seed development trial. This is reproducible trial evidence, not publication evidence and not yet the ten-seed confirmatory result.

## Design changes tested

The experiment implemented the parts of the proposed max-accuracy design that fit the actual datasets:

- frozen 20% protected test
- stratified five-fold cross-fitting on the 80% development set
- out-of-fold probability stacking
- regularised logistic-regression meta-learner
- three fixed development seeds: 11, 37 and 71
- three-booster stack: XGBoost, LightGBM and CatBoost
- heterogeneous stack: CatBoost, LightGBM, probabilistic SVC and logistic regression

Dense contextual embeddings, BM25 and TF-IDF were excluded because Breast Cancer Wisconsin, Wine and Digits are numeric datasets rather than text corpora.

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|
| **Heterogeneous stack** | **0.984893** | **0.984869** | **0.984253** | **0.104758** | **0.964912** |
| Heterogeneous soft vote | 0.981043 | 0.980786 | 0.980469 | 0.112358 | 0.956140 |
| Three-booster soft vote | 0.966244 | 0.965746 | 0.965250 | 0.143056 | 0.938596 |
| Three-booster stack | 0.961046 | 0.960939 | 0.959865 | 0.153904 | 0.938596 |

## Dataset-specific findings

| Dataset | Heterogeneous stack mean accuracy | Heterogeneous stack worst case |
|---|---:|---:|
| Breast Cancer Wisconsin | 0.982456 | 0.964912 |
| Digits | 0.990741 | 0.988889 |
| Wine | 0.981481 | 0.972222 |

## Interpretation

The heterogeneous stack was clearly superior to the three-booster stack. Its gain came from error diversity rather than from using three related boosting systems.

Compared with the current reproducible Experiment 008T benchmark of 0.981248, the heterogeneous stack improved mean accuracy by approximately 0.003645, or 0.3645 percentage points, in this three-seed development trial. It also improved worst-case accuracy from 0.947368 to 0.964912.

The three-booster stack underperformed both its own soft vote and the heterogeneous stack. This shows that XGBoost, LightGBM and CatBoost were not sufficiently complementary under the tested low-budget settings, and that stacking is not automatically beneficial when base errors are highly correlated.

## Current conclusion

The provisional leading architecture is:

```text
Numeric input features
        ↓
Stratified five-fold cross-fitting
        ↓
CatBoost + LightGBM + probabilistic SVC + logistic regression
        ↓
Out-of-fold probability matrix
        ↓
Regularised logistic-regression meta-learner
        ↓
Frozen protected-test prediction
```

The next step is a ten-seed confirmatory rerun of the heterogeneous stack, followed by a validation-gated laser rescue layer only if the gain remains stable.
