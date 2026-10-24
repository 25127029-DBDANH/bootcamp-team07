import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, int | float]]) -> dict:
    counts: Counter[str] = Counter()
    by_route: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        by_route[route].append(latency)

    p95: dict[str, float] = {}
    for route, latencies in by_route.items():
        sorted_latencies = sorted(latencies)
        idx = math.ceil(0.95 * len(sorted_latencies)) - 1
        p95[route] = sorted_latencies[idx]

    slowest = max(p95, key=lambda k: p95[k]) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
