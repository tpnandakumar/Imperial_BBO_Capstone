# BBD 020: F7 Discriminatory Falsification Design

## Purpose

BBD 019 showed that F7 is best reconstructed locally by the full 27-term quadratic model, with normalised chronological walk-forward MAE of approximately `0.03487`. BBD 020 asks the more demanding question: where do the surviving F7 explanations disagree most strongly?

The aim is falsification, not another retrospective fit.

## Competing explanations

The experiment compared five F7 mechanisms fitted to the thirteen-round history:

- the BBD 019 27-term quadratic ridge candidate;
- a simple linear ridge surface;
- a Matérn 2.5 Gaussian Process;
- the strongest available SOC model, `DistanceWeightedKNN`;
- the Rosenbrock-like benchmark candidate from BBD 005.

## Query search

A scrambled Sobol design explored the six-dimensional unit cube and was supplemented by all corners. Candidate points were ranked using model disagreement, maximum prediction spread and novelty relative to the historical F7 path. Spatial separation was then imposed so that the retained queries were not near-duplicates.

## Highest-value falsification point

The strongest proposed coordinate is:

`0.995702-0.280813-0.996209-0.835622-0.567576-0.879785`

Its discrimination score is approximately `5.899531`, with novelty `0.529917` and a normalised model-prediction spread of approximately `11.551954` observed F7 response ranges.

The competing predictions at that coordinate are approximately:

- BBD 019 quadratic: `4.088257`
- linear ridge: `3.623459`
- Matérn GP: `1.263479`
- SOC DistanceWeightedKNN: `1.108660`
- Rosenbrock-like benchmark: `-1.506670`

The candidate mechanisms therefore disagree not merely in magnitude but across a very wide response interval. One genuine evaluator result at this point would be highly discriminatory.

## Interpretation

If an independent black-box output were close to `4.09`, the BBD 019 quadratic would gain substantial support against the GP, SOC and benchmark alternatives. A result near `1.1` to `1.3` would instead favour the flexible local models and weaken the claim that the full quadratic is a generating mechanism. A negative result near `-1.5` would favour the Rosenbrock-like explanation and strongly falsify the current quadratic reconstruction.

The experiment also produced nine additional spatially distinct high-value coordinates. These should be treated as a sequential falsification queue rather than submitted simultaneously if evaluator access is limited. After each genuine result, all candidate models should be refitted and the next discriminatory point recalculated.

## Evidence boundary

BBD 020 produces prospective coordinates and model predictions only. It does not create or infer Imperial outputs for those coordinates. Exact F7 recovery remains false until independent evaluator observations are available.
