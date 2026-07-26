# PGC Experiment 008O: Bullet-Train Accelerated Trajectory Conduit

## Status

Completed trial evidence. Not publication evidence.

## Protected anchor

The adaptive-entry Combi Conduit remained the protected anchor. Trajectory planning identified locally promising specialist routes, focused acceleration increased their influence, continuous acceleration maintained that influence across staged route lock, and precision braking or rollback could return the decision to the anchor.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting

## Arms

1. Adaptive-entry Combi anchor
2. Trajectory-planned route
3. Focused acceleration
4. Continuous acceleration
5. Precision braking
6. Bullet-train rollback

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Adaptive-entry Combi anchor | 0.978645 | 0.977713 | 0.976630 | 0.135946 | 0 | 0 | 0 | 0.938596 |
| Trajectory-planned route | 0.978645 | 0.977713 | 0.976630 | 0.135949 | 0 | 0 | 0 | 0.938596 |
| **Focused acceleration** | **0.978738** | **0.977802** | **0.976723** | 0.135931 | 1 | 0 | **+1** | **0.938596** |
| **Continuous acceleration** | **0.978738** | **0.977802** | **0.976723** | 0.135931 | 1 | 0 | **+1** | **0.938596** |
| Precision braking | 0.978645 | 0.977713 | 0.976630 | **0.135819** | 0 | 0 | 0 | 0.938596 |
| Bullet-train rollback | 0.978645 | 0.977713 | 0.976630 | **0.135819** | 0 | 0 | 0 | 0.938596 |

## Dataset-specific findings

- Breast Cancer Wisconsin remained unchanged at 0.963158.
- Wine remained unchanged at 0.988889.
- Digits improved from 0.983889 to 0.984167 under focused and continuous acceleration.

## Interpretation

Focused and continuous acceleration produced one protected-test rescue with no harms. The gain was small but directionally consistent with the hypothesis that once a locally dominant route has been validated, increasing its influence can improve accuracy by avoiding dilution from weaker routes.

Precision braking and rollback improved log loss but suppressed the single successful rescue. The current brake rule is therefore too conservative for accuracy optimisation.

## Current conclusion

The provisional best architecture is:

```text
Adaptive-entry Combi anchor
        ↓
Trajectory scoring
        ↓
Focused route lock
        ↓
Continuous acceleration on validated specialist route
        ↓
Soft braking rather than hard rollback
```

The next refinement should replace the hard braking rule with a variable brake that reduces acceleration gradually instead of cancelling the intervention completely.
