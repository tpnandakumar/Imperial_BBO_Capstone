# Surrogate Function Evaluator Model Card

## Model purpose

The Surrogate Function Evaluator is a post capstone research extension for the Imperial BBO project. Its purpose is to approximate each of the eight hidden objective functions from the verified thirteen round input output history and to support further candidate generation inside the Advanced Extension Series.

It is not intended to recreate or claim access to the original hidden Imperial objective functions.

## Separation from assessed capstone

Weeks 01 to 13 remain the official optimisation record. No surrogate prediction is written back into those folders as though it were an observed result. All predicted values and post capstone candidate coordinates remain inside `Advanced_Extension_Series/Surrogate_Function_Evaluator` or later `Optimisation_Extension_XX` folders.

## Inputs

Each function uses its own historical coordinates and outputs:

- F1: 2 dimensions
- F2: 2 dimensions
- F3: 3 dimensions
- F4: 4 dimensions
- F5: 4 dimensions
- F6: 5 dimensions
- F7: 6 dimensions
- F8: 8 dimensions

The current modelling table contains thirteen weekly observations per function. The original complete Imperial starter arrays are not currently stored in the repository and are therefore excluded from the first surrogate experiment.

## Outputs

The evaluator produces:

- leave one out validation metrics for each candidate model family
- one preferred surrogate family per function
- a cautious validation confidence label
- predicted responses for post capstone candidates
- distance from each candidate to the nearest historically observed coordinate
- predicted gain over the strongest verified historical output
- separate exploitation and exploration candidate rankings

Predictions are clearly labelled as predictions.

## Candidate model families

The current comparison includes Gaussian Process regression with Matérn and RBF kernels, Random Forest regression, Extra Trees regression, distance weighted nearest neighbours and, where the available sample supports it, a quadratic ridge response surface.

The same winning model is not assumed for all functions.

## Validation

Leave one observation out cross validation is used because the data set is extremely small. Every historical observation is held out once and predicted from the remaining twelve observations.

The primary selection metric is RMSE. MAE, median absolute error, maximum absolute error and RMSE relative to the observed output range are retained as secondary evidence.

Training fit is not used as the main selection criterion because a flexible surrogate can fit sparse observations while extrapolating poorly.

## Confidence screening

The model selection table uses a deliberately simple screening interpretation based on held out RMSE relative to the observed output range:

- relative RMSE <= 0.10: higher surrogate confidence
- relative RMSE > 0.10 and <= 0.25: moderate surrogate confidence
- relative RMSE > 0.25: low surrogate confidence

These labels are research aids, not calibrated probabilities.

## Special handling of F6

F6 contains repeated recorded coordinates with different returned values. This means that a strict deterministic interpolation assumption is unsafe for that function.

Gaussian Process models include an explicit noise component. Other model families retain repeated observations as separate evidence. Candidate selection for F6 should therefore emphasise uncertainty and repeatability rather than simply taking the highest single prediction.

## Extrapolation safeguard

Post capstone candidate search includes a penalty based on the Euclidean distance from the nearest observed point. This prevents a high surrogate prediction in a remote, unsupported region from automatically being treated as the preferred candidate.

The candidate table reports this distance so that an assessor or researcher can distinguish interpolation from aggressive extrapolation.

## Intended use

Appropriate uses include:

- comparing how predictable the eight hidden landscapes appear from sparse observations
- generating post capstone optimisation hypotheses
- studying exploration versus exploitation decisions
- comparing manual strategy progression with model based candidate selection
- examining the effect of dimensionality on surrogate reliability
- deciding when further extension is no longer justified

## Uses outside scope

The evaluator should not be used to:

- claim the exact mathematical form of any Imperial hidden function
- replace a genuine returned BBO output with a prediction
- rewrite Weeks 01 to 13
- claim a global optimum without genuine evaluation or sufficiently strong validation
- treat a predicted candidate as a verified winner

## Winner definition

A final winner for a function should be separated into two possible categories:

1. **Verified winner**: strongest coordinate supported by genuine black box output evidence.
2. **Surrogate extension winner**: strongest post capstone coordinate supported by the surrogate and its validation evidence but not independently evaluated by the hidden objective.

Those categories must never be conflated.

## Stop decision

The extension should stop for a function when the active search no longer produces a meaningful predicted improvement, predictive uncertainty is adequately resolved for the available evidence, neighbouring alternatives are weaker, and any apparent improvement does not depend mainly on unsupported extrapolation.

For functions with noisy or inconsistent repeated observations, repeatability must also be considered before declaring the extension complete.

## Known limitations

The principal limitation is data scarcity. Thirteen observations are very few for a response surface, especially in six and eight dimensions. The sequential nature of the original search also creates adaptive sampling bias because later observations were deliberately concentrated around regions that appeared promising.

Consequently, validation error and candidate distance are central to interpretation. A sophisticated surrogate does not remove the information limit imposed by sparse observations.

## Reproducibility

The scripts use a fixed random state of 42 for model and candidate generation where randomness is involved. Generated CSV outputs are intended to be committed after execution so that model selection and candidate rankings can be inspected directly.
