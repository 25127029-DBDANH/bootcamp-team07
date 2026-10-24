def word_count(text: str) -> dict[str, int]:
    """Count words in text ignoring punctuation."""
    text = text.lower()
    for p in [".", ",", "!", "?", ";", ":"]:
        text = text.replace(p, " ")
    words = text.split()
    ket_qua: dict[str, int] = {}
    for i in words:
        if i in ket_qua:
            ket_qua[i] = ket_qua[i] + 1
        else:
            ket_qua[i] = 1
    return ket_qua


def get_count(pair: tuple[str, int]) -> int:
    """Return frequency count of word tuple."""
    return pair[1]


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k most frequent words sorted by count, then alphabetically."""
    if k <= 0:
        return []
    pairs = list(word_count(text).items())
    pairs.sort()
    pairs.sort(key=get_count, reverse=True)
    return pairs[:k]
