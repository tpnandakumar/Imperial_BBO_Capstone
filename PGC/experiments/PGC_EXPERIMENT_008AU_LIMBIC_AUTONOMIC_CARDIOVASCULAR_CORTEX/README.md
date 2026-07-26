# PGC Experiment 008AU: Limbic-Autonomic Cardiovascular Cortex Regulation

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test whether a limbic-autonomic cardiovascular controller can improve the current 0.988596 peak by dynamically redistributing model influence according to sample-level cognitive demand.

## Computational interpretation

- limbic salience: uncertainty, disagreement and low consensus confidence
- heart rate: responsiveness of resource allocation to salience
- blood pressure: strength of redistribution away from baseline
- vascular reliability: development-only estimate of how trustworthy each model is for a predicted class and confidence range
- basal flow: minimum contribution retained for every model
- autoregulatory recovery: return towards baseline to avoid runaway model dominance

## Locked architecture

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest
- ridge meta-classifier

## Experimental arms

- 008AR fixed reference
- heart-rate salience only
- blood-pressure blend only
- limbic-autonomic reliability
- vascular resource redistribution
- full autoregulated cardiovascular cortex

## Search design

- 60 configurations per arm
- 360 total configurations
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- controller reliability estimated within development folds only
- frozen protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **limbic-autonomic reliability**.

- winner configuration: 4
- ridge alpha: 1.442918
- demand gain: 0.761815
- pressure gain: 0.490745
- recovery: 0.644608
- minimum flow: 0.749785
- maximum flow: 1.299843
- mean out-of-fold accuracy: 0.985211
- protected-test mean accuracy: **0.988596**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: 0.809051

## Interpretation

The controller did not cross 0.99. It reproduced the 0.988596 peak.

The important result is efficiency. The peak-matching arm was identified at configuration 4, earlier than the configuration-9 result in 008AR. This suggests that limbic-autonomic reliability gating can direct the search towards the established optimum rapidly.

The evidence does not yet show that autonomic regulation raises the ceiling. It shows that it can reduce the search effort required to reach the current ceiling.

A valid attempt to move above 0.99 now requires a new predictive information source, stronger calibrated base learners, or a different meta-model. Further geometric or regulatory modulation alone is unlikely to exceed the current plateau on these datasets.
