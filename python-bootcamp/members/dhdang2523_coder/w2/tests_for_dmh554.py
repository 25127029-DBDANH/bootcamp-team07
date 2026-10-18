import pytest
from members.dmh554.w1.translate import count_freq, most_frequent


def test_count_freq_basic() -> None:
    assert count_freq([1, 2, 1, 3, 2, 1]) == {1: 3, 2: 2, 3: 1}


def test_count_freq_empty_list() -> None:
    assert count_freq([]) == {}


def test_most_frequent_clear_winner() -> None:
    assert most_frequent([4, 1, 4, 2, 4, 2]) == 4


def test_most_frequent_tie_returns_smallest() -> None:
    # 3 và 1 cùng xuất hiện 2 lần -> trả về số nhỏ hơn là 1
    assert most_frequent([3, 3, 1, 1, 2]) == 1


def test_most_frequent_empty_raises_value_error() -> None:
    with pytest.raises(ValueError, match="non-empty list"):
        most_frequent([])


def test_edge_case_negative_tie_and_single_element() -> None:
    # Edge case: hòa nhau giữa số âm và số dương (phải chọn số âm nhỏ hơn) và mảng 1 phần tử
    assert most_frequent([5, 5, -10, -10, 0]) == -10
    assert most_frequent([-999]) == -999
    assert count_freq([-5, -5, 0]) == {-5: 2, 0: 1}