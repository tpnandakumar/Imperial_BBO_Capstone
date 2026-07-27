# PGC Experiment 008Y: Pandora Box ATA Shake

## Status

Completed three-seed development trial. This is reproducible trial evidence, not confirmatory publication evidence.

## Pandora Box inventory

The experiment placed all currently favourable components into one randomised search field:

- locked core: XGBoost, LightGBM, probabilistic SVC and logistic regression
- add-on inventory: CatBoost, Extra Trees, histogram gradient boosting and Random Forest
- ATA crosslink modes: none, directed mean, difference, product and full pairwise expansion
- ATA strengths: 0.15, 0.30, 0.50 and 0.70
- ridge alpha: 0.3 or 1.0
- 10 random configurations per batch
- 10 batches
- 100 total configurations
- three development seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test opened only for the validation-selected winner

## Winning validation configuration

- search order: 13
- batch: 2
- trial: 3
- add-ons: CatBoost, Extra Trees and Random Forest
- ATA mode: none
- ATA strength field: 0.15, inactive because ATA mode was none
- ridge alpha: 1.0
- mean out-of-fold accuracy: 0.984967
- out-of-fold standard deviation: 0.007644
- worst development accuracy: 0.973626

## Protected-test result

- mean accuracy: **0.987622**
- macro-F1: **0.987291**
- balanced accuracy: **0.986745**
- log loss: 0.808338
- worst-case accuracy: **0.964912**

## Interpretation

The Pandora Box reproduced the previous three-seed peak of 0.987622. The strongest configuration kept the locked core and added CatBoost, Extra Trees and Random Forest.

The selected winner did not use ATA crosslink feature expansion. In this first implementation, model diversity improved performance, but the tested pairwise mean, difference, product and full ATA transformations did not surpass the unmodified stacked probability representation.

This does not reject the ATA concept. It indicates that simple static pairwise feature expansion is insufficient. A stronger ATA experiment should use case-specific, validation-gated crosslink activation rather than applying all pairwise transformations uniformly.

## Current conclusion

Pandora Box confirms that the high-accuracy region is concentrated around a seven-model heterogeneous stack:

```text
XGBoost
+ LightGBM
+ probabilistic SVC
+ logistic regression
+ CatBoost
+ Extra Trees
+ Random Forest
        ↓
ridge meta-classifier, alpha 1.0
```

The next confirmatory stage must repeat this winner over ten fixed seeds before promotion.
