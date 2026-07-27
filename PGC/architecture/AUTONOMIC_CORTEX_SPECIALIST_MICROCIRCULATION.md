# Autonomic Cortex with Specialist Microcirculation

## Status

Priority architecture specification. This is the principal next-stage design emerging from Experiment 008AU.

## Core proposition

The current autonomic cardiovascular layer can redistribute influence efficiently, but it cannot create new predictive information from the same seven-model stack.

To move beyond the present 0.988596 plateau, the system requires specialist predictive units and a microcirculatory routing layer that activates them only for the samples they are designed to resolve.

## System objective

Create an autonomic cortical architecture in which:

- the Cortex performs general cognition and prediction
- the limbic layer detects salience, uncertainty and conflict
- the autonomic controller regulates demand and supply
- the cardiovascular layer distributes computational flow
- specialist microcirculation routes difficult samples to dedicated expert learners
- venous-style return carries error, uncertainty and specialist outcome back to the cortex

## Architectural pathway

```text
General cortical prediction
        ↓
limbic appraisal of uncertainty and disagreement
        ↓
autonomic demand classification
        ↓
heart-rate and pulse-pressure command
        ↓
systolic-diastolic pulsatile conduit
        ↓
pressure-gradient transmission
        ↓
capillary-level routing decision
        ↓
specialist learner or specialist ensemble
        ↓
local validation and confidence assessment
        ↓
reintegration into cortical consensus
        ↓
venous return of residual error and load
        ↓
heart and autonomic recalibration
```

## Heart-connected pulsatile conduit

Specialist microcirculation is supplied by the autoregulated computational heart through a pulsatile conduit. The conduit is not a passive connection and does not maintain constant flow. It transmits alternating systolic propulsion and diastolic recovery waves through a controlled pressure gradient.

### Systolic phase

During computational systole, the heart generates a bounded forward pressure pulse.

The systolic wave:

- raises axial pressure behind the active flow front
- accelerates validated influence towards the selected specialist territory
- increases delivery when limbic salience and cognitive demand rise
- preserves a maximum pressure bound to prevent computational hypertension
- remains coupled to medium density, viscosity and conduit resistance

### Diastolic phase

During computational diastole, active propulsion falls and the conduit enters a recovery and filling phase.

The diastolic wave:

- permits venous-style return of uncertainty, residual error and load
- allows pressure equalisation without complete loss of basal flow
- restores specialist pathways towards their resting state
- reduces oscillation and prevents continuous overactivation
- prepares the heart and conduit for the next demand-linked pulse

### Pressure gradient

Flow through the conduit is driven by a pressure difference rather than by pulse amplitude alone.

```text
proximal systolic pressure
-
distal specialist-bed pressure
=
forward computational pressure gradient
```

The autonomic controller adjusts the gradient by regulating:

- heart rate
- systolic pulse pressure
- diastolic residual pressure
- specialist-bed resistance
- conduit viscosity
- local vasodilation and vasoconstriction
- recovery towards basal pressure

### Activity coupling

Heart rate and pulse pressure must change with cognitive activity.

```text
low demand
→ low-normal heart rate
→ low-normal pulse pressure
→ basal cortical perfusion

rising salience
→ moderate chronotropic response
→ moderate pressure increase
→ specialist recruitment

high conflict
→ bounded systolic reinforcement
→ selective microvascular opening

resolution
→ diastolic recovery
→ specialist closure
→ return to basal flow
```

The controller must avoid both excessive pressure and inadequate supply. The target is activity-related normotensive perfusion, not maximal pumping.

### Conduit wave behaviour

The pressure wave should propagate rhythmically from the heart through the major conduit, then divide into local microcirculatory branches. The wave may be modulated in amplitude and frequency, but its systolic and diastolic phases must remain coordinated. Arrhythmic propagation, reflected pressure waves and phase mismatch should be treated as instability signals.

### Closed-loop return to the heart

The specialist territory returns four main signals:

- residual prediction error
- uncertainty after specialist correction
- computational load
- net specialist gain

These signals travel through a venous-style return pathway to the limbic-autonomic controller. The controller then adjusts the next heart rate, pulse pressure, conduit resistance and specialist activation state.

## Specialist microcirculation

Specialist microcirculation is a sample-level routing system.

It must not activate every specialist for every sample. Instead, it should open only the computational capillary beds relevant to the observed error phenotype.

