# PGC Experiment 008AQ: Selective Local Thermal Regulation

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test whether temperature control can improve the strongest laminar regime by insulating the productive core while applying only local cooling or micro-heating outside that corridor.

## Computational interpretation

Temperature is a computational control-state proxy.

- core temperature: fixed operating state of the MaxInflu corridor
- local temperature: damping state of the outer field
- micro-cooling: local suppression of turbulent orthogonal motion
- micro-heating: restoration of exploratory motion during stagnation
- thermal effort: derived control-overhead proxy, not measured electrical energy

## Arms

- 008AM insulated reference
- outer-boundary cooling
- stagnation micro-heating
- turbulence micro-cooling
- bidirectional local thermostat
- insulated MaxInflu corridor

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **turbulence-triggered micro-cooling**.

- winner configuration: 26
- batch: 3
- trial: 6
- local temperature: 0.755597
- insulated core temperature: 0.82
- cooling action: 0.064403
- heating action: 0
- recoil: 0.047402
- accumulated spin: 0.35 radians
- rifling twist: 0.709944 radians
- mean out-of-fold accuracy: 0.985276
- protected-test mean accuracy: **0.985510**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.985445
- balanced accuracy: 0.984430
- log loss: **0.808314**

## Interpretation

Selective local cooling improved calibration further but did not raise peak accuracy above the 0.988596 level from 008AD, 008AJ, 008AL and 008AM.

The result shows that insulating the core avoids the larger accuracy loss seen with full immersion, but even local cooling still alters the candidate trajectory enough to reduce transfer. Temperature regulation therefore appears more useful as a calibration and stability mechanism than as a direct accuracy-improvement mechanism under the tested design.

The strongest thermal use is likely post-search or event-triggered, not continuously active during candidate generation.
