# 008CH Predictive Multi-Agent EFAMES Blueprint

## Objective

Transform EFAMES from reactive correction into a predictive, multi-agent cognitive framework while preserving the efficient ECSP three-model core.

## Architecture

```text
Input
→ Predictive Friction Check
→ Certainty Lock or Multi-Agent Audit
→ Vectorised Error Memory Match
→ Error-Type and Class-Pair Routing
→ Real-Time Calibration
→ Refined Output
→ Counterfactual Explanation
```

## Lightweight specialist agents

The initial agents should be implemented as independent scoring modules rather than heavyweight language-model processes:

- Logic Auditor: checks internal probability and route consistency.
- Edge-Case Finder: detects distance from development support and boundary risk.
- Calibration Critic: distinguishes calibration error from likely class error.
- Counterfactual Agent: finds the smallest probability or feature perturbation that changes the route.
- Efficiency Governor: enforces the per-sample computation budget.
- Memory Retriever: retrieves prior residual-error signatures and successful corrections.

Their recommendations are fused by a consensus controller. No single agent can force full rescue without the Efficiency Governor and intervention-benefit predictor agreeing.

## Predictive friction

Interaction telemetry is optional and must be explicitly supplied. Valid signals include:

- pause duration
- edit count
- backtracking
- repeated submission attempts
- response latency
- uncertainty markers

The current tabular benchmark datasets do not contain these signals. They cannot be retrospectively inferred or reported as measured.

## Vectorised error memory

Phase 1 uses a local nearest-neighbour vector store with a stable interface. FAISS or Chroma can later replace the local backend without changing the controller API.

Stored fields:

- uncertainty and disagreement vector
- top class pair
- error type
- successful specialist
- residual correction
- correction confidence
- dataset and engine context
- timestamp and validation status

## Asynchronous audit

Core prediction returns immediately. Deeper audits run concurrently only where the application permits reversible updates or delayed confirmation. For irreversible decisions, the system must await the required safety audit.

## RLFC

Reinforcement Learning from Critique should begin as an offline contextual-bandit loop, not unconstrained online reinforcement learning.

Reward:

```text
correct decision gain
+ calibration gain
+ floor protection
- false intervention
- missed error
- active-model cost
- latency cost
```

All policy updates remain quarantined until matched validation confirms improvement.

## Dynamic granularity

Explanation complexity is controlled independently of prediction complexity:

- low friction and high certainty: concise output
- moderate uncertainty: short rationale
- repeated error signature: targeted explanation
- high cognitive load or critical risk: staged explanation with counterfactuals

## Telemetry

Measure directly:

- prediction latency
- audit latency
- memory retrieval latency
- active models
- CPU utilisation
- peak memory
- intervention rate
- false-intervention rate

Electrical energy and financial cost remain unreported until directly measured.

## Experiment sequence

- 008CG: EFAMES versus ECSP-3 + 008CE
- 008CH-A: multi-agent audit ablation
- 008CH-B: vector-memory backend comparison
- 008CH-C: asynchronous latency study
- 008CH-D: offline RLFC policy study
- 008CH-E: counterfactual quality and false-positive study
