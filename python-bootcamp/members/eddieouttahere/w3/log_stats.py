"""Analysis helpers for route latency logs."""

from collections import Counter, defaultdict
from math import ceil


def _p95(values: list[int]) -> int:
    """Return the nearest-rank 95th percentile of a non-empty sequence."""
    ordered = sorted(values)
    return ordered[ceil(len(ordered) * 0.95) - 1]


def analyse(pairs: list[tuple[str, int]]) -> dict[str, object]:
    """Summarize request counts, per-route p95 latency, and the slowest route."""
    counts = Counter(route for route, _ in pairs)
    latencies: defaultdict[str, list[int]] = defaultdict(list)
    for route, latency_ms in pairs:
        latencies[route].append(latency_ms)
    p95 = {route: _p95(values) for route, values in latencies.items()}
    slowest = max(p95, key=p95.get) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
