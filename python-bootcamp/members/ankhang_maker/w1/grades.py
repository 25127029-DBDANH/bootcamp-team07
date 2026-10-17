"""W1-1: Grade summary – basic statistics for a list of scores."""


def summary(scores: list[float]) -> dict:
    """Return a dict with min, max, mean, and median of *scores*.

    Mean and median are rounded to 2 decimal places.
    Raises ``ValueError`` if *scores* is empty.
    """
    if not scores:
        raise ValueError("scores must not be empty")

    n = len(scores)

    # Find min and max without using built-in min/max
    lo = scores[0]
    hi = scores[0]
    total = 0.0
    for s in scores:
        lo = min(lo, s)
        hi = max(hi, s)
        total += s

    mean = round(total / n, 2)

    # Sort manually (insertion sort) for median calculation
    sorted_scores = list(scores)
    for i in range(1, n):
        key = sorted_scores[i]
        j = i - 1
        while j >= 0 and sorted_scores[j] > key:
            sorted_scores[j + 1] = sorted_scores[j]
            j -= 1
        sorted_scores[j + 1] = key

    if n % 2 == 1:
        median = round(sorted_scores[n // 2], 2)
    else:
        median = round((sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2, 2)

    return {"min": lo, "max": hi, "mean": mean, "median": median}
