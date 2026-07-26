# PGC Experiment 008BL: AX-R Stochastic Dropout and Regenerative Reuse

## Status

Completed as the first stage of the ordered AX-R, AY-R, Hybrid-R and final architecture-value comparison.

## Source integrity

AX-R used the exact preserved 008AX out-of-fold and protected-test probability records with the original seeds:

11, 23, 37, 53, 71, 89, 101, 127, 149 and 173.

## Design

- datasets: breast cancer, wine and digits
- nominal stack depths: 3, 5, 8 and 10
- 10 seeds
- 10 repeats per seed
- 10 development-only candidate configurations per repeat
- baseline AX compared with AX-R
- AX-R added stochastic model survival and regenerative computational reuse

## Strongest AX-R configuration

The nominal 3-stack AX-R ranked first.

- mean accuracy: 0.982704
- standard deviation: 0.008172
- maximum accuracy: 0.999074
- minimum accuracy: 0.954971
- macro-F1: 0.981913
- balanced accuracy: 0.980332
- log loss: 0.101082
- mean worst-dataset accuracy: 0.967306
- mean active models: 3.000
- mean dropout fraction: 0.700000
- mean cache reuse rate: 0.995709
- mean avoided-model fraction: 0.700000
- mean Net Regenerative Efficiency: 0.829334

## Stack-depth findings

- 3-stack AX-R versus baseline: +0.000615 mean accuracy
- 5-stack AX-R versus baseline: -0.000670
- 8-stack AX-R versus baseline: -0.000628
- 10-stack AX-R versus baseline: +0.000989

No comparison remained statistically significant after Holm correction.

## Interpretation

Stochastic dropout and regenerative reuse shifted AX towards lower operational complexity.

The strongest AX-R result came from the nominal 3-stack, while the 10-stack also improved relative to its baseline because stochastic survival reduced the mean active model count to 6.123.

The original AX 5-stack remained slightly stronger in mean accuracy than the AX-R 5-stack. This indicates that dropout is beneficial at the sparse and dense ends, but can remove useful complementarity from an already well-balanced medium stack.

The AX-R peak reached 99.9074%, exceeding the earlier AX reported peak of 99.6296%, but this is a comparative repeated evaluation rather than final confirmation.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
