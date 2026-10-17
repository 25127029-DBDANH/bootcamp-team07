"""W1-2: Word counter – frequency analysis of words in a text."""


def word_count(text: str) -> dict[str, int]:
    """Return a dict mapping each word (lower-case) to its frequency.

    Punctuation characters ``.,!?;:`` are stripped before counting.
    """
    counts: dict[str, int] = {}
    cleaned = text.lower()
    for ch in ".,!?;:":
        cleaned = cleaned.replace(ch, "")

    for word in cleaned.split():
        if word:
            counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the *k* most frequent words as ``(word, count)`` tuples.

    Sorted by count (descending), then alphabetically (ascending).
    """
    counts = word_count(text)
    if not counts:
        return []

    # Build list of (word, count) pairs
    items = [(w, c) for w, c in counts.items()]

    # Insertion sort by (-count, word) to avoid using sorted()
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and (-items[j][1], items[j][0]) > (-key[1], key[0]):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

    return items[:k]
