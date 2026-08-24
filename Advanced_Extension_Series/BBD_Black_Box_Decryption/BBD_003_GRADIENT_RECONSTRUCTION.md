# BBD 003: Directional Derivative and Gradient Reconstruction

## Purpose

BBD 003 moves from mechanism classification towards mathematical reconstruction. It uses the ordered Week 01 to Week 13 input-output path to estimate how changes in the submitted coordinates were associated with changes in each hidden objective.

For consecutive rounds,

```text
delta_x_t = x_t - x_(t-1)
delta_y_t = y_t - y_(t-1)
```

and, locally, a differentiable function would satisfy approximately

```text
delta_y_t = gradient(f)^T delta_x_t
```

The experiment therefore treats each observed transition as a directional-derivative constraint on an unknown local response surface.

## What is estimated

For each of F1 to F8, BBD 003 records:

- every consecutive coordinate displacement and objective change;
- the observed directional slope `delta_y / ||delta_x||`;
- a regularised global gradient vector fitted to all non-zero transitions;
- a recent gradient vector fitted to the final five transitions;
- leave-one-transition-out prediction error for the gradient model;
- agreement between global and recent gradient directions;
- coordinate rankings by absolute estimated gradient magnitude;
- near-axis transitions, where at least 80% of total coordinate movement occurred in one coordinate, as the closest available empirical approximation to a partial derivative.

## Why regularisation is required

The dataset is small and adaptively sampled. Several coordinates often change together, especially in the higher-dimensional functions. Ordinary least squares could therefore create unstable coefficient estimates. Ridge regularisation is used and its strength is selected by leave-one-transition-out prediction error.

## Interpretation boundary

The estimated gradient is an empirical reconstruction of the trajectory sampled during the capstone. It is not claimed to be the exact analytical derivative of the Imperial hidden function.

A gradient coefficient can be distorted by:

- correlated coordinate movement;
- nonlinear curvature;
- interactions between coordinates;
- sparse sampling;
- response noise or hidden state, particularly for F6;
- the fact that the search trajectory concentrated increasingly on promising regions.

For this reason BBD 003 reports global, recent and near-axis evidence separately rather than treating one coefficient vector as ground truth.

## Outputs

Running the experiment produces:

- `outputs/BBD_003_TRANSITION_DIAGNOSTICS.csv`
- `outputs/BBD_003_COORDINATE_GRADIENTS.csv`
- `outputs/BBD_003_GRADIENT_SUMMARY.csv`
- `outputs/BBD_003_NEAR_AXIS_DERIVATIVES.csv`

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_003_gradient_reconstruction.py
```

## Decision for BBD 004

BBD 003 is intended to identify which functions and coordinates have sufficiently coherent directional evidence to justify symbolic equation recovery. BBD 004 should give greatest weight to functions whose gradient model predicts held-out transitions well and whose global and recent gradient directions remain broadly consistent.
