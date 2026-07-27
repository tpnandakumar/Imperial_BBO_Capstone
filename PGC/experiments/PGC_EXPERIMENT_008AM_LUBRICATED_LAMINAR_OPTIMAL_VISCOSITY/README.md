# PGC Experiment 008AM: Lubricated Laminar Flow with Optimal Dynamic Viscosity

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test whether directional lubrication and viscosity control can smooth the 008AL search flow while preserving the asymmetric pear field, symmetrical rhythmic wavefront, dynamically tuned amplitude and frequency, goal-alignment spin and low-amplitude rifling.

## Computational interpretation

- lubrication: exponential smoothing of successive search directions
- viscosity: resistance to chamber deformation and wave propagation
- flow gain: inverse function of viscosity
- low viscosity: greater freedom and faster deformation
- high viscosity: stronger damping and slower deformation

## Arms

- 008AL reference
- low viscosity with high lubrication
- medium viscosity with high lubrication
- high viscosity with high lubrication
- dynamic viscosity
- adaptive optimal viscosity

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **high viscosity with high lubrication**.

- winner configuration: 48
- batch: 5
- trial: 8
- viscosity: 1.6
- lubrication: 0.75
- flow gain: 0.384615
- recoil: 0.030955
- accumulated spin: 0.35 radians
- rifling twist: 0.669803 radians
- ridge alpha: 1.290577
- mean out-of-fold accuracy: 0.985122
- protected-test mean accuracy: **0.988596**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: **0.808669**

## Interpretation

High viscosity with strong directional lubrication reproduced the 0.988596 peak while improving log loss relative to the recent peak-matching runs.

The result suggests that smoother flow does not require lower resistance. In this regime, higher viscosity reduced abrupt deformation and allowed the directional smoothing layer to preserve a stable laminar path.

The strongest operating regime is therefore:

- asymmetric pear-shaped search medium
- symmetrical rhythmic wavefront
- dynamically tuned amplitude and frequency
- goal-alignment spin
- low-amplitude rifling
- high directional lubrication
- high but bounded viscosity

This result requires exact extraction and ten-seed confirmation before promotion.
