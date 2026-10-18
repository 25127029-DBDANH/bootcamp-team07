"""T-W2 (T2): Extended tests for shared/study_planner/prioritise.py.

Written by ankhang-maker.
These tests complement test_prioritise_basic.py with additional edge cases
and scenarios not covered there.
"""

from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

TODAY = date(2026, 10, 20)


def _task(title: str, importance: int, effort_h: float, days: int) -> Task:
    """Helper to create a Task with deadline *days* after TODAY."""
    return Task(title, importance, effort_h, date.fromordinal(TODAY.toordinal() + days))


# ---- 1. Single task list ----

def test_single_task_returns_same():
    """A list with one task should return that task unchanged."""
    t = _task("solo", 3, 2.0, 5)
    result = prioritise([t], TODAY)
    assert result == [t]


# ---- 2. Importance beats distance when score differs ----

def test_high_importance_far_beats_low_importance_near():
    """A very important task far away can still outrank a less important near one."""
    # importance=5, days=5 -> score=1.0
    # importance=1, days=2 -> score=0.5
    far_important = _task("far_important", 5, 3.0, 5)
    near_trivial = _task("near_trivial", 1, 1.0, 2)
    result = prioritise([near_trivial, far_important], TODAY)
    assert result == [far_important, near_trivial]


# ---- 3. Multiple overdue tasks ----

def test_multiple_overdue_tasks_sorted_by_importance():
    """Multiple overdue tasks all get days_left=0 -> score=importance/1.
    Higher importance should come first.
    """
    low_overdue = _task("low_overdue", 2, 1.0, -5)
    high_overdue = _task("high_overdue", 5, 1.0, -2)
    result = prioritise([low_overdue, high_overdue], TODAY)
    assert result == [high_overdue, low_overdue]


# ---- 4. Mix of overdue, today, and future tasks ----

def test_mixed_overdue_today_future():
    """Overdue and today tasks (days_left=0) should be prioritised above future."""
    overdue = _task("overdue", 3, 1.0, -1)    # score=3/1=3
    today_task = _task("today", 3, 1.0, 0)     # score=3/1=3
    future = _task("future", 3, 1.0, 10)       # score=3/10=0.3
    result = prioritise([future, today_task, overdue], TODAY)
    # overdue and today_task have same score, keep original relative order
    # (today_task before overdue since today_task appears first in input after sorting)
    assert result[2] == future
    assert result[0].title in ("today", "overdue")
    assert result[1].title in ("today", "overdue")


# ---- 5. Large list maintains correct ordering ----

def test_large_list_ordering():
    """Verify correct ordering with many tasks of varying priorities."""
    tasks = [
        _task("a", 1, 1.0, 10),   # score=0.1
        _task("b", 5, 2.0, 1),    # score=5.0
        _task("c", 3, 1.0, 3),    # score=1.0
        _task("d", 4, 1.5, 2),    # score=2.0
        _task("e", 2, 0.5, 4),    # score=0.5
    ]
    result = prioritise(tasks, TODAY)
    titles = [t.title for t in result]
    assert titles == ["b", "d", "c", "e", "a"]


# ---- 6. Different effort_h does not affect priority ----

def test_effort_does_not_affect_priority():
    """effort_h should not influence prioritisation order."""
    big_effort = _task("big", 3, 100.0, 5)     # score=3/5=0.6
    small_effort = _task("small", 3, 0.1, 5)   # score=3/5=0.6
    result = prioritise([big_effort, small_effort], TODAY)
    # Same score, stable sort keeps original order
    assert result == [big_effort, small_effort]


# ---- 7. Return type is a new list ----

def test_returns_new_list_object():
    """prioritise() should return a NEW list, not the same object."""
    tasks = [_task("x", 2, 1.0, 3)]
    result = prioritise(tasks, TODAY)
    assert result is not tasks
