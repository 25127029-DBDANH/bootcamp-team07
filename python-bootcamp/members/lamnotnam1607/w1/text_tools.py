def word_count(text: str) -> dict[str, int]:
    """Count case-insensitive words after trimming common punctuation."""
    text = text.lower()
    words = text.split()

    cleaned: list[str] = []
    for word in words:
        word = word.strip(".,;:?!")
        if word != "":
            cleaned.append(word)

    counts: dict[str, int] = {}
    for word in cleaned:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return up to ``k`` words ordered by count, then alphabetically."""
    counts = word_count(text)
    items = list(counts.items())
    sorted_items = sorted(items, key=lambda item: (-item[1], item[0]))

    return sorted_items[:k]
