# Black Box Resolution mathematical models for F1 to F8

## Purpose

Black Box Resolution (BBR) asks how much mathematical structure can be recovered from a completed input and output record when the original generating equations remain hidden. It uses chronological prediction, equation-family comparison, repeat testing and falsification to separate useful structure from attractive but unsupported explanations.

The equations in this document are evidence-based surrogate models. They are not presented as the undisclosed Imperial functions. Positive and negative results are both retained because rejecting an unsuitable equation is part of resolving a black box.

The earlier numbered research files use the working title Black Box Decryption, or BBD. Those filenames are preserved as the historical audit trail. The consolidated method and its findings are published here under the final name **Black Box Resolution (BBR)**.

## BBR method

For each hidden function $f$ with observed coordinates $\mathbf{x}_i$ and outputs $y_i$, BBR follows five stages:

1. Fit candidate explanations using only the observations available inside a historical training window.
2. Predict the next observation without using its returned value.
3. Expand the training window by one observation and repeat.
4. Compare prediction error, equation complexity, coefficient stability and repeated-coordinate behaviour.
5. Retain, revise or reject each explanation according to the accumulated evidence.

For $H$ chronological tests, mean absolute error is:

$$
\mathrm{MAE}_f=\frac{1}{H}\sum_{h=1}^{H}\left|y_{f,h}-\widehat{y}_{f,h}\right|
$$

To compare functions with different output scales, BBR uses:

$$
\mathrm{NMAE}_f=
\frac{\mathrm{MAE}_f}
{\max_i(y_{f,i})-\min_i(y_{f,i})}
$$

A smaller normalised mean absolute error, or NMAE, indicates stronger chronological prediction. Low error alone is not sufficient. A retained model must also respect repeatability evidence and remain appropriately simple for the available sample.

## Shared input scaling

For models fitted to standardised coordinates:

$$
z_j=\frac{x_j-\mu_j}{s_j}
$$

where $\mu_j$ and $s_j$ are the mean and standard deviation of coordinate $j$ within the relevant training data. In a chronological test, they are recalculated inside each historical training window so that later observations cannot influence an earlier prediction.

## Model-family equations

### Linear surrogate

$$
\widehat{f}(\mathbf{x})=\beta_0+\sum_{j=1}^{d}\beta_jx_j
$$

This model represents a stable additive direction across the sampled region.

### Quadratic surrogate

$$
\widehat{f}(\mathbf{x})=
\beta_0+
\sum_{j=1}^{d}\beta_jx_j+
\sum_{j=1}^{d}\gamma_jx_j^2+
\sum_{j=1}^{d-1}\sum_{m=j+1}^{d}\delta_{jm}x_jx_m
$$

The squared terms represent curvature. The interaction terms allow the effect of one coordinate to depend on another.

### Cubic surrogate

Using multi-index notation, a cubic polynomial is:

$$
\widehat{f}(\mathbf{x})=
\sum_{|\boldsymbol{a}|\leq3}
\theta_{\boldsymbol{a}}\mathbf{x}^{\boldsymbol{a}}
$$

where $\boldsymbol{a}=(a_1,\ldots,a_d)$, $|\boldsymbol{a}|=\sum_j a_j$ and $\mathbf{x}^{\boldsymbol{a}}=\prod_jx_j^{a_j}$. Cubic models were restricted to F1 to F3 because higher-dimensional cubic libraries would be too large for the available evidence.

### Ridge estimation

Polynomial coefficients are estimated through:

$$
\widehat{\boldsymbol{\theta}}=
\underset{\boldsymbol{\theta}}{\mathop{\mathrm{arg\,min}}}
\left\{
\lVert\mathbf{y}-\Phi\boldsymbol{\theta}\rVert_2^2+
\lambda\lVert\boldsymbol{\theta}\rVert_2^2
\right\}
$$

where $\Phi$ is the selected feature matrix and $\lambda$ controls shrinkage. The intercept is not penalised.

### Matérn 2.5 surrogate

For a scaled coordinate $\mathbf{z}$ and training coordinate $\mathbf{z}_i$:

$$
r_i=\frac{\lVert\mathbf{z}-\mathbf{z}_i\rVert_2}{\ell}
$$

$$
K_{5/2}(\mathbf{z},\mathbf{z}_i)=
\left(1+\sqrt{5}r_i+\frac{5r_i^2}{3}\right)
\exp\left(-\sqrt{5}r_i\right)
$$

The predictive mean used by the representative BBR surrogate is:

$$
\widehat{f}(\mathbf{x})=
\bar{y}+s_y\sum_{i=1}^{n}\alpha_iK_{5/2}(\mathbf{z},\mathbf{z}_i)
$$

with weights:

$$
\boldsymbol{\alpha}=
\left(\mathbf{K}+\sigma_n^2\mathbf{I}+\varepsilon\mathbf{I}\right)^{-1}
\frac{\mathbf{y}-\bar{y}\mathbf{1}}{s_y}
$$

