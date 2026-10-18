"""W2-4: tests for 25127029_dbdanh's W1-4 (translate.py, insertion_sort)."""

import importlib.util
from pathlib import Path

# Load the reviewee's module straight from their folder: members/25127029_dbdanh/w1/
_PATH = Path(__file__).resolve().parents[2] / "25127029_dbdanh" / "w1" / "translate.py"
_spec = importlib.util.spec_from_file_location("dbdanh_translate", _PATH)
tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tr)


def test_sorts_unsorted_list():
    assert tr.insertion_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]


def test_already_sorted_list_is_unchanged():
    assert tr.insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted_list():
    assert tr.insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates_are_kept():
    assert tr.insertion_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_negative_numbers_and_zero():
    assert tr.insertion_sort([0, -5, 3, -1]) == [-5, -1, 0, 3]


def test_single_element():
    assert tr.insertion_sort([7]) == [7]


def test_sorts_in_place_and_returns_same_list():
    """Edge case not in tests/test_w1.py: the docstring promises that the
    input list itself is sorted and that the same list object is returned."""
    data = [3, 1, 2]
    result = tr.insertion_sort(data)
    assert result is data
    assert data == [1, 2, 3]


def test_matches_builtin_sorted():
    for case in ([9, 8, 7, 7, 1], [2, 2, 2], [-1, 5, -1, 0, 5]):
        assert tr.insertion_sort(list(case)) == sorted(case)
