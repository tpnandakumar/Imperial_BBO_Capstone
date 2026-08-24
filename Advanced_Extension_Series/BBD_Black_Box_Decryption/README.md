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

F8 is the strongest compact decryption candidate because an eight-term linear equation reproduces the observed relationship with very low held-out error and coefficient signs that agree with BBD 003. F5 has the lowest numerical validation error, but its 14-term quadratic and near-zero regularisation require stronger challenge testing before structural claims are made.

See [BBD 004: Symbolic Equation Recovery](BBD_004_SYMBOLIC_RECOVERY.md).

## BBD 005: Benchmark family matching

BBD 005 compares the observed history against constrained transformed versions of Sphere, Ellipsoid, Rastrigin, Ackley, Griewank, Schwefel and Rosenbrock functions.

The strongest new lead is **F4**, where a Rosenbrock-like transformed feature reduces normalised held-out error from about `0.118` for the BBD 004 quadratic to about `0.079`. F5, F7 and F8 also select Rosenbrock as the best tested benchmark family, but their BBD 004 equations remain substantially more predictive. This argues against simply identifying them as transformed Rosenbrock functions.

F1 selects Rastrigin and F2/F3 select Ackley, but their held-out errors remain too large for confident family identification. F6 selects Rosenbrock, while its non-identical repeated outputs still require an uncertainty or hidden-state term.

See [BBD 005: Benchmark Family Matching](BBD_005_BENCHMARK_MATCHING.md).

## BBD 006: Decryption ensemble and confidence ranking

BBD 006 combines the evidence from the first five stages rather than allowing one excellent fit to dominate the interpretation. The confidence ensemble separately scores predictive equation performance, equation compactness, gradient coherence, repeatability, mechanism simplicity and benchmark-family support.

The output is an auditable ranking for F1 to F8 with each component retained in the result table. The score measures how strongly the available evidence supports the current reconstruction. It is not interpreted as a probability that the exact Imperial equation has been recovered.

See [BBD 006: Decryption Ensemble and Confidence Ranking](BBD_006_DECRYPTION_CONFIDENCE.md).

## Why temporal ordering is retained

The thirteen observations are not treated as an unordered cloud. BBD preserves round order, coordinate displacement, objective change, repeated points and previous-state information. Later stages compare this sequential evidence with explicit equation families.

## Evidence boundary

All BBD equations, gradients, benchmark matches, confidence scores and model diagnostics are post-capstone reconstructions. They are never labelled as observed Imperial evaluations or exact hidden equations unless independent evidence could establish that claim.

## Outputs

BBD currently produces model-competition, temporal-residual, repeatability, transition, gradient, near-axis derivative, equation-recovery, benchmark-family and decryption-confidence datasets in `Advanced_Extension_Series/BBD_Black_Box_Decryption/outputs/`.

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
```

## Research sequence

**BBD 001** Static versus temporal mechanism competition  
**BBD 002** Residual temporal structure and repeatability analysis  
**BBD 003** Local directional derivative and gradient reconstruction  
**BBD 004** Symbolic equation recovery  
**BBD 005** Benchmark-family matching under constrained coordinate and output transformations  
**BBD 006** Decryption ensemble and confidence ranking  
**BBD 007** Predicted function challenge against SOC

The project advances only when each stage has a reproducible result and a stated uncertainty boundary.
