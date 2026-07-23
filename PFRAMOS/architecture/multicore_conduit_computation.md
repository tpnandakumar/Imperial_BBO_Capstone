# Multi-Core Coherence Conduit Computation

## Purpose

PFRAMOS treats independent coherence conduits as parallel optimisation cores. Each conduit may analyse a different function, model family, candidate region, uncertainty structure or robustness question.

The architecture mirrors selected principles of multi-core CPUs and shared memory systems while preserving full optimisation auditability.

## Computational analogy

| Computing concept | PFRAMOS equivalent |
|---|---|
| CPU core | Active coherence conduit |
| Shared RAM | Canonical data and shared computation cache |
| Private cache | Conduit-local intermediate state |
| Bus or interconnect | Bidirectional conduit links |
| Synchronisation barrier | Coherence junction |
| Scheduler | Conduit executor |
| Cache reuse | Shared deterministic calculation reuse |
| Process isolation | Separate conduit payload and result records |

## Execution model

1. Dependency-free conduits execute concurrently.
2. Shared deterministic calculations are cached and reused.
3. Dependent conduits wait until their required source conduits complete.
4. Compatible results meet at a Coherence Junction.
5. Junctions merge only when cross-conduit coherence exceeds the declared threshold and no unresolved conflict remains.
6. Original conduit identities remain attached to merged outputs.

## Supported modes

- Sequential execution for debugging and exact trace reconstruction
- Threaded execution for lightweight or I/O-heavy conduit tasks
- Multiprocessing for CPU-intensive analysis
- Batched or GPU execution for large candidate populations
- Distributed execution for future multi-machine deployments

Version 0.1 implements the threaded foundation and a thread-safe shared cache. Later execution backends must preserve the same task and audit contracts.

## Efficiency controls

The engine records:

- conduit start and completion
- dependency relationships
- reused cache keys
- duplicate calculations avoided
- coherence at each merge junction
- merge rejections and reasons
- source conduits retained after merging

Parallel execution is not accepted merely because it is faster. Results must remain deterministic within declared tolerance and must match the sequential reference mode.

## Governing rule

Conduits compute independently where independence is useful, share computation where evidence and transformations overlap, and synchronise only through coherence-controlled junctions.