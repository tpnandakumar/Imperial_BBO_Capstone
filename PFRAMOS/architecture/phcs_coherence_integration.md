# PHCS Coherence Integration

## Signed coherence scale

The PHCS Coherence Index is defined on `[-1, +1]`.

- `+1`: maximum validated coherence
- `0`: balanced, weak or unresolved evidence
- `-1`: maximum validated conflict

A coherence result must always retain its support strength, conflict strength, evidence volume, independence score and unresolved issue count.

## Coherence levels

### Data coherence

Measures whether the supplied data are harmonious, congruent and synchronised enough to enter the optimisation engine.

### Nodal coherence

Measures the internal consistency of one optimisation node's evidence, assumptions and recommendations.

### Internodal coherence

Measures support or conflict between a pair of connected optimisation nodes.

### Pathway coherence

Measures coherence along the active multi-spoke pathway leading towards the temporary Terminal Active Node.

### Engine coherence

Integrates data, nodal and internodal coherence for the current problem and run. It is not a permanent property of PFRAMOS.

## Coherence-stimulated nodal augmentation

A node with strong coherent connections may receive a bounded activity increase. This augmentation is permitted only when internodal coherence exceeds a declared threshold.

Augmentation must not create uncontrolled positive feedback. The engine therefore:

1. caps the maximum activity gain
2. discounts duplicated evidence lineage
3. records each contributing internodal link
4. treats negative coherence as an explicit conflict penalty
5. re-tests terminality after augmentation

## Maximum-result pathway

The engine constructs an auditable connected centreline through active nodes with the strongest supported results. This is a candidate pathway, not proof of a global optimum.

The pathway is surrounded by an adaptive search envelope:

- **Band:** narrow ordered or low-dimensional pathway
- **Cylinder:** stable directed pathway with approximately consistent coherence
- **Sphere:** radial region around a dominant hub or terminal candidate
- **Reducing layers:** nested envelopes that contract as coherence rises towards the centreline

High pathway coherence contracts the envelope and increases exploitation. Lower positive coherence broadens the envelope and preserves exploration. Negative coherence blocks automatic pathway forwarding.

## Governing rule

No activity augmentation, pathway contraction or terminal selection may occur solely from a high raw result. The decision must also satisfy data coherence, internodal coherence, independence, robustness and auditability requirements.