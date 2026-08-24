# BBD: Black Box Decryption

## Purpose

**BBD, Black Box Decryption**, is a post-capstone system-identification experiment. Its aim is not merely to predict a good next coordinate, but to determine what kind of mathematical mechanism could plausibly have generated the thirteen-round input-output history for each hidden function.

BBD is deliberately separate from the assessed Week 01 to Week 13 record. It does not alter historical observations and it does not claim access to the original Imperial objective functions.

## Central question

For each function, BBD asks:

> What is the simplest predictive mechanism consistent with the observed coordinates, outputs, repeated points, temporal order and movement between rounds?

The first competition distinguishes five broad hypotheses.

| Hypothesis | Model idea | Interpretation |
| --- | --- | --- |
| H0a | `y = f_linear(x)` | approximately static linear surface |
| H0b | `y = f_nonlinear(x)` | static nonlinear surface |
| H1 | `y = f(x) + noise` | static surface with response variability |
| H2 | `y = f(x,t)` | temporal information improves prediction beyond coordinates alone |
| H4/H5 | `y = f(x,t,y_prev,delta_x)` | path, state or movement history adds predictive information |

These are competing empirical explanations. Better prediction by a temporal model is evidence that temporal features contain information; it is not by itself proof that the hidden mathematical function literally changes with time.

## BBD 001: Static versus temporal system identification

The first experiment uses chronological walk-forward validation. For a test round, the model is trained only on earlier rounds. This avoids allowing future observations to influence predictions of the past.

Models currently competing are:

- static ridge regression;
- static quadratic ridge regression;
- static Gaussian process regression;
- time-augmented ridge regression;
- time-augmented Gaussian process regression;
- movement-aware ridge regression using coordinate displacement and step size;
- state-aware ridge regression using previous output as an additional feature.

Each function is evaluated independently because F1 to F8 have different dimensionalities, scales and response behaviour.

## BBD 002: Temporal residual structure and repeatability

BBD 002 starts from a coordinate-only Gaussian Process and studies the chronological residuals that remain after coordinate effects have been modelled. It tests whether time, previous residuals or repeated evaluations contain additional predictive information.

BBD 002 therefore provides a stricter test of the temporal signals suggested by BBD 001. A temporal explanation is treated as practically useful only if a correction trained solely on earlier residuals reduces later prediction error relative to leaving the static residual uncorrected.

See [BBD 002: Temporal Residual Structure and Repeatability](BBD_002_TEMPORAL_RESIDUALS.md).

## Why temporal ordering is retained

The thirteen observations are not treated as an unordered cloud. For round `t`, BBD derives:

- the coordinate vector `x_t`;
- normalised round index `t`;
- displacement `delta_x_t = x_t - x_(t-1)`;
- movement magnitude `||delta_x_t||`;
- previous observed output `y_(t-1)`.

This allows BBD to test whether the route through the search space contains predictive information that is lost by ordinary `x -> y` surrogate modelling.

## Natural repeatability experiments

Repeated coordinates are especially valuable. If the same recorded coordinate returns different outputs, a perfectly deterministic `y=f(x)` explanation cannot fit those observations simultaneously without a noise or hidden-state term.

F6 is therefore a particularly important diagnostic function. Other functions with exact repeated outputs provide the corresponding control evidence and prevent BBD from assuming temporal drift universally.

## Outputs

Running `bbd_001_system_identification.py` creates:

- `outputs/BBD_001_MODEL_COMPETITION.csv`
- `outputs/BBD_001_TEMPORAL_DIAGNOSTICS.csv`
- `outputs/BBD_001_HYPOTHESIS_SUMMARY.csv`

Running `bbd_002_temporal_residuals.py` creates:

- `outputs/BBD_002_TEMPORAL_RESIDUAL_SUMMARY.csv`
- `outputs/BBD_002_STATIC_GP_RESIDUALS.csv`
- `outputs/BBD_002_RESIDUAL_CORRECTION_COMPETITION.csv`
- `outputs/BBD_002_REPEATABILITY_DETAIL.csv` when repeated coordinates are present

The output values are model diagnostics and predictions. They are not Imperial black-box evaluations.

## Run

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_001_system_identification.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_002_temporal_residuals.py
```

## Research sequence

BBD is intended to develop in stages:

**BBD 001** Static versus temporal mechanism competition  
**BBD 002** Residual temporal structure and repeatability analysis  
**BBD 003** Local directional derivative and gradient reconstruction  
**BBD 004** Symbolic-regression search for compact equations  
**BBD 005** Benchmark-family matching under coordinate and output transformations  
**BBD 006** Decryption ensemble and confidence ranking  
**BBD 007** Predicted function challenge against SOC

The project advances only when each stage has a reproducible result and a stated uncertainty boundary.
