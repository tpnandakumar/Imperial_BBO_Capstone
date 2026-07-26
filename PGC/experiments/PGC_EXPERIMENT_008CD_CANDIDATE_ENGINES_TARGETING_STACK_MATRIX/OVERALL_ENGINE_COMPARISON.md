# Overall Engine Comparison and Improvement Roadmap

## Evidence status

This comparison integrates the comparative development evidence from Experiments 008CB, 008CC and 008CD. It is not final independent confirmation because the matched evaluation framework has been reused during controller development.

Net Regenerative Efficiency and active-model count are computational proxies. They are not direct measurements of electrical energy, runtime cost or monetary cost.

## Overall conclusion

No single configuration dominates accuracy, efficiency, versatility and cost effectiveness simultaneously.

### Best single engine family overall

**ECSP + A-DMIC**

It provides the strongest overall balance of accuracy, stability, calibration, versatility and moderate model use.

### Best pure accuracy configuration

**ECSP, 11-model stack, ILS-H**

- mean accuracy: 0.984698
- minimum accuracy: 0.977973
- sample SD: 0.005080
- median accuracy: 0.983821
- near-peak frequency at or above 99.0%: 20%
- mean active models: 11.0
- Net Regenerative Efficiency: 0.571616

This was the strongest combination of mean accuracy, minimum accuracy and low variability.

### Best median accuracy configuration

**AX-R-BK, 11-model stack, ILS-H**

- median accuracy: 0.984747
- mean accuracy: 0.984056
- sample SD: 0.006241
- minimum accuracy: 0.968713
- near-peak frequency: 19%
- targeting activation rate: 7.44%

### Best efficiency engine

**DTRRR protected stochastic + A-DMIC baseline**

From Experiment 008CB:

- median accuracy: 0.983821
- mean accuracy: 0.983043
- maximum accuracy: 0.997222
- mean active models: 2.714
- Net Regenerative Efficiency: 0.874492

This is the strongest low-cost serious candidate, although its floor and variability are weaker than ECSP.

### Best sparse guided balance

**AX-R-BK, 3-model stack, FBW-PVF**

- median accuracy: 0.982895
- mean accuracy: 0.982894
- minimum accuracy: 0.973977
- near-peak frequency: 24%
- mean active models: 6.442
- Net Regenerative Efficiency: 0.734801

The nominal three-model stack recruits more than six models on average after guidance, so it is not a true three-model inference cost.

### Best sparse versatility

**ECSP, 3-model stack, Dual MG-DMHLP-LOS-SSV**

- median accuracy: 0.982895
- mean accuracy: 0.982494
- minimum accuracy: 0.973002
- near-peak frequency: 27%
- mean active models: 7.110
- Net Regenerative Efficiency: 0.711520

## Overall scorecard

| Configuration | Accuracy | Efficiency | Versatility | Cost effectiveness | Recommended role |
|---|---|---|---|---|---|
| ECSP + A-DMIC baseline | Excellent | Excellent | Best | Excellent | Best overall single engine |
| ECSP 11 + ILS-H | Best | Low | Excellent | Moderate to low | Accuracy and stability ceiling |
| AX-R-BK 11 + ILS-H | Excellent | Low | Good | Moderate to low | Highest median accuracy |
| DTRRR protected stochastic + A-DMIC | Very good | Best | Good | Best | Low-cost default engine |
| AX-R-BK 3 + FBW-PVF | Very good | Good | Good | Good | Sparse guided balance |
| ECSP 3 + Dual MG-DMHLP-LOS-SSV | Very good | Moderate | Excellent | Moderate | Sparse adaptive route |

## Stack-aware targeting rule

The 008CD matrix produced a clear operational pattern:

```text
3 and 5-model stacks
→ FBW-PVF usually best

7-model stacks
→ engine-dependent transition zone

10 and 11-model stacks
→ ILS-H usually best
```

Sparse stacks need broad trajectory capture. Large stacks are already close to the consensus route and benefit more from low-activation precision honing.

## Recommended deployable architecture

A cost-aware cascade is preferable to continuous use of the most complex engine.

```text
DTRRR protected stochastic + A-DMIC
→ low-cost default route

uncertainty, disagreement or floor risk
→ ECSP + A-DMIC escalation

large trajectory deviation
→ FBW-PVF

close-range deviation
→ ILS-H

persistent uncertainty or unsafe route
→ ECSP 11 + ILS-H rescue route
```

### Operating hierarchy

1. **Default layer:** DTRRR protected stochastic + A-DMIC.
2. **Adaptive escalation:** ECSP + A-DMIC when disagreement, low margin or instability appears.
3. **Targeting:** FBW-PVF for large deviation, dual handover for intermediate deviation, ILS-H for close-range deviation, and zero correction when aligned.
4. **Rescue layer:** ECSP 11 + ILS-H only when lower-cost routes remain unsafe or unresolved.

## Priority improvements

### 1. Replace uncertainty gating with intervention-benefit prediction

The current controllers mainly detect uncertainty. The next controller should estimate whether intervention is likely to improve the trajectory.

A cross-fitted development-only predictor should use:

- confidence
- margin
- entropy
- model disagreement
- trajectory direction and velocity
- stack composition
- engine identity
- atmospheric state
- prior correction success

The output should be the estimated probability that targeting improves the final prediction.

### 2. Make targeting explicitly stack-aware

Use FBW-PVF as the normal sparse-stack controller, use an engine-specific transition rule around seven models, and use ILS-H for ten and eleven-model stacks.

### 3. Restrict stability-spin activation

Stability spin should activate only when measurable oscillation exists, including repeated route switching, confidence reversal, alternating specialist selection or class-margin fluctuation. It should decay to zero after stable line-of-sight lock.

### 4. Distil the 11-model teacher

Use ECSP 11 + ILS-H as a teacher for a smaller student engine. Distil class probabilities, route selection, intervention decisions and floor protection into a three or five-model student.

### 5. Use progressive model recruitment

```text
2 or 3 core models
→ assess agreement

uncertain
→ add specialist

still uncertain
→ add ECSP route

persistent uncertainty
→ activate full stack
```

This should improve cost effectiveness while preserving the accuracy floor.

### 6. Measure real deployment cost

Future experiments should record:

- wall-clock latency
- CPU and GPU utilisation
- peak memory
- energy consumption
- monetary inference cost

Until then, active-model count and Net Regenerative Efficiency remain proxies only.

### 7. Freeze an independent confirmation study

The final validation should use untouched datasets or splits, new seeds, fixed protocols, no tuning after outcome review, external datasets and direct runtime and energy measurement.

## Final recommendations

- **Best single engine:** ECSP + A-DMIC
- **Best accuracy configuration:** ECSP 11 + ILS-H
- **Best efficiency and cost configuration:** DTRRR protected stochastic + A-DMIC
- **Best practical architecture:** DTRRR → ECSP → stack-aware targeting → ECSP 11 rescue
