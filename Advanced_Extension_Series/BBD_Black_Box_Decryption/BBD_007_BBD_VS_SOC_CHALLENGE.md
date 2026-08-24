# BBD 007: BBD versus SOC Prediction Challenge

## Purpose

BBD 007 tests whether the reconstructed mathematical mechanisms can predict genuinely later observations better than the flexible SOC surrogate library.

The comparison is prospective within the historical record. At each test round, only earlier observations are available for model selection and fitting. The held-out later observation is then predicted. This avoids using the full thirteen-round history to choose a model before pretending to predict an earlier point.

## Competitors

### BBD

The BBD side selects between:

- regularised degree 1 symbolic equations;
- regularised degree 2 symbolic equations;
- constrained transformed benchmark families used in BBD 005.

Model selection is performed separately inside each training window using leave-one-out error.

### SOC

The SOC side uses the existing surrogate library, including Gaussian Processes, tree ensembles and distance-weighted nearest neighbours. Its model is also selected only from the training window using leave-one-out error.

## Challenge protocol

For each function:

1. begin once at least five earlier observations are available;
2. select the strongest BBD candidate using only those observations;
3. select the strongest SOC candidate using only those observations;
4. fit both competitors to the available history;
5. predict the next chronological observation;
6. reveal the true output and record both errors;
7. expand the training set by one observation and repeat.

This produces a sequence of pseudo-prospective tests rather than one retrospective fit.

## Primary metric

The main comparison is mean absolute prediction error normalised by the full observed response standard deviation for that function. The script also reports the number of individual test rounds won by BBD and SOC.

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
