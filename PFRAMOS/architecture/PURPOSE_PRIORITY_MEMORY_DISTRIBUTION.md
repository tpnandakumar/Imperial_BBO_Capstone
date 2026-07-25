# Purpose and Priority-Aware Memory Distribution

## Purpose

DMACCE must prevent memory hogging. A queued task must not retain large amounts of memory merely because it may run later.

Memory distribution is therefore governed by:

- active computational need
- task purpose
- criticality
- expected value
- deadline pressure
- minimum viable memory
- recomputation cost
- protected-function status
- reference state

## Allocation hierarchy

```text
Protected active functions
        ↓
High-criticality active functions
        ↓
Deadline-sensitive active functions
        ↓
Other active functions
        ↓
Queued functions receive limited reservations
        ↓
Unused capacity remains available as reserve
```

## Minimum viable allocation

Each task declares:

- minimum memory required to operate
- preferred memory for efficient operation
- maximum memory it is permitted to consume

The allocator first protects minimum viable operation for important functions. Additional memory is granted according to priority and available capacity.

## Queue rule

Queued work does not receive its full preferred allocation.

Unless it has an active reference, it receives only a small reservation. Its main allocation is made when it becomes active.

This prevents a low-priority queued task from depriving an important live function.

## Purpose awareness

Every memory request must state its computational purpose. Requests without a defined purpose are invalid.

Examples include:

- semantic graph construction
- protected-test inference
- visuospatial transformation
- BBO candidate analysis
- publication rendering
- Scout dataset validation

## Priority score

Priority combines:

- criticality
- expected value
- deadline pressure
- recomputation cost
- active-reference status
- protected-function status

Queued-only requests receive a penalty until activated.

## Memory reclamation

When a task completes:

1. its live references are closed
2. temporary memory is reclaimed
3. reusable validated state may be compressed or archived
4. reclaimed capacity returns immediately to the shared pool
5. waiting tasks are reconsidered in priority order

## Relationship with RaR

RaR prevents unsafe release while a valid reference exists.

Purpose and Priority-Aware Distribution prevents excessive retention by limiting how much memory each reference may command.

Together:

```text
RaR decides whether memory must remain
        ↓
Priority and purpose decide how much memory it receives
        ↓
DMACCE allocates, compresses, demotes or reclaims it
        ↓
PCECE measures cost and energy efficiency
```

## Governing rule

A reference justifies retention, but it does not justify unlimited allocation.
