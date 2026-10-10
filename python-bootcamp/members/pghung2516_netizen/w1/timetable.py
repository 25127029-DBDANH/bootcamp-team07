"""Timetable grouping utilities."""


def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course codes by day of week and sort courses alphabetically."""
    result: dict[str, list[str]] = {}
    for course, day in entries:
        result.setdefault(day, []).append(course)

    for courses in result.values():
        courses.sort()

    return result
