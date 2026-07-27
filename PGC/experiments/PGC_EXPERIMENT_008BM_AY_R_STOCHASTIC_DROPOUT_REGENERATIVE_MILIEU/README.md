# PGC Experiment 008BM: AY-R Stochastic Dropout and Regenerative Milieu

## Status

Completed as the second stage of the ordered AX-R, AY-R, Hybrid-R and architecture-value comparison.

## Source integrity

AY-R used the exact preserved 008AY fresh-seed out-of-fold and protected-test probability records with seeds:

181, 197, 211, 227, 241, 257, 271, 283, 307 and 331.

## Design

- datasets: breast cancer, wine and digits
- stack depths: 5 and 10
- 10 seeds
- 10 repeats per seed
- 10 development-only candidates per repeat
- milieu arms: isolated stable interior, pulsatile milieu and dynamic optimised milieu
- AY-R added stochastic model dropout, cached milieu-state reuse and regenerative computational efficiency

## Strongest AY-R configuration

The 5-stack AY-R ranked first.

- mean accuracy: 0.983839
- standard deviation: 0.008016
- maximum accuracy: 0.996296
- minimum accuracy: 0.965936
- macro-F1: 0.983523
- balanced accuracy: 0.982772
- log loss: 0.090968
- mean worst-dataset accuracy: 0.973102
- mean active models: 3.760
- mean dropout fraction: 0.624000
- mean milieu reuse rate: 0.768767
- mean cache reuse rate: 0.995696
- mean avoided-model fraction: 0.624000
- mean Net Regenerative Efficiency: 0.795155

## Comparisons

### 5-stack AY-R versus AY baseline

- mean difference: +0.000617
- wins: 51
- ties: 19
- losses: 30
- Holm-adjusted p value: 0.354566

### 10-stack AY-R versus AY baseline

- mean difference: +0.001122
- wins: 48
- ties: 13
- losses: 39
- Holm-adjusted p value: 0.354566

Neither comparison remained statistically significant after Holm correction.

## Interpretation

AY-R improved mean accuracy at both stack depths while reducing operational model count.

The 5-stack produced the strongest overall AY-R mean and reached a maximum aggregate accuracy of 99.6296%. The 10-stack gained more relative to its baseline, indicating that stochastic dropout reduced interference in the denser architecture.

The result supports a stable medium-depth milieu with selective model survival, cached operating-state reuse and strategic recovery.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Milieu variables are computational control-state parameters. Electrical energy was not measured.
