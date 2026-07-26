# Experiment 008AF Specification

## Title

Combined 008AD and 008AE: RIPPLE-Propagated MaxInflu in a Dynamic Rifled Pear Field

## Objective

Combine the asymmetric pear-shaped, purpose-directed, peristaltic search field from Experiment 008AD with the batch-wise MaxInflu propagation and dynamic rifling from Experiment 008AE.

## Locked predictive architecture

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest
- ridge meta-classifier

## Data protocol

- datasets: breast cancer, wine and digits
- development seeds: 11, 37 and 71
- frozen protected test: 20%
- cross-fitting: stratified five-fold
- protected-test labels excluded from search and selection

## Experimental arms

1. 008AD rifled pear with peristaltic recoil control
2. Pear with batch MaxInflu
3. Pear with momentum MaxInflu
4. Pear with dynamic rifled MaxInflu
5. Pear with dynamic rifled MaxInflu and recoil
6. Pear with dynamic rifled multi-front MaxInflu and recoil

## Search budget

- 100 configurations per arm
- 10 batches per arm
- 10 trials per batch
- 600 total configurations
- equal budget per arm
- all development winners fixed before protected-test evaluation

## Pear geometry

Each arm uses:

- a broad asymmetric exploration chamber
- progressive narrowing towards the extraction neck
- bounded purpose-directed stretch
- orthogonal random exploration within the pear cross-section

## MaxInflu propagation

At the end of each batch:

1. rank the 10 candidates by mean out-of-fold accuracy, worst accuracy and standard deviation
2. convert the best candidate scale vector into a direction from the neutral centre
3. normalise the direction
4. propagate it directly or through momentum, according to arm

## Dynamic purpose-directed rifling

For rifled arms:

- build an orthogonal local basis around the current propagated axis
- generate bounded helical displacement around the axis
- vary twist according to search progress and momentum magnitude
- damp helical radius during recoil

## Peristaltic recoil

Recoil is a phase-delayed travelling contraction that:

- compresses chamber radius
- reduces excess ridge displacement
- damps propagated momentum in recoil-enabled arms

## Multi-front arm

The multi-front arm carries both the best and second-best batch directions. The secondary front is weaker and decays with search progress.

## Candidate parameters

Each candidate contains:

- seven model probability-block scales
- ridge alpha
- purpose-axis components
- stretch magnitude
- recoil magnitude
- twist angle
- batch and trial indices

## Selection rule

Within each arm:

1. highest mean out-of-fold accuracy
2. highest worst-case out-of-fold accuracy
3. lowest out-of-fold standard deviation

## Primary metrics

- mean out-of-fold accuracy
- worst out-of-fold accuracy
- out-of-fold standard deviation
- protected-test mean accuracy
- protected-test worst accuracy
- macro-F1
- balanced accuracy
- log loss

## Promotion rule

A hybrid arm may be promoted only if it exceeds the 008AD benchmark of 0.988596 while preserving worst-case accuracy and without protected-test feedback.

## Interpretation boundary

This experiment tests whether the two search mechanisms are complementary. Failure to exceed either parent does not invalidate either mechanism independently. It indicates interference or over-modulation when combined under the tested schedule.
