import importlib
import sys
from pathlib import Path

import pytest

BOOTCAMP = Path(__file__).resolve().parents[3]
if str(BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP))

translate = importlib.import_module("members.ankhang_maker.w1.translate")
primes_up_to = translate.primes_up_to


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, int(n**0.5) + 1))


def test_small_known_values():
    assert primes_up_to(10) == [2, 3, 5, 7]
    assert primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_smallest_prime():
    assert primes_up_to(2) == [2]
    assert primes_up_to(3) == [2, 3]


@pytest.mark.parametrize("n", [0, -1, -100])
def test_zero_and_negative_give_empty_list(n):
    # Edge case: the instructor's tests only check n = 1.
    assert primes_up_to(n) == []


@pytest.mark.parametrize("n", [11, 13, 97])
def test_upper_bound_is_inclusive(n):
    assert primes_up_to(n)[-1] == n


@pytest.mark.parametrize("n", [4, 9, 25, 49])
def test_perfect_squares_are_not_listed(n):
    assert n not in primes_up_to(n)


def test_matches_reference_for_every_n_up_to_200():
    for n in range(201):
        expected = [x for x in range(2, n + 1) if is_prime(x)]
        assert primes_up_to(n) == expected, f"wrong result for n={n}"


def test_known_prime_counts():
    assert len(primes_up_to(100)) == 25
    assert len(primes_up_to(10_000)) == 1229


def test_result_is_sorted_and_has_no_duplicates():
    result = primes_up_to(500)
    assert result == sorted(set(result))
