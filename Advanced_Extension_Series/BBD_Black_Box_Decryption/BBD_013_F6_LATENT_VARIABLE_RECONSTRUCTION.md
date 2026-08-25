# BBD 013: F6 Latent Variable Reconstruction

## Purpose

BBD 012 left F6 with a strong static coordinate-dependent surface and a residual component that could not be explained confidently by simple time drift, state proxies or a clear autoregressive law. BBD 013 asks whether the unexplained component can be compressed into a low-dimensional latent state derived from observable context.

The aim is not to invent a hidden variable. It is to test whether several weak contextual signals become useful when combined into one or two orthogonal latent dimensions.

## Observable context

For every F6 observation, the experiment constructs six context variables from information available in the historical sequence:

- scaled week index;
- previous observed F6 output;
- movement from the previous F6 coordinate;
- distance to the nearest previously sampled coordinate;
- local mean output among nearby historical points;
- local output dispersion among nearby historical points.

These variables are standardised and compressed by PCA into one- and two-component latent representations.

## Baseline

The baseline remains the coordinate-only Gaussian Process established in BBD 010. Walk-forward residuals are generated without using future observations.

## Latent test

The latent components are tested in two ways.

First, the correlation between the leading latent component and the static-GP residual is recorded. Second, a ridge correction model is trained only on previously observed residuals and used prospectively to predict the next residual from the latent representation.

A latent explanation is treated as supported only if it reduces forward residual MAE relative to the uncorrected baseline on the same eligible observations.

## Repeated-coordinate context

Repeated F6 coordinates are analysed separately. For each repeat pair, the experiment records the output change and the distance between the corresponding observable-context vectors. This asks whether the same coordinate produced a different output when the surrounding context was materially different.

With only a few repeat pairs, any correlation is descriptive rather than confirmatory.

## Outputs

Running `bbd_013_f6_latent_variable_reconstruction.py` creates:

- `outputs/BBD_013_F6_BASELINE_RESIDUALS.csv`
- `outputs/BBD_013_F6_LATENT_COMPETITION.csv`
- `outputs/BBD_013_F6_LATENT_LOADINGS.csv`
- `outputs/BBD_013_F6_REPEAT_CONTEXT_DISTANCE.csv`
- `outputs/BBD_013_F6_LATENT_RECONSTRUCTION_SUMMARY.csv`

## Evidence boundary

BBD 013 remains a post-capstone reconstruction. PCA components are statistical summaries of the observable context variables, not proof of an actual hidden state in the original evaluator. Exact function recovery remains false unless an independent black-box evaluation can discriminate the surviving explanations.
