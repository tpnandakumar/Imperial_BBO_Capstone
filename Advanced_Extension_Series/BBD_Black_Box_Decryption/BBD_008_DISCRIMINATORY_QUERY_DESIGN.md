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

## Results

The first-ranked discriminatory coordinate for each function is shown below. Coordinates are rounded to six decimals for readability. The underlying CSV retains full numerical precision.

| Function | Highest-value discriminatory coordinate | Score | Normalised model spread | Novelty |
| --- | --- | ---: | ---: | ---: |
| F1 | `0.000000-1.000000` | 0.5413 | 1.2602 | 0.3260 |
| F2 | `0.590678-0.083736` | 4.8844 | 9.9580 | 0.5895 |
| F3 | `0.950204-0.562774-0.985180` | 0.3705 | 0.9255 | 0.2538 |
| F4 | `1.000000-1.000000-1.000000-1.000000` | 1.4029 | 3.1595 | 0.4359 |
| F5 | `0.514839-0.128857-0.019245-0.019528` | 3.5641 | 7.0133 | 0.7405 |
| F6 | `1.000000-1.000000-0.000000-0.000000-0.000000` | 2.5127 | 5.4474 | 0.5324 |
| F7 | `0.880336-0.186036-0.926111-0.890427-0.935082-0.257763` | 4.7577 | 9.8887 | 0.5812 |
| F8 | `0.493384-0.987872-0.420638-0.274838-0.260747-0.815423-0.367644-0.473387` | 4.6272 | 9.2452 | 0.4284 |

### What the ranking means

F2, F7 and F8 have the largest current model disagreement, followed by F5 and F6. These are therefore the most powerful single-query falsification opportunities under the present candidate roster. F1 and F3 show much smaller disagreement, meaning that an additional arbitrary query would be less likely to distinguish the surviving explanations unless it were chosen very carefully.

F5 is especially informative because its best proposed discriminatory point is also highly novel relative to the historical trajectory. The retained models disagree by more than seven observed response ranges at that point despite all passing the extrapolation filter. One independent evaluation there would therefore provide far more structural information than another small move around the historical F5 optimum.

F6 remains unusual. Its discriminatory query is a boundary corner and its competing models disagree strongly, which is consistent with the earlier evidence that F6 cannot be treated as a clean deterministic surface without accounting for variability or hidden state.

The result also reinforces the distinction established by BBD 007. A model can fit the historical path extremely well and still disagree sharply with other credible models away from that path. The unresolved information lies primarily in unsampled parts of the domain rather than in further refitting of the same thirteen observations.

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

The BBD workflow completed successfully after the import-path validation issue found in the first run was corrected. The final repository audit also passed on the same branch.
