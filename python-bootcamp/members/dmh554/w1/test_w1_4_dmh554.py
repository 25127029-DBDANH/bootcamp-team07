from members.dmh554.w1.translate import count_freq, most_frequent


def test_count_freq():
    assert count_freq([3, 1, 3, 2, 1, 3]) == {3: 3, 1: 2, 2: 1}
    assert count_freq([]) == {}


def test_most_frequent():
    assert most_frequent([3, 1, 3, 2, 1, 3]) == 3
    assert most_frequent([2, 2, 5, 5]) == 2
    assert most_frequent([7]) == 7


def test_most_frequent_empty_raises():
    try:
        most_frequent([])
    except ValueError:
        return
    raise AssertionError("expected ValueError")
