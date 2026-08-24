# SOC Model Card

## Model purpose

SOC, the Surrogate Optimisation Competition, is a post capstone research extension for the Imperial BBO project. Its purpose is to make several surrogate model families compete independently for each of the eight hidden objective functions using the verified thirteen round input output history.

SOC does not claim to recreate or reveal the original hidden Imperial functions. It selects the strongest available empirical approximation for each function from the evidence that is actually available.

## Separation from the assessed capstone

Weeks 01 to 13 remain the official optimisation record. No SOC prediction is written back into those folders as though it were an observed result. All model rankings, predictions and post capstone candidates remain inside `Advanced_Extension_Series/SOC_Surrogate_Optimisation_Competition` or later `Optimisation_Extension_XX` folders.

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

The first SOC run uses thirteen weekly observations per function. The original complete Imperial starter arrays are not currently stored in the repository and are therefore excluded rather than reconstructed.

## Competition outputs

SOC produces:

- leave one out validation metrics for each competing surrogate family
- one SOC winning surrogate per function
- a cautious validation confidence label
- predicted responses for post capstone candidates
- distance from each candidate to the nearest historical observation
- predicted gain over the strongest verified historical output
- separate exploration and exploitation candidate rankings

Predicted values remain explicitly labelled as predictions.

## Competing model families

The competition includes Gaussian Process regression with Matern and RBF kernels, Random Forest regression, Extra Trees regression, distance weighted nearest neighbours and, where the sample supports it, a quadratic ridge response surface.

The same model is not assumed to win for every function.

## Competition validation

Leave one observation out cross validation is used because the evidence set is small. Each historical observation is held out once and predicted from the remaining twelve observations.

The primary SOC selection metric is RMSE. MAE, median absolute error, maximum absolute error, error relative to the historical response range, stability and model simplicity are retained as secondary evidence.

Training fit is not the main competition criterion because a flexible surrogate can fit sparse observations while predicting unseen points poorly.

## Confidence screening

The first SOC implementation uses a deliberately simple held out RMSE interpretation relative to the observed output range:

- relative RMSE <= 0.10: higher surrogate confidence
- relative RMSE > 0.10 and <= 0.25: moderate surrogate confidence
- relative RMSE > 0.25: low surrogate confidence

These labels are research aids rather than calibrated probabilities.

## Special handling of F6

F6 contains repeated recorded coordinates with different returned values. This makes strict deterministic interpolation unsafe.

Gaussian Process competitors include an explicit noise component. Other competitors retain repeated observations as separate evidence. Candidate selection for F6 therefore emphasises predictive uncertainty and repeatability rather than the highest single predicted value alone.

## Extrapolation safeguard

Post capstone candidate search includes a penalty based on Euclidean distance from the nearest observed point. This prevents a remote high prediction from automatically becoming the preferred candidate.

Candidate tables retain this distance so interpolation, controlled extension and aggressive extrapolation can be distinguished.

## Winner definitions

Two different winner categories are preserved:

1. **SOC model winner**: the surrogate family with the strongest defensible held out predictive performance for a given function.
2. **Optimisation extension winner**: the coordinate retained at the end of the post capstone search for that function.

A surrogate extension winner is not a verified Imperial black box winner unless it receives a genuine objective evaluation.

## Intended use

SOC is designed for:

- comparing the predictability of the eight hidden landscapes
- selecting a surrogate model independently for each function
- generating post capstone optimisation hypotheses
- comparing manual strategy progression with model based candidate selection
- studying exploration, exploitation and extension under sparse evidence
- examining how dimensionality affects surrogate reliability
- defining rational stopping conditions

## Uses outside scope

SOC should not be used to:

- claim the exact mathematical form of an Imperial hidden function
- replace a genuine returned BBO output with a prediction
- rewrite Weeks 01 to 13
- claim global optimality from sparse surrogate evidence
- present a predicted candidate as an observed black box result

## Stop decision

The Advanced Extension Series should stop for a function when one defensible coordinate remains, nearby alternatives no longer offer meaningful expected improvement, predictive uncertainty is sufficiently resolved for the available evidence, and the apparent winner does not depend mainly on unsupported extrapolation.

For functions with inconsistent repeated observations, repeatability must also be addressed before closure.

## Known limitations

The main limitation is data scarcity. Thirteen observations are very few for response surface reconstruction, especially in six and eight dimensions. The original sequential search also creates adaptive sampling bias because later observations were concentrated around regions that appeared promising.

SOC therefore treats held out prediction error, candidate distance and uncertainty as central evidence. Model sophistication does not remove the information limit imposed by sparse observations.

## Reproducibility

The scripts use a fixed random state of 42 where randomness is involved. Generated CSV outputs are intended to be retained so the competition ranking and candidate selection can be inspected and reproduced.