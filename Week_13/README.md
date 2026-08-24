# Week_13

## Bayesian Black Box Optimisation Portfolio

### Final Round Analysis

## Documentation

- [Verified Week 13 Inputs](week_13_inputs.csv)
- [Verified Week 13 Results](week_13_results.csv)
- [Week 13 Analysis Summary](week_13_analysis_summary.csv)
- [Final Strategy Outcome](FINAL_STRATEGY_OUTCOME.md)
- [RL, MAB, MDP and Q Learning Review](RL_MAB_MDP_QLEARNING_REVIEW.md)
- [Validation Record](VALIDATION.md)
- [Final Analysis Code](week_13_analysis.py)
- [Figure Generation Code](generate_week_13_figures.py)

The input and result files are the authoritative numerical record for the final round.

## Contents

1. Introduction
2. Final Round Results
3. Week 12 to Week 13 Comparison
4. Function by Function Outcome
5. Final Strategy Assessment
6. Exploration and Exploitation
7. Reward Based Interpretation
8. Repeatability and Response Variability
9. Progress Across Thirteen Rounds
10. What Worked and What Did Not
11. Computational Analysis
12. Reproducibility
13. Overall Capstone Findings
14. Final Status
15. References

## 1. Introduction

Round 13 completed the thirteen round black box optimisation sequence. The final submission was made after the Week 12 analysis had separated several distinct types of evidence: confirmed best points, local improvement, recovery towards stronger historical regions, boundary refinement and the structural information obtained from PCA. Module 24 then provided a useful decision perspective through reinforcement learning, multi armed bandits, Markov decision processes and Q learning.

These ideas were treated as ways of examining sequential decisions rather than as proof that a single reinforcement learning algorithm generated the final coordinates. That distinction matters because the capstone has a continuous action space, a very small number of observations per function and no opportunity to learn a large Q table through repeated state action visits.

The final round produced three new overall best values, retained four established best values exactly, and produced one decline from the Week 12 peak. The result therefore gives a useful final test of both exploitation and controlled local movement.

## 2. Final Round Results

