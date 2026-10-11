import re


def word_count(text: str) -> dict[str, int]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
