"""Collect and screen recent AI, ML, LLM and deep learning research.

The initial implementation uses the official arXiv API. Scores are preliminary
screening signals derived from transparent keyword rules. They are not claims
about scientific validity and cannot authorise integration.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from PFRAMOS.analysis.learning_log import append_learning
from PFRAMOS.tech_sweep.models import ResearchCandidate


PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = PFRAMOS_ROOT / "outputs" / "public" / "tech_sweep"
PRIVATE_DIR = PFRAMOS_ROOT / "outputs" / "private" / "tech_sweep"
ARXIV_API = "https://export.arxiv.org/api/query"
CATEGORIES = ("cs.AI", "cs.LG", "cs.CL", "cs.CV", "stat.ML")
MAX_RESULTS = 80

RELEVANCE_TERMS = {
    "optimisation", "optimization", "bayesian optimisation", "black-box",
    "surrogate", "uncertainty", "calibration", "robustness", "interpretability",
    "sparse", "mixture of experts", "routing", "agent", "reasoning", "memory",
    "retrieval", "evaluation", "hallucination", "efficient", "energy",
    "distributed", "multimodal", "continual learning", "meta-learning",
}
REPRODUCIBILITY_TERMS = {"code", "repository", "open source", "benchmark", "dataset", "reproducible"}
MATURITY_TERMS = {"theorem", "proof", "ablation", "benchmark", "large-scale", "real-world", "evaluation"}
SAFETY_TERMS = {"safety", "robust", "calibration", "uncertainty", "alignment", "failure", "risk"}
EFFICIENCY_TERMS = {"efficient", "sparse", "quantization", "pruning", "distillation", "low-rank", "energy"}


def _contains(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term in lowered)


def _bounded(base: float, increment: float) -> float:
    return max(0.0, min(1.0, base + increment))


def _preliminary_scores(title: str, abstract: str, categories: Sequence[str]) -> Dict[str, float]:
    text = f"{title} {abstract}"
    relevance_hits = _contains(text, RELEVANCE_TERMS)
    reproducibility_hits = _contains(text, REPRODUCIBILITY_TERMS)
    maturity_hits = _contains(text, MATURITY_TERMS)
    safety_hits = _contains(text, SAFETY_TERMS)
    efficiency_hits = _contains(text, EFFICIENCY_TERMS)

    return {
        "relevance": _bounded(0.30, 0.08 * relevance_hits),
        "novelty": 0.55,
        "maturity": _bounded(0.35, 0.08 * maturity_hits),
        "reproducibility": _bounded(0.25, 0.12 * reproducibility_hits),
        "evidence_quality": _bounded(0.40, 0.07 * maturity_hits),
        "transferability": _bounded(0.35, 0.07 * relevance_hits),
        "compute_efficiency": _bounded(0.35, 0.10 * efficiency_hits),
        "energy_efficiency": _bounded(0.30, 0.10 * efficiency_hits),
        "safety": _bounded(0.45, 0.08 * safety_hits),
        "non_duplication": 0.60,
    }


def _fetch_arxiv() -> List[ResearchCandidate]:
    category_query = " OR ".join(f"cat:{category}" for category in CATEGORIES)
    params = urllib.parse.urlencode(
        {
            "search_query": category_query,
            "start": 0,
            "max_results": MAX_RESULTS,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    request = urllib.request.Request(
        f"{ARXIV_API}?{params}",
        headers={"User-Agent": "PFRAMOS-Tech-Sweep/0.1"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read()

    root = ET.fromstring(payload)
    atom = {"a": "http://www.w3.org/2005/Atom"}
    candidates: List[ResearchCandidate] = []

    for entry in root.findall("a:entry", atom):
        title = " ".join((entry.findtext("a:title", default="", namespaces=atom)).split())
        abstract = " ".join((entry.findtext("a:summary", default="", namespaces=atom)).split())
        source_url = entry.findtext("a:id", default="", namespaces=atom)
        published_at = entry.findtext("a:published", default="", namespaces=atom)
        categories = tuple(
            category.attrib.get("term", "")
            for category in entry.findall("a:category", atom)
            if category.attrib.get("term")
        )
        scores = _preliminary_scores(title, abstract, categories)
        candidate_id = hashlib.sha256(source_url.encode("utf-8")).hexdigest()[:16]
        candidates.append(
            ResearchCandidate(
                candidate_id=candidate_id,
                title=title,
                source="arXiv",
                source_url=source_url,
                published_at=published_at,
                abstract=abstract,
                categories=categories,
                **scores,
            )
        )
    return candidates


def main() -> None:
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)

    candidates = _fetch_arxiv()
    ranked = sorted(candidates, key=lambda item: item.recruitment_score, reverse=True)
    experimental = [item for item in ranked if item.recruitment_state == "experimental_node_candidate"]
    quarantined = [item for item in ranked if item.recruitment_state == "quarantined_candidate"]

    public_discoveries = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "official arXiv API",
        "candidate_count": len(ranked),
        "screening_notice": "Scores are preliminary transparent screening signals, not scientific validation.",
        "discoveries": [
            {
                "candidate_id": item.candidate_id,
                "title": item.title,
                "source": item.source,
                "source_url": item.source_url,
                "published_at": item.published_at,
                "categories": item.categories,
                "recruitment_score": item.recruitment_score,
                "recruitment_state": item.recruitment_state,
            }
            for item in ranked[:30]
        ],
    }
    (PUBLIC_DIR / "latest_discoveries.json").write_text(
        json.dumps(public_discoveries, indent=2), encoding="utf-8"
    )

    summary = {
        "generated_at": public_discoveries["generated_at"],
        "screened": len(ranked),
        "experimental_node_candidates": len(experimental),
        "quarantined_candidates": len(quarantined),
        "auto_integrated": 0,
        "human_approval_required": True,
    }
    (PUBLIC_DIR / "recruitment_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    private_payload = {
        "status": "quarantine_only_no_automatic_integration",
        "candidates": [asdict(item) | {
            "recruitment_score": item.recruitment_score,
            "recruitment_state": item.recruitment_state,
        } for item in ranked],
    }
    (PRIVATE_DIR / "recruitment_candidates.json").write_text(
        json.dumps(private_payload, indent=2), encoding="utf-8"
    )

    append_learning(
        stage="technology_sweep",
        finding="Recent AI and ML research was screened for possible PFRAMOS relevance.",
        evidence=summary,
        action_taken="Collected official arXiv metadata and applied transparent preliminary recruitment scoring.",
        outcome="Promising items were quarantined for human review; no technique was integrated automatically.",
        reusable_rule="Discovery may be automated, but recruitment and integration require traceable validation and explicit approval.",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
