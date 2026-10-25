"""Date parsing utilities for study tasks."""

from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Convert a supported due-date expression into a calendar date."""
    value = text.strip()
    if value == "tomorrow":
        return today + timedelta(days=1)
    if value.startswith("in ") and value.endswith(" days"):
        count = value[3:-5]
        if count.isdigit():
            return today + timedelta(days=int(count))
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass
    weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    if value in weekdays:
        target = weekdays.index(value)
        offset = (target - today.weekday()) % 7 or 7
        return today + timedelta(days=offset)
    raise ValueError(f"unsupported due date: {text}")
