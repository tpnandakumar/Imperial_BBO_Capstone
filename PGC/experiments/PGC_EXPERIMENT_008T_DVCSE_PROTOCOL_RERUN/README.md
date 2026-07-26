# PGC Experiment 008T: DVCSE Protocol Rerun

## Status

Completed reproducible rerun of the recovered Experiment 008 protocol. This is not claimed as an exact reproduction of the missing original implementation.

## Recovered design used

- Breast Cancer Wisconsin, Wine and Digits
- 60% training, 20% validation and 20% protected test
- ten fixed seeds per dataset
- standardised logistic regression, random forest and probabilistic SVC
- validation split in half
- first half used to train the meta-selector
- second half used to select routing and vectoring thresholds
- protected-test labels excluded from all tuning
- five paired models tested with vectoring off and on
- laser-focused accelerated Fusion Anchor tested as a successor arm

## Aggregate protected-test results

| Model | Routing | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Fixed hybrid** | **Without vectoring** | **0.981248** | **0.980603** | **0.979563** | 0.142101 | 0 | 0 | 0 | **0.947368** |
| Navier processing | Without vectoring | 0.980599 | 0.979971 | 0.978751 | 0.200400 | 0 | 0 | 0 | 0.947368 |
| Navier processing | With vectoring | 0.980015 | 0.979332 | 0.977966 | 0.202037 | 3 | 5 | -2 | 0.947368 |
| Rankine cruise | Without vectoring | 0.979922 | 0.979217 | 0.977850 | **0.091593** | 0 | 0 | 0 | 0.938596 |
| Dynamic scramjet | Without vectoring | 0.979844 | 0.979185 | 0.977888 | 0.095677 | 0 | 0 | 0 | 0.947368 |
| Dynamic scramjet | With vectoring | 0.979644 | 0.978959 | 0.977596 | 0.097237 | 4 | 4 | 0 | 0.947368 |
| Fixed hybrid | With vectoring | 0.979430 | 0.978721 | 0.977503 | 0.143990 | 6 | 8 | -2 | 0.947368 |
| Rankine cruise | With vectoring | 0.979215 | 0.978354 | 0.976896 | 0.093460 | 9 | 8 | +1 | 0.938596 |
| Laser-accelerated Fusion Anchor | Laser targeted | 0.977671 | 0.976852 | 0.975415 | 0.259753 | 3 | 0 | +3 | 0.944444 |
| Fusion Anchor | With vectoring | 0.976886 | 0.976043 | 0.974804 | 0.275999 | 4 | 3 | +1 | 0.944444 |
| Fusion Anchor | Without vectoring | 0.976793 | 0.975946 | 0.974721 | 0.277829 | 0 | 0 | 0 | 0.944444 |

## Interpretation

The best rerun arm was the fixed hybrid without vectoring at 98.1248% mean protected-test accuracy. This did not reproduce the historical 98.6126% Fusion Anchor result, so the original implementation still contained materially different modelling or calibration choices.

Vectoring produced a small positive net rescue only for Rankine cruise and the reconstructed Fusion Anchor. It harmed Navier processing and the fixed hybrid, and was neutral for the dynamic scramjet.

The laser-focused accelerated Fusion Anchor produced three rescues and no harms, but its full-coverage mean accuracy remained below the fixed hybrid and its log loss was substantially worse. It is therefore not promoted as the current best rerun model.

## Current scientific position

- Historical screenshot-supported maximum: 0.986126
- Best reproducible protocol rerun: 0.981248
- Best laser-targeted rerun: 0.977671

The historical result remains separate until its exact executable implementation is recovered or independently reproduced.
