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

## Results

The one-component latent model had a leading-component residual correlation of only `0.120759`. On the five observations eligible for prospective latent correction, the uncorrected residual MAE was `0.056843`, while the one-component latent correction increased MAE to `0.090492`. The resulting MAE gain was therefore `-0.033649`.

The two-component representation was worse again. Its prospective corrected residual MAE was `0.109641`, giving an MAE gain of `-0.052798` relative to the same baseline.

Neither latent representation therefore improved forward prediction. Under the pre-specified decision rule, the available observable context does not support a useful low-dimensional latent state for F6.

Four repeated-coordinate pairs were available for the context comparison. The descriptive correlation between context distance and absolute output change was approximately `-0.644142`. With only four pairs this is not reliable evidence of a mechanism, and its negative direction does not support a simple claim that greater observable-context change produced greater repeat-output variation.

The current interpretation is therefore **no observable latent-context advantage**. This does not rule out an unobserved latent variable that was never recorded. It shows that the particular context variables available from the thirteen-round history do not reconstruct such a state in a way that improves prospective residual prediction.

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
