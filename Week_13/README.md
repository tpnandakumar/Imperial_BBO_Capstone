# Week_13

## Bayesian Black Box Optimisation Portfolio

### Final Round Analysis

## Documentation

- [Verified Week 13 Inputs](week_13_inputs.csv)
- [Verified Week 13 Results](week_13_results.csv)
- [Week 13 Analysis Summary](week_13_analysis_summary.csv)
- [Week 13 Figure Data Summary](week_13_figure_data_summary.csv)
- [Final Analysis Code](week_13_analysis.py)
- [Figure Generation Code](generate_week_13_figures.py)
- [Final Strategy Outcome](FINAL_STRATEGY_OUTCOME.md)
- [RL, MAB, MDP and Q Learning Review](RL_MAB_MDP_QLEARNING_REVIEW.md)
- [Validation Record](VALIDATION.md)

The input and result files are the authoritative numerical record for the final competition round. All comparisons below are derived from those verified values and the committed Weeks 1 to 12 history. No source value has been rounded, shortened or reconstructed from an estimate.

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

Week 13 completed the thirteen round black box optimisation sequence. The final submission did not use one common step size or one common rule. Four functions repeated the Week 12 coordinate exactly, two made small local moves, Function 5 made a tightly controlled boundary adjustment, and Function 6 repeated the Week 12 coordinate because the response at that point required further confirmation.

The final round produced new overall best outputs for Functions 3, 5 and 6. Functions 1, 4, 7 and 8 retained their established best values exactly. Function 2 declined from its Week 12 peak after a small local move. This gives the final dataset both successful exploitation and useful negative evidence.

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

The final comparison is clearer when objective change is considered alongside the amount of movement in the input vector. L1 movement is the sum of the absolute coordinate changes. Squared Euclidean movement is retained exactly without taking a square root.

| Function | Week 12 output | Week 13 output | Exact change | L1 movement | Squared Euclidean movement |
| --- | ---: | ---: | ---: | ---: | ---: |
| Function 1 | `0.025559285339829783` | `0.025559285339829783` | `0` | `0` | `0` |
| Function 2 | `0.7335252043269003` | `0.6413430885133908` | `-0.0921821158135095` | `0.005000` | `0.000025000000` |
| Function 3 | `-0.05985127532683556` | `-0.05685061601567621` | `0.00300065931115935` | `0.015000` | `0.000075000000` |
| Function 4 | `-4.359874926582439` | `-4.359874926582439` | `0` | `0` | `0` |
| Function 5 | `4427.343995806448` | `4440.957216598753` | `13.613220792305` | `0.011001` | `0.000100998003` |
| Function 6 | `-0.7078316130911375` | `-0.6071562248604215` | `0.1006753882307160` | `0` | `0` |
| Function 7 | `1.3809299933612855` | `1.3809299933612855` | `0` | `0` | `0` |
| Function 8 | `9.58024` | `9.58024` | `0` | `0` | `0` |

Function 2 moved only `0.005000` in one coordinate and deteriorated. Function 3 moved `0.005000` in each of three coordinates and improved. Function 5 made a small structured four coordinate adjustment and improved substantially. Function 6 did not move at all, yet its output changed by `0.1006753882307160`.

## 4. Function by Function Outcome

### Function 1

The final query repeated `0.600000,0.600000` and again returned `0.025559285339829783`, matching the best value already seen in Weeks 3, 11 and 12. This strengthens the evidence that the tested point is repeatable.

### Function 2

Week 12 produced the best observed value at `0.690000,0.950000`, returning `0.7335252043269003`. Week 13 changed only the first coordinate to `0.685000`. The output fell to `0.6413430885133908`, an exact change of `-0.0921821158135095`. The previous local improvement therefore did not continue through another step in the same direction.

### Function 3

The final input moved from `0.850000,0.150000,0.850000` to `0.855000,0.145000,0.855000`. The L1 movement was `0.015000`. The output improved from `-0.05985127532683556` to `-0.05685061601567621`, an exact gain of `0.00300065931115935` and a new overall best.

### Function 4

Function 4 repeated `0.600000,0.430000,0.420000,0.250000` and returned `-4.359874926582439` again. This value was first observed in Week 1 and recovered in Week 12. Week 13 reproduced it for a third time at the same coordinate.

### Function 5

Week 12 used `0.100000,0.999000,1.000000,1.000000`. Week 13 changed this to `0.090000,0.999999,0.999999,0.999999`. The first coordinate fell by `0.010000`, the second moved closer to the upper boundary by `0.000999`, and the third and fourth moved `0.000001` away from the exact boundary. The L1 movement was `0.011001` and the squared Euclidean movement was `0.000100998003`.

The output increased from `4427.343995806448` to `4440.957216598753`, an exact gain of `13.613220792305`. This was a new overall best. The result supports the broader boundary focused pattern, but it also shows that the useful move was not simply to push every coordinate monotonically towards `1.000000`.

### Function 6

Function 6 repeated the Week 12 coordinate exactly: `0.700000,0.200000,0.700000,0.700000,0.200000`. Despite zero input movement, the output changed from `-0.7078316130911375` to `-0.6071562248604215`, an exact improvement of `0.1006753882307160`.

The same coordinate produced `-0.648848297397347` in Week 3. The history therefore establishes non identical repeated evaluations at this coordinate. It does not establish whether the cause is stochasticity, hidden state, evaluator variation or another mechanism not represented by the submitted coordinates.

### Function 7

Function 7 retained `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` and again returned `1.3809299933612855`. This matches the best value seen in Week 5 and Week 12.

### Function 8