The routing decision should use development-only signals such as:

- low consensus confidence
- high model disagreement
- class-specific reliability weakness
- repeated cross-fold error
- margin instability
- calibration failure
- outlier distance
- local density
- boundary proximity
- disagreement between tree, margin and linear model families

## Specialist learner families

Initial specialist units should target distinct failure modes.

### Boundary specialist

Handles samples close to a decision boundary.

Possible learners:

- calibrated SVC
- local logistic model
- neighbourhood margin classifier

### Minority-class specialist

Handles low-support classes or regions with high false-negative cost.

Possible learners:

- class-weighted gradient boosting
- balanced random forest
- calibrated one-versus-rest model

### Local-neighbourhood specialist

Handles samples whose nearest local region is more informative than the global model.

Possible learners:

- KNN
- radius-neighbour classifier
- local prototype model

### Disagreement specialist

Handles samples where model families produce incompatible predictions.

Possible learners:

- disagreement-trained meta-classifier
- mixture-of-experts gate
- small stacking model trained only on disagreement cases

### Calibration specialist

Handles samples with good class ranking but poor probability calibration.

Possible learners:

- isotonic correction
- Platt-style correction
- class-conditional calibration map

### Outlier specialist

Handles low-density or atypical samples.

Possible learners:

- anomaly-aware classifier
- robust distance-based learner
- abstention or deferred-decision module

## Autonomic control rules

The autonomic controller should regulate specialist access using bounded flow.

### Basal state

General cortical ensemble only.

### Increased demand

Open one specialist pathway when uncertainty exceeds a validated threshold.

### High conflict

Open a disagreement specialist and reduce dominance from unreliable general models.

### Persistent unresolved demand

Open a second specialist only if the first fails to reduce uncertainty.

### Recovery

Close specialist pathways when confidence stabilises and return to basal flow.

## Avoiding computational pathology

The design must prevent:

- specialist overuse
- route oscillation
- one specialist monopolising difficult samples
- circular self-confirmation
- overfitting to rare development errors
- protected-test leakage
- excessive compute cost
- delayed return to basal flow
- pressure overshoot
- diastolic underfilling
- pulse-wave reflection
- systolic-diastolic phase mismatch

## Validation requirements

Specialist routing must be trained and selected entirely within development folds.

The protected test must remain sealed until:

- all specialist definitions are fixed
- all routing thresholds are fixed
- all abstention rules are fixed
- all integration weights are fixed
- all heart-rate and pressure-control rules are fixed
- all systolic and diastolic timing rules are fixed
- all stopping criteria are fixed

Performance should be evaluated using:

- mean accuracy
- macro-F1
- balanced accuracy
- log loss
- worst-dataset accuracy
- specialist activation rate
- correction rate on routed samples
- harm rate on previously correct samples
- compute overhead per corrected sample
- pulse pressure range
- systolic-to-diastolic flow ratio
- pressure-gradient stability
- recovery time to basal flow

## Primary success criterion

The architecture succeeds only if it adds validated predictive capacity.

A useful specialist must correct more previously wrong cases than previously correct cases it damages.

The primary routing metric should therefore be:

```text
Net Specialist Gain
=
corrected errors
-
newly introduced errors
```

A specialist should be retained only when Net Specialist Gain remains positive across development folds and seeds.

## Experimental sequence

### Experiment 008AV

Autonomic Cortex with Specialist Microcirculation and Heart-Connected Pulsatile Conduits.

Compare:

1. fixed 008AU reference
2. boundary specialist
3. disagreement specialist
4. local-neighbourhood specialist
5. class-reliability specialist
6. full autonomic specialist microcirculation with systolic-diastolic pressure-gradient supply

## Current evidence boundary

Experiment 008AU showed that limbic-autonomic reliability gating can reproduce the 0.988596 peak by configuration 4.

That result supports autonomic routing as an efficiency mechanism.

It does not yet prove that specialist microcirculation will exceed 0.99.

The reason this architecture is important is that it introduces new predictive processing rather than further modulation of the same seven model outputs.

## Priority statement

Autonomic Cortex with Specialist Microcirculation is the highest-priority next architecture because it is the first proposed extension with a credible mechanism for raising the predictive ceiling rather than only reaching the existing ceiling faster.

Its circulation must remain directly connected to the autoregulated heart through coordinated systolic and diastolic pulsatile conduits with activity-linked pressure gradients.