"""Text processing and word count utilities."""


def word_count(text: str) -> dict[str, int]:
    """Count word frequencies in text ignoring punctuation and case."""
    cleaned = ""
    for ch in text.lower():
        if ch in ".,!?;:":
            cleaned += " "
        else:
            cleaned += ch

    words = cleaned.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k frequent words, sorted by frequency (desc) then alphabetically."""
    if not text or k <= 0:
        return []

    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]
