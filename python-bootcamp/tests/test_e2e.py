"""T3-3: End-to-end tests for the shared study planner.

Written by ankhang-maker.
Tests both the CLI via subprocess and the function pipeline directly.
"""

import subprocess
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

BOOTCAMP = Path(__file__).resolve().parents[1]
SAMPLES = BOOTCAMP / "samples"
TODAY = date(2026, 10, 26)


# ---- CLI (subprocess) tests ----


def test_cli_normal_run():
    """Running the planner with valid CSV returns exit code 0."""
    result = subprocess.run(
        [
            sys.executable, "-m", "shared.study_planner",
            str(SAMPLES / "tasks.csv"),
            "--hours", "2",
            "--today", "2026-10-26",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert result.returncode == 0


def test_cli_output_contains_assignment():
    """Output should list Assignment with 1.5 h first (higher priority)."""
    result = subprocess.run(
        [
            sys.executable, "-m", "shared.study_planner",
            str(SAMPLES / "tasks.csv"),
            "--hours", "2",
            "--today", "2026-10-26",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert "Assignment" in result.stdout
    assert "1.5 h" in result.stdout


def test_cli_output_contains_ds_exam():
    """Output should list DS exam with 0.5 h second."""
    result = subprocess.run(
        [
            sys.executable, "-m", "shared.study_planner",
            str(SAMPLES / "tasks.csv"),
            "--hours", "2",
            "--today", "2026-10-26",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert "DS exam" in result.stdout
    assert "0.5 h" in result.stdout


def test_cli_output_order():
    """Assignment should appear before DS exam in output."""
    result = subprocess.run(
        [
            sys.executable, "-m", "shared.study_planner",
            str(SAMPLES / "tasks.csv"),
            "--hours", "2",
            "--today", "2026-10-26",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert result.stdout.index("Assignment") < result.stdout.index("DS exam")


def test_cli_tonight_header():
    """Output should start with a 'Tonight' header showing total hours."""
    result = subprocess.run(
        [
            sys.executable, "-m", "shared.study_planner",
            str(SAMPLES / "tasks.csv"),
            "--hours", "2",
            "--today", "2026-10-26",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert "Tonight" in result.stdout
    assert "2.0 h" in result.stdout


# ---- Function-level pipeline test ----


def test_pipeline_render_output():
    """Calling parse → prioritise → allocate → render produces expected text."""
    tasks = parse_csv(SAMPLES / "tasks.csv")
    ordered = prioritise(tasks, TODAY)
    blocks = allocate(ordered, 2)
    output = render(blocks)

    # Assignment (importance=4, 1 day left → score=4) comes before
    # DS exam (importance=5, 4 days left → score=1.25)
    assert "Assignment" in output
    assert "1.5 h" in output
    assert "DS exam" in output
    assert "0.5 h" in output
    # Assignment should be listed first (item 1)
    assert output.index("Assignment") < output.index("DS exam")


def test_pipeline_empty_hours():
    """Zero hours should produce no blocks and empty render output."""
    tasks = parse_csv(SAMPLES / "tasks.csv")
    ordered = prioritise(tasks, TODAY)
    blocks = allocate(ordered, 0)
    output = render(blocks)
    assert output == ""
    assert blocks == []
