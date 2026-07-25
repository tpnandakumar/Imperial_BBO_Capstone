"""YouTube-BoundingBoxes temporal tracking Scout integration for PACC.

YouTube-BB provides densely sampled object annotations across short video
segments. It is used for object permanence, temporal tracking, attention
continuity, motion-aware retrieval and robustness to missing or corrupted
frames. Dataset annotations and metadata are licensed under CC BY 4.0, while
source-video availability and YouTube terms must still be checked at
acquisition time.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class YouTubeBBSource:
    source_id: str
    name: str
    official_url: str
    licence: str
    default_state: str
    intended_uses: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    storage_policy: str
    notes: str


YOUTUBE_BB = YouTubeBBSource(
    source_id="youtube_bounding_boxes",
    name="YouTube-BoundingBoxes Dataset",
    official_url="https://research.google.com/youtube-bb/",
    licence="CC BY 4.0 for dataset annotations and metadata",
    default_state="usable_pending_normal_checks",
    intended_uses=(
        "object_tracking",
        "object_permanence",
        "temporal_attention",
        "attention_continuity",
        "motion_aware_retrieval",
        "frame_loss_robustness",
        "temporal_localisation",
        "cross_dataset_transfer_with_coco_and_kinetics",
    ),
    required_checks=(
        "annotation_version_pin",
        "official_split_preservation",
        "video_identifier_and_timestamp_record",
        "source_video_availability_check",
        "youtube_terms_review",
        "removed_clip_record",
        "no_video_redistribution_without_permission",
        "protected_test_separation",
        "citation_and_attribution",
    ),
    storage_policy="Source videos remain outside GitHub in controlled trial storage or temporary workflow artefacts.",
    notes="Prefer metadata validation and small balanced tracking subsets before full-scale acquisition.",
)


FIRST_TRIAL_SEQUENCE = (
    "validate annotation files and class distribution",
    "measure current source-video availability on a stratified sample",
    "run single-object tracking on a small balanced subset",
    "test object permanence across temporary occlusion",
    "test frame-loss and temporal-gap robustness",
    "compare tracking continuity against COCO still-image recognition",
    "compare low-level tracking against Kinetics action recognition",
)


PACC_PUBLICATION_TRACKS = (
    "PACC-P2",
    "PACC-P4",
    "PACC-P7",
    "PACC-P8",
)
