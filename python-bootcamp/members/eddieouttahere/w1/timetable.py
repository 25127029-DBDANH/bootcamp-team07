def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for course, day in entries:
        grouped.setdefault(day, []).append(course)
    for courses in grouped.values():
        courses.sort()
    return grouped
