# PGC Experiment 008AO: Immersed Cooling Medium with Thermal Laminar Control

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test whether immersing the 008AM high-viscosity, high-lubrication pear system in a computational cooling medium can remove excess search energy while preserving the useful peristaltic ripple.

## Computational interpretation

The cooling medium acts as thermal damping of:

- chamber deformation
- spin rate
- rifling amplitude
- ridge-alpha jitter
- directional turbulence

## Arms

- 008AM reference
- constant mild cooling
- confidence-controlled cooling
- turbulence-controlled cooling
- adaptive thermal bath
- overcooled control

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **constant mild cooling**.

- winner configuration: 40
- batch: 4
- trial: 10
- temperature: 0.720100
- cooling strength: 0.18
- turbulence: 0.353160
- recoil: 0.016649
- accumulated spin: 0.35 radians
- rifling twist: 0.936284 radians
- mean out-of-fold accuracy: 0.985044
- protected-test mean accuracy: **0.985510**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.985445
- balanced accuracy: 0.984430
- log loss: **0.808612**

## Interpretation

Cooling improved damping and calibration slightly, but it reduced accuracy below the 0.988596 peak from 008AD, 008AJ, 008AL and 008AM.

The likely failure mode is over-damping. The cooling medium reduced chamber freedom, spin energy, rifling amplitude and alpha variation at the same time. That removed some unstable motion, but also removed part of the low-amplitude exploratory energy required to reach the strongest configuration.

The result indicates that cooling should not be applied continuously to the whole system. A better design is selective cooling that activates only when measured turbulence or uncertainty crosses a threshold, while the productive ripple remains thermally insulated.

The active leader remains 008AM for calibration and 008AD, 008AJ and 008AL for peak accuracy.
