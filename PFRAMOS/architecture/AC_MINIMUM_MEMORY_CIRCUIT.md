# AC Minimum Computational Memory Circuit

## Foundational principle

Recall is not memory itself. Recall is an observable output produced by a wider cognitive circuit.

At minimum, successful recall requires:

1. attention
2. semantic organisation
3. encoding
4. retention
5. retrieval

A failure at any one of these stages can produce poor recall.

## Minimum circuit

```text
Input
  ↓
Attention
  ↓
Semantic organisation
  ↓
Encoding
  ↓
Retention
  ↓
Retrieval
  ↓
Recall
```

## Mathematical structure

For item i, semantic organisation is:

```text
S_i = 0.45F_i + 0.30C_i + 0.25P_i
```

Where:

- F_i is semantic fit
- C_i is contextual coherence
- P_i is prior knowledge

Encoding is:

```text
E_i = A_i × S_i × (1 - I_i) × (0.85 + 0.15N_i)
```

Where:

- A_i is attention
- I_i is interference
- N_i is novelty

Retention is:

```text
M_i(t) = E_i exp(-lambda_i t) + eta_i R_i(1 - E_i exp(-lambda_i t))
```

Where:

- lambda_i is the forgetting rate
- eta_i is consolidation efficiency
- R_i is reactivation

Retrieval accessibility is:

```text
Q_i = M_i(t) × (0.40U_i + 0.35V_i + 0.25X_i) × (1 - K_i)
```

Where:

- U_i is cue similarity
- V_i is semantic route quality
- X_i is contextual match
- K_i is retrieval competition

Recall probability is:

```text
P(recall_i) = Q_i × (0.55 + 0.25A_i + 0.20S_i)
```

## Diagnostic interpretation

Low recall must be decomposed into its weakest component:

- attention failure
- semantic failure
- encoding failure
- retention failure
- retrieval failure

This prevents AC from treating every memory error as a storage problem.

## Computational consequence

Each failure mode requires a different corrective action.

| Failure mode | AC response |
|---|---|
| Attention | increase focus, reduce distraction, reprioritise evidence |
| Semantic | strengthen concept relationships and contextual meaning |
| Encoding | improve association, structure and consolidation conditions |
| Retention | reactivate, rehearse, reduce inappropriate forgetting |
| Retrieval | generate cues, widen semantic routes, reduce competition |

## Integration with PIMF

PIMF monitors how each memory component changes over time:

```text
Attention
  ↓
ΔA
  ↓
Δ²A
  ↓
Δ³A
```

The same applies to semantic strength, encoding, retention and retrieval.

This allows AC to detect whether the memory circuit is improving, plateauing, reversing, oscillating or approaching a boundary.

## Integration with PFRAMOS

PFRAMOS selects the corrective conduit according to the diagnosed failure mode, coherence, uncertainty, risk and expected gain.

Examples:

- poor attention activates an attention-regulation conduit
- weak semantic organisation activates a semantic-reconstruction conduit
- poor retrieval activates a cue-generation conduit
- unstable retention activates a consolidation conduit

## Governing statement

Memory is a distributed cognitive process. Recall is only the final visible expression of that process.
