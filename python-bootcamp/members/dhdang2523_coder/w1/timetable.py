def by_day(courses: list[tuple[str, str]]) -> dict:
    result = {}
    for course, day in courses:
        result.setdefault(day, []).append(course)
        
    for courses_list in result.values():
        courses_list.sort()
        
    return result