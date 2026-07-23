# PFRAMOS

## Pisharam Fit-Regulated, Agreement-Guided Multinodal, Multilayer Cross-Optimisation System

**Status:** Experimental founding version 0.1

PFRAMOS is an open, auditable-box optimisation engine for sparse, sequential and uncertain optimisation problems. Every node performs a defined optimisation task. Nodes communicate through feed-forward, feedback, lateral and non-adjacent bidirectional multi-spoke links.

Any eligible node may become the temporary Terminal Active Node. Terminal authority is not predetermined or random. It emerges from problem-specific evidence, validated contribution, cross-node support, robustness and uncertainty control.

## Core principles

1. Every node is an optimisation node.
2. All nodes have equal eligibility for temporary terminality.
3. Nodes activate according to problem relevance and evidence.
4. Dormant nodes do not influence the live pathway.
5. Active nodes form the current optimisation pathway.
6. Cross-node agreement strengthens evidence only after dependency correction.
7. Fragile or duplicated signals lose decision authority.
8. Every transformation, rejection, feedback event and final decision is auditable.
9. Nodes may be proposed, validated, activated, deprecated, retired and archived.
10. PFRAMOS supports domain adapters while preserving a general core.

## Relationship to the Imperial BBO challenge

The first adapter uses Weeks 1 to 11 as the historical evidence base for the next smart submission. PFRAMOS does not rewrite previous submissions. Candidate values remain private until validated and officially submitted.

## Relationship to PIMF

PIMF identifies influence, persistence, trajectory and state. PFRAMOS uses those outputs as optimisation evidence. PFRAMOS does not replace or invalidate PIMF.

```text
BBO observations
        ↓
PIMF influence and trajectory diagnosis
        ↓
PFRAMOS multinodal cross-optimisation
        ↓
Audited candidate shortlist
        ↓
Final BBO submission decision
```

## Initial implementation

- `core/node_contract.py`: common contract for optimisation nodes
- `core/node_registry.py`: lifecycle and eligibility registry
- `core/audit_engine.py`: append-only audit records
- `adapters/imperial_bbo/`: BBO-specific data and objective adapter
- `analysis/`: walk-forward, fit-regulation and candidate robustness experiments

## Validation rule

No PFRAMOS recommendation controls a live submission unless it performs at least as reliably as the existing BBO approach under historical walk-forward and stress testing.