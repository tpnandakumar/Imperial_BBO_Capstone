"""Publication text cleaner and style audit for PFRAMOS manuscripts.

The cleaner removes prohibited dash characters and explicit machine-generated
markers. It also reports suspicious style patterns for human review. It does
not claim to prove whether text was written by a human or an AI system.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Tuple


PROHIBITED_CHARACTERS = {
    "\u2014": ", ",
    "\u2013": " to ",
    "\u2212": "-",
}

EXPLICIT_AI_MARKERS = (
    r"\bas an ai language model\b",
    r"\bi cannot browse the internet\b",
    r"\bmy training data\b",
    r"\bi do not have personal opinions\b",
    r"\bhere is a polished version\b",
    r"\bcertainly[!,]?\s+here(?:'s| is)\b",
)

STYLE_REVIEW_PATTERNS = {
    "formulaic_transition": (
        r"\bit is important to note that\b",
        r"\bin today's rapidly evolving landscape\b",
        r"\bdelve into\b",
        r"\ba tapestry of\b",
        r"\bserves as a testament to\b",
    ),
    "unsupported_emphasis": (
        r"\bundeniably\b",
        r"\bclearly demonstrates\b",
        r"\bgroundbreaking\b",
        r"\brevolutionary\b",
    ),
    "reader_address": (
        r"\byou can see\b",
        r"\blet us explore\b",
        r"\bwe can clearly see\b",
    ),
}


@dataclass(frozen=True)
class CleanResult:
    cleaned_text: str
    replacements: Tuple[str, ...]
    style_flags: Tuple[str, ...]

    @property
    def publication_clean(self) -> bool:
        return not self.style_flags and not any(char in self.cleaned_text for char in PROHIBITED_CHARACTERS)


def clean_publication_text(text: str) -> CleanResult:
    cleaned = text
    replacements = []

    for character, replacement in PROHIBITED_CHARACTERS.items():
        count = cleaned.count(character)
        if count:
            cleaned = cleaned.replace(character, replacement)
            replacements.append(f"replaced_{ord(character):04x}:{count}")

    for pattern in EXPLICIT_AI_MARKERS:
        cleaned, count = re.subn(pattern, "", cleaned, flags=re.IGNORECASE)
        if count:
            replacements.append(f"removed_explicit_ai_marker:{count}")

    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r" +([,.;:!?])", r"\1", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()

    flags = []
    for category, patterns in STYLE_REVIEW_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, cleaned, flags=re.IGNORECASE):
                flags.append(category)
                break

    return CleanResult(
        cleaned_text=cleaned,
        replacements=tuple(replacements),
        style_flags=tuple(sorted(set(flags))),
    )


def audit_publication_text(text: str) -> Tuple[str, ...]:
    issues = []
    if "\u2014" in text:
        issues.append("em_dash_present")
    if "\u2013" in text:
        issues.append("en_dash_present")
    for pattern in EXPLICIT_AI_MARKERS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            issues.append("explicit_ai_marker_present")
            break
    for category, patterns in STYLE_REVIEW_PATTERNS.items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            issues.append(category)
    return tuple(sorted(set(issues)))
