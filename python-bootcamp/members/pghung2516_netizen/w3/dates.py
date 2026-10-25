"""Date parsing utilities for bootcamp week 3 (W3-1)."""

import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tues": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thur": 3,
    "thurs": 3,
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

    Supported patterns:
    - ISO format: "YYYY-MM-DD" (e.g. "2026-10-30")
    - Relative day keywords: "today", "tomorrow"
    - Relative duration: "in N days" or "in N day"
    - Weekdays: "Mon", "Tue", "Wednesday", etc. (always the next occurrence, never today)

    Raises:
        ValueError: If text cannot be parsed into a valid due date.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Due date string cannot be empty")

    # 1. Try ISO date (YYYY-MM-DD)
    try:
        return date.fromisoformat(cleaned)
    except ValueError:
        pass

    normalized = cleaned.lower()

    # 2. Keywords
    if normalized == "today":
        return today
    if normalized == "tomorrow":
        return today + timedelta(days=1)

    # 3. Relative "in N days" / "in N day"
    match = re.fullmatch(r"in\s+(\d+)\s+days?", normalized)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Weekday names (next occurrence, strictly in the future)
    if normalized in _WEEKDAYS:
        target_weekday = _WEEKDAYS[normalized]
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date format: {text!r}")
