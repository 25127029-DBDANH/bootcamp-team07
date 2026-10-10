"""Module for translating matrix transpose function from C++ to Python."""


def transpose(m: list[list[int]]) -> list[list[int]]:
    """Transpose a 2D matrix (vector of vectors in C++).

    Differences from the C++ version:
    1. Python handles dynamic list dimensions dynamically without needing to
       explicitly pre-allocate vector sizes or track size_t indices.
    2. Python list comprehensions offer a more expressive, concise, and Pythonic
       way to construct the transposed matrix than nested index-based for loops.
    3. Empty matrix conditions are checked simply using Python's truthiness (`if not m`).
    """
    if not m or not m[0]:
        return []

    rows = len(m)
    cols = len(m[0])
    return [[m[i][j] for i in range(rows)] for j in range(cols)]
