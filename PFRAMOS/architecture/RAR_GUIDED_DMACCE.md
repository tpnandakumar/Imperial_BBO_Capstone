# RaR-Guided DMACCE

## Definition

**RaR** means **Reference-Aware Retention**.

RaR guides DMACCE by determining whether a memory allocation is still required by any active, queued, dependent or anticipated computation.

## Governing principle

Memory must not be released merely because it is old or temporarily inactive.

It must first be proven that:

- no active computation references it
- no queued computation references it
- no dependent computation requires it
- no anticipated computation has a justified reference
- it is not protected persistent memory

## Decision priority

```text
Live reference
    ↓
Anticipated reference
    ↓
Persistent status
    ↓
Retention score
    ↓
Compression or cold demotion
    ↓
Release only when safe
```

## Retention score

The RaR retention score combines:

- live or explicit reference state
- anticipated reference state
- recent activity
- current relevance
- anticipated relevance
- recomputation risk

Reference state has the greatest weight.

## Actions

RaR-guided DMACCE may:

- retain active memory
- retain compressed memory
- compress persistent memory
- demote memory to cold storage
- release memory

## Release rule

Release is permitted only when all reference sets are empty and the retention score is low enough.

A release condition must also be present, such as:

- high memory pressure
- high energy pressure
- sufficient idle duration

## PACC integration

RaR applies to:

- working memory
- semantic activation state
- episodic traces
- visuospatial configurations
- executive plans
- retrieval caches
- temporary hypothesis states

## PIMF integration

PIMF can monitor retention pressure and memory utility through change over time. A rapidly declining reference signature may justify compression or release. A persistent or re-emerging signature may justify retention.

## PFRAMOS integration

PFRAMOS uses RaR to select the most coherent memory conduit while PCECE evaluates the total cost and energy benefit.

## Governing statement

Memory is released only when it is no longer referenced, no longer anticipated, and no longer worth retaining relative to its computational cost.
