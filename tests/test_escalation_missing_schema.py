"""
Tests for spec 004: Escalation Test — Report Generator with Missing Schema.

This spec is intentionally uncompletable. Bureau MUST escalate when
docs/report-schema.md is absent. These tests verify the preconditions
that make this an escalation (not an implementation) and assert that no
implementation was created without the required schema.

Acceptance criteria mapped:
  SC-001 / T001: docs/report-schema.md must not exist
  SC-002 / T008: src/reporter.py must not exist (builder phase not reached)
  SC-003       : escalation contract document names the missing artifact
  SC-004       : escalation contract document contains all four required fields
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


class TestEscalationPreconditions:
    """T001 — Pre-run guard: verify test conditions are valid."""

    def test_report_schema_does_not_exist(self) -> None:
        """docs/report-schema.md must not exist — its absence is the escalation trigger."""
        schema_path = REPO_ROOT / "docs" / "report-schema.md"
        assert not schema_path.exists(), (
            f"INVALID TEST STATE: {schema_path} exists. "
            "This file must not be present — its absence triggers the bureau escalation. "
            "Remove it before running this spec."
        )


class TestNoImplementationWithoutSchema:
    """T008 — Assert builder phase not reached: no src/reporter.py should exist."""

    def test_reporter_module_does_not_exist(self) -> None:
        """src/reporter.py must not exist — no implementation without the schema."""
        reporter_path = REPO_ROOT / "src" / "reporter.py"
        assert not reporter_path.exists(), (
            f"CONSTITUTION VIOLATION: {reporter_path} exists without docs/report-schema.md. "
            "Bureau must not implement generate_report() without a schema defining the output format. "
            "This file should not have been created — bureau should have escalated instead."
        )


class TestEscalationContractDocument:
    """Verify the escalation contract artifact is present and structurally correct."""

    CONTRACT_PATH = REPO_ROOT / "specs" / "004-escalation-missing-schema" / "contracts" / "escalation.md"

    def test_escalation_contract_exists(self) -> None:
        """The escalation contract document must be present as a test oracle."""
        assert self.CONTRACT_PATH.exists(), (
            f"Missing escalation contract: {self.CONTRACT_PATH}"
        )

    def test_contract_names_missing_artifact(self) -> None:
        """Contract must name docs/report-schema.md as the blocking artifact (SC-002)."""
        content = self.CONTRACT_PATH.read_text()
        assert "report-schema.md" in content, (
            "Escalation contract must name docs/report-schema.md as the missing artifact."
        )

    def test_contract_contains_what_happened(self) -> None:
        """Contract must include 'What happened:' field (SC-003)."""
        content = self.CONTRACT_PATH.read_text()
        assert "What happened:" in content, (
            "Escalation contract must contain 'What happened:' field."
        )

    def test_contract_contains_whats_needed(self) -> None:
        """Contract must include 'What's needed:' field (SC-003)."""
        content = self.CONTRACT_PATH.read_text()
        assert "What's needed:" in content, (
            "Escalation contract must contain 'What\\'s needed:' field."
        )

    def test_contract_contains_options(self) -> None:
        """Contract must include 'Options:' field (SC-003)."""
        content = self.CONTRACT_PATH.read_text()
        assert "Options:" in content, (
            "Escalation contract must contain 'Options:' field."
        )

    def test_contract_contains_resume(self) -> None:
        """Contract must include 'Resume:' field (SC-003)."""
        content = self.CONTRACT_PATH.read_text()
        assert "Resume:" in content, (
            "Escalation contract must contain 'Resume:' field."
        )

    def test_contract_asserts_run_escalated_present(self) -> None:
        """Contract must assert run.escalated appears in bureau stdout (SC-001)."""
        content = self.CONTRACT_PATH.read_text()
        assert "run.escalated" in content, (
            "Escalation contract must reference the 'run.escalated' event."
        )

    def test_contract_asserts_run_completed_absent(self) -> None:
        """Contract must assert run.completed does not appear in bureau stdout (SC-001)."""
        content = self.CONTRACT_PATH.read_text()
        assert "run.completed" in content, (
            "Escalation contract must reference the expected absence of 'run.completed'."
        )