Function 8 again used `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` and returned `9.58024`. The same result was seen in Weeks 1, 11 and 12, giving a fourth exact confirmation at this point.

## 5. Final Strategy Assessment

The final round supports four clear strategy lessons. Repeating a confirmed best point worked for Functions 1, 4, 7 and 8. Small local refinement remained useful for Function 3. The Function 2 decline showed that a local trend can stop after a very small further step. Function 5 showed that controlled boundary refinement can remain productive when the historical evidence is strong.

Function 6 adds a separate lesson. A better observed value at the same coordinate is evidence about response variability, not evidence that a coordinate change caused the improvement.

## 6. Exploration and Exploitation

There was no later competition query available to recover from an unsuccessful final experiment, so broad exploration carried a higher cost than in earlier rounds. This shifted the portfolio towards exploitation, but the degree of exploitation still differed by function.

Functions 1, 4, 7 and 8 used direct exploitation. Function 6 repeated a known point to test response consistency. Functions 2 and 3 used small local moves. Function 5 continued a boundary focused refinement because the history still supported movement in that region.

## 7. Reward Based Interpretation

The reinforcement learning material provides a useful language for reviewing the sequence. Each submitted coordinate can be viewed as an action and each returned objective as a reward. The information available after each round changes what should be attempted next.

A multi armed bandit analogy helps with the exploration and exploitation trade off, but each function has a continuous coordinate space rather than a small fixed set of arms. A Markov decision process analogy is useful if the state is treated as the accumulated knowledge about the function. Q learning is less directly suited to this dataset because there are too few repeated state and action visits to estimate a stable action value table.

## 8. Repeatability and Response Variability

Functions 1, 4, 7 and 8 repeated the Week 12 input exactly and reproduced the Week 12 output exactly. Their final query movement was `0` and their objective change was also `0`.

Function 6 also repeated the Week 12 input exactly, but its objective changed by `0.1006753882307160`. The same coordinate returned:

- Week 3: `-0.648848297397347`
- Week 12: `-0.7078316130911375`
- Week 13: `-0.6071562248604215`

Repeatability therefore has to be assessed function by function rather than assumed across the whole portfolio.

## 9. Progress Across Thirteen Rounds

Function 5 produced the clearest sustained numerical gain, rising from `1415.8763939603884` in Week 1 to `4440.957216598753` in Week 13. Functions 2, 3, 6 and 7 also ended substantially stronger than many of their early observations, although their trajectories were less smooth.

Functions 1, 4 and 8 followed a different pattern. Their strongest values appeared early, were lost during later exploration and were eventually recovered. The full history therefore remained useful both for deciding where to continue and for deciding where to return.

## 10. What Worked and What Did Not

Retaining exact historical values prevented strong early regions from being forgotten. Clustering helped describe repeated local behaviour without overstating certainty from a small sample. PCA helped describe concentration in the submitted higher dimensional trajectories, but it was not treated as a direct gradient of the hidden objective.

The final round reinforces that caution. Function 5 showed that a concentrated trajectory can align with continued improvement. Function 2 showed that recent local improvement does not guarantee another nearby step will help. Function 6 showed that identical coordinates do not necessarily imply identical outputs.

## 11. Computational Analysis

`week_13_analysis.py` rebuilds the thirteen round record from the committed exact history for Weeks 1 to 11 and the verified Week 12 and Week 13 files. It validates the eight functions, dimensions and input bounds before calculating the final summary.

The script uses `Decimal` arithmetic for output change, L1 input movement and squared Euclidean movement. It identifies the best observed output and every round in which that best occurred. It also checks the complete history for repeated coordinates with non identical outputs.

`generate_week_13_figures.py` writes `week_13_figure_data_summary.csv` and creates five figures directly inside `Week_13`. Floating point conversion is used only for plotting.

## 12. Reproducibility

From the repository root:

```bash
python Week_13/week_13_analysis.py
python Week_13/generate_week_13_figures.py
```

The analysis uses `PFRAMOS/data/recovered_exact_history.csv` for Weeks 1 to 11 together with the verified Week 12 and Week 13 input and result files. It does not infer missing values. The core Week 13 record remains flat and no separate figures directory is required.

## 13. Overall Capstone Findings

The useful search structure was function specific. Some functions benefited from progressive movement, some from recovery to an earlier point, and some from repeated confirmation. Structural methods were most useful when their interpretation was checked against the actual objective values.

The final record also shows that repeatability cannot be assumed across every function because Function 6 returned different outputs at the same submitted coordinate. These findings describe the observed search history. They do not reveal the hidden objective equations and they do not prove that the best observed coordinates are global optima.

## 14. Final Status

All thirteen competition query rounds are complete. Week 13 produced new overall best outputs for Functions 3, 5 and 6. Functions 1, 4, 7 and 8 retained their best observed values. Function 2 ended below its Week 12 best after a small final local move.

Further work belongs to evaluation, reflection, visualisation and clearly separated post capstone research. No later experiment should be presented as an additional competition result.

## 15. References

1. `Week_13/week_13_inputs.csv`, verified final round inputs.
2. `Week_13/week_13_results.csv`, verified final round outputs.
3. `Week_12/week_12_inputs.csv` and `Week_12/week_12_results.csv`, verified preceding round record.
4. `PFRAMOS/data/recovered_exact_history.csv`, committed exact Weeks 1 to 11 history.
5. `Week_11/PCA_STRATEGY_COMPARISON.md` and `Week_11/WEEK_12_DECISION_RECORD.md`.
6. Module 24 course material covering reinforcement learning, multi armed bandits, Markov decision processes and Q learning.
