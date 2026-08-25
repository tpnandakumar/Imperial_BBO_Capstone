# BBD 008: Discriminatory Query Design

## Purpose

BBD 008 changes the question from *which model fits the observed history best?* to *which new coordinate would most efficiently distinguish the remaining candidate mechanisms?*

The aim is function identification rather than objective maximisation. A useful query is therefore one at which credible candidate models make materially different predictions.

## Candidate mechanisms

For each function, BBD 008 forms a compact roster from the strongest available candidates across:

- regularised degree 1 symbolic equations;
- regularised degree 2 symbolic equations;
- constrained benchmark-family reconstructions;
- SOC surrogate models, including Gaussian Processes, tree ensembles and nearest-neighbour models.

Models are ranked using the complete thirteen-round history, but structural diversity is preserved so that the final roster does not consist of several nearly identical variants of the same family.

## Candidate coordinate generation

The search domain remains the original bounded hypercube `[0,1]^d` for each function. A scrambled Sobol sequence provides deterministic space-filling coverage. Explicit boundary corners are also included because disagreement between candidate mechanisms can concentrate at the edge of the sampled domain.

## Discrimination score

For each candidate coordinate, every retained model predicts the response. BBD 008 then calculates:

- prediction standard deviation across models;
- maximum prediction spread across models;
- novelty, defined as distance from the nearest historical query.

All disagreement terms are normalised by the observed response range for the function. The final score is:

`(0.65 × prediction_std + 0.35 × prediction_spread) × (0.60 + 0.40 × novelty)`

The score therefore prioritises disagreement while giving additional value to coordinates that provide information beyond already sampled regions.

Points at which any model produces extreme numerical extrapolation beyond five observed response ranges from the historical median are excluded. This prevents unstable polynomial extrapolation from being mistaken for scientifically useful disagreement.

## Output

The experiment produces five diverse discriminatory coordinates for each of F1 to F8, together with the predictions made by every retained candidate model.

The first-ranked coordinate is the single point that would currently provide the greatest expected ability to eliminate competing mathematical explanations, if another genuine black-box evaluation were available.

## Interpretation boundary

These coordinates are **proposed identification experiments only**. They are not Imperial submissions, not observed outputs, and not evidence that the original hidden function has been recovered.

Without a new independent black-box evaluation, BBD 008 can identify the most informative unresolved experiments but cannot determine which competing mechanism is correct.

## Outputs

Running `bbd_008_discriminatory_query_design.py` creates:

- `outputs/BBD_008_DISCRIMINATORY_QUERIES.csv`
- `outputs/BBD_008_MODEL_ROSTER.csv`

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_008_discriminatory_query_design.py
```
