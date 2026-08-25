# BBD 023: F5-Specific Decryption

## Purpose

F5 is one of the most important contradictions in the BBD programme. BBD 004 produced an exceptionally accurate full-history quadratic reconstruction, with normalised leave-one-out MAE of approximately `0.005749`, and BBD 003 found near-perfect agreement between global and recent gradient directions. However, BBD 007 found that the SOC surrogate family predicted F5 better under its prospective challenge.

BBD 023 therefore rebuilds F5 as a dedicated four-dimensional identification problem and tests whether the strong quadratic interpretation survives stricter chronological prediction.

## Function-specific model set

The thirteen F5 observations are ordered by week. Each candidate is trained only on observations available before the test week and then predicts the next unseen observation. Testing begins after five training observations, producing eight chronological forward tests.

The candidate set includes ordinary and regularised linear regression, quadratic and cubic ridge models, Matérn and RBF Gaussian Processes, gradient boosting, random forest, extra trees, and a boundary-aware feature model using raw coordinates together with distance-to-upper-boundary transforms.

The boundary-aware candidate was included because the historical F5 trajectory moved strongly towards `x2`, `x3` and `x4` values close to 1. It was treated as a competing hypothesis rather than an assumed mechanism.

## Result

The dedicated chronological experiment changed the F5 interpretation substantially. The best model was the **Matérn 2.5 Gaussian Process**, with normalised walk-forward MAE of approximately `0.001616`. The RBF Gaussian Process was second at approximately `0.001666`.

The leading deterministic polynomial model was quadratic ridge with `alpha = 1e-4`, at approximately `0.005802` normalised MAE. This is close to the earlier BBD 004 full-history LOOCV value of `0.005749`, showing that the quadratic reconstruction was genuinely strong, but the smooth Gaussian-process surface predicted the chronological sequence considerably better.

Selected ranking:

| Rank | Model | Normalised walk-forward MAE |
|---:|---|---:|
| 1 | Matérn 2.5 GP | 0.001616 |
| 2 | RBF GP | 0.001666 |
| 3 | Quadratic ridge 1e-4 | 0.005802 |
| 4 | Cubic ridge 1e-2 | 0.005995 |
| 5 | Cubic ridge 1e-4 | 0.006051 |
| 6 | Quadratic ridge 1e-8 | 0.006330 |
| 8 | Linear ridge 1e-2 | 0.007194 |
| 10 | Ordinary linear regression | 0.007425 |

The boundary-transformed models performed extremely poorly. Their failure is useful evidence because it rejects the simple hypothesis that an explicit reciprocal or logarithmic distance-to-one transform explains F5 by itself.

## Directional structure

The expanding-window linear fits retained stable signs for all four coordinates. The full-history linear coefficients ranked the coordinates approximately as:

1. `x2`: `+17750.44`
2. `x3`: `+3956.27`
3. `x4`: `+3956.27`
4. `x1`: `+588.76`

The sign stability was 100% for `x2`, `x3` and `x4`, and about 88.9% for `x1`. This agrees with BBD 003, where the global and recent gradient estimates had cosine similarity of approximately `0.992036`.

The resulting evidence strongly supports a stable direction of improvement, dominated by increasing `x2`, with `x3` and `x4` also strongly positive over the sampled region.

## Repeatability

One F5 coordinate was repeated exactly:

`0.120000-0.997000-0.999800-0.999800`

The two recorded outputs were identical, giving a repeat range of zero. There is therefore no observed repeatability contradiction to coordinate-only determinism for F5.

## Interpretation

BBD 023 resolves the earlier contradiction more clearly than either BBD 004 or BBD 007 alone.

The F5 quadratic reconstruction was not a spurious retrospective fit. It remains highly predictive under chronological testing. However, a smooth Matérn Gaussian-process surface is materially better over the observed trajectory:

`0.001616` versus `0.005802` normalised MAE.

The current best description is therefore a **strong, smooth, boundary-directed static response surface**, with exceptionally stable directional structure but unresolved exact functional form.

The result also improves substantially on both values retained from BBD 007:

- earlier BBD prospective normalised MAE: `0.028072`;
- earlier SOC prospective normalised MAE: `0.009054`;
- BBD 023 Matérn GP: `0.001616`.

This comparison is informative but is not labelled as a fresh SOC contest because the BBD 007 SOC model was not rerun under the exact BBD 023 protocol.

## Evidence boundary

The experiment supports a highly predictable deterministic surface over the sampled F5 trajectory. It does not establish the exact Imperial generating equation. The very low prediction error may still reflect local smoothness along a narrow optimisation path.

Exact function recovery therefore remains false. The next decisive experiment should compare the Matérn GP, the quadratic reconstruction and the strongest SOC alternatives at coordinates where their predictions diverge most, using independent black-box evaluation if it becomes available.
