# PGC Experiment 008AP: Dynamic Efficient Temperature Regulation

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test bidirectional temperature regulation around an efficient operating band. The controller is designed to avoid both overcooling and overheating while preserving accuracy, calibration and search efficiency.

## Computational interpretation

Temperature is a control-state proxy, not a physical temperature measurement.

- low temperature: stronger damping and reduced exploratory motion
- high temperature: greater deformation, spin and parameter variation
- heating action: restores motion when the system becomes over-damped or stagnant
- cooling action: suppresses excess turbulence and uncertainty
- regulation effort: derived proxy for control overhead, not measured electrical energy

## Arms

- 008AM without thermal control
- fixed optimal temperature band
- confidence thermostat
- turbulence thermostat
- efficiency thermostat
- full dynamic temperature regulation

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was the **confidence thermostat**.

- winner configuration: 50
- batch: 5
- trial: 10
- temperature: 0.820550
- nominal efficient band: 0.68 to 0.84
- regulation effort at winner: 0
- recoil: 0.022675
- accumulated spin: 0.35 radians
- rifling twist: 1.036207 radians
- mean out-of-fold accuracy: 0.985044
- protected-test mean accuracy: **0.987622**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.987291
- balanced accuracy: 0.986745
- log loss: **0.808652**

## Interpretation

Dynamic temperature regulation improved on the fully immersed cooling experiment and identified a useful operating temperature near 0.821.

However, it did not recover the 0.988596 peak from 008AD, 008AJ, 008AL and 008AM. The confidence thermostat was stronger than the fully dynamic controller, suggesting that temperature regulation should remain simple and primarily tied to uncertainty rather than reacting simultaneously to every signal.

The result supports an efficient thermal band rather than continuous cooling or unrestricted heating. The next confirmation should treat approximately 0.78 to 0.84 as the candidate operating zone and use narrow, low-cost corrections only when bootstrap confidence falls outside its expected range.
