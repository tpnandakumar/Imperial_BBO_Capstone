# Final Capstone Datasheet

## Scope

This datasheet follows the Module 25 course template and describes the complete assessment-facing dataset for the thirteen-round Imperial Black Box Optimisation capstone. The eight objectives were anonymous mathematical functions. No real-world scenario, equation, gradient, noise process or global optimum was disclosed, so none is inferred here.

## Function overview

Imperial supplied 175 starter observations. I then submitted one prospective query per function in each of 13 rounds, adding 104 portal evaluations. The complete dataset therefore contains 279 input-output observations.

| Function | Input dimension | Starter observations | Prospective queries | Total observations | Best participant-query output | Best query week or weeks |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| F1 | 2 | 10 | 13 | 23 | `0.025559285339829783` | 3, 11, 12, 13 |
| F2 | 2 | 10 | 13 | 23 | `0.7335252043269003` | 12 |
| F3 | 3 | 15 | 13 | 28 | `-0.05685061601567621` | 13 |
| F4 | 4 | 30 | 13 | 43 | `-4.359874926582439` | 1, 12, 13 |
| F5 | 4 | 20 | 13 | 33 | `4440.957216598753` | 13 |
| F6 | 5 | 20 | 13 | 33 | `-0.6071562248604215` | 13 |
| F7 | 6 | 30 | 13 | 43 | `1.3809299933612855` | 5, 12, 13 |
| F8 | 8 | 40 | 13 | 53 | `9.58024` | 1, 11, 12, 13 |

Every input coordinate was constrained to `[0,1]`. The output was the scalar objective value returned by the course portal. All eight objectives were maximised, but their raw scales differ and must not be compared as though they shared one unit.

## Dataset structure and provenance

The canonical machine-readable dataset is [`BBO_Dashboard/data/complete_internal_evidence.csv`](../../BBO_Dashboard/data/complete_internal_evidence.csv). Each row contains:

- function number;
- source, either `starter` or `week_01` to `week_13`;
- within-source sequence;
- coordinates `x1` to `x8`, with unused dimensions left empty;
- the returned objective value; and
- a provenance field recording whether an external hash was available.

The weekly folders retain the chronological decision record. All supplied observations and participant queries are consolidated in the audited [`complete_internal_evidence.csv`](../../BBO_Dashboard/data/complete_internal_evidence.csv). Weeks 12 and 13 also retain their verified input and result CSV files directly. The final winner table is [`FINAL_RESULTS_SUMMARY.csv`](../Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv).

New observations were not sampled independently. Each weekly query was chosen after reviewing the outputs available at that time. The dataset therefore becomes increasingly concentrated around promising, recovering or deliberately repeated coordinates.

## Observed function characteristics

| Function | Evidence-led interpretation | Most informative observations |
| --- | --- | --- |
| F1 | A sharply localised productive region was difficult to find, but the winning coordinate was exactly repeatable. | The move to `[0.600000, 0.600000]` and later exact replications. |
| F2 | Local improvement was real but sensitive. A further small step after Week 12 reduced the result, and an earlier repeated coordinate produced different outputs. | Weeks 12 and 13 on opposite sides of the local decision, plus the repeated Weeks 1 and 8 coordinate. |
| F3 | Small local refinements near the final region improved a negative objective towards zero. A repeated coordinate in Weeks 4 and 12 also differed slightly. | The Week 13 movement of `0.015000`, which produced a new participant-query best. |
| F4 | Broad exploration entered much weaker regions. Recovery to the Week 1 coordinate restored the best value exactly. | Weeks 1, 12 and 13 at the same winning coordinate. |
| F5 | The clearest directional response occurred near a boundary. Controlled boundary refinement produced sustained gains. | The Week 1 to Week 13 trajectory and final movement to `0.999999` on three coordinates. |
| F6 | Repeated-coordinate outputs showed the largest variation, so a deterministic interpretation is not supported by the available evidence. | The same coordinate in Weeks 3, 12 and 13 returned three different outputs. |
| F7 | A strong historical coordinate remained stable and reproducible. | Exact recovery in Weeks 12 and 13. |
| F8 | The earliest winning coordinate was repeatedly confirmed despite later exploration. | Identical best outputs in Weeks 1, 11, 12 and 13. |

