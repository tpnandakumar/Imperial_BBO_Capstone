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
8. multi-parameter coordinated DLHCR
9. oracle

## Homeostatic and coordinated controller

- target corridor: 0.40 to 0.60
- hard limits: 0.20 to 0.80
- upward correction rate: 0.10
- downward correction rate: 0.20
- critical correction rate: 0.30
- inertia: 0.90
- hysteresis: 0.04
- maximum laminar update step: 0.035
- contextual target centre adjusted by validation reliability and modality disagreement
- corridor width adjusted by ambiguity
- coordinated switching cost adjusted by validation reliability

High coherence is compressed towards the upper target boundary. Low coherence is raised towards the lower target boundary. The laminar variants add inertia, bounded update steps and oscillation monitoring.

## Conduit maintenance metrics

- mean coherence step variation
- oscillation reversal rate
- laminarity index
- route-switch rate
- coherence-adjustment rate

## Completed trial results

The unweighted fusion baseline achieved the highest non-oracle protected-test action accuracy at 0.9933. Reliability-weighted fusion achieved 0.9900. Static PGC, unrestricted DLHCR, laminar DLHCR and coordinated DLHCR each achieved 0.6867.

DLHCR adjusted coherence on every protected-test observation. Unrestricted DLHCR produced mean step variation of 0.002825, oscillation reversal rate of 0.4336 and laminarity index of 0.5099.

Laminar conduit maintenance reduced mean step variation to 0.000969 and oscillation reversal rate to 0.0924, raising the laminarity index to 0.8882. This improvement was consistent across all five seeds.

Urgent-threat recall remained 1.0000 for all PGC dynamic variants, with zero missed threats and zero false escalations in this synthetic trial.

## Interpretation

This is a valid stabilisation result and a null task-performance result. Dynamic live homeostatic regulation materially improved conduit smoothness and reduced oscillatory reversal, but it did not alter the selected actions or improve protected-test accuracy.

The current downstream action logic remains too threshold-dominated. Regulated coherence is active, but most adjusted values stay on the same side of the action gates. The next experiment should connect effective coherence to graded action margins, adaptive switching cost, abstention thresholds and error-predictive timing.

## Future cerebellar-style integration

A future cerebellar-like modulation layer should be tested separately. Its proposed role is to predict the next coherence state, detect phase and amplitude error, damp overshoot, anticipate oscillatory reversals and apply rapid corrective micro-adjustments to the laminar conduit. It must remain subordinate to factual accuracy, safety and protected-test governance.

This component was not included in Experiment 004, so no cerebellar performance claim is made here.

## Evidence status

All outputs are trial evidence and are not publication evidence.
