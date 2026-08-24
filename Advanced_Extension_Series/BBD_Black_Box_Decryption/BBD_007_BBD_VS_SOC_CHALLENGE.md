# BBD 007: BBD versus SOC Prediction Challenge

## Purpose

BBD 007 tests whether reconstructed mathematical mechanisms can predict later observations better than the flexible SOC surrogate library.

The comparison is prospective within the historical record. At each test round, only earlier observations are available for model selection and fitting. The held-out later observation is then predicted. This avoids using the complete thirteen-round history to choose a model before pretending to predict an earlier point.

## Competitors

### BBD

The BBD side selects between:

- regularised degree 1 symbolic equations;
- regularised degree 2 symbolic equations;
- constrained transformed benchmark families used in BBD 005.

### SOC

The SOC side uses the existing surrogate library, including Gaussian Processes, tree ensembles and distance-weighted nearest neighbours.

## Inner model selection

Within each training window, the most recent available observation is reserved as an **inner chronological validation point**. Candidate models are fitted only to the observations before that point and are ranked by their error on the reserved observation. The selected model is then refitted to the complete training window before predicting the next unseen round.

This rolling-origin inner validation was chosen instead of ordinary leave-one-out selection because it preserves temporal direction and avoids repeatedly allowing later training observations to predict earlier ones. It also keeps the full BBD versus SOC challenge computationally reproducible.

## Challenge protocol

For each function:

1. begin once at least six earlier observations are available;
2. reserve the latest of those observations for inner chronological model selection;
3. select the strongest BBD candidate without seeing the next round;
4. select the strongest SOC candidate under the same rule;
5. refit both selected competitors to all currently available observations;
6. predict the next chronological observation;
7. reveal the true output and record both errors;
8. expand the training set by one observation and repeat.

This produces a sequence of pseudo-prospective tests rather than one retrospective fit.

## Primary metric

The main comparison is mean absolute prediction error normalised by the full observed response standard deviation for that function. The script also reports the number of individual forward tests won by BBD and SOC.

## Interpretation boundary

BBD 007 does not prove that a recovered equation is the original Imperial equation. If BBD wins, it means the constrained mathematical reconstruction generalises better over these historical forward tests than the tested SOC surrogate library. If SOC wins, the flexible surrogate retains superior predictive value.

The thirteen observations remain a small adaptively sampled dataset, so the result is treated as a validation challenge rather than definitive system identification.

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
