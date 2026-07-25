"""COCO contextual vision Scout integration for PACC.

COCO is used for object recognition in context, image-caption alignment,
instance and panoptic segmentation, person keypoints and visuospatial
organisation. Images and annotations remain outside the repository in
controlled trial storage. Every run records dataset year, annotation type,
train-validation-test split, source terms and exact evaluation protocol.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class COCOSource:
    source_id: str
    name: str
    official_url: str
    access_state: str
    intended_uses: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    storage_policy: str
    notes: str


COCO = COCOSource(
    source_id="coco_common_objects_in_context",
    name="COCO: Common Objects in Context",
    official_url="https://cocodataset.org/",
    access_state="public_research_dataset_with_source_specific_terms",
    intended_uses=(
        "image_caption_alignment",
        "semantic_grounding",
        "object_recognition_in_context",
        "instance_segmentation",
        "panoptic_segmentation",
        "person_keypoint_localisation",
        "scene_understanding",
        "visuospatial_organisation",
        "cross_dataset_transfer_with_imagenet",
    ),
    required_checks=(
        "dataset_year_and_version_pin",
        "annotation_type_record",
        "official_train_validation_test_split",
        "source_terms_review",
        "image_rights_awareness",
        "no_unapproved_redistribution",
        "evaluation_protocol_lock",
        "protected_test_separation",
        "citation_and_attribution",
    ),
    storage_policy="Images and annotations remain outside GitHub in controlled trial storage or workflow artefacts.",
    notes="Prefer caption grounding and smaller validation subsets before full-scale segmentation or keypoint training.",
)


FIRST_TRIAL_SEQUENCE = (
    "caption-image semantic alignment on a small validation subset",
    "object-in-context recognition with a frozen visual backbone",
    "instance segmentation shadow evaluation",
    "panoptic scene-organisation trial",
    "person-keypoint spatial-relation trial",
    "cross-dataset comparison against ImageNet recognition",
)


PACC_PUBLICATION_TRACKS = (
    "PACC-P3",
    "PACC-P4",
    "PACC-P8",
)
