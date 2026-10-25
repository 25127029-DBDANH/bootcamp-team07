"""Unit tests for Week 3 individual exercises of pghung2516_netizen."""

from datetime import date
from pathlib import Path

import pytest
from members.pghung2516_netizen.w3.cli import main
from members.pghung2516_netizen.w3.dates import parse_due
from members.pghung2516_netizen.w3.log_stats import analyse

BASE_DATE = date(2026, 10, 6)  # Tuesday


def test_dates_parsing_iso():
    """Test ISO format parsing."""
    assert parse_due("2026-10-30", BASE_DATE) == date(2026, 10, 30)
    assert parse_due("2027-01-01", BASE_DATE) == date(2027, 1, 1)


def test_dates_parsing_relative():
    """Test relative keywords and expressions."""
    assert parse_due("today", BASE_DATE) == BASE_DATE
    assert parse_due("tomorrow", BASE_DATE) == date(2026, 10, 7)
    assert parse_due("Tomorrow", BASE_DATE) == date(2026, 10, 7)
    assert parse_due("in 1 day", BASE_DATE) == date(2026, 10, 7)
    assert parse_due("in 3 days", BASE_DATE) == date(2026, 10, 9)
    assert parse_due("in 10 days", BASE_DATE) == date(2026, 10, 16)


def test_dates_parsing_weekdays():
    """Test weekday calculations always return strictly future occurrences."""
    # BASE_DATE is Tuesday (weekday 1)
    # Next Wed (weekday 2): +1 day -> 2026-10-07
    assert parse_due("Wed", BASE_DATE) == date(2026, 10, 7)
    assert parse_due("wednesday", BASE_DATE) == date(2026, 10, 7)
    # Next Fri (weekday 4): +3 days -> 2026-10-09
    assert parse_due("Fri", BASE_DATE) == date(2026, 10, 9)
    # Next Tue (same weekday): strictly next week (+7 days) -> 2026-10-13
    assert parse_due("Tue", BASE_DATE) == date(2026, 10, 13)
    assert parse_due("Tuesday", BASE_DATE) == date(2026, 10, 13)


def test_dates_parsing_errors():
    """Test that invalid inputs raise ValueError."""
    with pytest.raises(ValueError):
        parse_due("", BASE_DATE)
    with pytest.raises(ValueError):
        parse_due("   ", BASE_DATE)
    with pytest.raises(ValueError):
        parse_due("someday", BASE_DATE)
    with pytest.raises(ValueError):
        parse_due("next week", BASE_DATE)


def test_log_stats_analyse_basic():
    """Test basic request counts and p95 calculations."""
    pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    res = analyse(pairs)
    assert res["counts"]["fee"] == 3
    assert res["counts"]["rag"] == 2
    assert res["p95"]["fee"] == 300.0
    assert res["p95"]["rag"] == 1100.0
    assert res["slowest"] == "rag"


def test_log_stats_analyse_empty():
    """Test log stats analysis with empty input."""
    res = analyse([])
    assert len(res["counts"]) == 0
    assert res["p95"] == {}
    assert res["slowest"] is None


def test_log_stats_analyse_multiple_values():
    """Test p95 nearest-rank calculations for more samples."""
    # 20 samples: 95th percentile corresponds to rank ceil(0.95*20) = 19 -> index 18 (0-indexed)
    latencies = [i * 10 for i in range(1, 21)]  # 10, 20, ..., 200
    pairs = [("api", lat) for lat in latencies]
    res = analyse(pairs)
    assert res["counts"]["api"] == 20
    assert res["p95"]["api"] == 190.0
    assert res["slowest"] == "api"


def test_cli_execution_and_errors(capsys):
    """Test CLI runs correctly and handles errors properly."""
    sample_csv = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"

    # Test valid run
    ret = main([str(sample_csv), "--hours", "2", "--today", "2026-10-26"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Tonight (2.0 h):" in captured.out
    assert "Assignment" in captured.out

    # Test missing file error
    ret_bad = main(["nonexistent.csv", "--hours", "2"])
    assert ret_bad == 1
    captured_bad = capsys.readouterr()
    assert "Error: Tasks file not found" in captured_bad.err
