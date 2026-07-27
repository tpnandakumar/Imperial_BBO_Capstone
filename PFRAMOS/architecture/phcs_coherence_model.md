# PHCS Coherence Model

## Scope

PHCS is the Harmony, Congruence, Synchronisation and Coherence layer within PFRAMOS.

It evaluates coherence at four levels:

1. **Data coherence** for the evidence supplied to the engine.
2. **Nodal coherence** within each optimisation node.
3. **Internodal coherence** across bidirectional multi-spoke links.
4. **Engine coherence** across the complete active pathway.

## Signed scale

The coherence index lies in the interval `[-1, +1]`.

- `+1` means maximum validated coherence.
- `0` means balanced, weak or unresolved evidence.
- `-1` means maximum validated conflict.

The index is calculated from dependency-adjusted support and conflict:

```text
CI = (support - conflict) / (support + conflict + epsilon)
```

The index must always be accompanied by support strength, conflict strength, evidence volume, independence score and unresolved issue count.

## Nodal augmentation

A node may receive temporary activity augmentation when its connected pathways show high positive internodal coherence.

Augmentation is:

- thresholded
- capped
- temporary
- fully audited
- unable to create terminal authority by itself

Conflict penalties remain separate from augmentation so positive support and opposition are never hidden inside one transformation.

## Maximum-result pathway

The active graph produces an auditable centreline through connected nodes with the strongest validated optimisation results. This centreline is not necessarily the final candidate by itself. It identifies the pathway through which the strongest coherent result is propagating.

## Coherence envelopes

The maximum-result pathway is surrounded by an adaptive coherence envelope:

- **Band** for short, ordered or near-planar pathways.
- **Cylinder** for stable directed pathways extending through several nodes.
- **Sphere** for a hub receiving multidirectional coherent support.

The envelope radius decreases as coherence increases. Nested layers represent reducing coherence index thresholds moving away from the centreline.

A narrow envelope means that the high-result pathway is strongly localised and consistently supported. A wide envelope means that uncertainty, conflict or dispersion remains high.

## Safeguards

1. High coherence cannot compensate for incomplete or invalid data.
2. Correlated evidence is dependency-discounted.
3. Coherence augmentation is capped to prevent self-reinforcing node dominance.
4. Negative coherence cannot be silently converted into inactivity. Conflict remains visible.
5. A highly active node still requires independent pathway support before terminality.
6. Geometry is an analytical representation of pathway structure, not proof of an underlying physical shape.
