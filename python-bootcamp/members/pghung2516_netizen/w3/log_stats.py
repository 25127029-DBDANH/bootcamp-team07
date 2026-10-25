"""Chat log latency and traffic analysis utilities for bootcamp week 3 (W3-2)."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Analyse request log pairs and compute route counts, p95 latency, and the slowest route.

    Args:
        pairs: A list of (route_name, latency_ms) tuples.

    Returns:
        A dictionary with keys:
        - "counts": Counter mapping route name to number of requests.
        - "p95": Dictionary mapping route name to nearest-rank p95 latency.
        - "slowest": Name of the route with the highest p95 latency (or None if empty).
    """
    counts: Counter[str] = Counter()
    by_route: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        by_route[route].append(float(latency))

    p95: dict[str, float] = {}
    for route, latencies in by_route.items():
        sorted_latencies = sorted(latencies)
        # Nearest-rank method: rank = ceil(p * N), 0-indexed idx = rank - 1
        idx = math.ceil(0.95 * len(sorted_latencies)) - 1
        p95[route] = sorted_latencies[idx]

    slowest: str | None = None
    if p95:
        slowest = max(p95, key=lambda r: p95[r])

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
