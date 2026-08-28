# Advanced PDHIS Delta analysis

## Question

Can Delta information available at the end of one week help classify whether the following weekly output improves?

## Design

The analysis contains 56 forward cases from eight functions. The outcome is balanced: 29 improvements and 27 non-improvements. Delta 1 to Delta 5 are scaled only with history available by the prediction week. Regularised logistic regression is compared with a prevalence baseline. Leave-one-function-out testing assesses transfer to an unseen function, while expanding-week testing preserves chronology.

## Main results

The full Delta signature reached leave-one-function-out balanced accuracy of 0.624, ROC AUC of 0.659 and Brier score of 0.238. Expanding-week balanced accuracy was 0.563, with ROC AUC 0.642 and Brier score 0.275. The within-function permutation p value was 0.0297. The largest absolute standardised coefficient was delta5_scaled at -0.688, with a cluster-bootstrap interval from -1.028 to -0.068.

## Interpretation

Gradient-based optimisation is used only to fit the logistic model. It is not treated as separate scientific evidence. The model is exploratory because the dataset is small, repeated observations within a function are dependent and several Delta features are related. A useful out-of-sample result would justify prospective testing on later data. It would not recover a hidden equation or establish a causal influence state.

## Original research direction

PDHIS proposes a testable idea: change may carry a multilevel signature that is more informative than a single first difference. In this study, that signature combines the direction and size of Delta 1 to Delta 5 with persistence, sign change and agreement across levels. The first result suggests that this combined description may transfer between functions, but the chronological test is weaker and its probability estimates do not beat the simple baseline.

The next research stage should be registered before new outcomes are collected. Its primary hypothesis should compare the full Delta signature with Delta 1 alone using balanced accuracy and Brier score. Secondary work can examine how early a useful signature appears, whether the influence states remain stable across different processes and whether the model can identify when no reliable prediction should be made.

A credible study would include a larger independent dataset, untouched test functions, repeated measurements where outputs may vary, confidence intervals defined in advance and comparison with simple time-series and persistence baselines. An external replication should use the same Delta definitions and locked model before any local adjustment. These steps would show whether the present pattern is reproducible, generalisable and practically useful.

The research contribution is therefore a falsifiable framework and an auditable testing method. It is not a claim that PDHIS has already discovered a universal law of change.

## Higher-order pointers

The later behaviour is the target. A separate forward analysis asks whether oscillation in Delta 6 to Delta 10 points towards a positive Delta 1, Delta 2 or Delta 3 value one week later. [Read the complete higher-order result](PDHIS_HIGH_ORDER_POINTERS.md).

For the specific Delta 9 to Delta 3 question, only 16 forward cases are available. Delta 9 oscillated in 15 cases and positive Delta 3 followed in 6 of those 15. The two-sided exact p value is 0.438. Delta 9 oscillation therefore does not predict positive Delta 3 in the present record. Its near-universal occurrence also suggests that very high-order oscillation may arise from repeated differencing rather than identify a distinctive future state.

## Influence-state summary

| Influence state | Cases | Next improvements | Next improvement rate | Median next change |
| --- | ---: | ---: | ---: | ---: |
| Reversal | 20 | 9 | 0.450 | -0.000 |
| Plateau | 19 | 8 | 0.421 | 0.000 |
| Irregular or oscillating | 8 | 6 | 0.750 | 0.051 |
| Directed improvement | 5 | 3 | 0.600 | 35.484 |
| Directed decline | 4 | 3 | 0.750 | 0.188 |

## Reproducibility

Run `python Post_BBO_BBR/PDHIS/generate_pdhis_advanced_analysis.py` from the repository root.
