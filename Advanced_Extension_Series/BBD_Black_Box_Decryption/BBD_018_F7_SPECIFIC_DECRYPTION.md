# BBD 018: F7-Specific Decryption

## Purpose

BBD 018 begins function-specific decryption of F7 after F6 reached the current evidence ceiling available from the thirteen-round history.

F7 is a strong candidate because earlier stages found very high gradient coherence and strong retrospective symbolic structure, while BBD 007 showed that SOC still predicted F7 slightly better prospectively. This stage therefore asks whether F7 is best described by a compact linear surface, a quadratic interaction surface, or a flexible Gaussian Process when all models are judged by chronological walk-forward prediction.

## Competing models

The experiment compares:

- Matérn 2.5 Gaussian Process;
- linear ridge models;
- quadratic ridge models with several regularisation strengths;
- sparse quadratic Lasso models.

All comparisons preserve chronological ordering. Each prediction is made from earlier rounds only.

## Result

The strongest model was **quadratic ridge with alpha 1e-4**, with normalised chronological walk-forward MAE of approximately `0.034870` across eight prospective historical tests.

The ranking was:

| Rank | Model | Normalised walk-forward MAE |
| --- | --- | ---: |
| 1 | quadratic ridge 1e-4 | 0.034870 |
| 2 | linear ridge 1e-4 | 0.041639 |
| 3 | quadratic ridge 1e-2 | 0.045187 |
| 4 | quadratic ridge 0.1 | 0.055636 |
| 5 | linear ridge 1e-2 | 0.056973 |
| 6 | quadratic Lasso 1e-3 | 0.057266 |
| 7 | quadratic Lasso 1e-2 | 0.059168 |
| 8 | Matérn 2.5 GP | 0.097483 |

This is a substantial improvement over the earlier BBD 007 F7 mechanism, which had normalised prospective MAE of approximately `0.291394`. It is also well below the SOC value reported in BBD 007, approximately `0.195676`. The comparison is not a rerun of SOC under BBD 018, so it should be read as evidence that the F7-specific reconstruction has materially improved, not as a new head-to-head challenge.

## Coordinate effects

The full-history linear ridge diagnostic estimated the strongest coordinate effects as:

1. `x5`: decrease, effect approximately `-4.585639`
2. `x2`: decrease, effect approximately `-3.014723`
3. `x6`: decrease, effect approximately `-2.474043`
4. `x4`: increase, effect approximately `+1.785813`
5. `x1`: increase, effect approximately `+0.958966`
6. `x3`: increase, effect approximately `+0.878948`

These directions agree with the sign pattern identified in BBD 003, which reported a global-to-recent gradient cosine of approximately `0.975357`.

## Repeatability

F7 contains one repeated-coordinate group in the recovered history, and its outputs are identical. The maximum repeated-coordinate range is therefore `0.0` in the current data. Unlike F6, the existing F7 evidence does not contradict coordinate-only determinism.

## Interpretation

BBD 018 provides strong evidence that F7 behaves as a **static, structured coordinate-dependent surface over the sampled region**, with a lightly regularised quadratic representation currently giving the best chronological prediction.

The result does not establish the exact Imperial equation. The remaining uncertainty concerns global extrapolation and whether the quadratic structure survives discriminatory queries outside the historical trajectory.

Exact function recovery therefore remains `False`, and an independent query is still required for strict decryption.
