"""W2-4: Tests for dhdang2523-coder's W1-4 translate.py (gcd and lcm)."""

from members.dhdang2523_coder.w1.translate import gcd, lcm

# ---------- gcd tests ----------


class TestGcd:
    """Tests for the gcd function."""

    def test_basic(self) -> None:
        """GCD of two positive integers with a common factor."""
        assert gcd(12, 8) == 4

    def test_coprime(self) -> None:
        """GCD of two coprime numbers should be 1."""
        assert gcd(7, 13) == 1

    def test_same_number(self) -> None:
        """GCD of a number with itself is that number."""
        assert gcd(5, 5) == 5

    def test_one_is_zero(self) -> None:
        """GCD(0, n) should return n (edge case)."""
        assert gcd(0, 9) == 9
        assert gcd(9, 0) == 9

    def test_both_zero(self) -> None:
        """GCD(0, 0) should return 0 (edge case not in instructor tests)."""
        assert gcd(0, 0) == 0

    def test_one_is_one(self) -> None:
        """GCD of any number and 1 is always 1."""
        assert gcd(1, 100) == 1
        assert gcd(100, 1) == 1

    def test_large_numbers(self) -> None:
        """GCD should work with large numbers."""
        assert gcd(1000000, 500000) == 500000


# ---------- lcm tests ----------


class TestLcm:
    """Tests for the lcm function."""

    def test_basic(self) -> None:
        """LCM of two positive integers."""
        assert lcm(4, 6) == 12

    def test_coprime(self) -> None:
        """LCM of coprime numbers is their product."""
        assert lcm(3, 7) == 21

    def test_one_is_zero(self) -> None:
        """LCM is 0 if either argument is 0."""
        assert lcm(0, 5) == 0
        assert lcm(5, 0) == 0

    def test_both_zero(self) -> None:
        """LCM(0, 0) should return 0 (edge case not in instructor tests)."""
        assert lcm(0, 0) == 0

    def test_same_number(self) -> None:
        """LCM of a number with itself is that number."""
        assert lcm(7, 7) == 7

    def test_one_is_multiple(self) -> None:
        """LCM when one number is a multiple of the other."""
        assert lcm(3, 9) == 9
        assert lcm(9, 3) == 9
