# Dynamic Middle-Pool Memory Allocation

## Structure

The memory controller uses three pools within usable memory:

- 35% guaranteed for high-priority functions
- 15% guaranteed for medium and low-priority functions
- 50% central dynamic pool

The guaranteed half preserves the 70/30 allocation principle:

```text
High priority guarantee: 35 of 50 guaranteed units = 70%
Medium and low guarantee: 15 of 50 guaranteed units = 30%
```

## Dynamic central pool

The central 50% is not permanently assigned to any band.

It is distributed according to:

- current function priority
- task purpose
- active reference state
- criticality
- expected value
- deadline pressure
- dependency pressure
- minimum viable need
- RaR retention score
- protected-function status

## Why the central pool is needed

A fixed 70/30 split can leave capacity idle in one band while another band is under pressure.

The dynamic pool allows the architecture to respond to actual computational need without removing the guaranteed protection for important functions or starving medium and low-priority work.

## Queue rule

Queued tasks without an active reference may receive only a small dynamic reservation.

They cannot occupy a full preferred allocation simply because they may run later.

## Reclamation

All memory granted from the dynamic pool is reclaimable.

When:

- the computation completes
- the reference expires
- the function is demoted
- the task becomes blocked
- a higher-priority need emerges

DMACCE may recover some or all of the dynamic allocation and redistribute it.

Guaranteed memory is also reviewed when a function completes or loses its minimum viable need.

## Control sequence

```text
Function priority level and sublevel
        ↓
RaR reference check
        ↓
Guaranteed pool assignment
        ↓
Dynamic central-pool competition
        ↓
Purpose and minimum viable allocation
        ↓
Computation
        ↓
Completion or reprioritisation
        ↓
Memory reclamation and redistribution
```

## Relationship with PCECE

PCECE measures whether the 35/15/50 structure improves:

- validated output quality
- coherence
- robustness
- useful work per unit of memory
- energy cost
- compute cost
- idle-resource fraction
- routing friction

## Governing principle

Guaranteed pools protect continuity. The dynamic middle pool follows present computational need.
