"""Date parsing utilities for bootcamp week 3."""

import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse human-readable due date expressions into a concrete date object.

    Accepted formats:
    - ISO format: "YYYY-MM-DD" (e.g., "2026-10-30")
    - Relative words: "tomorrow", "today"
    - Relative duration: "in N days" (e.g., "in 3 days")
    - Weekdays: "Fri", "Tuesday", etc. (next occurrence, not today)

    Raises:
        ValueError: If text does not match any recognized due date pattern.
    """
    normalized = text.strip()
    if not normalized:
        raise ValueError("Due date string cannot be empty")

    # 1. Try ISO date (YYYY-MM-DD)
    try:
        return date.fromisoformat(normalized)
    except ValueError:
        pass

    lower = normalized.lower()

    # 2. Keywords
    if lower == "tomorrow":
        return today + timedelta(days=1)
    if lower == "today":
        return today

    # 3. Relative "in N days" / "in N day"
    match = re.fullmatch(r"in\s+(\d+)\s+days?", lower)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Weekday names (next occurrence, strictly in the future)
    if lower in _WEEKDAYS:
        target_weekday = _WEEKDAYS[lower]
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date format: {text!r}")
