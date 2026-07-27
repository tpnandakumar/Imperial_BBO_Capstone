# PGC Experiment 008Z: Dynamic Free-Form ATA

## Status

Completed three-seed development trial. This is development evidence, not confirmatory publication evidence.

## Purpose

Test the intended meaning of free-to-form ATA Crosslinks: links form only when a particular case needs them, and any model may connect to any other model.

## Locked network

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest

## Dynamic ATA search

- 100 random configurations
- 10 configurations per batch
- 10 batches
- three development seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- all directed source-to-destination links available
- case-specific link activation
- thresholds: 0.02 to 0.10
- strengths: 0.15 to 0.70
- maximum active links: 1 to 4
- signals: mean, residual, difference or adaptive
- ridge alpha: 0.3 or 1.0
- frozen protected test opened only for the validation-selected winner

## Winning configuration

- search order: 96
- batch: 10
- trial: 6
- activation threshold: 0.10
- crosslink strength: 0.15
- maximum links per case: 1
- signal mode: adaptive
- ridge alpha: 1.0
- mean out-of-fold accuracy: 0.984800
- worst development accuracy: 0.971429
- validation activation rate: 0.849328

## Protected-test result

- mean accuracy: **0.981449**
- macro-F1: **0.981551**
- balanced accuracy: **0.981013**
- log loss: 0.809601
- worst-case accuracy: **0.964912**
- protected-test ATA activation rate: 0.826511
- mean active links per case: 0.826511

## Interpretation

Dynamic free-form ATA performed materially worse than the Pandora Box winner without ATA, which reached 0.987622 in the same three-seed development setting.

The winning ATA controller was conservative in topology, selecting at most one adaptive crosslink per case. However, it activated on approximately 83% of protected-test cases. This suggests that the current need gate remained too permissive. Crosslinks became nearly routine rather than exceptional.

The result does not reject free-form ATA. It shows that crosslinks must be trained to predict actual rescue probability and actual harm probability, rather than being activated from confidence, entropy and disagreement alone.

## Next ATA requirement

The next dynamic implementation must use validation-labelled rescue-minus-harm learning:

1. identify cases where one node corrects another
2. learn which directed link produces a rescue
3. estimate harm probability for the same link
4. activate only when expected rescue minus expected harm is positive
5. retain the unmodified Pandora stack as the protected fallback

No ATA configuration is promoted from this experiment.
