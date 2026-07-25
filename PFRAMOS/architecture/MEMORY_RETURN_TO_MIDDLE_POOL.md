# Memory Return to the Dynamic Middle Pool

## Governing rule

All working memory is reclaimable.

When no valid computation is using an allocation, its capacity returns to the central 50% dynamic middle pool.

## Persistence versus residency

Persistent information may survive through:

- checkpointing
- serialisation
- compressed state
- durable storage
- reproducible reconstruction

Persistence does not mean that working memory must remain resident.

## Return conditions

Memory returns to the dynamic middle pool when:

- no active reference remains
- no queued reference remains
- no dependent reference remains
- no justified anticipated reference remains
- any required checkpoint is complete

## Lifecycle

```text
Allocated working memory
        ↓
Computation and reference tracking
        ↓
Reference closure
        ↓
Checkpoint durable state if required
        ↓
Return all working memory units
        ↓
Central 50% dynamic middle pool
        ↓
Redistribution by priority, purpose and need
```

## Guaranteed pools

The 35% high-priority guarantee and 15% medium and low-priority guarantee define access protection, not permanent residency.

When a guaranteed allocation is unused, its working-memory units also return to the middle pool. The function retains its right to compete for an appropriate allocation when it becomes active again.

## RaR integration

RaR prevents premature reclamation while a valid reference exists.

Once no valid reference remains, RaR permits the allocation to return to the middle pool.

## DMACCE integration

DMACCE performs the actual reclamation and makes the returned capacity available for redistribution.

## PCECE integration

PCECE records:

- returned memory units
- idle-memory reduction
- recomputation cost
- checkpoint cost
- energy saved
- useful work per memory unit

## Governing statement

Information may persist, but unused working memory must circulate.
