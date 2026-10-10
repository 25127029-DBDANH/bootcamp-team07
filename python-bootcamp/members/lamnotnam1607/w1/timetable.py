def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for course, day in entries:
        if day not in result:
            result[day] = []
        result[day].append(course)
    for courses in result.values():
        courses.sort()
    return result