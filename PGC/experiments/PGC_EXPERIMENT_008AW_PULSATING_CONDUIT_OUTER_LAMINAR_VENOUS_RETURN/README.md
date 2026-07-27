# PGC Experiment 008AW: Pulsating Conduit with Outer Laminar Venous Return

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test whether an inner pulsatile systolic-diastolic conduit, driven by a pressure gradient and paired with an outer laminar venous return sheath, can improve the 008AR medium-density, medium-viscosity closed-space regime.

## Arms

- 008AR static reference
- fixed pulse conduit
- systolic-only conduit
- systolic-diastolic conduit
- pulsatile conduit with pressure gradient
- full closed loop with outer laminar venous return

## Search design

- 60 configurations per arm
- 360 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen protected test
- all development winners fixed before protected-test evaluation

## Best result

The strongest arm was **pulsatile conduit with pressure gradient**.

- winner configuration: 3
- winning phase: systole
- heart-rate proxy: 2.629438
- pulse-pressure proxy: 0.076851
- forward pressure gradient: 0.009454
- venous pressure gradient: 0.015250
- arterial drive: 0.004372
- mean out-of-fold accuracy: 0.985288
- protected-test mean accuracy: **0.988596**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: **0.808843**

## Interpretation

The pulsatile pressure-gradient conduit reproduced the existing 0.988596 peak by configuration 3, earlier than the configuration-4 peak from 008AU and the configuration-9 peak from 008AR.

The result suggests that explicit systolic propulsion through a pressure gradient is an efficient search mechanism. The full outer venous-return arm did not win on peak accuracy. Under this implementation, venous return appears more useful for recovery, stabilisation and closed-loop regulation than for producing the forward optimum directly.

The result does not cross 0.99 and remains a three-seed development trial. Exact extraction and independent multi-seed confirmation are required before promotion.

## Measurement boundary

Heart rate, pressure, arterial drive and venous return are computational control-state proxies. They are not physiological or physical energy measurements.
