# PGC Experiment 008AC: Conical Laminar Pandora Shape

## Status

Completed three-seed shape-comparison trial. This is development evidence, not confirmatory publication evidence.

## Purpose

Test whether the geometry of the Pandora search field redirects optimisation squeeze and force sufficiently to improve model discovery.

## Locked architecture

The seven-model Pandora stack was held constant:

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest

Only the candidate-generation geometry changed.

## Shapes compared

- rectangular
- spherical
- ellipsoidal
- funnel
- spiral
- conical laminar

Each shape received 100 configurations, giving 600 total configurations. All six development winners were fixed before protected-test evaluation.

## Main result

The ellipsoidal Box produced the strongest protected-test result:

- mean accuracy: **0.987622**
- worst-case accuracy: **0.964912**
- macro-F1: **0.987291**
- balanced accuracy: **0.986745**
- log loss: 0.808633

This exactly reproduced the existing three-seed Pandora peak.

## Interpretation

The result supports the view that Box geometry redirects search pressure. The ellipsoid preserved movement around the validated heterogeneous stack while limiting unnecessary displacement in weaker directions.

The conical laminar shape did not exceed the ellipsoid in this first implementation. Its axial redirection was therefore not yet superior to a stable anisotropic search field.

The current evidence suggests:

1. the Box performs an outer search-space squeeze
2. the shape controls the direction and concentration of that squeeze
3. the ellipsoid is currently the most reliable geometry
4. the extracted seven-model stack remains the active predictive architecture

No shape exceeded 0.987622 in this trial. The ellipsoidal Box is promoted as the preferred search geometry for the next confirmatory extraction and ten-seed reproduction stage.
