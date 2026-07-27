# PGC Experiment 002

## Title

Evidence-Aware Expert Routing on the UCI Iris Dataset

## Dataset

- Name: Iris
- Source: UCI Machine Learning Repository
- UCI identifier: 53
- DOI: 10.24432/C56C76
- Licence: Creative Commons Attribution 4.0 International
- Samples: 150
- Features: 4 continuous measurements
- Classes: 3
- Execution loader: `sklearn.datasets.load_iris`

The execution record stores a SHA-256 checksum of the loaded feature and target arrays. The scikit-learn bundled copy is used to avoid network-dependent changes during repeat runs, and the loader is recorded explicitly because it contains corrected observations that may differ from historical raw UCI files.

## Separation

Each of five fixed seeds creates an independent stratified split:

- 60% training
- 20% validation
- 20% protected test

The protected-test labels are not used by the deployable routing arms. They are used only to score outcomes and to construct the non-deployable oracle upper bound.

## Candidate experts

- standardised logistic regression
- standardised 5-nearest neighbours
- Gaussian naive Bayes
- depth-3 decision tree

## Routing arms

1. strongest validation expert
2. random router
3. confidence-only router
4. oracle router
5. PGC evidence-aware router
6. PGC without coherence
7. PGC without efficiency

## PGC evidence inputs

The PGC router receives only training and validation-derived evidence plus each expert's current prediction distribution:

- validation balanced accuracy
- predicted-class validation recall
- bootstrap validation stability
- prediction confidence and entropy
- expert agreement as coherence
- measured inference efficiency

## Metrics

- protected-test task success
- balanced accuracy
- macro F1
- multiclass log loss
- exact routing agreement with the oracle selection
- routing regret against the oracle outcome
- abstention rate
- routing latency

## Evidence status

This experiment is trial evidence only. It is not publication evidence and it does not establish a general PGC advantage.
