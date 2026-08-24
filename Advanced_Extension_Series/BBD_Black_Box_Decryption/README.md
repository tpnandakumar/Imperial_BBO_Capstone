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

Models currently competing are static ridge regression, static quadratic ridge regression, static Gaussian process regression, time-augmented models, movement-aware regression and state-aware regression.

## BBD 002: Temporal residual structure and repeatability

BBD 002 starts from a coordinate-only Gaussian Process and studies the chronological residuals that remain after coordinate effects have been modelled. It tests whether time, previous residuals or repeated evaluations contain additional predictive information.

See [BBD 002: Temporal Residual Structure and Repeatability](BBD_002_TEMPORAL_RESIDUALS.md).

## BBD 003: Directional derivative and gradient reconstruction

BBD 003 converts consecutive Week 01 to Week 13 input-output changes into directional-derivative constraints. It estimates regularised global and recent gradient vectors, tests their held-out transition prediction and identifies near-axis movements that provide the closest available empirical partial-derivative evidence.

The first reconstruction found the strongest coherent directional structure in **F5, F7 and F8**, with F2 as a secondary candidate. F6 retained a strong global fit but poor recent-gradient agreement, consistent with its repeatability uncertainty. F1, F3 and F4 did not support a useful first-order gradient representation.

See [BBD 003: Directional Derivative and Gradient Reconstruction](BBD_003_GRADIENT_RECONSTRUCTION.md).

## Why temporal ordering is retained

The thirteen observations are not treated as an unordered cloud. For round `t`, BBD derives the coordinate vector, round index, coordinate displacement, movement magnitude and previous observed output. Later stages also use the ordered transition relation `delta_y_t` versus `delta_x_t`.

This allows BBD to test whether the route through the search space contains predictive information that is lost by ordinary `x -> y` surrogate modelling.

## Natural repeatability experiments

Repeated coordinates are especially valuable. If the same recorded coordinate returns different outputs, a perfectly deterministic `y=f(x)` explanation cannot fit those observations simultaneously without a noise or hidden-state term.

F6 remains an important diagnostic function because its repeated-coordinate evidence differs from the more stable repeatability seen in several other functions.

## Outputs

BBD currently produces model-competition, temporal-residual, repeatability, transition, gradient and near-axis derivative datasets in `Advanced_Extension_Series/BBD_Black_Box_Decryption/outputs/`.

These values are model diagnostics and reconstructions. They are not Imperial black-box evaluations.

## Run

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_001_system_identification.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_002_temporal_residuals.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_003_gradient_reconstruction.py
```

## Research sequence

**BBD 001** Static versus temporal mechanism competition  
**BBD 002** Residual temporal structure and repeatability analysis  
**BBD 003** Local directional derivative and gradient reconstruction  
**BBD 004** Symbolic-regression search for compact equations  
**BBD 005** Benchmark-family matching under coordinate and output transformations  
**BBD 006** Decryption ensemble and confidence ranking  
**BBD 007** Predicted function challenge against SOC

The project advances only when each stage has a reproducible result and a stated uncertainty boundary.
