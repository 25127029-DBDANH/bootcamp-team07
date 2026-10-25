"""T3-4: Tests for error-handling paths in the shared study planner CLI.

Written by dmh554 (Minh Hạo).
Tests use subprocess to invoke ``python -m shared.study_planner`` and verify
that each error case:
  - exits with the correct return code, and
  - prints a message to stderr that matches the agreed-upon prefix/pattern.

Error-message conventions (agreed with T3-2 / dhdang2523_coder):
  - All hard errors use the prefix ``error:`` and exit with code 1.
  - An infeasible plan prints a ``warning:`` to stderr but still exits 0
    (or exits 1 when ``--strict`` is passed).
"""

import subprocess
import sys
from pathlib import Path

import pytest

BOOTCAMP = Path(__file__).resolve().parents[1]
SAMPLES = BOOTCAMP / "samples"


def _run(*args: str) -> subprocess.CompletedProcess:
    """Helper: run the study planner with the given extra arguments."""
    return subprocess.run(
        [sys.executable, "-m", "shared.study_planner", *args],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
    )


# ---------------------------------------------------------------------------
# 1. File does not exist
# ---------------------------------------------------------------------------


def test_missing_file_exit_code():
    """Non-existent CSV → exit code 1."""
    result = _run("nonexistent_file_that_will_never_exist.csv", "--hours", "2")
    assert result.returncode == 1


def test_missing_file_stderr_not_empty():
    """Non-existent CSV → something informative is printed to stderr."""
    result = _run("nonexistent_file_that_will_never_exist.csv", "--hours", "2")
    assert result.stderr.strip() != ""


def test_missing_file_stderr_has_error_prefix():
    """Non-existent CSV → stderr message starts with 'error:'."""
    result = _run("nonexistent_file_that_will_never_exist.csv", "--hours", "2")
    assert result.stderr.strip().startswith("error:")


# ---------------------------------------------------------------------------
# 2. Empty CSV (header only, no data rows)
# ---------------------------------------------------------------------------


def test_empty_csv_exit_code():
    """CSV with only header → exit code 1."""
    result = _run(str(SAMPLES / "tasks_empty.csv"), "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 1


def test_empty_csv_stderr_not_empty():
    """CSV with only header → something informative is printed to stderr."""
    result = _run(str(SAMPLES / "tasks_empty.csv"), "--hours", "2", "--today", "2026-10-26")
    assert result.stderr.strip() != ""


def test_empty_csv_stderr_has_error_prefix():
    """CSV with only header → stderr message starts with 'error:'."""
    result = _run(str(SAMPLES / "tasks_empty.csv"), "--hours", "2", "--today", "2026-10-26")
    assert result.stderr.strip().startswith("error:")


# ---------------------------------------------------------------------------
# 3. Malformed CSV data (tasks_bad.csv — row 3 has bad importance value)
# ---------------------------------------------------------------------------


def test_bad_csv_exit_code():
    """CSV with invalid data → exit code 1."""
    result = _run(str(SAMPLES / "tasks_bad.csv"), "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 1


def test_bad_csv_stderr_mentions_line_3():
    """CSV with bad row 3 → stderr should mention 'line 3'."""
    result = _run(str(SAMPLES / "tasks_bad.csv"), "--hours", "2", "--today", "2026-10-26")
    assert "line 3" in result.stderr


def test_bad_csv_stderr_has_error_prefix():
    """CSV with invalid data → stderr message starts with 'error:'."""
    result = _run(str(SAMPLES / "tasks_bad.csv"), "--hours", "2", "--today", "2026-10-26")
    assert result.stderr.strip().startswith("error:")


# ---------------------------------------------------------------------------
# 4. Infeasible plan (total effort > available hours)
# ---------------------------------------------------------------------------


def test_infeasible_plan_default_exits_zero():
    """Infeasible plan without --strict → still exits 0, plan is printed."""
    # tasks.csv total effort = 7.5 h; we only provide 2 h
    result = _run(
        str(SAMPLES / "tasks.csv"),
        "--hours", "2",
        "--today", "2026-10-26",
    )
    assert result.returncode == 0


def test_infeasible_plan_prints_warning():
    """Infeasible plan → a warning line is printed to stderr."""
    result = _run(
        str(SAMPLES / "tasks.csv"),
        "--hours", "2",
        "--today", "2026-10-26",
    )
    assert "warning:" in result.stderr


def test_infeasible_plan_warning_mentions_hours():
    """Infeasible plan warning → mentions both needed and available hours."""
    result = _run(
        str(SAMPLES / "tasks.csv"),
        "--hours", "2",
        "--today", "2026-10-26",
    )
    # The warning should contain some hint of hours (e.g. "7.5 h", "2.0 h")
    assert "h" in result.stderr


def test_infeasible_plan_still_outputs_plan():
    """Infeasible plan without --strict → the partial plan is still printed to stdout."""
    result = _run(
        str(SAMPLES / "tasks.csv"),
        "--hours", "2",
        "--today", "2026-10-26",
    )
    assert "Tonight" in result.stdout
    assert "Assignment" in result.stdout


@pytest.mark.parametrize("hours", ["0.5", "1"])
def test_infeasible_plan_strict_exits_one(hours):
    """Infeasible plan with --strict → exit code 1."""
    result = _run(
        str(SAMPLES / "tasks.csv"),
        "--hours", hours,
        "--today", "2026-10-26",
        "--strict",
    )
    assert result.returncode == 1


def test_feasible_plan_no_warning():
    """When plan IS feasible → no warning on stderr."""
    # Provide more hours than needed (7.5 h total in tasks.csv)
    result = _run(
        str(SAMPLES / "tasks.csv"),
        "--hours", "10",
        "--today", "2026-10-26",
    )
    assert result.returncode == 0
    assert "warning:" not in result.stderr
