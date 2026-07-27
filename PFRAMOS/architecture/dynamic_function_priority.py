"""Dynamic 15-level function priority system for PFRAMOS.

Functions operate within fifteen general priority levels. Optional sublevels
allow finer ordering without changing the main level. Priority can be promoted
or demoted according to criticality, urgency, dependency pressure, expected
value, risk, resource pressure, waiting time, completion and failure state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


MIN_PRIORITY_LEVEL = 1
MAX_PRIORITY_LEVEL = 15
MIN_SUBLEVEL = 0
MAX_SUBLEVEL = 99


@dataclass(frozen=True, order=True)
class FunctionPriority:
    level: int
    sublevel: int = 0

    def __post_init__(self) -> None:
        if not MIN_PRIORITY_LEVEL <= self.level <= MAX_PRIORITY_LEVEL:
            raise ValueError("priority level must be between 1 and 15")
        if not MIN_SUBLEVEL <= self.sublevel <= MAX_SUBLEVEL:
            raise ValueError("priority sublevel must be between 0 and 99")

    @property
    def rank(self) -> int:
        return self.level * 100 + self.sublevel

    def promote(self, levels: int = 1, sublevels: int = 0) -> "FunctionPriority":
        if levels < 0 or sublevels < 0:
            raise ValueError("promotion values cannot be negative")
        new_level = min(MAX_PRIORITY_LEVEL, self.level + levels)
        new_sublevel = min(MAX_SUBLEVEL, self.sublevel + sublevels)
        if new_level == MAX_PRIORITY_LEVEL and self.level + levels > MAX_PRIORITY_LEVEL:
            new_sublevel = MAX_SUBLEVEL
        return FunctionPriority(new_level, new_sublevel)

    def demote(self, levels: int = 1, sublevels: int = 0) -> "FunctionPriority":
        if levels < 0 or sublevels < 0:
            raise ValueError("demotion values cannot be negative")
        new_level = max(MIN_PRIORITY_LEVEL, self.level - levels)
        new_sublevel = max(MIN_SUBLEVEL, self.sublevel - sublevels)
        if new_level == MIN_PRIORITY_LEVEL and self.level - levels < MIN_PRIORITY_LEVEL:
            new_sublevel = MIN_SUBLEVEL
        return FunctionPriority(new_level, new_sublevel)


@dataclass(frozen=True)
class PriorityContext:
    function_id: str
    criticality: float
    urgency: float
    dependency_pressure: float
    expected_value: float
    failure_risk: float
    waiting_pressure: float
    resource_pressure: float
    active: bool
    queued: bool
    completed: bool
    blocked: bool
    protected: bool = False

    def __post_init__(self) -> None:
        for name in (
            "criticality",
            "urgency",
            "dependency_pressure",
            "expected_value",
            "failure_risk",
            "waiting_pressure",
            "resource_pressure",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class PriorityChange:
    function_id: str
    previous: FunctionPriority
    current: FunctionPriority
    direction: str
    reasons: Tuple[str, ...]


def calculate_target_priority(context: PriorityContext) -> FunctionPriority:
    if context.completed:
        return FunctionPriority(1, 0)

    score = (
        0.24 * context.criticality
        + 0.20 * context.urgency
        + 0.16 * context.dependency_pressure
        + 0.14 * context.expected_value
        + 0.10 * context.failure_risk
        + 0.08 * context.waiting_pressure
        + 0.08 * (1.0 - context.resource_pressure)
    )

    if context.active:
        score += 0.08
    if context.protected:
        score += 0.12
    if context.queued and not context.active:
        score -= 0.08
    if context.blocked:
        score -= 0.12

    score = max(0.0, min(1.0, score))
    level = max(MIN_PRIORITY_LEVEL, min(MAX_PRIORITY_LEVEL, 1 + int(score * 14)))
    fractional = score * 14 - int(score * 14)
    sublevel = int(round(fractional * MAX_SUBLEVEL))
    return FunctionPriority(level, sublevel)


def reprioritise(
    current: FunctionPriority,
    context: PriorityContext,
    max_level_step: int = 2,
    max_sublevel_step: int = 25,
) -> PriorityChange:
    if max_level_step < 1 or max_sublevel_step < 1:
        raise ValueError("reprioritisation steps must be positive")

    target = calculate_target_priority(context)
    level_delta = target.level - current.level
    sublevel_delta = target.sublevel - current.sublevel

    bounded_level = current.level + max(-max_level_step, min(max_level_step, level_delta))
    bounded_sublevel = current.sublevel + max(
        -max_sublevel_step,
        min(max_sublevel_step, sublevel_delta),
    )
    bounded_sublevel = max(MIN_SUBLEVEL, min(MAX_SUBLEVEL, bounded_sublevel))

    if context.completed:
        updated = FunctionPriority(1, 0)
    else:
        updated = FunctionPriority(bounded_level, bounded_sublevel)

    reasons = []
    if context.protected:
        reasons.append("protected_function")
    if context.active:
        reasons.append("active")
    if context.urgency >= 0.70:
        reasons.append("high_urgency")
    if context.dependency_pressure >= 0.70:
        reasons.append("high_dependency_pressure")
    if context.waiting_pressure >= 0.70:
        reasons.append("starvation_prevention")
    if context.resource_pressure >= 0.75:
        reasons.append("resource_pressure")
    if context.blocked:
        reasons.append("blocked")
    if context.completed:
        reasons.append("completed")

    if updated.rank > current.rank:
        direction = "promoted"
    elif updated.rank < current.rank:
        direction = "demoted"
    else:
        direction = "unchanged"

    return PriorityChange(
        function_id=context.function_id,
        previous=current,
        current=updated,
        direction=direction,
        reasons=tuple(reasons),
    )
