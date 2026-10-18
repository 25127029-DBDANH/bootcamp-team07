from datetime import date

from shared.contract import Task
from shared.study_planner.allocate import allocate


def mk(title, effort_h):
    return Task(title, 3, effort_h, date(2026, 10, 30))


def test_empty_tasks():
    assert allocate([], 5) == []


def test_zero_hours():
    tasks = [mk("a", 2)]
    assert allocate(tasks, 0) == []


def test_hours_less_than_first_task():
    tasks = [mk("a", 3), mk("b", 2)]
    blocks = allocate(tasks, 1)
    assert len(blocks) == 1
    assert blocks[0].hours == 1


def test_hours_more_than_total_effort():
    tasks = [mk("a", 2), mk("b", 1)]
    blocks = allocate(tasks, 10)
    assert len(blocks) == 2
    assert blocks[0].hours == 2
    assert blocks[1].hours == 1


def test_order_is_preserved():
    tasks = [mk("a", 1), mk("b", 1)]
    blocks = allocate(tasks, 2)
    assert [b.task.title for b in blocks] == ["a", "b"]
