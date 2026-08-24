# Surrogate Function Evaluator

## Advanced Extension Series

This experiment begins after completion of the official thirteen round Imperial BBO capstone. It does not alter, reinterpret or replace Weeks 01 to 13. Those folders remain the authoritative record of the submitted coordinates and returned black box outputs.

The purpose here is different. The thirteen rounds are treated as an observed input output sample from each hidden objective function. Separate surrogate models are then fitted to Functions 1 to 8 to estimate the response surface that may have generated those observations.

The resulting models are **predicted functions**, not recovered Imperial functions. With only thirteen weekly evaluations per function, many mathematical functions can agree with the observed data. A surrogate can therefore support interpolation, uncertainty analysis and candidate generation, but it cannot establish the exact hidden objective.

## Research question

Can the complete thirteen round history support a useful empirical evaluator for each hidden function, and can that evaluator identify post capstone candidate coordinates that are more defensible than manual extrapolation alone?

A second question follows naturally: if several plausible surrogate families are compared rather than selecting one convenient model, which functions appear sufficiently predictable to justify computational extension and which remain too uncertain for confident extrapolation?

## Evidence boundary

The primary evidence set contains the verified weekly coordinates and returned values from Weeks 01 to 13. Weeks 01 to 11 are recovered from the exact history file already stored in the repository. Weeks 12 and 13 are read directly from their verified input and result CSV files.

The Week 01 README also records the strongest starter coordinate supplied by Imperial for each function. The original complete starter arrays are not currently stored in this repository, so they are not silently reconstructed or invented. If those arrays are recovered later, they can be added as a separately identified evidence layer and the surrogate comparison rerun.

## Function dimensions

| Function | Dimensions |
| --- | ---: |
| F1 | 2 |
| F2 | 2 |
| F3 | 3 |
| F4 | 4 |
| F5 | 4 |
| F6 | 5 |
| F7 | 6 |
| F8 | 8 |

All coordinates remain within the original [0, 1] domain.

## Model families

The evaluator deliberately compares several surrogate families instead of assuming that one architecture is suitable for all eight functions:

1. Gaussian Process regression with a Matérn kernel.
2. Gaussian Process regression with an RBF kernel.
3. Radial basis function interpolation where numerically feasible.
4. Quadratic response surfaces where the sample size supports the number of fitted terms.
5. Random Forest regression as a nonlinear tree based comparison.
6. Extra Trees regression as a second tree based comparison.
7. Distance weighted nearest neighbour regression as a conservative local baseline.

The available sample is very small relative to the dimensionality of F5 to F8. Complex models are therefore not automatically preferred. Predictive validation is more important than training fit.

## Validation design

Each function is evaluated independently using leave one observation out cross validation. For each held out historical point, the model is trained on the remaining observations and asked to predict the unseen output.

The comparison records:

- mean absolute error
- root mean squared error
- median absolute error
- maximum absolute error
- rank of each surrogate family for that function

A model that interpolates the training data perfectly but predicts held out observations poorly is not considered a reliable evaluator.

## Duplicate coordinates and response variability

Duplicate coordinates are retained because they are evidence. F6 is especially important because the same recorded coordinate has returned different values on different rounds. The modelling workflow therefore does not assume that every objective is perfectly deterministic.

For Gaussian Process models, a small observation noise term is estimated or supplied rather than forcing exact interpolation. For other models, repeated coordinates remain separate observations so that prediction error reflects the observed variability.

## Surrogate selection

The winning surrogate for each function is selected primarily by leave one out RMSE, with MAE and stability used as secondary checks. If two models are effectively tied, the simpler or more conservative model is preferred.

A model is not promoted to the optimisation stage merely because it has the lowest error. The validation report also considers whether error is acceptably small relative to the observed output range and whether the proposed optimum lies close to or far outside the sampled region.

## Post capstone optimisation

Once a surrogate is accepted for a function, optimisation proceeds only inside the **Advanced Extension Series**. It is never labelled Week 14.

The research lifecycle is:

**Explore -> Exploit -> Extend -> Eliminate -> Validate -> Winner -> Stop**

Candidate generation combines three searches:

- global space filling candidates across [0, 1]^d
- local perturbations around the best verified coordinate
- boundary candidates when historical evidence shows continuing improvement towards a boundary

The surrogate predicts a mean response for each candidate. Gaussian Process models additionally provide predictive uncertainty. The extension engine keeps exploitation candidates with high predicted response and exploration candidates where uncertainty remains informative.

## Stopping rule

Each function is handled separately. The extension stops when one winning coordinate remains and further search no longer has a defensible expected benefit.

A function can stop when all of the following are satisfied:

1. the winning coordinate is the strongest verified or surrogate supported candidate within the resolved region
2. nearby candidates fail to produce a meaningful predicted improvement
3. uncertainty around the candidate is sufficiently small for the available evidence
4. the candidate is not being preferred solely because the surrogate extrapolates far beyond sampled data
5. repeated or noisy observations, where present, have been explicitly considered

Stopping is therefore an optimisation decision rather than an arbitrary limit on the number of extensions.

## Current function status before surrogate fitting

| Function | Capstone status | Extension interpretation |
| --- | --- | --- |
| F1 | Best retained | Validate plateau and local basin before reopening |
| F2 | Week 13 below Week 12 peak | Active local recovery problem |
| F3 | New Week 13 best | Active directional extension problem |
| F4 | Best retained | Validate basin and stop unless surrogate finds credible improvement |
| F5 | New Week 13 best | Active boundary extension problem |
| F6 | New Week 13 best with repeated input variability | Active uncertainty and repeatability problem |
| F7 | Best retained | Validate local winner and stop unless evidence justifies reopening |
| F8 | Best retained | Validate stability and stop unless evidence justifies reopening |

## Files

- `build_surrogate_dataset.py` reconstructs the thirteen round modelling table from verified repository files.
- `surrogate_evaluator.py` compares model families by leave one out validation and identifies the preferred surrogate for each function.
- `advanced_candidate_search.py` uses the selected surrogate to generate post capstone candidates while preserving the separation from the official capstone.
- `SURROGATE_MODEL_CARD.md` records intended use, limits, uncertainty and stopping safeguards.

## Interpretation

This extension deliberately steps beyond the original capstone without pretending to know the hidden functions. The scientific value lies in asking how much of each response surface can be inferred from sparse sequential observations, how prediction quality changes with dimensionality, and whether an explicit surrogate would have changed the next decision.
