def word_count(text: str) -> dict[str, int]:
    for p in ".,!?;:":
        text = text.replace(p, "")
        
    words = text.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
        
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    # Sắp xếp theo số lượng đếm (giảm dần), sau đó theo từ (tăng dần)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]