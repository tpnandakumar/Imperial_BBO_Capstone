# PGC Experiment 004

## Title

Dynamic Live Homeostatic Coherence Regulation with Laminar Conduit Maintenance

## Objective

Test whether live upper-lower homeostatic coherence regulation can keep effective coherence inside a fine operating corridor while maintaining stable laminar conduit flow, without using protected-test labels for adaptation.

## Design

The deterministic multimodal emotional scenario generator from Experiment 003 was retained so that the controller modification was isolated. Five fixed seeds were used. Each seed was divided into 60% train, 20% validation and 20% protected test partitions.

Validation data estimated coherence reliability. Protected-test labels were used only after routing for evaluation and never for tuning.

## Comparison arms

1. factual perception only
2. emotional signal only
3. unweighted fusion
4. reliability-weighted fusion
5. static PGC coherence
6. dynamic live homeostatic coherence regulation, DLHCR
7. DLHCR with laminar conduit maintenance
8. oracle

## Homeostatic controller

- target corridor: 0.40 to 0.60
- hard limits: 0.20 to 0.80
- upward correction rate: 0.10
- downward correction rate: 0.20
- critical correction rate: 0.30
- inertia: 0.90
- hysteresis: 0.04
- maximum laminar update step: 0.035

High coherence is compressed towards the upper target boundary. Low coherence is raised towards the lower target boundary. The laminar variant adds inertia, bounded update steps and oscillation monitoring.

## Conduit maintenance metrics

- mean coherence step variation
- oscillation reversal rate
- laminarity index
- route-switch rate
- coherence-adjustment rate

## Result summary

The unweighted fusion baseline achieved the highest non-oracle protected-test action accuracy at 0.9792. Reliability-weighted fusion achieved 0.9708. Static PGC, DLHCR and laminar DLHCR each achieved 0.7000.

DLHCR was active on all protected-test observations. The laminar conduit variant achieved a mean laminarity index of 0.9863, compared with 0.9861 for unrestricted DLHCR. Neither dynamic variant changed route-switch rate or task accuracy relative to static PGC.

## Interpretation

This is a valid null result. The controller successfully maintained a stable, low-variation coherence conduit, but the current downstream decision logic is insufficiently sensitive to the regulated coherence value. Coherence presently acts mainly as a gate and empathy modifier, so values remaining above the gate often produce the same action.

The next refinement should connect regulated coherence to graded routing margins, switching costs or abstention thresholds, then repeat the protected-test comparison.

## Evidence status

All outputs are trial evidence and are not publication evidence.
