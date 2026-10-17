"""W1-4: GCD and LCM translated from C++."""


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b (Euclid's algorithm).

    Difference from C++: Python can assign several variables at once
    (a, b = b, a % b), so the temporary variable `t` is not needed.
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b; 0 if either is 0.

    Difference from C++: Python integers never overflow, so there is no
    need to cast to `long long` before multiplying.
    """
    if a == 0 or b == 0:
        return 0
    return (a // gcd(a, b)) * b
