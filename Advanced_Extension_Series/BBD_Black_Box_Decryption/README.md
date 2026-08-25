# BBD: Black Box Decryption

## Purpose

**BBD, Black Box Decryption**, is a post-capstone system-identification experiment. Its aim is not merely to predict a good next coordinate, but to determine what kind of mathematical mechanism could plausibly have generated the thirteen-round input-output history for each hidden function.

BBD is deliberately separate from the assessed Week 01 to Week 13 record. It does not alter historical observations and it does not claim access to the original Imperial objective functions.

## Central question

For each function, BBD asks:

> What is the simplest predictive mechanism consistent with the observed coordinates, outputs, repeated points, temporal order and movement between rounds?

## BBD 001: Static versus temporal system identification

BBD 001 compares static, nonlinear, temporal, movement-aware and state-aware predictors using chronological walk-forward validation.

## BBD 002: Temporal residual structure and repeatability

BBD 002 starts from a coordinate-only Gaussian Process and studies chronological residuals and repeated-coordinate behaviour. It showed that most apparent temporal effects did not survive direct residual correction, while F6 retained the clearest variability or short-memory signal.

See [BBD 002: Temporal Residual Structure and Repeatability](BBD_002_TEMPORAL_RESIDUALS.md).

## BBD 003: Directional derivative and gradient reconstruction

BBD 003 converts consecutive Week 01 to Week 13 input-output changes into directional-derivative constraints. It estimates regularised global and recent gradient vectors and identifies near-axis movements that provide the closest available empirical partial-derivative evidence.

The strongest coherent directional structure was found in **F5, F7 and F8**, with F2 as a secondary candidate. F6 retained a strong global transition fit but poor recent-gradient agreement. F1, F3 and F4 did not support a useful first-order gradient representation.

See [BBD 003: Directional Derivative and Gradient Reconstruction](BBD_003_GRADIENT_RECONSTRUCTION.md).

## BBD 004: Symbolic equation recovery

BBD 004 tests explicit regularised polynomial equations with leave-one-out validation and a mild complexity penalty.

The strongest current equation-recovery results are:

- **F5:** quadratic, normalised LOOCV MAE about `0.00575`;
- **F8:** simple linear equation, normalised LOOCV MAE about `0.0173`;
- **F7:** quadratic, normalised LOOCV MAE about `0.0257`;
- **F4:** quadratic, normalised LOOCV MAE about `0.118`, revealing nonlinear structure missed by a first-order gradient description.

These are strong retrospective reconstructions, not proof of exact hidden equations.

See [BBD 004: Symbolic Equation Recovery](BBD_004_SYMBOLIC_RECOVERY.md).

## BBD 005: Benchmark family matching

BBD 005 compares the observed history against constrained transformed versions of Sphere, Ellipsoid, Rastrigin, Ackley, Griewank, Schwefel and Rosenbrock functions.

The strongest new lead is **F4**, where a Rosenbrock-like transformed feature reduces normalised held-out error from about `0.118` for the BBD 004 quadratic to about `0.079`. F5, F7 and F8 also select Rosenbrock as the best tested benchmark family, but their BBD 004 equations remain substantially more predictive over full-history validation.

See [BBD 005: Benchmark Family Matching](BBD_005_BENCHMARK_MATCHING.md).

## BBD 006: Decryption ensemble and confidence ranking

BBD 006 combines the evidence from the first five stages. It separately scores predictive equation performance, equation compactness, gradient coherence, repeatability, mechanism simplicity and benchmark-family support.

Before prospective challenge testing, F8 and F5 ranked highest. These scores should now be read specifically as **retrospective structural confidence**, because BBD 007 showed that strong full-history reconstruction does not automatically imply superior forward prediction.

See [BBD 006: Decryption Ensemble and Confidence Ranking](BBD_006_DECRYPTION_CONFIDENCE.md).

## BBD 007: BBD versus SOC prediction challenge

BBD 007 moves beyond retrospective fit. It performs expanding-window chronological prediction in which BBD and SOC select and fit their models without access to the next historical output.

SOC won 7 of the 8 functions. BBD won F6 only. Across functions, mean normalised MAE was approximately `0.3159` for BBD and `0.2118` for SOC.

See [BBD 007: BBD versus SOC Prediction Challenge](BBD_007_BBD_VS_SOC_CHALLENGE.md).

## BBD 008: Discriminatory query design

BBD 008 changes the objective from prediction to falsification and identification. It searches the original bounded coordinate space for points where the strongest remaining BBD and SOC mechanisms make maximally different predictions.

