from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Any

def analyse(pairs: List[Tuple[str, float]]) -> Dict[str, Any]:
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    counts = Counter()
    latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)

    p95_stats = {}
    slowest_route = None
    max_p95 = -1

    for route, lats in latencies.items():
        lats.sort()
        idx = int(len(lats) * 0.95)
        if idx == len(lats):
             idx = len(lats) -1
             
        p95_val = lats[idx]
        p95_stats[route] = p95_val

        if p95_val > max_p95:
            max_p95 = p95_val
            slowest_route = route

    return {
        "counts": counts,
        "p95": p95_stats,
        "slowest": slowest_route
    }