# Multilevel Reverse Feedback Control

## Purpose

Reverse feedback prevents uncontrolled overdrive and detects underperformance caused by insufficient information, poor confidence, excessive inhibition or inadequate resource allocation.

## Feedback hierarchy

### Level 1: Local execution feedback

Corrects latency, command mismatch, minor overshoot, signal loss and local resource spikes.

### Level 2: Correcting and co-ordinating feedback

Regulates timing, trajectory, gain, oscillation, pathway conflict, overshoot, undershoot and loss of equilibrium.

### Level 3: Parallel controller feedback

A-DMIC receives resource, energy, memory, load, stability and recovery signals.

PCC receives task success, accuracy, target error, confidence and strategic outcome signals.

The controllers may share, augment or act independently in response.

### Level 4: Executive feedback

Persistent failure, conflict or uncertainty returns to the Cognitive Array Cortex and Limbic Computational System for strategic revision, reprioritisation, suspension or human escalation.

## Lowest competent correction principle

Correction should occur at the lowest level capable of resolving the problem. Higher levels intervene only when the error exceeds local authority, competence or stability limits.

## Bidirectional control

Descending flow:

Intent -> control -> correction -> relay -> execution

Ascending flow:

Outcome -> error -> state -> evaluation -> adaptation

## Anti-overdrive and anti-underperformance checks

Every control cycle should assess:

- excessive gain
- accelerating resource demand
- instability or oscillation
- diminishing returns
- inadequate evidence
- low confidence
- insufficient exploration
- excessive conservation
- information starvation

The response may be to reduce, pause, acquire information, allocate resources, expand exploration, revise strategy or escalate.
