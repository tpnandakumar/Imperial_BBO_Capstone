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

The result was deliberately challenging for BBD. **SOC won 7 of the 8 functions. BBD won F6 only.** Across functions, mean normalised MAE was approximately `0.3159` for BBD and `0.2118` for SOC.

This is one of the most important findings in the decryption series. F5 and F8 can be described extremely closely by compact equations when the complete history is available, yet the flexible SOC models predict later observations more accurately. The distinction between *describing the sampled history* and *recovering a mechanism that generalises prospectively* is therefore now explicit.

F6 is the exception. BBD achieved lower forward error than SOC despite F6's repeated-coordinate variability. That result makes F6 a priority for uncertainty-aware structural investigation rather than a candidate for simple deterministic decryption.

See [BBD 007: BBD versus SOC Prediction Challenge](BBD_007_BBD_VS_SOC_CHALLENGE.md).

## BBD 008: Discriminatory query design

BBD 008 changes the objective from prediction to **falsification and identification**. It searches the original bounded coordinate space for points where the strongest remaining BBD and SOC mechanisms make maximally different predictions.

A discriminatory query is valuable because one genuine evaluation at such a point could eliminate several competing explanations at once. The design combines normalised prediction disagreement, maximum model spread and distance from previously sampled coordinates. Numerically explosive extrapolations are excluded so that unstable polynomial behaviour is not mistaken for useful evidence.

BBD 008 produces five diverse proposed identification coordinates for every function and records the prediction of every retained candidate model. These are proposed experiments only, not Imperial submissions or observed outputs.

See [BBD 008: Discriminatory Query Design](BBD_008_DISCRIMINATORY_QUERY_DESIGN.md).

## BBD 009: Prospective-evidence confidence recalibration

BBD 009 recalibrates the earlier structural ranking using the forward-prediction evidence from BBD 007 and the unresolved mechanism disagreement from BBD 008. The new score is deliberately prospective-heavy. Retrospective fit contributes only one quarter of the index, while prospective competitiveness and forward test wins contribute three fifths.

If SOC wins the function-level forward challenge, the recalibrated index cannot enter the strongest evidence band regardless of how closely a full-history equation fits. Large BBD 008 prediction spread also lowers the score because it shows that materially different mechanisms remain compatible with the historical data.

The output is an evidence-strength index rather than a probability of exact recovery. Every function remains explicitly marked as not exactly recovered until a genuinely independent discriminatory evaluation is available.

See [BBD 009: Prospective-Evidence Confidence Recalibration](BBD_009_PROSPECTIVE_CONFIDENCE.md).

## BBD 010: F6-specific decryption

BBD 010 begins function-specific decryption with F6 because F6 ranked first after the prospective recalibration and was the only function where BBD beat SOC in the function-level forward challenge.

The experiment separates coordinate-only and state-aware explanations using expanding-window prediction. State-aware candidates include the F6 coordinates together with week index, previous observed F6 output and movement from the preceding F6 coordinate. Exact repeated coordinates are analysed separately to quantify the inconsistency that a deterministic coordinate-only equation cannot explain.

The purpose is to determine whether F6 is better described as a static response surface or as a response surface plus a state, path or hidden-context component. It does not assume that the available state proxies are the true hidden variables.

See [BBD 010: F6-Specific Decryption](BBD_010_F6_SPECIFIC_DECRYPTION.md).

## Why temporal ordering is retained

The thirteen observations are not treated as an unordered cloud. BBD preserves round order, coordinate displacement, objective change, repeated points and previous-state information.

## Evidence boundary

All BBD equations, gradients, benchmark matches, confidence scores, discriminatory queries and model diagnostics are post-capstone reconstructions. They are never labelled as observed Imperial evaluations or exact hidden equations unless independent evidence could establish that claim.

## Outputs

BBD produces model-competition, temporal-residual, repeatability, transition, gradient, near-axis derivative, equation-recovery, benchmark-family, decryption-confidence, BBD-versus-SOC prospective prediction, discriminatory-query, prospectively recalibrated evidence and F6-specific mechanism datasets in `Advanced_Extension_Series/BBD_Black_Box_Decryption/outputs/`.

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

The project advances only when each stage has a reproducible result and a stated uncertainty boundary.
