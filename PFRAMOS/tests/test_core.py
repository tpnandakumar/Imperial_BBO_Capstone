from PFRAMOS.core.node_contract import EvidenceSignal
from PFRAMOS.core.strength_integrator import integrate_signals
from PFRAMOS.core.terminality_engine import NodeActivity, select_terminal_node


def test_shared_lineage_is_discounted() -> None:
    signals = [
        EvidenceSignal(
            name="increase_x2",
            value=True,
            strength=0.8,
            confidence=0.8,
            stability=0.8,
            identifiability=0.8,
            independence=0.5,
            lineage=("weeks_07_11",),
        ),
        EvidenceSignal(
            name="increase_x2",
            value=True,
            strength=0.8,
            confidence=0.8,
            stability=0.8,
            identifiability=0.8,
            independence=0.5,
            lineage=("weeks_07_11",),
        ),
    ]

    result = integrate_signals(signals)[0]
    assert result.dependency_adjusted_support < result.raw_support
    assert 0.0 <= result.final_strength <= 1.0


def test_terminal_selection_requires_support() -> None:
    activities = [
        NodeActivity("boundary", 0.9, 0.9, 0.9, 0.9, 0.1, 0.1, 0.1),
        NodeActivity("trajectory", 0.7, 0.7, 0.7, 0.8, 0.2, 0.2, 0.2),
        NodeActivity("uncertainty", 0.6, 0.6, 0.7, 0.7, 0.2, 0.2, 0.2),
    ]

    decision = select_terminal_node(activities)
    assert decision.terminal_node_id == "boundary"
    assert decision.unresolved is False
    assert len(decision.supporting_nodes) >= 2


def test_near_tie_remains_unresolved() -> None:
    activities = [
        NodeActivity("a", 0.8, 0.8, 0.8, 0.8, 0.1, 0.1, 0.1),
        NodeActivity("b", 0.79, 0.8, 0.8, 0.8, 0.1, 0.1, 0.1),
        NodeActivity("c", 0.7, 0.7, 0.7, 0.7, 0.2, 0.2, 0.2),
    ]

    decision = select_terminal_node(activities)
    assert decision.unresolved is True
