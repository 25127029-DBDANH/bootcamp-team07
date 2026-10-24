"""W3-1: Date parsing – accept various human-friendly date formats."""

from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0, "tue": 1, "wed": 2, "thu": 3,
    "fri": 4, "sat": 5, "sun": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a due-date string relative to *today*.

    Accepted formats
    ----------------
    - ``"YYYY-MM-DD"`` – an ISO date literal.
    - ``"tomorrow"`` – the day after *today*.
    - ``"in N days"`` – *N* days after *today*.
    - A three-letter weekday abbreviation (e.g. ``"Fri"``) – the **next**
      occurrence of that weekday, never *today* itself.

    Parameters
    ----------
    text : str
        The date string to parse.
    today : date
        Reference date for relative calculations.

    Returns
    -------
    date
        The resolved date.

    Raises
    ------
    ValueError
        If *text* does not match any recognised format.
    """
    stripped = text.strip()

    # ISO format: YYYY-MM-DD
    if len(stripped) == 10 and stripped[4] == "-" and stripped[7] == "-":
        try:
            return date.fromisoformat(stripped)
        except ValueError:
            pass

    # "tomorrow"
    if stripped.lower() == "tomorrow":
        return today + timedelta(days=1)

    # "in N days"
    lower = stripped.lower()
    if lower.startswith("in ") and lower.endswith(" days"):
        middle = lower[3:-5].strip()
        try:
            n = int(middle)
            return today + timedelta(days=n)
        except ValueError:
            pass

    # Weekday abbreviation (Mon, Tue, ...)
    weekday_key = stripped[:3].lower()
    if weekday_key in _WEEKDAYS:
        target = _WEEKDAYS[weekday_key]
        current = today.weekday()
        diff = (target - current) % 7
        if diff == 0:
            diff = 7  # next occurrence, not today
        return today + timedelta(days=diff)

    msg = f"unknown date format: {text!r}"
    raise ValueError(msg)
