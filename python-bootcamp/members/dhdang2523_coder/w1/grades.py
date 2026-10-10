def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("List cannot be empty")
    
    n = len(scores)
    scores_sorted = sorted(scores)
    
    min_val = scores_sorted[0]
    max_val = scores_sorted[-1]
    mean_val = round(sum(scores) / n, 2)
    
    if n % 2 == 0:
        median_val = (scores_sorted[n//2 - 1] + scores_sorted[n//2]) / 2
    else:
        median_val = scores_sorted[n//2]
        
    median_val = round(median_val, 2)
    
    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
    }