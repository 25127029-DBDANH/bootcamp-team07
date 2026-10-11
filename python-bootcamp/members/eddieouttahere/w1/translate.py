def binary_search(a: list[int], key: int) -> int:
    """Return the index of key in sorted list a, or -1 if not found.

    Difference from C++: there is no integer overflow to worry about
    when computing mid = lo + (hi - lo) // 2, since Python ints never
    overflow; `//` is used instead of `/` to keep the division integer,
    because `/` in Python always returns a float.
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
