"""AudioSet auditory scene Scout integration for PACC.

AudioSet provides a hierarchical ontology and human-labelled ten-second clips
covering speech, human sounds, music, animals, vehicles, tools and everyday
environmental events. It is used for auditory scene understanding, temporal
attention, hierarchical sound semantics, multimodal grounding and robustness
to noisy acoustic environments.

The Scout records the exact ontology and metadata version used because the
official site currently exposes different class counts in different summary
sections. Source clips are linked to YouTube and must be checked for current
availability and applicable terms at acquisition time.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class AudioSetSource:
    source_id: str
    name: str
    official_url: str
    default_state: str
    intended_uses: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    storage_policy: str
    notes: str


AUDIOSET = AudioSetSource(
    source_id="google_audioset",
    name="Google AudioSet",
    official_url="https://research.google.com/audioset/",
    default_state="usable_pending_normal_checks",
    intended_uses=(
        "auditory_scene_understanding",
        "audio_event_detection",
        "hierarchical_sound_semantics",
        "temporal_attention",
        "multilabel_audio_classification",
        "multimodal_audio_visual_grounding",
        "noise_robustness",
        "cross_dataset_transfer_with_librispeech_and_common_voice",
    ),
    required_checks=(
        "ontology_version_pin",
        "metadata_version_pin",
        "official_split_preservation",
        "source_clip_availability_check",
        "youtube_terms_review",
        "removed_clip_record",
        "no_audio_redistribution_without_permission",
        "protected_test_separation",
        "citation_and_attribution",
    ),
    storage_policy="Source audio remains outside GitHub in controlled trial storage or temporary workflow artefacts.",
    notes="Begin with ontology and metadata validation, then a small balanced subset and frozen audio features before full training.",
)


FIRST_TRIAL_SEQUENCE = (
    "validate ontology and metadata version",
    "measure source-clip availability on a stratified sample",
    "run multilabel classification on a small balanced subset",
    "test hierarchical sound-category retrieval",
    "test robustness to noise and partial masking",
    "compare speech and non-speech auditory representations",
    "evaluate audio-visual grounding with COCO or YouTube-BB aligned trials",
)


PACC_PUBLICATION_TRACKS = (
    "PACC-P2",
    "PACC-P3",
    "PACC-P7",
    "PACC-P8",
)
