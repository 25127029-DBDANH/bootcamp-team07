from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

TODAY = date(2026, 10, 20)


def make_task(title: str, importance: int, days: int) -> Task:
    return Task(title, importance, 2.0, date.fromordinal(TODAY.toordinal() + days))


def test_empty_list():
    assert prioritise([], TODAY) == []


def test_nearer_deadline_first_when_same_importance():
    far = make_task("far", 3, 10)
    near = make_task("near", 3, 2)
    assert prioritise([far, near], TODAY) == [near, far]


def test_higher_importance_first_when_same_deadline():
    low = make_task("low", 2, 5)
    high = make_task("high", 5, 5)
    assert prioritise([low, high], TODAY) == [high, low]


def test_due_today_does_not_divide_by_zero():
    today_task = make_task("today", 4, 0)
    later = make_task("later", 4, 4)
    assert prioritise([later, today_task], TODAY) == [today_task, later]


def test_overdue_task_is_handled():
    overdue = make_task("overdue", 5, -3)
    later = make_task("later", 5, 3)
    assert prioritise([later, overdue], TODAY) == [overdue, later]


def test_equal_scores_keep_original_order():
    a = make_task("a", 4, 4)
    b = make_task("b", 4, 4)
    assert prioritise([a, b], TODAY) == [a, b]
    assert prioritise([b, a], TODAY) == [b, a]


def test_input_list_is_not_modified():
    tasks = [make_task("far", 3, 10), make_task("near", 3, 2)]
    original = list(tasks)
    prioritise(tasks, TODAY)
    assert tasks == original
