# Common-Pool-First Underuse Redistribution

## Rule

When more than 50% of memory is unused, the common pool is filled first.

Any remaining unused memory is divided equally between:

- the high-priority pool
- the medium and low-priority pool

## Pull from the common pool

Either priority group may pull additional memory from the common pool when there is:

- an active computation
- a validated purpose
- a current dynamic priority
- a minimum viable memory requirement
- available common-pool capacity

## Reclamation

Memory pulled from the common pool remains reclaimable. It returns when:

- the computation completes
- the reference expires
- the purpose no longer applies
- the function is reprioritised downward
- another function has a stronger justified need

## Governing statement

When more than half of memory is unused, the common pool is filled first and the rest is divided equally between the two priority reserves.
