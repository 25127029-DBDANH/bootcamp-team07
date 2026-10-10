"""W1-4: Translate C++ to Python – Sieve of Eratosthenes.

Difference from the C++ version:
    In C++, a ``std::vector<bool>`` of size ``n + 1`` is used and indices are
    handled with C-style ``for`` loops using ``(long long)i * i <= n`` to avoid
    integer overflow.  In Python, integers have arbitrary precision so there is
    no overflow concern; we simply use ``i * i <= n`` with a ``while`` loop and
    build the result list via a list comprehension instead of ``push_back``.
"""


def primes_up_to(n: int) -> list[int]:
    """Return all prime numbers from 2 to *n* (inclusive) using the Sieve of Eratosthenes.

    If *n* < 2, return an empty list.

    Unlike the C++ version that requires a ``(long long)`` cast to prevent
    integer overflow when computing ``i * i``, Python's arbitrary-precision
    integers make this unnecessary.
    """
    if n < 2:
        return []

    # Create boolean sieve list, all True initially
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    # Mark multiples of each prime as not prime
    i = 2
    while i * i <= n:
        if is_prime[i]:
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1

    # Collect primes using list comprehension
    return [x for x in range(2, n + 1) if is_prime[x]]
