def count_freq(a: list[int]) -> dict[int, int]:
    """Count how many times each value appears in a.

    Difference from C++: in C++ `freq[x]++` works even when x is new,
    because std::map creates the key with value 0. In Python the same
    thing raises KeyError, so we use dict.get(x, 0) instead.
    """
    freq: dict[int, int] = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    return freq


def most_frequent(a: list[int]) -> int:
    """Return the most frequent value; on a tie, the smallest value.

    Difference from C++: C++ reads a[0] on an empty vector (undefined
    behaviour). Python raises ValueError with a clear message instead.
    """
    if not a:
        raise ValueError("most_frequent() needs a non-empty list")
    freq = count_freq(a)
    best = a[0]
    for value, cnt in freq.items():
        if cnt > freq[best] or (cnt == freq[best] and value < best):
            best = value
    return best
