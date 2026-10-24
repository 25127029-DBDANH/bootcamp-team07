"""W3-2: Chat log analysis – request counts and p95 latency per route."""

from collections import Counter


def analyse(pairs: list[tuple[str, int]]) -> dict:
    """Analyse a list of ``(route, latency_ms)`` pairs.

    Returns
    -------
    dict
        ``"counts"`` – requests per route (``Counter``).
        ``"p95"`` – 95th-percentile latency per route.
        ``"slowest"`` – the route with the highest p95.
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[int]] = {}

    for route, latency in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency)

    p95: dict[str, int] = {}
    for route, times in latencies.items():
        times.sort()
        idx = int(len(times) * 0.95)
        # Clamp index to last element
        idx = min(idx, len(times) - 1)
        p95[route] = times[idx]

    slowest = max(p95, key=lambda r: p95[r]) if p95 else ""

    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
