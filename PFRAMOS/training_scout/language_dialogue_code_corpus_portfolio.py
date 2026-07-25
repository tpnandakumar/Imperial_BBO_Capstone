"""Governed language, dialogue and code corpus portfolio for PACC and PFRAMOS.

This portfolio consolidates large text corpora, dialogue datasets, code corpora
and small semantic trial sets. It assigns each source an operational role,
priority, acquisition mode and governance status. The portfolio avoids treating
all public datasets as equally suitable or equally licensed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CorpusSource:
    source_id: str
    name: str
    official_url: str
    corpus_type: str
    priority: int
    default_state: str
    acquisition_mode: str
    intended_uses: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    notes: str


CORPORA = (
    CorpusSource(
        source_id="oasst1",
        name="OpenAssistant Conversations Dataset OASST1",
        official_url="https://huggingface.co/datasets/OpenAssistant/oasst1",
        corpus_type="multilingual_human_annotated_dialogue",
        priority=1,
        default_state="usable_pending_normal_checks",
        acquisition_mode="small_full_dataset_or_streamed_sample",
        intended_uses=(
            "dialogue_structure_learning",
            "preference_and_quality_signal_learning",
            "conversation_tree_reasoning",
            "multilingual_assistant_behaviour",
            "response_ranking",
            "safety_and_toxicity_analysis",
        ),
        required_checks=(
            "apache_2_licence_record",
            "dataset_version_pin",
            "deleted_and_spam_message_filter",
            "language_distribution_record",
            "toxicity_and_safety_review",
            "protected_test_split",
            "citation_and_attribution",
        ),
        notes="Best first dialogue corpus because it is manageable, multilingual, human-generated and Apache 2.0 licensed.",
    ),
    CorpusSource(
        source_id="english_quotes",
        name="English Quotes Dataset",
        official_url="https://huggingface.co/datasets/Abirate/english_quotes",
        corpus_type="small_quote_attribution_and_tagging_dataset",
        priority=2,
        default_state="shadow_use",
        acquisition_mode="full_small_dataset",
        intended_uses=(
            "semantic_tagging",
            "author_attribution",
            "misattribution_detection",
            "small_multilabel_classification",
            "retrieval_and_citation_trial",
        ),
        required_checks=(
            "dataset_card_licence_record",
            "source_and_quote_rights_review",
            "misattribution_audit",
            "no_memorisation_claim",
            "no_verbatim_generation_objective",
            "protected_test_split",
        ),
        notes="Use for classification, attribution and semantic retrieval only. Do not treat the dataset licence as overriding rights in individual quotations.",
    ),
    CorpusSource(
        source_id="lmsys_chat_1m",
        name="LMSYS-Chat-1M",
        official_url="https://huggingface.co/datasets/lmsys/lmsys-chat-1m",
        corpus_type="gated_real_world_llm_conversations",
        priority=3,
        default_state="discovery_and_verification",
        acquisition_mode="gated_metadata_then_small_approved_sample",
        intended_uses=(
            "real_world_prompt_distribution",
            "model_routing",
            "request_dispatch",
            "safety_and_content_moderation",
            "evaluation_method_research",
            "conversation_pattern_analysis",
        ),
        required_checks=(
            "accept_dataset_licence_agreement",
            "contact_information_gate",
            "deletion_request_compliance",
            "termination_and_destruction_process",
            "privacy_and_sensitive_content_review",
            "dataset_version_pin",
            "protected_test_split",
        ),
        notes="Valuable for routing and real-world behaviour research, but gated and subject to deletion and termination obligations.",
    ),
    CorpusSource(
        source_id="the_stack",
        name="The Stack",
        official_url="https://huggingface.co/datasets/bigcode/the-stack",
        corpus_type="gated_multilingual_source_code_corpus",
        priority=4,
        default_state="discovery_and_verification",
        acquisition_mode="narrow_language_and_licence_filtered_subset",
        intended_uses=(
            "code_understanding",
            "code_generation_shadow_trial",
            "repository_structure_learning",
            "licence_aware_code_retrieval",
            "programming_language_transfer",
        ),
        required_checks=(
            "accept_stack_terms",
            "per_file_licence_preservation",
            "attribution_tracking",
            "latest_usable_version_check",
            "validated_removal_update_process",
            "malicious_code_filter",
            "provenance_preservation",
            "protected_test_split",
        ),
        notes="Use only narrow, provenance-preserving subsets. The corpus contains multiple licences and must track removals and latest usable versions.",
    ),
    CorpusSource(
        source_id="redpajama_v2",
        name="RedPajama-Data-V2",
        official_url="https://github.com/togethercomputer/RedPajama-Data",
        corpus_type="large_common_crawl_pretraining_corpus_and_quality_signals",
        priority=5,
        default_state="discovery_and_verification",
        acquisition_mode="code_and_metadata_first_then_tiny_quality_signal_sample",
        intended_uses=(
            "corpus_quality_signal_research",
            "deduplication_research",
            "web_text_filtering",
            "multilingual_corpus_analysis",
            "data_pipeline_reproducibility",
        ),
        required_checks=(
            "repository_code_licence_record",
            "common_crawl_terms_review",
            "snapshot_version_pin",
            "quality_signal_definition_record",
            "deduplication_status",
            "privacy_and_personal_data_filter",
            "contamination_review",
        ),
        notes="Use first for data-engineering and quality research, not immediate full-corpus training. Repository code is Apache 2.0, while corpus use follows source terms.",
    ),
    CorpusSource(
        source_id="the_pile",
        name="The Pile",
        official_url="https://pile.eleuther.ai/",
        corpus_type="historical_multi_component_language_model_corpus",
        priority=6,
        default_state="discovery_only",
        acquisition_mode="processing_code_and_component_specific_review",
        intended_uses=(
            "historical_corpus_design_review",
            "component_weighting_analysis",
            "data_pipeline_comparison",
            "clean_component_selection",
            "contamination_and_licence_case_study",
        ),
        required_checks=(
            "component_specific_licence",
            "component_specific_provenance",
            "exclude_unusable_or_disputed_components",
            "processing_code_version_pin",
            "privacy_and_copyright_review",
            "contamination_review",
        ),
        notes="Treat as a historical design reference and component catalogue. Do not assume a single blanket licence covers every component.",
    ),
)


FIRST_TRIAL_SEQUENCE = (
    "Acquire and validate OASST1 train and validation splits",
    "Run conversation-tree reconstruction and response-ranking trial",
    "Use English Quotes for attribution and semantic-tagging shadow tests",
    "Prepare LMSYS-Chat-1M access and deletion-compliance process",
    "Select a narrow licence-filtered Python subset from The Stack",
    "Use RedPajama metadata and quality signals for corpus-filtering research",
    "Review The Pile components only where provenance and rights are clear",
)


def by_priority() -> Tuple[CorpusSource, ...]:
    return tuple(sorted(CORPORA, key=lambda source: source.priority))


def source_by_id(source_id: str) -> CorpusSource:
    for source in CORPORA:
        if source.source_id == source_id:
            return source
    raise ValueError(f"unknown corpus source: {source_id}")
