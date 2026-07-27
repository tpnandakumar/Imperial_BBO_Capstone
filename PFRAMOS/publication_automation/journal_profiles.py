"""Journal-specific manuscript formatting profiles.

Profiles record current verified requirements and must be rechecked against the
official journal website before final submission. Automation may validate and
render formats, but it must not submit a manuscript or accept legal terms.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Tuple


@dataclass(frozen=True)
class JournalProfile:
    journal_id: str
    journal_name: str
    verified_on: date
    manuscript_format: str
    official_template_required: bool
    review_model: str
    anonymised_submission: bool
    main_file_type: str
    appendix_policy: str
    supplementary_policy: str
    reference_style: str
    figure_policy: Tuple[str, ...]
    table_policy: Tuple[str, ...]
    required_sections: Tuple[str, ...]
    required_disclosures: Tuple[str, ...]
    submission_platform: str
    licence: str
    special_checks: Tuple[str, ...]


JOURNAL_PROFILES = {
    "tmlr": JournalProfile(
        journal_id="tmlr",
        journal_name="Transactions on Machine Learning Research",
        verified_on=date(2026, 7, 25),
        manuscript_format="Official TMLR LaTeX style file and template without layout alteration",
        official_template_required=True,
        review_model="double blind open review",
        anonymised_submission=True,
        main_file_type="PDF generated from LaTeX",
        appendix_policy="Appendix may follow references in the main PDF; reviewer consultation is optional",
        supplementary_policy="Up to 100 MB in anonymised PDF or ZIP; code, data and videos may be included",
        reference_style="TMLR template bibliography format with verified citations",
        figure_policy=(
            "figures must remain legible at manuscript scale",
            "captions must explain the evidence shown",
            "all plotted values must resolve to traceable data",
            "author-identifying repository links must be anonymised during review",
        ),
        table_policy=(
            "tables must be numbered and cited in the text",
            "measured and derived values must be distinguishable",
            "best-result emphasis must not conceal uncertainty or negative results",
        ),
        required_sections=(
            "abstract",
            "introduction",
            "related work",
            "methodology",
            "results",
            "discussion",
            "limitations",
            "conclusion",
            "references",
            "broader impact statement when material risks exist",
        ),
        required_disclosures=(
            "funding",
            "competing interests",
            "conflicts of interest",
            "human-subject reporting where applicable",
            "ethical and societal risks",
            "author responsibility for any LLM-assisted content",
        ),
        submission_platform="OpenReview",
        licence="CC BY 4.0 from submission onward",
        special_checks=(
            "all authors have complete active OpenReview profiles",
            "submission and supplement are anonymised",
            "no prohibited dual submission or reused archival text, figures or results",
            "template fonts, spacing and layout are unchanged",
            "main body length above 12 pages may lengthen review",
        ),
    ),
}


def get_journal_profile(journal_id: str) -> JournalProfile:
    try:
        return JOURNAL_PROFILES[journal_id]
    except KeyError as exc:
        raise ValueError(f"unknown journal profile: {journal_id}") from exc
