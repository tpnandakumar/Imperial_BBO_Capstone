# Representative F5 and F7 surrogate equations

These models approximate the complete sampled input-output record. They are not the original hidden BBO equations and should not be extrapolated beyond the observed domain without new validation.

## F5 Matérn 2.5 surrogate

The representative equation is:

`F5_hat(x) = output_mean + output_scale * sum(alpha_i * K52(z, z_i))`

where `z_j = (x_j - mean_j) / scale_j` and:

`K52 = (1 + sqrt(5)r + 5r^2/3) * exp(-sqrt(5)r)`

The selected standardised length scale is `10.0` and the diagonal noise setting is `1e-08`. Weekly walk-forward MAE was `49.918573`, equal to `0.011241` of the complete F5 output range.

`F5_INPUT_SCALING.csv` contains the coordinate transformation. `F5_MATERN52_WEIGHTS.csv` contains every training coordinate and kernel weight required to calculate the surrogate.

## F7 quadratic surrogate

The representative equation is:

`F7_hat(x) = beta_0 + sum(beta_j * phi_j(z))`

where `z_j = (x_j - mean_j) / scale_j`. The 27 features comprise six linear terms, six squared terms and fifteen pairwise interactions. Ridge alpha `1e-06` was selected by weekly walk-forward validation. MAE was `0.066669`, equal to `0.048373` of the complete F7 output range.

`F7_INPUT_SCALING.csv` contains the coordinate transformation. `F7_QUADRATIC_COEFFICIENTS.csv` contains the intercept and all 27 numerical coefficients.

## Validation boundary

Hyperparameters were selected by predicting each of the thirteen weekly observations from the starter data and earlier weeks only. The final parameters were then refitted to the complete evidence for representative use. This final refit describes the sampled record and is not an independent prospective validation.
