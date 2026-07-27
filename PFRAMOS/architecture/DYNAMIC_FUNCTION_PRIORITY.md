# Dynamic Function Priority System

## Structure

PFRAMOS uses fifteen general priority levels:

```text
P1  lowest general priority
P2
P3
P4
P5
P6
P7
P8
P9
P10
P11
P12
P13
P14
P15 highest general priority
```

Each level may use sublevels from 00 to 99.

Examples:

```text
P8.10
P8.55
P8.90
P12.25
P15.99
```

A higher level always outranks a lower level. Within the same level, the higher sublevel runs first.

## Dynamic behaviour

Priority is not permanently fixed. A function may be promoted or demoted according to:

- criticality
- urgency
- dependency pressure
- expected value
- failure risk
- waiting duration
- resource pressure
- active or queued state
- blocked state
- completion state
- protected-function status

## Controlled movement

Normal reprioritisation is rate-limited so a function does not oscillate violently between levels.

The default maximum change per decision cycle is:

- two general levels
- twenty-five sublevels

Completion is an exception. A completed function falls immediately to P1.00 and its temporary memory becomes reclaimable.

## Starvation prevention

Waiting pressure rises when a valid function remains unserved. This can promote the function gradually, preventing indefinite starvation by repeatedly dominant tasks.

## Memory integration

The priority system controls how much memory a function may receive.

```text
RaR establishes whether memory must remain
        ↓
Function priority establishes service order
        ↓
Purpose and minimum need establish allocation size
        ↓
DMACCE allocates and reclaims memory
        ↓
PCECE measures system efficiency
```

## Safety rule

Priority does not override hard safety, privacy, protected-test or provenance controls.

## Governing principle

Priority reflects present computational need and can rise or fall as that need changes.
