# SOC 1: Surrogate Optimisation Competition

## Advanced Extension Series

SOC is our post capstone surrogate competition. It begins only after the official thirteen round Imperial BBO capstone and remains completely separate from Weeks 01 to 13. Those weekly folders remain the authoritative record of submitted coordinates and returned black box outputs.

The purpose of SOC is to make several plausible surrogate models compete for each of Functions 1 to 8. The competition is decided by predictive performance on held out historical observations rather than by training fit or model complexity.

The winning surrogate for each function becomes the model used to generate candidates for the Advanced Extension Series. A surrogate prediction is never presented as a genuine Imperial objective value.

## Research question

Can the thirteen round input output history support a useful empirical approximation for each hidden objective function, and which surrogate family predicts unseen historical observations most reliably for each function?

The second question is operational: once a winning surrogate is identified, can it improve the next Explore, Exploit and Extend decisions compared with manual extrapolation alone?

## SOC competition pathway

**Observed 13 round evidence -> competing surrogate models -> leave one out validation -> predictive ranking -> winning surrogate per function -> candidate generation -> Optimisation Extension series -> validate -> winner -> stop**

SOC therefore precedes the optimisation extension runs. The competition chooses the evaluator. The Optimisation Extension series uses that evaluator to search for one defensible winning coordinate per function.

## Evidence boundary

The primary evidence set contains the verified weekly coordinates and returned values from Weeks 01 to 13. Weeks 01 to 11 are recovered from the exact history already stored in the repository. Weeks 12 and 13 are read directly from their verified input and result CSV files.

The Week 01 README records the strongest starter coordinate supplied by Imperial for each function. The original complete starter arrays are not currently stored in this repository, so they are not reconstructed or invented. If those arrays are recovered later, they can be added as a separate evidence layer and SOC can be rerun.

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

All coordinates remain inside the original [0, 1] domain.

## Competing surrogate families

SOC compares multiple model families rather than forcing one model across all eight functions:

1. Gaussian Process regression with a Matern kernel.
2. Gaussian Process regression with an RBF kernel.
3. Radial basis function interpolation where numerically feasible.
4. Quadratic response surfaces where the number of observations supports the fitted terms.
5. Random Forest regression.
6. Extra Trees regression.
7. Distance weighted nearest neighbour regression as a conservative local baseline.

The sample is sparse, particularly for the higher dimensional functions, so greater model complexity is not treated as evidence of superiority.

## Competition scoring

Each function is evaluated independently using leave one observation out cross validation. Every observation is held out once and predicted from the remaining historical observations.

SOC records:

- mean absolute error
- root mean squared error
- median absolute error
- maximum absolute error
- error relative to the observed response range
- model rank for that function

The primary ranking metric is held out RMSE. MAE, stability, extrapolation behaviour and model simplicity are secondary checks.

A model that fits the training observations exactly but performs poorly on held out points loses the competition.

## SOC winner rule

There is one surrogate winner per function. F1 to F8 do not compete against one another because they represent separate objective functions on different scales.

A surrogate wins its function when it has the strongest defensible held out predictive performance and does not rely on unstable or unsupported extrapolation. If two models are effectively tied, the simpler or more conservative model is preferred.

A low validation error does not by itself prove that the hidden function has been recovered. SOC selects the best available approximation from the competing models.

## F6 noise aware competition

F6 requires separate treatment because the same recorded coordinate has returned different objective values across rounds. A strict deterministic interpolation assumption is therefore unsafe.

For F6, Gaussian Process competitors include an observation noise component. Other competitors retain duplicate observations as separate evidence. SOC judges F6 on predictive performance while preserving the observed response variability rather than averaging it away without explanation.

## Candidate generation after SOC

Once a winning surrogate is selected, the next stage uses three complementary candidate sources:

- global space filling exploration across [0, 1]^d
- local exploitation around the strongest verified coordinate
- directional or boundary extension when the historical trajectory still supports movement

Predicted gain is considered together with distance from observed data and, where available, predictive uncertainty. Remote high predictions are penalised rather than automatically accepted.

## Relationship to the Advanced Extension Series

The lifecycle is:

**SOC -> Explore -> Exploit -> Extend -> Eliminate -> Validate -> Winner -> Stop**

SOC identifies the most defensible surrogate evaluator for each function. Optimisation Extension 1 then uses those winners to generate the first post capstone candidate set. Subsequent optimisation extensions continue only where evidence justifies further work.

## Current function status entering SOC

| Function | Capstone status | SOC purpose |
| --- | --- | --- |
| F1 | Best retained | Test whether the apparent plateau is predictable and whether reopening is justified |
| F2 | Week 13 below Week 12 peak | Model the local peak and recovery region |
| F3 | New Week 13 best | Test whether the improving direction can be extended |
| F4 | Best retained | Test basin stability and whether further movement has expected value |
| F5 | New Week 13 best | Model the continuing boundary improvement |
| F6 | New Week 13 best with response variability | Compete noise aware surrogates and resolve uncertainty |
| F7 | Best retained | Validate the current local winner and stop unless a credible improvement appears |
| F8 | Best retained | Validate stability and stop unless the surrogate provides strong evidence to reopen |

## Files

- `build_surrogate_dataset.py` reconstructs the verified thirteen round modelling table.
- `surrogate_evaluator.py` runs the SOC model competition and ranks surrogate families by held out performance.
- `advanced_candidate_search.py` uses each SOC winning surrogate to generate post capstone Explore, Exploit and Extend candidates.
- `SOC_MODEL_CARD.md` records intended use, limits, uncertainty and stopping safeguards.
- `requirements.txt` records the software dependencies.

## Interpretation

SOC deliberately steps beyond the original capstone without changing it. The competition asks how much of each hidden response surface can be inferred from sparse sequential observations and whether one modelling family consistently predicts the historical landscape better than alternatives.

The output of SOC is not a claim that the Imperial functions have been reverse engineered exactly. It is a reproducible competition that selects the strongest surrogate approximation available from the observed evidence.