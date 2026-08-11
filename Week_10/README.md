# Week_10

## Bayesian Black Box Optimisation Portfolio

### Week 10 Analysis

## Stage 2 Component 22.1: Clustering Lens and Week 11 Strategy Refinement

The Week 10 evidence was reviewed through a clustering lens before the 11th round of queries was selected. With only ten observations per function, I did not treat the emerging groups as statistically established clusters. Instead, I looked for repeated local behaviour, the distance between successive queries, stability of nearby outputs and signs that a productive region was beginning to plateau. This gave me a more disciplined way to distinguish recurring structure from isolated results.

### How earlier academic feedback changed the strategy

Feedback on Component 12.1 highlighted two weaknesses in the earlier approach. First, the analysis could become repetitive when similar local refinement arguments were described separately for every function. Second, decisions about when to stop exploiting a strong region relied too heavily on visual trends. From Week 10 onwards, I therefore compare functions directly and use clearer switching signals alongside visual interpretation.

The practical triggers are deliberately simple because the dataset remains small:

| Trigger | Evidence considered | Strategy response |
| --- | --- | --- |
| Plateau | No meaningful improvement across 2 or more consecutive rounds | Reduce exploitation and test a neighbouring or alternative region |
| Diminishing return | Successive gains become progressively smaller | Tighten the step once, then reassess if improvement remains weak |
| Local concentration | Several consecutive queries remain close together without a new best result | Increase exploratory distance |
| Material deterioration | A local move produces a clear fall in objective value | Stop continuing in that direction and reassess |
| Boundary concentration | Improvement repeatedly pushes coordinates towards 0 or 1 | Test the boundary carefully while retaining an alternative search route |
| Weak coverage | A local region is well sampled but much of the search space remains untested | Allocate a query to broader exploration |

These are decision rules rather than calibrated statistical thresholds. Their purpose is to make the reasoning explicit and to prevent a promising local pattern from becoming an automatic exploitation loop.

### F1 to F8 clustering evidence and Week 11 decisions

| Function | Week 10 evidence | Cluster or recurring-region interpretation | Similarity or distance cue | Less effective direction avoided | Week 11 decision |
| --- | --- | --- | --- | --- | --- |
| F1 | `2.8950706668499033e-23`, still effectively zero | No reliable productive cluster | A substantial move still produced negligible response | Repeated refinement of a near-zero region | Explore at `0.600000,0.600000` |
| F2 | Improved from `0.47297842839949866` to `0.5311818841205426` | Emerging positive neighbourhood | Remain close enough to test whether the improvement persists | Large jump away from the improving region | Refine at `0.695000,0.950000` |
| F3 | Improved from `-0.1156707106126581` to `-0.08697581687486715` | Better region emerging, but not yet a stable cluster | Improvement justifies another structured test | Returning to weaker earlier combinations | Reassess at `0.840000,0.160000,0.840000` |
| F4 | Declined from `-11.788939969158545` to `-13.483642655031158` | Week 10 point separated from the better local region | Material deterioration triggers a change of direction | Continuing the Week 10 movement | Redirect to `0.620000,0.420000,0.440000,0.250000` |
| F5 | Repeated `4394.868042481448` at `0.120000,0.997000,0.999800,0.999800` | Clearest high-performing boundary region | Very small distance from the best point, with several coordinates close to 1 | A large jump away from the repeated peak | Boundary refinement at `0.110000,0.998000,0.999900,0.999900` |
| F6 | Declined from `-1.1733030029888645` to `-1.2283806967341901` | Current local direction is not supported | Deterioration separates the new point from stronger earlier observations | Further movement along the same path | Reassess at `0.720000,0.190000,0.700000,0.710000,0.150000` |
| F7 | Positive but declined slightly to `1.285160161342515` | Stable positive neighbourhood | Small changes around an established region | A large move that could lose the positive region | Conservative refinement at `0.045000,0.485000,0.255000,0.220000,0.420000,0.745000` |
| F8 | Small decline to `9.4646525` | Stable high-performing region with plateau characteristics | Nearby queries continue to return similar high values | Aggressive movement away from a reliable region | Controlled variation at `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` |

### Reflection against the 22.1 rubric

**Patterns from past queries.** F5 provides the clearest recurring pattern. Successive refinements concentrated near a boundary region and the Week 10 repeat returned exactly `4394.868042481448`. F2 and F3 improved, which justified further targeted investigation. F4 and F6 moved in the opposite direction, so their latest paths were not continued. F7 and F8 remained positive but slipped slightly, suggesting that smaller changes were more appropriate than aggressive movement.

