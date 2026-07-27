from datetime import date

from PFRAMOS.publication_automation.journal_profiles import get_journal_profile


def test_tmlr_requires_official_template_and_anonymity() -> None:
    profile = get_journal_profile("tmlr")
    assert profile.official_template_required
    assert profile.anonymised_submission
    assert profile.submission_platform == "OpenReview"


def test_tmlr_profile_records_policy_verification_date() -> None:
    profile = get_journal_profile("tmlr")
    assert isinstance(profile.verified_on, date)


def test_tmlr_supplement_policy_is_recorded() -> None:
    profile = get_journal_profile("tmlr")
    assert "100 MB" in profile.supplementary_policy


def test_tmlr_prevents_layout_changes() -> None:
    profile = get_journal_profile("tmlr")
    assert any("layout" in check for check in profile.special_checks)
