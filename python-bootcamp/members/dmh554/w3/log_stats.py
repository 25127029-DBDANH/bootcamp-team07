"""W3-2: Chat-log analyser — request counts and p95 latency per route.

The ``analyse`` function takes a list of ``(route, latency_ms)`` pairs and
returns a summary dict with three keys:

``"counts"``
    A dict mapping each route name to the number of requests seen.
``"p95"``
    A dict mapping each route name to its 95th-percentile latency (ms).
    The p95 is the value at index ``ceil(0.95 * N) - 1`` of the sorted
    latency list (1-based nearest-rank method).
``"slowest"``
    The route name with the highest p95 latency.
"""

import math
from collections import defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Analyse a sequence of ``(route, latency_ms)`` log pairs.

    Parameters
    ----------
    pairs:
        Iterable of ``(route: str, latency_ms: int | float)`` tuples.
        May contain multiple entries for the same route.

    Returns
    -------
    dict
        ``"counts"``  – ``dict[str, int]``, requests per route.
        ``"p95"``     – ``dict[str, float]``, p95 latency per route.
        ``"slowest"`` – ``str``, the route with the highest p95 (or ``""``
                        when *pairs* is empty).

    Examples
    --------
    >>> pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    >>> result = analyse(pairs)
    >>> result["counts"] == {"fee": 3, "rag": 2}
    True
    >>> result["slowest"]
    'rag'
    >>> result["p95"]["fee"]
    300
    """
    counts: dict[str, int] = {}
    latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] = counts.get(route, 0) + 1
        latencies[route].append(float(latency_ms))

    p95: dict[str, float] = {}
    for route, times in latencies.items():
        times_sorted = sorted(times)
        # Nearest-rank p95: rank = ceil(0.95 * N), then 0-indexed as rank-1.
        # E.g. for N=3 → rank=3 → idx=2 → the 3rd (largest) value.
        # This matches: fee=[100,200,300] → p95["fee"]=300.
        idx = math.ceil(0.95 * len(times_sorted)) - 1
        p95[route] = times_sorted[idx]

    slowest = max(p95, key=lambda r: p95[r]) if p95 else ""

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