See [BBD 008: Discriminatory Query Design](BBD_008_DISCRIMINATORY_QUERY_DESIGN.md).

## BBD 009: Prospective-evidence confidence recalibration

BBD 009 recalibrates the earlier structural ranking using the forward-prediction evidence from BBD 007 and the unresolved mechanism disagreement from BBD 008. F6 becomes the strongest current candidate after prospective evidence is given greater weight.

See [BBD 009: Prospective-Evidence Confidence Recalibration](BBD_009_PROSPECTIVE_CONFIDENCE.md).

## BBD 010: F6-specific decryption

BBD 010 begins function-specific decryption with F6. Coordinate-only Gaussian Process prediction outperformed the tested state-aware alternatives, favouring a static response surface despite non-identical repeated outputs.

See [BBD 010: F6-Specific Decryption](BBD_010_F6_SPECIFIC_DECRYPTION.md).

## BBD 011: F6 residual decomposition

BBD 011 holds the static F6 surface as the baseline and studies the remaining unexplained component. It tests GP uncertainty, coordinate novelty, movement, local response roughness, nearest-output difference, week and previous residual.

The strongest residual correction used the **previous residual alone**, reducing MAE on the five eligible forward tests from `0.056843` to `0.048096`. Other broad state proxies did not improve prediction. The current F6 interpretation is therefore a strong static coordinate-dependent surface plus a small unresolved residual component with preliminary short-memory evidence.

See [BBD 011: F6 Residual Decomposition](BBD_011_F6_RESIDUAL_DECOMPOSITION.md).

## BBD 012: F6 stochastic-versus-deterministic decomposition

BBD 012 asks whether the remaining F6 residual is better described as independent Gaussian variation, a first-order autoregressive process, or heteroscedastic variation linked to GP uncertainty. Model comparison uses AICc because the residual sequence is very small.

Repeated coordinates remain a separate determinism test. Non-identical outputs at an identical coordinate falsify exact coordinate-only determinism for the observed data, while still leaving open stochasticity, hidden evaluator state and other unobserved mechanisms.

See [BBD 012: F6 Stochastic-versus-Deterministic Decomposition](BBD_012_F6_STOCHASTIC_DETERMINISTIC.md).

## BBD 013: F6 latent variable reconstruction

BBD 013 tests whether several weak contextual signals can be compressed into a low-dimensional latent representation that explains part of the residual left by the static F6 surface. Week, previous output, movement, coordinate novelty and local response statistics are standardised and reduced by PCA to one- and two-component latent states.

The latent representation is judged by forward residual correction, not by retrospective correlation alone. Repeated-coordinate pairs are also compared in context space to see whether identical coordinates that produced different outputs occurred under materially different surrounding conditions.

See [BBD 013: F6 Latent Variable Reconstruction](BBD_013_F6_LATENT_VARIABLE_RECONSTRUCTION.md).

## Why temporal ordering is retained

The thirteen observations are not treated as an unordered cloud. BBD preserves round order, coordinate displacement, objective change, repeated points and previous-state information.

## Evidence boundary

All BBD equations, gradients, benchmark matches, confidence scores, discriminatory queries and model diagnostics are post-capstone reconstructions. They are never labelled as observed Imperial evaluations or exact hidden equations unless independent evidence could establish that claim.

## Run

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_001_system_identification.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_002_temporal_residuals.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_003_gradient_reconstruction.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_004_symbolic_recovery.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_005_benchmark_matching.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_006_decryption_confidence.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_007_bbd_vs_soc_challenge.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_008_discriminatory_query_design.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_009_prospective_confidence.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_010_f6_specific_decryption.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_011_f6_residual_decomposition.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_012_f6_stochastic_deterministic.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_013_f6_latent_variable_reconstruction.py
```

## Research sequence

**BBD 001** Static versus temporal mechanism competition  
**BBD 002** Residual temporal structure and repeatability analysis  
**BBD 003** Local directional derivative and gradient reconstruction  
**BBD 004** Symbolic equation recovery  
**BBD 005** Benchmark-family matching under constrained coordinate and output transformations  
**BBD 006** Decryption ensemble and retrospective confidence ranking  
**BBD 007** Prospective BBD versus SOC prediction challenge  
**BBD 008** Discriminatory query design for active falsification  
**BBD 009** Prospective-evidence confidence recalibration  
**BBD 010** F6-specific static-versus-state mechanism decryption  
**BBD 011** F6 residual decomposition and short-memory test  
**BBD 012** F6 stochastic-versus-deterministic residual classification  
**BBD 013** F6 low-dimensional latent-context reconstruction

The project advances only when each stage has a reproducible result and a stated uncertainty boundary.
