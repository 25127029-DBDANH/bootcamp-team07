"""Prioritise tasks by importance divided by days left."""

from datetime import date

from shared.contract import Task


def _days_left(task: Task, today: date) -> int:
    """Days until the deadline, never below 0."""
    return max(0, (task.deadline - today).days)


def _score(task: Task, today: date) -> float:
    """Priority score = importance / days_left.

    A task due today or overdue has days_left == 0, which would divide by
    zero. We treat it as 1 day left, so it gets the highest score a task of
    that importance can have.
    """
    return task.importance / max(1, _days_left(task, today))


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Return a new list of tasks, highest priority first.

    Tasks with the same score keep their original relative order.
    The input list is not modified.
    """
    return sorted(tasks, key=lambda task: _score(task, today), reverse=True)
