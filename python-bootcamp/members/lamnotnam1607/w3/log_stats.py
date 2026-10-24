"""Summarise request counts and p95 latency by route."""

from collections import Counter, defaultdict
from math import ceil
from typing import TypedDict


class LogAnalysis(TypedDict):
    """Aggregated chat-log statistics returned by :func:`analyse`."""

    counts: Counter[str]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: list[tuple[str, float]]) -> LogAnalysis:
    """Return request counts, nearest-rank p95 values, and the slowest route."""
    counts: Counter[str] = Counter()
    latencies_by_route: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency_ms)

    p95: dict[str, float] = {}
    for route, latencies in latencies_by_route.items():
        ordered = sorted(latencies)
        rank = ceil(0.95 * len(ordered))
        p95[route] = ordered[rank - 1]

    slowest = max(p95, key=p95.__getitem__) if p95 else None
    return {"counts": counts, "p95": p95, "slowest": slowest}
