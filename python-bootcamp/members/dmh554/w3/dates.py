"""W3-1: Parse human-friendly due-date strings into concrete date objects.

Supported formats:
- ``"YYYY-MM-DD"``       — ISO date literal, e.g. "2026-10-30"
- ``"tomorrow"``         — the day after today
- ``"in N days"``        — N days from today (e.g. "in 3 days")
- Weekday abbreviation  — "Mon" / "Tue" / "Wed" / "Thu" / "Fri" / "Sat" / "Sun"
                          resolves to the *next* occurrence, never today itself
"""

from datetime import date, timedelta

# Map lowercase 3-letter weekday abbreviation → Python weekday number (Mon=0)
_WEEKDAY_MAP: dict[str, int] = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse *text* as a due-date relative to *today*.

    Parameters
    ----------
    text:
        A human-readable date string (see module docstring for formats).
    today:
        The reference date used for relative expressions.

    Returns
    -------
    date
        The resolved calendar date.

    Raises
    ------
    ValueError
        If *text* does not match any recognised format.

    Examples
    --------
    >>> from datetime import date
    >>> today = date(2026, 10, 6)  # Tuesday
    >>> parse_due("2026-10-30", today)
    datetime.date(2026, 10, 30)
    >>> parse_due("tomorrow", today)
    datetime.date(2026, 10, 7)
    >>> parse_due("in 3 days", today)
    datetime.date(2026, 10, 9)
    >>> parse_due("Fri", today)
    datetime.date(2026, 10, 9)
    >>> parse_due("Tue", today)   # next Tuesday, not today
    datetime.date(2026, 10, 13)
    """
    stripped = text.strip()
    lower = stripped.lower()

    # 1. ISO date: YYYY-MM-DD
    try:
        return date.fromisoformat(stripped)
    except ValueError:
        pass

    # 2. "tomorrow"
    if lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. "in N days"
    if lower.startswith("in ") and lower.endswith((" days", " day")):
        parts = lower.split()
        # expected tokens: ["in", "<number>", "days"] or ["in", "<number>", "day"]
        if len(parts) == 3:
            try:
                n = int(parts[1])
                return today + timedelta(days=n)
            except ValueError:
                pass

    # 4. Weekday abbreviation (case-insensitive, first 3 chars)
    abbr = lower[:3]
    if abbr in _WEEKDAY_MAP:
        target_wd = _WEEKDAY_MAP[abbr]
        delta = (target_wd - today.weekday()) % 7
        # Never return today — always the *next* occurrence
        if delta == 0:
            delta = 7
        return today + timedelta(days=delta)

    raise ValueError(f"unrecognised due-date format: {text!r}")
