"""Experimental BG-cerebellar-descending-tract regulator for PGC.

This module is opt-in. It does not replace the established PGC execution path.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Tuple

Vector = Tuple[float, float]


@dataclass(frozen=True)
class RegulationState:
    direct_gain: float
    indirect_gain: float
    hyperdirect_brake: bool
    cerebellar_damping: float
    orientation_alignment: float
    output: Vector


class BGCerebellarDescendingRegulator:
    """Select, smooth and stabilise a two-dimensional update command."""

    def regulate(
        self,
        current: Vector,
        target: Vector,
        proposed: Vector,
        previous: Vector = (0.0, 0.0),
        error_trend: float = 0.0,
    ) -> RegulationState:
        dx, dy = target[0] - current[0], target[1] - current[1]
        error = math.hypot(dx, dy)

        # Basal ganglia analogue: facilitate, suppress and brake.
        direct = 1.0 + 0.22 * math.tanh(max(0.0, error - 0.45))
        indirect = 1.0 / (
            1.0 + 1.6 * max(0.0, error_trend) + 2.2 * max(0.0, 0.25 - error)
        )
        ux, uy = proposed[0] * direct * indirect, proposed[1] * direct * indirect
        brake = math.hypot(ux, uy) > 0.5 or error_trend > 0.28
        if brake:
            ux, uy = 0.18 * ux, 0.18 * uy

        # Cerebellar analogue: predictive damping.
        ux, uy = ux - 0.52 * previous[0], uy - 0.52 * previous[1]

        # Vestibulospinal analogue: preserve orientation.
        un, dn = math.hypot(ux, uy), math.hypot(dx, dy)
        alignment = 1.0
        if un > 1e-12 and dn > 1e-12:
            alignment = max(-1.0, min(1.0, (ux * dx + uy * dy) / (un * dn)))
            if alignment < 0.65:
                ux, uy = (
                    0.72 * ux + 0.28 * un * dx / dn,
                    0.72 * uy + 0.28 * un * dy / dn,
                )

        # Tectospinal analogue: reorient towards the target.
        ux, uy = ux + 0.08 * dx, uy + 0.08 * dy

        # Reticulospinal analogue: maintain a global gain envelope.
        limit = 0.22 + 0.06 * math.tanh(error)
        un = math.hypot(ux, uy)
        if un > limit:
            ux, uy = ux * limit / un, uy * limit / un

        # Rubrospinal analogue: fine local correction.
        if error < 0.35:
            ux, uy = ux + 0.045 * dx, uy + 0.045 * dy

        return RegulationState(
            direct_gain=direct,
            indirect_gain=indirect,
            hyperdirect_brake=brake,
            cerebellar_damping=0.52,
            orientation_alignment=alignment,
            output=(ux, uy),
        )
