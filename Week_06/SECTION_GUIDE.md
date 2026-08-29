# Week_06

## Bayesian Black Box Optimisation Portfolio
### Week 06 Analysis

## Contents

1. Introduction
2. Week 6 Results
3. Comparison of Week 5 and Week 6 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 7 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Automation Decision
15. References

## 1. Introduction

By Week 06 I had enough observations to stop treating the eight functions as variations of the same problem. Their behaviour was clearly different. Function 5 was improving rapidly, Function 2 had responded well to refinement, Functions 7 and 8 were positive but comparatively stable, and several of the remaining functions were still difficult to read.

The practical question was therefore not simply whether to explore or exploit. It was where another query was likely to teach me something useful. I used the previous results to decide which functions justified a small local move and which still needed a wider search.

## 2. Week 6 Results

The exact returned values are preserved in `week_06_results.csv`.

| Function | Week 06 output | What I took from it |
| --- | ---: | --- |
| F1 | 0.0000000026752879910742468 | Effectively near zero and still unresolved |
| F2 | 0.5712475315739602 | Clear improvement |
| F3 | -0.3071823694141529 | Worse than Week 05 |
| F4 | -31.20347777578016 | Further deterioration |
| F5 | 3922.7652233497042 | Strong new best |
| F6 | -1.3792272680368016 | Worse than Week 05 |
| F7 | 1.3529491169887171 | Positive, with a small decline |
| F8 | 9.5148 | Small improvement in an already strong region |

The most useful result was F5. Its rise to `3922.7652233497042` strengthened the case for staying close to that region. F2 also improved markedly. In contrast, F3, F4 and F6 moved in the wrong direction, which made further movement along the same path harder to justify.

## 3. Comparison of Week 5 and Week 6 Performance

| Function | Week 05 | Week 06 | Direction |
| --- | ---: | ---: | --- |
| F1 | 0.012779642669914939 | 0.0000000026752879910742468 | Declined |
| F2 | 0.28016822307722516 | 0.5712475315739602 | Improved |
| F3 | -0.11392206377710448 | -0.3071823694141529 | Declined |
| F4 | -27.44051496086922 | -31.20347777578016 | Declined |
| F5 | 3682.2110623386798 | 3922.7652233497042 | Improved |
| F6 | -1.073875453695542 | -1.3792272680368016 | Declined |
| F7 | 1.3809299933612855 | 1.3529491169887171 | Slight decline |
| F8 | 9.5113 | 9.5148 | Slight improvement |

This was not a uniformly successful round. F2 and F5 improved substantially and F8 edged upwards, but four functions deteriorated and F7 slipped slightly. That mixed result argued against applying one search rule across the portfolio.

## 4. Query Selection Strategy

My Week 06 choices were based on the behaviour seen up to Week 05. The submitted vectors are preserved in `week_06_inputs.csv`.

F5 received the strongest exploitation bias because its recent trajectory was clearly upward. F2, F7 and F8 were treated as refinement problems because each had already produced useful positive outputs. F1, F3, F4 and F6 were less convincing, so I kept more search freedom there.

The Week 06 outputs then changed that picture. F2 supported the refinement decision. F5 strongly supported continued work near its current region. The deterioration in F3, F4 and F6 showed that exploration can be informative without being immediately successful.

## 5. Exploration vs Exploitation Analysis

The portfolio split for this round was:

- **Explore:** F1, F3, F4 and F6
- **Refine:** F2, F7 and F8
- **Exploit:** F5

I did not regard these labels as permanent. They described the action justified by the evidence available at that point. F7 is a useful example. It remained positive, but its small decline meant that refinement should stay cautious rather than becoming aggressive exploitation.

F5 was different. Its continued rise gave a stronger reason to concentrate queries around the current high performing region, while still recognising that the true global optimum was unknown.

## 6. Reflection on Week 7 Query Selection

Week 06 made the next decisions more differentiated. F5 had earned another tightly controlled local move. F2 also justified continued refinement after nearly doubling its Week 05 output.

F3, F4 and F6 required a rethink because the latest moves had reduced their objective values. I did not want to keep moving in the same direction simply because that direction had already been chosen once. F1 also remained uncertain because its value had collapsed back towards zero.

For F7 and F8, the evidence favoured small changes. Both were already in useful positive regions, but neither result justified a large jump.

## 7. Functional Ranking Evolution

