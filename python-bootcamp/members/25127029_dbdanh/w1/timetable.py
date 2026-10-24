def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort course list."""
    result: dict[str, list[str]] = {}
    for course, day in pairs:
        result.setdefault(day, []).append(course)
    for courses in result.values():
        courses.sort()
    return result
