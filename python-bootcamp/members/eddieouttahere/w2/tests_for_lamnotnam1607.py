from members.lamnotnam1607.w1.translate import is_palindrome, reverse_string


def test_reverse_basic():
    assert reverse_string("git") == "tig"


def test_reverse_empty():
    assert reverse_string("") == ""


def test_palindrome_true():
    assert is_palindrome("level") is True


def test_palindrome_false():
    assert is_palindrome("hello") is False


def test_palindrome_case_sensitive():
    # edge case not covered by the instructor's tests/test_w1.py:
    # same word but different case should NOT be treated as palindrome
    assert is_palindrome("Level") is False