The raw magnitudes cannot be used to compare the hidden functions as if they shared a common scale. Ranking is used here only as a portfolio view of the returned values.

| Rank by Week 06 returned value | Function | Output |
| ---: | --- | ---: |
| 1 | F5 | 3922.7652233497042 |
| 2 | F8 | 9.5148 |
| 3 | F7 | 1.3529491169887171 |
| 4 | F2 | 0.5712475315739602 |
| 5 | F1 | 0.0000000026752879910742468 |
| 6 | F3 | -0.3071823694141529 |
| 7 | F6 | -1.3792272680368016 |
| 8 | F4 | -31.20347777578016 |

The more useful observation was the direction of travel within each function. F5 and F2 were improving strongly. F8 was stable. F3, F4 and F6 needed a change of approach.

## 8. High Performing Region Identification

The clearest productive region was around the Week 06 F5 input `0.14, 0.97, 0.995, 0.995`. That point returned `3922.7652233497042`, improving on the Week 05 value of `3682.2110623386798`. I treated it as a strong local region, not as proof of a global optimum.

F8 also continued to return values around 9.5, while F7 remained around 1.35. F2's increase to `0.5712475315739602` made its local neighbourhood more interesting than it had been a week earlier.

## 9. Decision Matrix and Resource Allocation

| Function | Week 06 evidence | Next emphasis |
| --- | --- | --- |
| F1 | Fell back to near zero | Explore |
| F2 | Strong improvement | Refine |
| F3 | Deteriorated | Redirect exploration |
| F4 | Deteriorated further | Redirect exploration |
| F5 | Strong new best | Exploit carefully |
| F6 | Deteriorated | Redirect exploration |
| F7 | Positive with a small decline | Refine cautiously |
| F8 | Positive with a small improvement | Refine cautiously |

The limited query budget made selective attention important. F5 deserved protection because it was producing the largest gains in its own trajectory. At the same time, concentrating every uncertain query near known regions would have increased the risk of premature convergence.

## 10. Information Gain Analysis

Week 06 was useful precisely because the results were mixed. F2 and F5 showed where local concentration was paying off. F3, F4 and F6 showed where the latest direction had not worked. F1 showed that a seemingly reasonable point could still return almost no signal.

A poor query was not a desirable outcome, but once observed it reduced the value of repeating the same local assumption. Each returned value changed the next decision.

## 11. Computational Analysis and Coding Implementation

The Week 06 folder includes `week_06_analysis.py` and `generate_week_06_figures.py`. The analysis script reads the stored inputs and outputs, compares the current round with Week 05 and produces the supporting summary data. The figure script creates the visual material used in the weekly analysis.

The code is supporting evidence rather than a substitute for the competition record. The submitted vectors and returned outputs remain the primary numerical sources.

## 12. Repository Files and Reproducibility

The principal Week 06 files are:

- `README.md`
- `week_06_inputs.csv`
- `week_06_results.csv`
- `week_06_analysis_summary.csv`
- `week_06_figure_data_summary.csv`
- `week_06_analysis.py`
- `generate_week_06_figures.py`

The validation experiment is documented separately under `Experiments/WEEK_06_VALIDATION/`.

## 13. Conclusion

Week 06 did not simply confirm the existing strategy. It separated the functions more clearly. F5 and F2 strengthened the case for local refinement, F8 remained steady, and F3, F4 and F6 showed that their current directions needed reconsideration.

The main lesson I carried forward was that the strategy had to change when the evidence changed. The limited query budget made that more important than maintaining a uniform optimisation rule across all eight functions.

## 14. Automation Decision

The analysis was automated where calculation and repeatability benefited from code, including reading stored results, comparing rounds and generating figures. Query selection remained a human decision informed by those outputs.

That separation reduced clerical error and made the numerical analysis reproducible, while the final choice of where to query still required judgement about uncertainty, recent movement and the value of exploration.

## 15. References

- Imperial College Business School, Artificial Intelligence and Machine Learning Programme, Black Box Optimisation capstone materials.
- Frazier, P. I. (2018). A Tutorial on Bayesian Optimization. arXiv:1807.02811.
- Shahriari, B., Swersky, K., Wang, Z., Adams, R. P. and de Freitas, N. (2016). Taking the Human Out of the Loop: A Review of Bayesian Optimization. Proceedings of the IEEE, 104(1), 148 to 175.

