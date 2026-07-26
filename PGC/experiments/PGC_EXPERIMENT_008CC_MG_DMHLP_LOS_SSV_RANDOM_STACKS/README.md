# PGC Experiment 008CC: MG-DMHLP-LOS-SSV Random Stacks

## Status

Completed fresh matched comparative development experiment. This is not final confirmatory evidence.

## Design

- datasets: breast cancer, wine and digits
- random stack sizes: 3, 5, 7, 10 and 11
- 10 independent cycle seeds
- 10 random repeats per cycle
- 100 aggregate evaluations per stack size
- 11 candidate models including RBF SVC specialist
- no holdout labels used for guidance

## Protocol

```text
A-DMIC
→ mandatory guidance
→ radar and ripple capture
→ FBW pulse-vector funnel
→ dual-mode handover
→ ILS-H precision approach
→ line-of-sight propagation
→ stability-spin damping
→ floor-protected docking
```

## Best protocol stack

The 3-model random stack with MG-DMHLP-LOS-SSV ranked first by median accuracy among the protocol arms.

- median accuracy: 0.982432
- bootstrap 95% CI for median: 0.978558 to 0.983821
- modal band: 0.9829
- modal frequency: 9 of 100
- sample SD: 0.006519
- mean accuracy: 0.982260
- mean 95% CI: 0.980966 to 0.983553
- minimum accuracy: 0.972125
- maximum accuracy: 0.994298
- near-peak frequency at or above 99.0%: 22%
- mean active models: 7.544
- Net Regenerative Efficiency: 0.696100

## Accuracy changes versus baseline

- 3-model stack: +0.013206 mean accuracy, Holm p 1.62e-10
- 5-model stack: +0.003750, Holm p 3.82e-06
- 7-model stack: +0.001270, Holm p 0.01227
- 10-model stack: -0.000047, not significant
- 11-model stack: no accuracy change

## Interpretation

The full docking protocol strongly improved small random stacks by guiding them towards the 11-model consensus route.

The gain was largest for the 3-model stack, whose minimum accuracy improved from 0.906823 to 0.972125 and whose SD fell from 0.019380 to 0.006519.

This improvement required substantial additional model participation. The 3-model protocol arm used 7.544 active models on average and reduced Net Regenerative Efficiency relative to the sparse baseline.

For 10 and 11 models, the guidance protocol did not improve accuracy because those stacks were already close to the full-route target.

The protocol stack-size comparison was not statistically significant overall after convergence of the guided arms:

- Friedman p value: 0.267244

This suggests the protocol compressed performance differences between stack sizes.

## Evidence boundary

Radar, ripple, FBW, ILS, line-of-sight, stability-spin and docking terms are computational control analogues. Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
