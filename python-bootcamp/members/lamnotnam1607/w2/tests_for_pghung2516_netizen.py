"""Cross-tests for pghung2516_netizen's W1-4 transpose function."""

from members.pghung2516_netizen.w1.translate import transpose


def test_transpose_rectangular_matrix():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]


def test_transpose_square_matrix():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_transpose_single_row():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_transpose_single_column():
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


def test_transpose_single_element_matrix():
    """Edge case not covered by the instructor's transpose tests."""
    assert transpose([[42]]) == [[42]]
