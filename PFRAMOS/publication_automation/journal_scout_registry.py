"""Journal Scout registry for PACC and PFRAMOS publication planning.

Journal requirements and costs can change. Every profile must be rechecked
against the official journal website before submission. The registry supports
fit assessment and formatting preparation only. It does not submit papers.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Tuple


@dataclass(frozen=True)
class JournalScoutProfile:
    journal_id: str
    journal_name: str
    publisher: str
    official_url: str
    verified_on: date
    primary_scope: Tuple[str, ...]
    suitable_tracks: Tuple[str, ...]
    review_model: str
    open_access_model: str
    reproducibility_priority: str
    format_requirement: str
    submission_risk: Tuple[str, ...]
    notes: str


JOURNALS = (
    JournalScoutProfile(
        journal_id="tmlr",
        journal_name="Transactions on Machine Learning Research",
        publisher="JMLR",
        official_url="https://jmlr.org/tmlr/author-guide.html",
        verified_on=date(2026, 7, 25),
        primary_scope=("machine_learning", "learning_systems", "reproducible_methods"),
        suitable_tracks=("PFRAMOS-P1", "PFRAMOS-P2", "PACC-P7", "PACC-P8"),
        review_model="double_blind_openreview",
        open_access_model="CC_BY_4_0",
        reproducibility_priority="high",
        format_requirement="official TMLR LaTeX template and anonymised PDF",
        submission_risk=("anonymity", "dual_submission", "template_integrity", "self_plagiarism"),
        notes="Best current primary target for the core PFRAMOS architecture and integrated PACC validation.",
    ),
    JournalScoutProfile(
        journal_id="jmlr",
        journal_name="Journal of Machine Learning Research",
        publisher="JMLR",
        official_url="https://www.jmlr.org/author-info.html",
        verified_on=date(2026, 7, 25),
        primary_scope=("machine_learning", "principled_algorithms", "learning_theory", "empirical_validation"),
        suitable_tracks=("PFRAMOS-P1", "PFRAMOS-P2", "PACC-P1", "PACC-P8"),
        review_model="editorial_peer_review",
        open_access_model="open_access",
        reproducibility_priority="high",
        format_requirement="official JMLR LaTeX style for final publication",
        submission_risk=("high_novelty_threshold", "long_review_cycle", "theoretical_depth"),
        notes="Strong target for mature, comprehensive and deeply validated work.",
    ),
    JournalScoutProfile(
        journal_id="jmlr_mloss",
        journal_name="JMLR Machine Learning Open Source Software",
        publisher="JMLR",
        official_url="https://www.jmlr.org/mloss/",
        verified_on=date(2026, 7, 25),
        primary_scope=("open_source_software", "machine_learning_tools", "reproducible_implementations"),
        suitable_tracks=("PFRAMOS-P2", "PFRAMOS-P3", "PACC-P7"),
        review_model="software_and_paper_review",
        open_access_model="open_access",
        reproducibility_priority="very_high",
        format_requirement="JMLR software-paper format with accessible code",
        submission_risk=("software_maturity", "documentation", "maintenance", "licence_clarity"),
        notes="Suitable once PFRAMOS or PACC becomes a stable, documented and reusable software package.",
    ),
    JournalScoutProfile(
        journal_id="cognitive_science",
        journal_name="Cognitive Science",
        publisher="Wiley and the Cognitive Science Society",
        official_url="https://onlinelibrary.wiley.com/journal/15516709",
        verified_on=date(2026, 7, 25),
        primary_scope=("cognition", "knowledge_representation", "memory", "learning", "reasoning", "perception", "language"),
        suitable_tracks=("PACC-P1", "PACC-P2", "PACC-P3", "PACC-P4", "PACC-P5", "PACC-P6"),
        review_model="peer_review",
        open_access_model="hybrid_or_standard_publishing",
        reproducibility_priority="medium_to_high",
        format_requirement="journal-specific manuscript format",
        submission_risk=("multidisciplinary_clarity", "cognitive_theory_depth", "human_relevance"),
        notes="Primary interdisciplinary target for the PACC cognitive architecture and domain models.",
    ),
    JournalScoutProfile(
        journal_id="neural_computation",
        journal_name="Neural Computation",
        publisher="MIT Press",
        official_url="https://direct.mit.edu/neco",
        verified_on=date(2026, 7, 25),
        primary_scope=("neural_computation", "mathematical_modelling", "cognition", "perception", "behaviour", "artificial_neural_systems"),
        suitable_tracks=("PACC-P1", "PACC-P2", "PACC-P3", "PACC-P4", "PACC-P5"),
        review_model="peer_review",
        open_access_model="hybrid",
        reproducibility_priority="high",
        format_requirement="MIT Press journal format",
        submission_risk=("mathematical_depth", "neural_or_computational_grounding", "strong_validation"),
        notes="Strong target for mathematical models of semantic, memory, visuospatial and executive cognition.",
    ),
    JournalScoutProfile(
        journal_id="nature_machine_intelligence",
        journal_name="Nature Machine Intelligence",
        publisher="Nature Portfolio",
        official_url="https://www.nature.com/natmachintell/submission-guidelines/about/aims",
        verified_on=date(2026, 7, 25),
        primary_scope=("artificial_intelligence", "machine_learning", "robotics", "cognitive_science", "neuro_inspired_computing"),
        suitable_tracks=("PFRAMOS-P1", "PACC-P1", "PACC-P7", "PACC-P8"),
        review_model="editorial_screening_and_peer_review",
        open_access_model="subscription_or_open_access_options",
        reproducibility_priority="high",
        format_requirement="Nature Portfolio submission requirements",
        submission_risk=("very_high_selectivity", "broad_significance", "strong_independent_validation", "publication_cost_if_open_access"),
        notes="A later-stage target if PACC or PFRAMOS demonstrates broad scientific importance and independent validation.",
    ),
    JournalScoutProfile(
        journal_id="ieee_tpami",
        journal_name="IEEE Transactions on Pattern Analysis and Machine Intelligence",
        publisher="IEEE Computer Society",
        official_url="https://technav.ieee.org/topic/ieee-transactions-on-pattern-analysis-and-machine-intelligence/",
        verified_on=date(2026, 7, 25),
        primary_scope=("pattern_analysis", "machine_intelligence", "computer_vision", "machine_learning"),
        suitable_tracks=("PACC-P4", "PACC-P8", "PFRAMOS-P1"),
        review_model="peer_review",
        open_access_model="hybrid",
        reproducibility_priority="high",
        format_requirement="IEEE journal format",
        submission_risk=("archival_significance", "strong_benchmarks", "substantial_novelty"),
        notes="Relevant mainly for visuospatial cognition, pattern analysis and integrated machine-intelligence validation.",
    ),
)


def journal_by_id(journal_id: str) -> JournalScoutProfile:
    for journal in JOURNALS:
        if journal.journal_id == journal_id:
            return journal
    raise ValueError(f"unknown journal: {journal_id}")


def journals_for_track(track_id: str) -> Tuple[JournalScoutProfile, ...]:
    return tuple(journal for journal in JOURNALS if track_id in journal.suitable_tracks)
