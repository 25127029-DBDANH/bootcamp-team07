"""W1-5: Group the timetable – organize courses by day."""


def by_day(
    schedule: list[tuple[str, str]],
) -> dict[str, list[str]]:
    """Return a dict mapping each day to a **sorted** list of course codes.

    Parameters
    ----------
    schedule : list of (course, day) tuples

    Examples
    --------
    >>> by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")])
    {'Mon': ['CSC10001', 'CSC10014'], 'Tue': ['MTH00003']}
    """
    result: dict[str, list[str]] = {}
    for course, day in schedule:
        result.setdefault(day, []).append(course)

    # Sort each day's course list manually (insertion sort)
    for day, courses in result.items():
        for i in range(1, len(courses)):
            key = courses[i]
            j = i - 1
            while j >= 0 and courses[j] > key:
                courses[j + 1] = courses[j]
                j -= 1
            courses[j + 1] = key

    return result
