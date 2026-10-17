"""Unit tests verifying Week 1 code of Leader Danh (25127029-DBDANH)."""

import importlib
import sys
from pathlib import Path

import pytest

BOOTCAMP = Path(__file__).resolve().parents[3]
if str(BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP))

_BASE = "members.25127029_dbdanh.w1"
_grades = importlib.import_module(f"{_BASE}.grades")
_text_tools = importlib.import_module(f"{_BASE}.text_tools")
_rules = importlib.import_module(f"{_BASE}.rules")
_translate = importlib.import_module(f"{_BASE}.translate")
_timetable = importlib.import_module(f"{_BASE}.timetable")

summary = _grades.summary
word_count = _text_tools.word_count
top_k = _text_tools.top_k
can_register_thesis = _rules.can_register_thesis
missing = _rules.missing
insertion_sort = _translate.insertion_sort
by_day = _timetable.by_day


def test_danh_grades():
    """Test W1-1 grades summary calculation and empty list error."""
    assert summary([7.5, 9.0, 6.0, 8.0]) == {
        "min": 6.0,
        "max": 9.0,
        "mean": 7.62,
        "median": 7.75,
    }
    assert summary([5.0]) == {
        "min": 5.0,
        "max": 5.0,
        "mean": 5.0,
        "median": 5.0,
    }
    with pytest.raises(ValueError):
        summary([])


def test_danh_text_tools():
    """Test W1-2 word_count and top_k frequency ranking."""
    text = "Python is great! Python is simple and clean."
    counts = word_count(text)
    assert counts["python"] == 2
    assert counts["is"] == 2
    assert counts["great"] == 1
    assert counts["clean"] == 1

    ranked = top_k("banana apple banana orange apple banana", 2)
    assert ranked == [("banana", 3), ("apple", 2)]
    assert top_k("", 5) == []
    assert top_k("hello world", 0) == []


def test_danh_rules():
    """Test W1-3 thesis eligibility check and missing requirements."""
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 3.5) is False
    assert can_register_thesis(130, 1.9) is False

    assert missing(120, 2.0) == []
    assert missing(110, 3.0) == ["need 10 more credits"]
    assert missing(125, 1.8) == ["need GPA of at least 2.0"]
    reasons = missing(100, 1.5)
    assert len(reasons) == 2
    assert "need 20 more credits" in reasons[0]
    assert "need GPA of at least 2.0" in reasons[1]


def test_danh_insertion_sort():
    """Test W1-4 insertion_sort in-place behavior and edge cases (Variant 2)."""
    # Standard unsorted list
    assert insertion_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]

    # Verify in-place mutation property
    original = [4, 1, 3, 2]
    result = insertion_sort(original)
    assert result is original
    assert result == [1, 2, 3, 4]

    # Already sorted and reverse sorted
    assert insertion_sort([10, 20, 30]) == [10, 20, 30]
    assert insertion_sort([50, 40, 30, 20, 10]) == [10, 20, 30, 40, 50]

    # Duplicates and negative numbers
    assert insertion_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]

    # Edge cases: empty list and single element
    assert insertion_sort([]) == []
    assert insertion_sort([99]) == [99]


def test_danh_timetable():
    """Test W1-5 timetable grouping by day and sorting."""
    schedule = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
        ("PHY00001", "Wed"),
    ]
    grouped = by_day(schedule)
    assert grouped == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
        "Wed": ["PHY00001"],
    }
    assert by_day([]) == {}
