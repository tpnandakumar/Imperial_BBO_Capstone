from PFRAMOS.core.coherence_engine import (
    CoherenceEvidence,
    build_pathway_envelope,
    maximum_result_path,
    signed_coherence,
    stimulate_activity,
)


def test_signed_coherence_bounds_and_direction() -> None:
    coherent = signed_coherence(
        [
            CoherenceEvidence("a", 0.9, 0.1, 0.9, 0.9, ("source_a",)),
            CoherenceEvidence("b", 0.8, 0.1, 0.8, 0.8, ("source_b",)),
        ]
    )
    conflicted = signed_coherence(
        [
            CoherenceEvidence("a", 0.1, 0.9, 0.9, 0.9, ("source_a",)),
            CoherenceEvidence("b", 0.1, 0.8, 0.8, 0.8, ("source_b",)),
        ]
    )

    assert 0.0 < coherent.index <= 1.0
    assert -1.0 <= conflicted.index < 0.0


def test_shared_lineage_is_discounted() -> None:
    score = signed_coherence(
        [
            CoherenceEvidence("a", 1.0, 0.0, 1.0, 1.0, ("same",)),
            CoherenceEvidence("b", 1.0, 0.0, 1.0, 1.0, ("same",)),
        ]
    )
    assert score.support_strength == 1.0


def test_high_internodal_coherence_stimulates_activity() -> None:
    augmented = stimulate_activity(0.5, [0.8, 0.9])
    unchanged = stimulate_activity(0.5, [0.2, -0.5])

    assert augmented > 0.5
    assert unchanged == 0.5
    assert augmented <= 1.0


def test_maximum_result_path_is_connected_and_non_repeating() -> None:
    scores = {"a": 0.4, "b": 0.7, "c": 0.9, "d": 0.3}
    links = {"a": ["b", "d"], "b": ["a", "c"], "c": ["b"]}

    path = maximum_result_path(scores, links, start_node="a")
    assert path == ("a", "b", "c")
    assert len(path) == len(set(path))


def test_adaptive_envelope_contracts_with_coherence() -> None:
    high = build_pathway_envelope(("a", "b", "c"), (0.9, 0.85, 0.8))
    low = build_pathway_envelope(("a", "b", "c"), (0.3, 0.2, 0.1))

    assert high.outer_radius < low.outer_radius
    assert high.geometry in {"band", "cylinder", "sphere"}
    assert high.inner_radius <= high.outer_radius
