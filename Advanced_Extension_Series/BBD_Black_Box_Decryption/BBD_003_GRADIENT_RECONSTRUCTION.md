# BBD 003: Directional Derivative and Gradient Reconstruction

## Purpose

BBD 003 moves from mechanism classification towards mathematical reconstruction. It uses the ordered Week 01 to Week 13 input-output path to estimate how coordinate movement was associated with objective movement.

For consecutive rounds,

```text
delta_x_t = x_t - x_(t-1)
delta_y_t = y_t - y_(t-1)
```

and a locally differentiable response would satisfy approximately

```text
delta_y_t = gradient(f)^T delta_x_t
```

Each observed transition is therefore treated as a directional-derivative constraint on an unknown response surface.

## Method

For each of F1 to F8, BBD 003 records every consecutive displacement and objective change, fits a ridge-regularised global gradient, fits a recent gradient to the final five transitions, scores gradient prediction with leave-one-transition-out validation, compares global and recent gradient directions, and isolates near-axis moves where at least 80% of total coordinate movement occurred in one coordinate.

Ridge regularisation is required because the data are sparse, several coordinates often move together, and the path was adaptively chosen rather than designed for derivative estimation.

## Results

The strongest gradient reconstruction occurred in **F5, F7 and F8**.

| Function | Gradient-model evidence | Global versus recent direction | Interpretation |
| --- | --- | --- | --- |
| F1 | weak | cosine 0.003 | no useful linear gradient recovered |
| F2 | moderate | cosine 0.999 | coherent two-coordinate direction |
| F3 | weak | cosine -0.234 | local direction changed materially |
| F4 | weak | cosine -0.316 | global linear gradient is not a useful description |
| F5 | very strong | cosine 0.992 | highly coherent directional structure |
| F6 | strong global fit but unstable recent gradient | cosine 0.163 | interpretation limited by variability and changing local behaviour |
| F7 | very strong | cosine 0.975 | stable directional structure |
| F8 | very strong | cosine 0.937 | stable directional structure |

F5 was the clearest result. The fitted transition model achieved an `R2-like` value of approximately **0.996**, while global and recent gradient directions were almost aligned. Coordinate 2 had by far the largest estimated positive gradient, followed by coordinates 3 and 4. Four near-axis transitions were also available for F5, giving additional empirical derivative evidence.

F7 and F8 also showed extremely strong trajectory reconstruction, with `R2-like` values of approximately **0.999** and **0.99998** respectively. Their global and recent gradients remained strongly aligned. These results support testing compact mathematical forms in BBD 004.

F2 showed a coherent gradient direction but materially weaker predictive accuracy than F5, F7 and F8. Both estimated coefficients were negative in the fitted trajectory, with coordinate 2 having the larger magnitude.

F6 requires caution. Its global transition fit was strong, but the recent gradient collapsed towards near zero and its global versus recent cosine agreement was only about **0.16**. Together with the repeatability findings from BBD 002, this argues against interpreting its global coefficients as a stable derivative field.

F1, F3 and F4 did not yield useful linear gradient reconstructions. Their best regularised solutions were either close to zero or unstable between the full and recent trajectories. These functions should not be forced into a first-order model merely because a gradient can be fitted numerically.

## Coordinate-level signals

The most reproducible directional patterns from this experiment were:

- **F5:** strongest positive sensitivity in coordinate 2, with positive contributions also estimated for coordinates 3 and 4.
- **F7:** strongest negative sensitivities in coordinates 5, 2 and 6; global and recent signs were consistent across all six coordinates.
- **F8:** strongest negative sensitivities in coordinates 6 and 7; coordinates 3, 4 and 5 remained positive in both global and recent fits.
- **F2:** both coordinates were negative in global and recent fits, with coordinate 2 dominant.

These are trajectory-specific empirical gradients, not exact analytical derivatives of the Imperial functions.

## Outputs

Running the experiment produces:

- `outputs/BBD_003_TRANSITION_DIAGNOSTICS.csv`
- `outputs/BBD_003_COORDINATE_GRADIENTS.csv`
- `outputs/BBD_003_GRADIENT_SUMMARY.csv`
- `outputs/BBD_003_NEAR_AXIS_DERIVATIVES.csv`

## Interpretation boundary

The estimates can be distorted by correlated movement, nonlinear curvature, interactions, sparse sampling, adaptive search concentration and response variability. BBD 003 therefore reports global, recent and near-axis evidence separately.

The strongest conclusion is not that an exact gradient has been decrypted. It is that **F5, F7 and F8 contain sufficiently coherent directional structure to justify explicit equation recovery**, while F2 is a secondary candidate and F6 should retain a variability-aware treatment.

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_003_gradient_reconstruction.py
```

## Decision for BBD 004

BBD 004 will prioritise symbolic and compact response-form recovery for F5, F7 and F8, retain F2 as a secondary target, and avoid forcing first-order structure onto F1, F3 or F4. F6 will be modelled with an explicit uncertainty boundary.
