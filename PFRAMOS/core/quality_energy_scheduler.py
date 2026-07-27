"""Quality-first scheduling for PFRAMOS conduit computation.

Result quality is lexicographically primary. Computational cost and energy
are minimised only among candidates inside the declared quality basin and
with acceptable coherence, robustness and uncertainty.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class ExecutionOption:
    option_id: str
    validated_quality: float
    coherence: float
    robustness: float
    uncertainty: float
    compute_cost: float
    energy_cost: float
    memory_cost: float = 0.0

    def __post_init__(self) -> None:
        for name in (
            "validated_quality",
            "coherence",
            "robustness",
            "uncertainty",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        for name in ("compute_cost", "energy_cost", "memory_cost"):
            if getattr(self, name) < 0.0:
                raise ValueError(f"{name} must be non-negative")

    @property
    def resource_cost(self) -> float:
        return self.compute_cost + self.energy_cost + self.memory_cost


@dataclass(frozen=True)
class SchedulingDecision:
    selected_option_id: str
    quality_floor: float
    eligible_options: Tuple[str, ...]
    resource_saving: float
    reason: str


def select_quality_first(
    options: Sequence[ExecutionOption],
    *,
    quality_tolerance: float = 0.02,
    minimum_coherence: float = 0.40,
    minimum_robustness: float = 0.50,
    maximum_uncertainty: float = 0.50,
) -> SchedulingDecision:
    if not options:
        raise ValueError("At least one execution option is required")
    if not 0.0 <= quality_tolerance <= 1.0:
        raise ValueError("quality_tolerance must be between 0 and 1")

    best_quality = max(option.validated_quality for option in options)
    quality_floor = best_quality * (1.0 - quality_tolerance)

    eligible: List[ExecutionOption] = [
        option
        for option in options
        if option.validated_quality >= quality_floor
        and option.coherence >= minimum_coherence
        and option.robustness >= minimum_robustness
        and option.uncertainty <= maximum_uncertainty
    ]

    if not eligible:
        highest = max(options, key=lambda option: option.validated_quality)
        return SchedulingDecision(
            selected_option_id=highest.option_id,
            quality_floor=quality_floor,
            eligible_options=(highest.option_id,),
            resource_saving=0.0,
            reason="No option satisfied all safeguards, so the highest-quality option was preserved.",
        )

    selected = min(
        eligible,
        key=lambda option: (
            option.resource_cost,
            -option.coherence,
            -option.robustness,
            option.uncertainty,
            option.option_id,
        ),
    )
    most_expensive = max(option.resource_cost for option in eligible)

    return SchedulingDecision(
        selected_option_id=selected.option_id,
        quality_floor=quality_floor,
        eligible_options=tuple(sorted(option.option_id for option in eligible)),
        resource_saving=max(0.0, most_expensive - selected.resource_cost),
        reason="Selected the lowest-resource option inside the protected quality basin.",
    )


def marginal_quality_return(
    previous_quality: float,
    proposed_quality: float,
    additional_compute: float,
    additional_energy: float,
    *,
    epsilon: float = 1e-12,
) -> float:
    denominator = additional_compute + additional_energy
    return (proposed_quality - previous_quality) / (denominator + epsilon)


def should_continue_computation(
    *,
    expected_quality_gain: float,
    additional_compute: float,
    additional_energy: float,
    minimum_marginal_return: float,
) -> bool:
    return (
        marginal_quality_return(
            0.0,
            expected_quality_gain,
            additional_compute,
            additional_energy,
        )
        >= minimum_marginal_return
    )
