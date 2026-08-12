# Week_09

## Bayesian Black Box Optimisation Portfolio
### Week 09 Analysis

## Documentation

- [Datasheet](DATASHEET.md)
- [Model Card](MODEL_CARD.md)
- [Dataset Record](DATASET.md)
- [Assumptions](ASSUMPTIONS.md)
- [Validation](VALIDATION.md)
- [Decision Card](DECISION_CARD.md)
- [Changelog](CHANGELOG.md)

## 1. Introduction

By Week 09, the main question was no longer where every function might be worth sampling. Several functions had developed recognisable local histories. I therefore focused on whether the strongest regions were still improving and whether recent declines were large enough to justify a change of direction.

## 2. Week 09 Results

| Function | Week 09 output |
| --- | ---: |
| F1 | -1.4546199699251391e-58 |
| F2 | 0.47297842839949866 |
| F3 | -0.1156707106126581 |
| F4 | -11.788939969158545 |
| F5 | 4394.868042481448 |
| F6 | -1.1733030029888645 |
| F7 | 1.314307996450604 |
| F8 | 9.4709436 |

F5 improved from `4359.384134322703` to `4394.868042481448`. F4 also improved slightly from `-12.305008897187289` to `-11.788939969158545`. F2, F3, F6, F7 and F8 declined. F1 again remained effectively zero.

## 3. Comparison with Week 08

The Week 09 result did not support a general claim of improvement. The useful pattern was narrower. F5 continued its sustained rise and F4 recovered slightly, while several otherwise productive functions moved down. The small F7 and F8 declines suggested caution rather than abandonment of those regions. F2's larger fall deserved closer attention.

## 4. Query Selection Strategy

F5 remained the strongest exploitation candidate because the region had improved repeatedly. F7 and F8 remained suitable for small local changes because both were still positive and relatively stable. F2 required a tighter probe rather than a large move. F3, F4 and F6 still needed function specific reassessment, while F1 remained exploratory.

## 5. Exploration and Exploitation

I used four practical actions rather than a simple two way split: explore, refine, reassess and exploit. That made it easier to distinguish a stable positive function from a function that had just deteriorated, even when both might otherwise have been labelled for local search.

## 6. Reflection on Week 10 Query Selection

The Week 09 evidence made repeatability important. F5 had reached a strong value after several gains, so repeating the exact point in Week 10 offered a direct test of whether the result was stable. For the other functions, the next query was chosen according to the size and direction of the latest change rather than rank alone.

## 7. Functional Ranking

F5 remained first by a wide margin, followed by F8, F7 and F2. F1 was effectively zero. F3, F6 and F4 remained negative. Because the objective scales differ, I used the ranking as a navigation aid rather than as a cross function performance metric.

## 8. High Performing Regions

The clearest region was F5 near the boundary. F8 and F7 also retained stable positive areas. F2 remained positive but had weakened. The evidence for the negative functions was still more about direction and recovery than about a settled high performing region.

## 9. Decision Matrix and Resource Allocation

| Function | Week 09 reading | Week 10 approach |
| --- | --- | --- |
| F1 | Repeated near zero result | Explore |
| F2 | Positive but lower | Refine carefully |
| F3 | Deteriorated | Reassess |
| F4 | Small recovery | Test revised local direction |
| F5 | New best | Repeat point to test stability |
| F6 | Deteriorated | Reassess |
| F7 | Small decline, still positive | Conservative refinement |
| F8 | Very small decline, still positive | Conservative refinement |

## 10. Information Gain Analysis

The planned F5 repeat was deliberately different from another local improvement attempt. Its purpose was to reduce uncertainty about the reliability of the strongest observed point. Elsewhere, the declines supplied negative evidence that helped determine where another local move was worth the query cost.

## 11. Computational Analysis and Coding Implementation

`week_09_analysis.py` and `generate_week_09_figures.py` provide the reproducible calculations and visual summaries. Derived CSV files are kept separate from the submitted inputs and returned outputs.

## 12. Repository Files and Reproducibility

Week 09 contains the source data, analysis code, figure data, datasheet, model card, assumptions, validation record and decision documentation. These files allow the numerical record and the interpretation to be reviewed separately.

## 13. Conclusion

Week 09 strengthened the F5 case but also showed that several positive functions could decline without losing their broader local structure. The resulting Week 10 strategy became more selective and introduced an explicit repeatability test for the strongest point.

## 14. Automation Decision

Computational analysis was used to check values, compare rounds and prepare figures. Final strategy selection remained manually supervised.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.