These are descriptions of the observed sample path, not claims about the complete hidden response surfaces.

## Optimisation strategy

The starting strategy used direct inspection of the supplied observations and function-specific local or exploratory moves. As the evidence grew, the decision set became more explicit:

- **Explore:** test a materially different region when the current evidence was weak.
- **Refine:** make a small movement around a promising coordinate.
- **Exploit:** continue a direction while repeated outputs supported it.
- **Recover:** return to an earlier strong coordinate after an exploratory decline.
- **Repeat:** re-evaluate a coordinate to examine stability.
- **Stop or retain:** protect a reproducible winner when no credible alternative justified further risk.

Clustering was introduced using Week 10 evidence to inform Week 11. K-means compared `k=2` and `k=3`, used `n_init=50` and `random_state=42`, and selected the exploratory partition by silhouette score. Principal component analysis was added in Week 11 to describe coordinated movement and redundancy. Chronological surrogate comparisons and the held-out Week 13 policy experiment were used as decision checks. They did not replace the returned objective values or retrospectively generate earlier submissions.

## Data handling and preprocessing

Inputs already lay in `[0,1]`, so no rescaling was needed for direct coordinate comparisons. For clustering and some multivariate analyses, coordinates were standardised within the relevant function. Outputs were analysed separately because their scales differ. Within-function normalisation was used only for visual comparison of progress.

No objective value was deleted as an outlier. Extreme or disappointing returns were retained because they affected later decisions. Repeated-coordinate disagreement in F2, F3 and F6 was reported as unresolved variability rather than corrected or averaged away. F6 showed the largest range and therefore remained the principal repeatability concern.

Surrogate work compared polynomial Ridge models and Gaussian-process variants where appropriate. Hyperparameter comparisons used chronological validation so that later observations did not leak into earlier predictions. Model-generated surfaces are labelled as inferred and are not presented as observations.

## Weekly iteration and learning

- **Weeks 1 to 3:** moved from starter observations to direct evidence from participant-selected queries.
- **Weeks 4 to 6:** separated productive directions from failed momentum and began function-specific strategies.
- **Weeks 7 to 9:** tightened successful regions while preserving exploratory checks.
- **Week 10:** used clustering and hyperparameter comparison to organise recurring sampled regions.
- **Week 11:** used principal component analysis to examine correlated movement and redundancy.
- **Week 12:** recovered or repeated established winners and refined unresolved functions.
- **Week 13:** prospectively tested retain, local refinement, boundary refinement and repeat actions.

If restarting, I would reserve early queries for structured space-filling and explicit boundary probes, pre-register failure criteria, and schedule replications earlier. F2 would be bracketed on both sides of a promising point. F6 would receive a designed repeatability study before further optimisation.

## Performance and results

Within the participant-query record, the final round produced new best values for F3, F5 and F6. F1, F4, F7 and F8 retained previously established query winners. F2 declined from its Week 12 maximum after a further local step. F5 improved from `1415.8763939603884` in Week 1 to `4440.957216598753` in Week 13, the clearest sustained trajectory. Starter observations remained stronger than the participant-query maxima for F3, F4 and F8, so the two evidence sources are reported separately in the final notebook.

Confidence is highest where a winning coordinate was repeated with the same output, as in F1, F4, F7 and F8. Confidence is lower for F2 because the neighbourhood was incompletely bracketed, and repeated-coordinate disagreement in F2, F3 and F6 limits deterministic interpretation. None of the observed winners proves a global optimum.

## Ethical, practical and general considerations

This synthetic challenge illustrates decision-making when evaluations are scarce and expensive. The central transferable lessons are to preserve provenance, separate observations from inference, test assumptions, report negative evidence and define stopping criteria. These principles can inform real-world optimisation, but the capstone policy cannot be transferred directly to clinical or operational systems without external validation, safety thresholds, subgroup assessment and prospective monitoring.

The principal risks are overinterpreting sparse adaptive samples, treating an isolated extreme as stable, comparing raw outputs across incompatible scales, imposing a familiar function shape and allowing later evidence to leak into earlier validation. Human review remained responsible for every portal submission.

## Post-capstone boundary

Black Box Resolution and the Advanced Extension Series use the completed observation history for later research. They did not alter the official Week 1 to Week 13 inputs, outputs or final ranking.
