"""W1-4: insertion sort translated from C++."""


def insertion_sort(a: list[int]) -> list[int]:
    """Sort list in-place and return the sorted list.

    Difference from C++: C++ version returns void and modifies std::vector<int>&,
    whereas Python function mutates the list in-place and also returns it for chaining.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
