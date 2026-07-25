# Seventy Percent Underuse Redistribution

## Trigger

When a memory pool or allocation is at least 70% unused, the unused capacity is redistributed.

## Redistribution rule

Of the unused capacity:

- 50% returns to the central dynamic pool
- 25% is assigned to the high-priority reserve
- 25% is assigned to the medium and low-priority reserve

The original pool retains none of the unused portion after redistribution.

## Example

If a 100-unit pool uses only 30 units, 70 units are unused.

The 70 unused units are redistributed as:

- 35 units to the central dynamic pool
- 17.5 units to the high-priority reserve
- 17.5 units to the medium and low-priority reserve

The 30 units still in use remain with the active computation.

## Pull from the middle pool

Both reserve groups may request additional capacity from the central pool.

A pull request must have:

- an active computation
- a validated purpose
- a current dynamic priority
- a stated minimum viable requirement
- a stated preferred requirement

The granted amount depends on current priority and available central capacity.

## Reclamation

Any capacity pulled from the central pool remains reclaimable. It returns when:

- the computation completes
- the reference expires
- the purpose no longer applies
- the function is reprioritised downward
- a more critical function requires the capacity

## Relationship with the 35/15/50 model

The baseline structure remains:

- 35% high-priority guarantee
- 15% medium and low-priority guarantee
- 50% central dynamic pool

The 70% underuse rule acts as an additional redistribution mechanism. It prevents guaranteed or temporary pools from holding excessive idle capacity.

## Governing statement

Substantial underuse causes automatic redistribution, while the central pool remains available to every active function according to priority, purpose and need.