**Clusters and recurring regions.** I treated a cluster as nearby queries producing broadly consistent or improving results, not simply functions with similar output values. F5 has the strongest high-performing grouping. F7 and F8 show compact positive regions, while F2 appears to be developing a productive neighbourhood. F1 still lacks a meaningful cluster because materially different inputs continue to return values effectively equal to zero. F3 has improved, but the evidence remains too sparse to describe its current region as stable with confidence.

**Ineffective strategies and adjustments.** F4 and F6 show why local refinement should not continue automatically. Both deteriorated in Week 10, which triggered reassessment. F1 also shows that repeated refinement of an uninformative region is not useful. At the other extreme, the repeated F5 result raises the risk of becoming too exploitation-heavy. Its next move is therefore deliberately small, and a further plateau would be a reason to widen the search rather than continue tightening indefinitely.

**Relationship to clustering.** The optimisation process now uses clustering ideas in a practical sense. Repeated strong neighbouring observations suggest local concentration. Isolated observations are treated more cautiously because they may represent noise. F5 illustrates boundary tightening around a well-supported region. F4 and F6 illustrate separation, where a deteriorating point moves away from the better-performing neighbourhood and prompts a change of direction.

**Expected visual patterns and next actions.** If the queries were plotted, I would expect F5 to form a tight concentration near the upper boundary, F7 and F8 to form compact positive groupings, and F2 to show an emerging local cluster. F1 would remain comparatively dispersed without a useful output gradient. F4 and F6 would show recent points moving away from better earlier regions. These patterns help determine whether the next step should stay local, test a boundary or deliberately increase exploratory distance.

## Week 10 Results

| Function | Week 10 input | Week 10 output | Interpretation |
| --- | --- | ---: | --- |
| Function 1 | 0.450000,0.650000 | 2.8950706668499033e-23 | Near zero, broader exploration still required |
| Function 2 | 0.700000,0.955000 | 0.5311818841205426 | Improved positive result |
| Function 3 | 0.280000,0.875000,0.315000 | -0.08697581687486715 | Improved within the negative region |
| Function 4 | 0.290000,0.730000,0.690000,0.210000 | -13.483642655031158 | Declined and requires reassessment |
| Function 5 | 0.120000,0.997000,0.999800,0.999800 | 4394.868042481448 | Stable leading result |
| Function 6 | 0.260000,0.780000,0.260000,0.840000,0.300000 | -1.2283806967341901 | Small decline and requires reassessment |
| Function 7 | 0.060000,0.500000,0.250000,0.220000,0.430000,0.740000 | 1.285160161342515 | Positive but slightly lower |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.470000,0.875000,0.575000,0.985000 | 9.4646525 | Stable positive region with a small decline |

## Week 09 to Week 10 comparison

| Function | Week 09 output | Week 10 output | Change | Direction |
| --- | ---: | ---: | ---: | --- |
| F1 | -1.4546199699251391e-58 | 2.8950706668499033e-23 | approximately +2.8951e-23 | Improved, but effectively zero |
| F2 | 0.47297842839949866 | 0.5311818841205426 | +0.05820345572104394 | Improved |
| F3 | -0.1156707106126581 | -0.08697581687486715 | +0.02869489373779095 | Improved |
| F4 | -11.788939969158545 | -13.483642655031158 | -1.694702685872613 | Declined |
| F5 | 4394.868042481448 | 4394.868042481448 | 0 | Unchanged, repeatability evidence |
| F6 | -1.1733030029888645 | -1.2283806967341901 | -0.0550776937453256 | Declined |
| F7 | 1.314307996450604 | 1.285160161342515 | -0.029147835108089 | Declined |
| F8 | 9.4709436 | 9.4646525 | -0.0062911 | Declined |

## Documentation

- [Datasheet](DATASHEET.md)
- [Model Card](MODEL_CARD.md)
- [Dataset Record](DATASET.md)
- [Assumptions](ASSUMPTIONS.md)
- [Validation Record](VALIDATION.md)
- [Decision Card](DECISION_CARD.md)
- [Evidence and Provenance Matrix](EVIDENCE_PROVENANCE.md)
- [Reproducibility Checklist](REPRODUCIBILITY_CHECKLIST.md)
- [Negative Evidence and Failed Hypotheses](NEGATIVE_EVIDENCE.md)
- [Documentation Changelog](CHANGELOG.md)
- [Research Note](RESEARCH_NOTE.md)

The submitted inputs and returned results remain the authoritative numerical record for Week 10. The clustering interpretation and switching triggers provide an analytical framework for explaining the Week 11 strategy. They do not alter the historical observations.