# PGC Experiment 008AA: Rescue-Trained ATA with Vmax and A0 Maintenance

## Status

Completed three-seed development trial. This is development evidence, not confirmatory publication evidence.

## Architecture

The unmodified seven-model Pandora stack was retained as the protected fallback:

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest

All 42 directed ATA links were available. Each link had separate cross-fitted rescue and harm predictors trained on development labels only.

## Acceleration schedule

For an activated link:

1. A0 maintenance thrust remained active throughout.
2. The route accelerated towards Vmax according to predicted rescue-minus-harm utility.
3. Vmax was used for route acquisition and lock.
4. The excess above A0 was removed at the terminal phase.
5. The final output retained only A0 influence, provided the accelerated and terminal routes agreed.

## Search design

- 100 random configurations
- 10 batches
- 10 trials per batch
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- one sparse ATA link per case
- frozen protected test opened only for the selected winner

## Winning validation configuration

- search order: 46
- batch: 5
- trial: 6
- rescue-minus-harm threshold: 0.06
- harm weight: 3.0
- A0: 0.10
- Vmax: 0.55
- acceleration curve: square root
- mean out-of-fold accuracy: 0.985199
- net development rescue: +3
- activation rate: 0.520044

## Protected-test result

- ATA accuracy: **0.984227**
- Pandora fallback accuracy: **0.987622**
- macro-F1: 0.984125
- balanced accuracy: 0.983782
- log loss: 0.751582
- worst-case accuracy: 0.964912
- rescues: 0
- harms: 2
- net rescue: -2
- activation rate: 0.452534
- mean peak thrust on active cases: 0.314696
- terminal A0: 0.10

## Interpretation

The rescue-trained controller improved development accuracy slightly, but the gain did not transfer to the protected test. It produced no protected-test rescues and introduced two harms.

The acceleration schedule itself behaved as designed: A0 was maintained, Vmax rose temporarily, and the excess thrust was removed before the final decision. The failure came from controller generalisation, not from violating the thrust schedule.

No ATA configuration is promoted from this experiment. The seven-model Pandora stack remains the active fallback and current three-seed leader.

## Next requirement

Any successor must be substantially sparser than this experiment. Protected-test activation approached 45%, which is still too frequent for a rescue-only system. The next gate should target exceptional cases only, with stronger abstention and a hard no-harm constraint.