| Function | Week 13 input | Week 13 output | Final position |
| --- | --- | ---: | --- |
| Function 1 | `0.600000,0.600000` | `0.025559285339829783` | Best retained exactly |
| Function 2 | `0.685000,0.950000` | `0.6413430885133908` | Below Week 12 best |
| Function 3 | `0.855000,0.145000,0.855000` | `-0.05685061601567621` | New overall best |
| Function 4 | `0.600000,0.430000,0.420000,0.250000` | `-4.359874926582439` | Best retained exactly |
| Function 5 | `0.090000,0.999999,0.999999,0.999999` | `4440.957216598753` | New overall best |
| Function 6 | `0.700000,0.200000,0.700000,0.700000,0.200000` | `-0.6071562248604215` | New overall best |
| Function 7 | `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` | `1.3809299933612855` | Best retained exactly |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` | Best retained exactly |

## 3. Week 12 to Week 13 Comparison

Exact decimal differences are retained in `week_13_analysis_summary.csv`.

| Function | Week 12 | Week 13 | Exact change |
| --- | ---: | ---: | ---: |
| Function 1 | `0.025559285339829783` | `0.025559285339829783` | `0` |
| Function 2 | `0.7335252043269003` | `0.6413430885133908` | `-0.0921821158135095` |
| Function 3 | `-0.05985127532683556` | `-0.05685061601567621` | `0.00300065931115935` |
| Function 4 | `-4.359874926582439` | `-4.359874926582439` | `0` |
| Function 5 | `4427.343995806448` | `4440.957216598753` | `13.613220792305` |
| Function 6 | `-0.7078316130911375` | `-0.6071562248604215` | `0.1006753882307160` |
| Function 7 | `1.3809299933612855` | `1.3809299933612855` | `0` |
| Function 8 | `9.58024` | `9.58024` | `0.00000` |

The final round therefore improved three functions, held four at their best values and reduced one function relative to Week 12.

## 4. Function by Function Outcome

### Function 1

The final query repeated `0.600000,0.600000`. The same output, `0.025559285339829783`, had already been observed in Weeks 3, 11 and 12. Week 13 reproduced it again. This is the strongest repeatability pattern in Function 1 and supports the decision not to risk the final query on a new region.

### Function 2

Week 12 had produced a clear new best at `0.690000,0.950000`, returning `0.7335252043269003`. Week 13 reduced the first coordinate to `0.685000` while holding the second at `0.950000`. The result fell to `0.6413430885133908`.

This is the only final round deterioration. It suggests that the profitable local movement seen from `0.695000` to `0.690000` did not continue monotonically to `0.685000`. The available evidence is consistent with a local peak near the Week 12 region, but the sparse observations do not justify a precise claim about the exact optimum.

### Function 3

The final move from `0.850000,0.150000,0.850000` to `0.855000,0.145000,0.855000` improved the result from `-0.05985127532683556` to `-0.05685061601567621`. This became the best observed value across all thirteen rounds. The result supports a small local refinement after the historical recovery achieved in Week 12.

### Function 4

The final query repeated `0.600000,0.430000,0.420000,0.250000` and returned `-4.359874926582439` again. This value had first appeared in Week 1 and was recovered in Week 12. The repeated result in Week 13 provides strong evidence that the point is stable under the observed competition conditions.

### Function 5

Function 5 produced the strongest sustained optimisation trajectory in the capstone. The final input `0.090000,0.999999,0.999999,0.999999` returned `4440.957216598753`, improving on the Week 12 value `4427.343995806448`.

The result extends the long pattern of improvement as the first coordinate was reduced and the remaining coordinates moved towards their upper boundary. The PCA analysis had already shown that the submitted Function 5 trajectory was highly concentrated in one principal direction. The final round confirms that this structural concentration was aligned with useful objective improvement in this function.

### Function 6

Function 6 returned `-0.6071562248604215`, the best value observed across all thirteen rounds. The important detail is that the Week 13 input is identical to the Week 12 input, yet the returned value changed from `-0.7078316130911375` to `-0.6071562248604215`.

The same coordinate had also returned `-0.648848297397347` in Week 3. This means Function 6 cannot be treated as perfectly repeatable at that tested point. The evidence is consistent with response variability, stochasticity or another source of non identical evaluation. The data establish the variability; they do not identify its cause.

### Function 7

The final query retained the Week 12 point and reproduced `1.3809299933612855`. This was also the best value recorded in Week 5. The repeated recovery supports the decision to exploit the known productive region rather than use the final round for a larger exploratory move.

### Function 8

Function 8 again returned `9.58024` at the same point first used in Week 1. The value was also reproduced in Weeks 11 and 12. The final result strengthens the evidence that this tested point is repeatable and remained the strongest known choice at the end of the capstone.

## 5. Final Strategy Assessment

The final round did not support a single rule for all functions. Four patterns were more useful:

1. Retain a repeatedly confirmed best point where the cost of exploration was high, as in Functions 1, 4, 7 and 8.
2. Use small local refinement where recent evidence showed a clear directional gain, as in Functions 2 and 3.
3. Continue a boundary trend where both structural and objective evidence agreed, as in Function 5.
4. Treat repeated evaluations cautiously where the same input did not always return the same value, as revealed by Function 6.

The only clear final round miss was Function 2. This is useful negative evidence because it shows why a local trend should not be assumed to continue indefinitely.

## 6. Exploration and Exploitation

The final round carried a different exploration cost from earlier rounds because there was no later query available to recover from an unsuccessful experiment. That shifted the strategy towards exploitation of known strong regions.

Functions 1, 4, 7 and 8 were therefore conservative choices. Functions 3 and 5 justified controlled movement because recent gains and structural evidence still pointed in a favourable direction. Function 2 also received a small local move, but the reward declined, showing the residual risk even when the adjustment is small.

## 7. Reward Based Interpretation

Module 24 provides a useful language for interpreting the final decision process. Each query can be viewed as an action and each returned objective as a reward. The accumulated history forms the information available before the next action is selected.

A multi armed bandit analogy is useful for the exploration and exploitation trade off, but each BBO function has a continuous coordinate space rather than a small fixed set of arms. An MDP interpretation is also informative if the state is understood as the current knowledge about the function, not simply the current coordinate.

Q learning is less directly suited to the observed data because the continuous action space and small number of visits do not provide the repeated state action coverage normally needed for a stable Q table. The capstone evidence therefore supports using reinforcement learning concepts as decision frameworks while retaining function specific numerical analysis for the actual coordinates.

## 8. Repeatability and Response Variability

The final dataset contains both repeatable and non repeatable behaviour at fixed inputs.

Functions 1, 4, 7 and 8 reproduced known best values exactly at repeated coordinates. Function 5 had also shown exact repeatability at a plateau point in Weeks 9 and 10.

Function 6 is different. The coordinate `0.700000,0.200000,0.700000,0.700000,0.200000` produced three different outputs across Weeks 3, 12 and 13: `-0.648848297397347`, `-0.7078316130911375` and `-0.6071562248604215`.

This is an important final finding. It means that repeatability should be assessed function by function rather than assumed from the behaviour of another objective.

## 9. Progress Across Thirteen Rounds

The clearest long term gain occurred in Function 5, which rose from `1415.8763939603884` in Week 1 to `4440.957216598753` in Week 13. Functions 2, 3, 6 and 7 also ended with values substantially stronger than their early observations, although their trajectories were less smooth.

Functions 1 and 8 showed a different pattern. Their strongest points appeared early and were later rediscovered and confirmed. Function 4 behaved similarly, with its Week 1 best recovered only near the end of the project.

The complete history therefore contains both optimisation by progressive movement and optimisation by recovering previously strong regions.

## 10. What Worked and What Did Not

The strongest methods were those matched to the observed behaviour of each function. Historical recovery worked well for Functions 4 and 7. Repeatability testing was valuable for Functions 1 and 8. Local refinement worked for Function 3 and failed in the final step for Function 2. Boundary refinement remained productive for Function 5.

PCA was useful for identifying concentrated query trajectories, especially Function 5, but it was not treated as direct evidence of the objective gradient. The final results support that caution. Structural concentration was informative when it agreed with objective improvement, but direct performance evidence remained necessary.

The most important unexpected result is Function 6, where the same coordinate produced different outputs. That finding places a clear limit on any analysis that assumes a deterministic response surface for every function.

## 11. Computational Analysis

`week_13_analysis.py` reads the verified weekly result files, calculates exact Week 12 to Week 13 changes with decimal arithmetic, identifies the best observed value and the week or weeks in which it occurred, and checks for repeated inputs with non identical outputs.

`generate_week_13_figures.py` prepares final round comparison figures and a complete thirteen round trajectory summary. Plotting uses floating point conversion only for visualisation. The stored source values remain unchanged.

## 12. Reproducibility

From the repository root:

```bash
python Week_13/week_13_analysis.py
python Week_13/generate_week_13_figures.py
```

The analysis expects the verified weekly result files to remain in the established Week_01 to Week_13 folders.

## 13. Overall Capstone Findings

The thirteen round record shows a clear change in decision quality over time. Early rounds relied more heavily on broad search and individual outcomes. Later rounds used historical comparison, clustering, PCA, repeatability checks and explicit strategy comparison before selecting each query.

The final evidence supports three broader conclusions. First, the useful search structure was function specific. Second, dimensional or trajectory simplification was valuable only when checked against actual objective behaviour. Third, exploitation became increasingly appropriate as the query budget narrowed, but limited local refinement still produced new best values where the evidence remained directional.

## 14. Final Status

All thirteen query rounds are complete. The final round produced new overall best values for Functions 3, 5 and 6, retained the best observed values for Functions 1, 4, 7 and 8, and ended below the Week 12 best for Function 2.

No further competition query remains. Subsequent work should therefore focus on final evaluation, reflection, visualisation and assessment documentation rather than additional optimisation claims.

## 15. References

1. Verified Week 1 to Week 13 input and output history supplied with the final round record.
2. `Week_11/PCA_STRATEGY_COMPARISON.md`.
3. `Week_11/WEEK_12_DECISION_RECORD.md`.
4. `Week_12/README.md` and Week 12 verified results.
5. Module 24 course material covering reinforcement learning, multi armed bandits, Markov decision processes and Q learning.
