"""Grade calculation utilities."""


def summary(scores: list[float]) -> dict[str, float]:
    """Calculate min, max, mean, and median from a list of scores."""
    if not scores:
        raise ValueError("Score list cannot be empty.")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    min_val = sorted_scores[0]
    max_val = sorted_scores[-1]
    mean_val = round(sum(sorted_scores) / n, 2)

    if n % 2 == 1:
        median_val = sorted_scores[n // 2]
    else:
        median_val = round((sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2, 2)

    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val,
    }
