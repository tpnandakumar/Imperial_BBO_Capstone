# PGC Experiment 008BD: Strategic Feed-Forward Pulse Pressure with Symmetrical Dynamic Peristalsis and Posterior Pear Stretch

## Status

Completed cross-domain dynamic-geometry validation. This is not a final confirmatory result.

## Purpose

Test a coordinated cardiovascular control architecture combining:

- strategic feed-forward pulse pressure
- symmetrical dynamic peristalsis
- posterior pear-shaped stretch
- strategic diastolic recoil
- outer laminar venous return
- an optimised internal milieu

## Design

- 12 heterogeneous datasets
- 3 new seeds: 809, 827 and 853
- 36 dataset-seed units
- three-fold cross-fitting
- development-only optimisation
- 108 candidate configurations per dataset-seed unit

## Systems compared

- static 5-model interior
- strategic diastole reference
- feed-forward pulse pressure
- symmetrical dynamic peristalsis
- full posterior pear optimised milieu

## Main result

The strategic diastole reference was strongest overall.

- mean accuracy: 0.872076
- worst-unit accuracy: 0.400000
- macro-F1: 0.796789
- balanced accuracy: 0.796253
- log loss: 0.348999
- mean models activated: 6.474
- mean milieu stability: 0.958130

## Dynamic geometry findings

The full posterior pear optimised milieu was identical to the static 5-model interior across all 36 dataset-seed units.

Feed-forward pulse pressure, symmetrical dynamic peristalsis and full posterior pear dynamics also produced no measurable accuracy difference from one another under the selected development policies.

Compared with strategic diastole, the full pear milieu was lower by 0.000203 mean accuracy.

The Friedman test approached but did not reach significance:

- statistic: 8.000000
- p value: 0.091578

## Interpretation

The geometry was stable but too conservative to alter predictive outcomes. The optimiser repeatedly returned the system towards the stable 5-stack interior.

This indicates that symmetrical peristalsis, feed-forward pressure and posterior stretch should not act merely as additional blending geometry. To add predictive capacity, they must control genuinely distinct specialist pathways or feature-space transformations.

Strategic diastole remains the strongest control layer in this experiment because it preserved selective specialist activation while maintaining high milieu stability.

## Evidence boundary

Pressure, peristalsis, pear stretch, recoil and milieu stability are computational control-state proxies. Training and inference time were measured as wall-clock time. Electrical energy was not measured.
