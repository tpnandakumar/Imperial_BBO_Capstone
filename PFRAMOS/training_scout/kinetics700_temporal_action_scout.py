"""Kinetics-700 temporal action Scout integration for PACC.

Kinetics-700 is used for action recognition, temporal attention, event
segmentation, human-object interaction, human-human interaction, sequence
memory and motion-aware cognition. The release is based on video identifiers
and clip time ranges, so availability and provenance must be checked at
acquisition time. Dataset editions and splits must not be mixed casually.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class KineticsSource:
    source_id: str
    name: str
    official_repository: str
    paper_reference: str
    default_state: str
    intended_uses: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    storage_policy: str
    notes: str


KINETICS_700_2020 = KineticsSource(
    source_id="kinetics_700_2020",
    name="Kinetics-700-2020 Human Action Dataset",
    official_repository="https://github.com/cvdfoundation/kinetics-dataset",
    paper_reference="https://arxiv.org/abs/2010.10864",
    default_state="usable_pending_normal_checks",
    intended_uses=(
        "human_action_recognition",
        "temporal_attention",
        "event_segmentation",
        "sequence_memory",
        "motion_aware_cognition",
        "human_object_interaction",
        "human_human_interaction",
        "temporal_transfer_learning",
        "continual_video_learning",
        "temporal_robustness_testing",
    ),
    required_checks=(
        "exact_edition_pin",
        "official_split_preservation",
        "cross_version_overlap_check",
        "video_identifier_and_timestamp_record",
        "source_availability_check",
        "removed_or_unavailable_clip_record",
        "youtube_source_terms_review",
        "no_video_redistribution_without_permission",
        "protected_test_separation",
        "citation_and_attribution",
    ),
    storage_policy="Video clips remain outside GitHub in controlled trial storage or temporary workflow artefacts.",
    notes="Prefer metadata validation, a small accessible subset and frozen temporal features before full video training.",
)


FIRST_TRIAL_SEQUENCE = (
    "validate metadata, edition and split integrity",
    "measure current clip availability on a small sample",
    "run frozen-feature action classification on a balanced subset",
    "compare single-frame and temporal models",
    "test short-term sequence memory under clip perturbation",
    "measure action-recognition robustness to missing frames",
    "evaluate temporal transfer across selected action groups",
)


PACC_PUBLICATION_TRACKS = (
    "PACC-P2",
    "PACC-P4",
    "PACC-P7",
    "PACC-P8",
)
