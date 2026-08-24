# BBD 007: BBD versus SOC Prediction Challenge

## Purpose

BBD 007 tests whether reconstructed mathematical mechanisms can predict later observations better than the flexible SOC surrogate library.

The comparison is prospective within the historical record. At each test round, only earlier observations are available for model selection and fitting. The held-out later observation is then predicted. This avoids using the complete thirteen-round history to choose a model before pretending to predict an earlier point.

## Competitors

### BBD

The BBD side selects between regularised degree 1 symbolic equations, regularised degree 2 symbolic equations and constrained transformed benchmark families used in BBD 005.

### SOC

The SOC side uses the existing surrogate library, including Gaussian Processes, tree ensembles and distance-weighted nearest neighbours.

## Inner model selection

Within each training window, the most recent available observation is reserved as an **inner chronological validation point**. Candidate models are fitted only to the observations before that point and are ranked by their error on the reserved observation. The selected model is then refitted to the complete training window before predicting the next unseen round.

This rolling-origin inner validation preserves temporal direction and avoids repeatedly allowing later training observations to predict earlier ones.

## Challenge protocol

For each function:

1. begin once at least six earlier observations are available;
2. reserve the latest available observation for inner chronological model selection;
3. select the strongest BBD candidate without seeing the next round;
4. select the strongest SOC candidate under the same rule;
5. refit both selected competitors to all currently available observations;
6. predict the next chronological observation;
7. reveal the true output and record both errors;
8. expand the training set by one observation and repeat.

Seven forward tests were available for each function.

## Results

| Function | BBD normalised MAE | SOC normalised MAE | Winner | BBD test wins | SOC test wins |
| --- | ---: | ---: | --- | ---: | ---: |
| F1 | 0.3877 | 0.1756 | SOC | 1 | 6 |
| F2 | 0.6891 | 0.4990 | SOC | 1 | 6 |
| F3 | 0.5490 | 0.2737 | SOC | 1 | 6 |
| F4 | 0.1852 | 0.0528 | SOC | 2 | 5 |
| F5 | 0.0281 | 0.0091 | SOC | 0 | 7 |
| F6 | 0.2291 | 0.4448 | **BBD** | 4 | 3 |
| F7 | 0.2914 | 0.1957 | SOC | 3 | 4 |
| F8 | 0.1675 | 0.0439 | SOC | 1 | 6 |

Overall, **SOC won 7 of the 8 functions**, while BBD won F6. Mean normalised MAE across functions was approximately **0.3159 for BBD** and **0.2118 for SOC**.

## What the result changes

BBD 007 is an important negative result. BBD 004 to BBD 006 showed that several compact mathematical descriptions fit the complete observed history extremely well, particularly F5, F7 and F8. However, once the experiment was converted into forward prediction, those reconstructions did not outperform the flexible SOC surrogates.

This means the earlier high decryption-confidence scores should be interpreted as **confidence in retrospective structural reconstruction**, not as evidence that the original hidden equations had been recovered. Excellent full-history fit and coherent gradients are not sufficient to establish prospective predictive superiority.

F5 illustrates this clearly. Its full-history quadratic reconstruction had exceptionally low leave-one-out error, yet SOC won all seven forward tests. F8 showed the same distinction: the compact linear equation remains a strong description of the sampled history, but SOC generalised more accurately to later observations.

F6 is the exception. Despite its repeated-coordinate variability and lower BBD 006 structural confidence, BBD won the forward challenge for F6. This suggests that the BBD candidate family captured useful predictive structure there even though exact deterministic decryption remains unsupported.

## Interpretation boundary

BBD 007 does not invalidate BBD. It separates two questions that had previously been too easy to conflate:

- **Can a compact mathematical expression describe the observations already collected?**
- **Can that expression predict observations that were not available when it was chosen?**

For most functions in this dataset, SOC currently answers the second question better.

The thirteen observations remain a small adaptively sampled dataset. BBD 007 is therefore a strong internal challenge test, not definitive proof about the original Imperial functions.

## Outputs

Running `bbd_007_bbd_vs_soc_challenge.py` creates:

- `outputs/BBD_007_PROSPECTIVE_PREDICTIONS.csv`
- `outputs/BBD_007_BBD_VS_SOC_SUMMARY.csv`
- `outputs/BBD_007_OVERALL_RESULT.csv`

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_007_bbd_vs_soc_challenge.py
```

## Next decision

The next BBD stage should recalibrate the decryption confidence framework using prospective evidence. Retrospective fit, structural simplicity and gradient coherence should remain useful, but they should no longer dominate confidence when forward prediction disagrees.
