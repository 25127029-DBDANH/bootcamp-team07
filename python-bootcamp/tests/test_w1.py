import pytest


def test_w1_1_summary(load):
    g = load("w1", "grades")
    assert g.summary([7.5, 9, 6, 8]) == {"min": 6, "max": 9, "mean": 7.62, "median": 7.75}
    assert g.summary([5])["median"] == 5
    with pytest.raises(ValueError):
        g.summary([])


def test_w1_2_word_count(load):
    t = load("w1", "text_tools")
    assert t.word_count("Git is fun. Git is fast!") == {"git": 2, "is": 2, "fun": 1, "fast": 1}
    assert t.top_k("Git is fun. Git is fast!", 2) == [("git", 2), ("is", 2)]
    assert t.top_k("", 3) == []


def test_w1_3_thesis(load):
    r = load("w1", "rules")
    assert r.can_register_thesis(120, 2.0)
    assert not r.can_register_thesis(118, 3.1)
    assert r.missing(118, 3.1) == ["need 2 more credits"]
    assert r.missing(120, 2.0) == []
    assert len(r.missing(100, 1.5)) == 2


def test_w1_4_translate(load, variant):
    tr = load("w1", "translate")
    if variant == 1:
        assert tr.binary_search([1, 3, 5, 7], 5) == 2
        assert tr.binary_search([1, 3, 5, 7], 4) == -1
        assert tr.binary_search([], 1) == -1
    elif variant == 2:
        assert tr.insertion_sort([3, 1, 2]) == [1, 2, 3]
        assert tr.insertion_sort([]) == []
    elif variant == 3:
        assert tr.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        assert tr.transpose([]) == []
    # ---- Team 07 extension: extra variants 5-7 (original branches 1-4 are unchanged) ----
    elif variant == 5:  # GCD / LCM
        assert tr.gcd(12, 18) == 6
        assert tr.gcd(7, 13) == 1
        assert tr.gcd(10, 5) == 5
        assert tr.gcd(0, 5) == 5
        assert tr.gcd(5, 0) == 5
        assert tr.lcm(4, 6) == 12
        assert tr.lcm(3, 7) == 21
        assert tr.lcm(5, 5) == 5
        assert tr.lcm(0, 7) == 0
        assert tr.lcm(7, 0) == 0
        assert tr.lcm(10**10, 10**10 + 1) == 10**10 * (10**10 + 1)
    elif variant == 6:  # palindrome / reverse (case-sensitive)
        assert tr.is_palindrome("level") is True
        assert tr.is_palindrome("abba") is True
        assert tr.is_palindrome("a") is True
        assert tr.is_palindrome("") is True
        assert tr.is_palindrome("git") is False
        assert tr.is_palindrome("Level") is False
        assert tr.reverse_string("git") == "tig"
        assert tr.reverse_string("Hello") == "olleH"
        assert tr.reverse_string("a") == "a"
        assert tr.reverse_string("") == ""
    elif variant == 7:  # frequency count
        assert tr.count_freq([3, 1, 3, 2, 1, 3]) == {3: 3, 1: 2, 2: 1}
        assert tr.count_freq([]) == {}
        assert tr.count_freq([5]) == {5: 1}
        assert tr.count_freq([-1, -1, 0]) == {-1: 2, 0: 1}
        assert tr.most_frequent([3, 1, 3, 2, 1, 3]) == 3
        assert tr.most_frequent([2, 2, 5, 5]) == 2
        assert tr.most_frequent([5, 5, 2, 2]) == 2
        assert tr.most_frequent([-3, -3, 4, 4]) == -3
        assert tr.most_frequent([7]) == 7
        with pytest.raises(ValueError) as exc:
            tr.most_frequent([])
        assert str(exc.value)
    # ---- end of extension ----
    else:
        assert tr.primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
        assert tr.primes_up_to(1) == []
    assert tr.__doc__ or any(getattr(tr, n).__doc__ for n in dir(tr) if callable(getattr(tr, n)))


def test_w1_5_by_day(load):
    tt = load("w1", "timetable")
    got = tt.by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")])
    assert got == {"Mon": ["CSC10001", "CSC10014"], "Tue": ["MTH00003"]}
    assert tt.by_day([]) == {}