Here, $\ell$ is the length scale, $\sigma_n^2$ is the diagonal noise setting and $\varepsilon$ is a small numerical stabiliser.

## Function-by-function resolution

| Function | Best-supported current description | Main validation result | Resolution status |
| --- | --- | ---: | --- |
| F1 | Cubic polynomial candidate | Shared-study NMAE `0.697160` | Weak recovery |
| F2 | Quadratic polynomial candidate | Shared-study NMAE `0.486712` | Moderate but unconfirmed |
| F3 | Linear polynomial candidate | Shared-study NMAE `0.660674` | No useful compact recovery |
| F4 | Matérn 2.5 smooth nonlinear surrogate | Walk-forward NMAE `0.021834` | Strong local surrogate |
| F5 | Matérn 2.5 smooth boundary-directed surrogate | Dedicated walk-forward NMAE `0.001616` | Strongest chronological result |
| F6 | Matérn 2.5 coordinate surface plus unresolved variability | Walk-forward NMAE `0.044066` | Strong surface, incomplete mechanism |
| F7 | Full quadratic interaction surrogate | Walk-forward NMAE `0.034870` | Strong local quadratic |
| F8 | Compact linear surrogate | Walk-forward NMAE `0.016539` | Strong compact reconstruction |

## F1: cubic candidate, weak recovery

F1 selected a cubic family in the shared symbolic competition:

$$
\widehat{F}_1(\mathbf{x})=
\sum_{|\boldsymbol{a}|\leq3}
\theta_{1,\boldsymbol{a}}\mathbf{x}^{\boldsymbol{a}}
$$

The NMAE was `0.697160`, despite the added cubic complexity. This is a negative result. The observed F1 sequence does not support a reliable compact polynomial equation. A dedicated function-specific comparison is still required.

## F2: quadratic candidate, moderate evidence

F2 selected a quadratic family:

$$
\widehat{F}_2(\mathbf{x})=
\beta_{2,0}+
\sum_{j=1}^{2}\beta_{2,j}x_j+
\sum_{j=1}^{2}\gamma_{2,j}x_j^2+
\delta_{2,12}x_1x_2
$$

Its shared-study NMAE was `0.486712`. The result is better than F1 and F3 but is not sufficiently strong to publish a numerical equation as a representative F2 model. The Week 13 decline after a small coordinate change also shows why the local region requires dedicated bracketing.

## F3: linear candidate rejected as useful recovery

F3 selected a linear family:

$$
\widehat{F}_3(\mathbf{x})=
\beta_{3,0}+\beta_{3,1}x_1+\beta_{3,2}x_2+\beta_{3,3}x_3
$$

The shared-study NMAE was `0.660674`, and the training $R^2$-like measure was approximately `0.010017`. This is clear negative evidence against a useful global linear description of the observed F3 record.

## F4: smooth nonlinear surface

F4 is best represented by a Matérn 2.5 surrogate:

$$
\widehat{F}_4(\mathbf{x})=
\bar{y}_4+s_{y,4}
\sum_{i=1}^{n_4}\alpha_{4,i}
K_{5/2}(\mathbf{z},\mathbf{z}_i)
$$

The dedicated chronological NMAE was `0.021834`. A nested Rosenbrock representation remained competitive but ranked fifth at `0.032816`. The positive result is a repeatable, locally smooth nonlinear surface. The negative result is that the earlier Rosenbrock-like clue did not remain the strongest explanation under stricter chronological selection.

## F5: strongest chronological surrogate

F5 is represented by:

$$
\widehat{F}_5(\mathbf{x})=
\bar{y}_5+s_{y,5}
\sum_{i=1}^{n_5}\alpha_{5,i}
K_{5/2}(\mathbf{z},\mathbf{z}_i)
$$

The dedicated BBR study produced a walk-forward NMAE of `0.001616`. A quadratic Ridge model remained strong at `0.005802`, confirming genuine polynomial structure, but the Matérn surrogate predicted the historical chronology more accurately. Boundary-transformed reciprocal and logarithmic explanations performed poorly. Their rejection is an important negative result because improvement towards the boundary does not prove a simple boundary singularity.

The compact repository package uses a separately reproduced representative refit with its full scaling and kernel weights. Differences between validation summaries must therefore be read with their stated protocol rather than treated as interchangeable scores.

## F6: static surface with unresolved variability

The broad F6 response is represented by:

$$
y_{6,t}=g_6(\mathbf{x}_t)+\varepsilon_{6,t}
$$

with the coordinate surface approximated by:

$$
\widehat{g}_6(\mathbf{x})=
\bar{y}_6+s_{y,6}
\sum_{i=1}^{n_6}\alpha_{6,i}
K_{5/2}(\mathbf{z},\mathbf{z}_i)
$$

