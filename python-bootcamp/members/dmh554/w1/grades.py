from statistics import median


def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("Empty list!")
    
    return {
        "min":    min(scores),
        "max":    max(scores),
        "mean":   round(sum(scores) / len(scores), 2),
        "median": round(median(scores), 2),
    }