# PGC Experiment 008CG: EFAMES Full Ablation

## Status

Completed fresh matched development experiment. This is not final independent confirmation.

## Design

- datasets: breast cancer, wine and digits
- seeds: 601, 619, 631, 647, 661, 677, 691, 709, 727 and 743
- 10 repeats per seed
- 100 aggregate evaluations per arm
- seven arms
- training, development and untouched test splits kept separate
- holdout labels were not used for routing
- A-DMIC Computational Milieu Intérieur preserved as the basal regulatory layer

## Arms

1. ECSP-3 + 008CE reference
2. certainty lock
3. single micro-expert
4. class-pair expert
5. residual learner
6. residual error memory
7. full EFAMES

## Main result

The residual learner achieved the strongest multi-objective rank.

- median accuracy: 0.978801
- mean accuracy: 0.977714
- minimum accuracy: 0.958236
- sample SD: 0.008850
- mean active models: 3.000
- NRE proxy: 0.905000
- full rescue rate: 0%

Compared with the ECSP-3 + 008CE reference, mean accuracy increased by 0.001072. The paired Wilcoxon comparison remained significant after Holm correction, p = 0.021166.

## Full EFAMES

- median accuracy: 0.977973
- mean accuracy: 0.977071
- minimum accuracy: 0.961306
- sample SD: 0.008817
- mean active models: 3.266
- NRE proxy: 0.898362
- full rescue rate: 2.19%

Full EFAMES produced the strongest minimum accuracy and improved mean accuracy by 0.000428 versus the reference. The paired comparison was significant after Holm correction, p = 0.023228. Full rescue fell from 2.95% in the reference to 2.19%, but did not reach the under-2% target.

## Important ablation findings

- Residual correction was the strongest accuracy-efficiency component.
- A single micro-expert improved mean accuracy by 0.000892, Holm p = 0.032637.
- Class-pair routing did not improve accuracy and should not be promoted in its current form.
- Residual error memory improved mean accuracy, but the paired result was not significant after multiplicity correction.
- Certainty locking improved efficiency and removed full rescue, but its accuracy gain did not remain significant after Holm correction.

## Target assessment

No arm reached the previously stated absolute mean or minimum accuracy targets on these stricter fresh splits. Every arm remained below four active models and passed the NRE proxy target. All arms except the reference and full EFAMES passed the under-2% full-rescue target.

The previous absolute targets were derived from earlier reused development splits and should not be treated as directly transferable to this stricter three-way split design.

## Evidence boundary

NRE is a computational reuse proxy, not electrical energy. Electrical energy and monetary cost were not measured. The experiment provides comparative development evidence only.

## Decision

Promote the residual learner as the preferred EFAMES correction mechanism. Retain the full EFAMES structure for floor protection, but reduce its compact and full rescue thresholds before the next validation. Replace the current class-pair expert before further testing.