The coordinate-only Matérn model achieved a walk-forward NMAE of approximately `0.044066` and outperformed the tested state-aware alternatives. This is positive evidence for a strong static coordinate surface. However, identical coordinates returned different values, with a maximum observed range of approximately `0.100675`. The unresolved term $\varepsilon_{6,t}$ is therefore required. The available record does not establish whether it represents noise, hidden state, numerical context or another mechanism.

## F7: distributed quadratic interaction surface

The retained F7 structure is:

$$
\widehat{F}_7(\mathbf{x})=
\beta_{7,0}+
\sum_{j=1}^{6}\beta_{7,j}x_j+
\sum_{j=1}^{6}\gamma_{7,j}x_j^2+
\sum_{j=1}^{5}\sum_{m=j+1}^{6}\delta_{7,jm}x_jx_m
$$

Quadratic Ridge with $\lambda=10^{-4}$ achieved a chronological NMAE of `0.034870`. The complete 27-term form remained the strict predictive winner. A 20-term version was close, but stronger pruning progressively reduced performance. The negative finding is therefore useful: the current evidence does not support replacing F7 with an elegant three-term or five-term equation.

The complete numerical coefficients are preserved in the historical F7 resolution study and the representative coefficient table.

## F8: compact linear reconstruction

F8 produced the clearest explicit equation:

$$
\begin{aligned}
\widehat{F}_8(\mathbf{x})={}&10.97788502
+0.116539399x_1
+0.1910685871x_2\\
&+0.05156106233x_3
+0.8145764473x_4
+0.3239666929x_5\\
&-1.411856604x_6
-0.7715635142x_7
-0.04556514659x_8
\end{aligned}
$$

The dedicated chronological NMAE was `0.016539`. All coefficient signs were stable in at least 75 per cent of expanding training windows, and the same coordinate returned the same output on four occasions. This is strong evidence for a stable low-complexity surface over the sampled region. It remains a reconstruction rather than proof of the undisclosed global equation.

## Positive findings

1. F4, F5, F6, F7 and F8 contain reproducible coordinate structure that predicts chronologically held-out observations.
2. F5 has the strongest dedicated chronological surrogate result.
3. F8 has the clearest compact explicit reconstruction.
4. F7 supports a distributed quadratic interaction surface.
5. F4 supports a smooth nonlinear surface rather than a simple linear rule.
6. F6 supports a strong coordinate surface even though its complete response mechanism remains unresolved.

## Negative findings

1. F1 and F3 do not yet support useful compact polynomial recovery.
2. F2 remains only moderately resolved and needs a dedicated function-specific study.
3. F4 is not established as a transformed Rosenbrock function.
4. F5 is not explained by a simple reciprocal or logarithmic distance-to-boundary transformation.
5. F6 cannot be represented as a deterministic coordinate-only equation without an unresolved variability term.
6. F7 does not retain its best chronological performance after aggressive term pruning.
7. No model has been proved to equal an original Imperial hidden function outside the sampled region.

## Worked interpretation example

For F8, the largest coefficient magnitude belongs to $x_6$:

$$
\frac{\partial\widehat{F}_8}{\partial x_6}=-1.411856604
$$

Within the linear surrogate, increasing $x_6$ by $0.10$ while holding the other coordinates fixed changes the predicted output by:

$$
\Delta\widehat{F}_8=-1.411856604(0.10)=-0.1411856604
$$

This is an interpretation of the recovered local surrogate. It is not a causal claim about the undisclosed original function.

## Evidence boundary and next research stage

BBR has recovered useful mathematical behaviour, rejected several weak explanations and identified the strongest current model family for each function. Exact function identity remains unproved. The decisive next stage is to evaluate new authorised coordinates chosen where the leading candidate models disagree most. Such tests would provide greater resolving power than adding more points close to already sampled trajectories.

## Supporting evidence

- [Historical resolution research series](../Advanced_Extension_Series/BBD_Black_Box_Decryption/SECTION_GUIDE.md)
- [Representative F5 and F7 coefficient package](representative_surrogates/SECTION_GUIDE.md)
- [F4 dedicated chronological comparison](../Advanced_Extension_Series/BBD_Black_Box_Decryption/BBD_025_F4_SPECIFIC_DECRYPTION.md)
- [F5 dedicated chronological comparison](../Advanced_Extension_Series/BBD_Black_Box_Decryption/BBD_023_F5_SPECIFIC_DECRYPTION.md)
- [F6 dedicated resolution study](../Advanced_Extension_Series/BBD_Black_Box_Decryption/BBD_010_F6_SPECIFIC_DECRYPTION.md)
- [F7 dedicated chronological comparison](../Advanced_Extension_Series/BBD_Black_Box_Decryption/BBD_018_F7_SPECIFIC_DECRYPTION.md)
- [F8 explicit reconstruction](../Advanced_Extension_Series/BBD_Black_Box_Decryption/BBD_021_F8_SPECIFIC_DECRYPTION.md)

