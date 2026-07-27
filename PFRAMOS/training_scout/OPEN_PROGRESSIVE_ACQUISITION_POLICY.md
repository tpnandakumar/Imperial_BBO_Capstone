# Open Progressive Acquisition Policy

## Governing principle

The programme remains open by default.

Data is considered usable unless its intended use is unethical, unsafe, unlawful, scientifically invalid, or explicitly restricted by the source, licence, access terms, privacy obligations or data-use conditions.

Lawfully accessible, traceable and ethically acceptable data should proceed without unnecessary delay.

Uncertainty is not treated as a permanent stop. It triggers verification, substitution, shadow use or a smaller controlled trial.

## Default presumption

The default state is `usable_pending_normal_checks`, not `blocked_pending_proof`.

A candidate may progress when:

- its source can be identified
- its intended use is not prohibited
- no material privacy or safety concern is present
- its use can be recorded and reproduced

A missing detail triggers targeted verification while other safe work continues.

## Operating states

Every candidate resource is assigned one of six states:

1. `usable_pending_normal_checks`
2. `active_acquisition`
3. `shadow_use`
4. `discovery_and_verification`
5. `substitute_required`
6. `hard_stop`

A hard stop is used only when the intended use is clearly prohibited, unsafe, unethical, unlawful or scientifically invalid.

## Smart routing

When a resource cannot proceed directly:

- unclear licence becomes targeted licence verification
- restricted access becomes metadata review or public substitute search
- unavailable compute becomes a smaller CPU trial or delayed GPU validation
- unavailable data becomes a benchmark, synthetic equivalent or repository-owned dataset
- privacy risk becomes de-identified, aggregated, synthetic or non-human data
- contamination risk becomes a fresh protected test
- incompatible format becomes an adapter or conversion layer
- failed acquisition becomes an alternative-source search

## Parallel progression

While one resource is being verified, other safe work continues:

- architecture validation
- benchmark execution
- ablation studies
- synthetic trials
- metadata screening
- publication planning
- reproducibility work
- efficiency measurement

## Evidence boundary

Open progression does not weaken evidence standards.

Discovery, shadow use, trial evidence and publication evidence remain clearly separated.

## Governing statement

Every usable resource should advance the programme. Stop only for a genuine legal, ethical, safety or scientific reason. Otherwise verify, adapt, substitute or reroute.
