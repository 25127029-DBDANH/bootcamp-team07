"""Unit tests verifying Week 1 code of Eddie (eddieouttahere)."""

import sys
from pathlib import Path

import pytest

BOOTCAMP_DIR = Path(__file__).resolve().parents[3]
if str(BOOTCAMP_DIR) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP_DIR))

from members.eddieouttahere.w1.grades import summary  # noqa: E402
from members.eddieouttahere.w1.rules import can_register_thesis, missing  # noqa: E402
from members.eddieouttahere.w1.text_tools import top_k, word_count  # noqa: E402
from members.eddieouttahere.w1.timetable import by_day  # noqa: E402
from members.eddieouttahere.w1.translate import binary_search  # noqa: E402


def test_eddie_grades():
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


def test_eddie_text_tools():
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


def test_eddie_rules():
    """Test W1-3 thesis eligibility check and missing requirements."""
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 3.5) is False
    assert can_register_thesis(130, 1.9) is False

    assert missing(120, 2.0) == []
    assert missing(110, 3.0) == ["need 10 more credits"]
    assert missing(125, 1.8) == ["need gpa of at least 2.0, currently 1.8"]
    reasons = missing(100, 1.5)
    assert len(reasons) == 2
    assert "need 20 more credits" in reasons[0]


def test_eddie_translate_binary_search():
    """Test W1-4 binary_search implementation (Eddie's variant 1)."""
    arr = [2, 4, 6, 8, 10, 12]
    assert binary_search(arr, 2) == 0
    assert binary_search(arr, 8) == 3
    assert binary_search(arr, 12) == 5
    assert binary_search(arr, 5) == -1
    assert binary_search(arr, 100) == -1
    assert binary_search([], 7) == -1


def test_eddie_timetable():
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
