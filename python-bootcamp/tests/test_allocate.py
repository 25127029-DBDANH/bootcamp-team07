from datetime import date

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def make_task(title: str, effort_h: float) -> Task:
    return Task(title, 3, effort_h, date(2026, 10, 30))


def test_empty_tasks_returns_no_blocks():
    assert allocate([], 5) == []


def test_zero_hours_returns_no_blocks():
    tasks = [make_task("a", 2)]

    assert allocate(tasks, 0) == []


def test_hours_below_first_task_effort_partially_allocates_first_task():
    first = make_task("a", 3)
    second = make_task("b", 2)

    blocks = allocate([first, second], 1)

    assert blocks == [Block(first, 1)]


def test_hours_above_total_effort_allocates_all_tasks():
    first = make_task("a", 2)
    second = make_task("b", 1)

    blocks = allocate([first, second], 10)

    assert blocks == [Block(first, 2), Block(second, 1)]
    assert sum(block.hours for block in blocks) == 3
    assert sum(block.hours for block in blocks) <= 10


def test_greedy_allocation_fills_first_then_partially_fills_next_in_order():
    first = make_task("a", 2)
    second = make_task("b", 3)
    third = make_task("c", 4)

    blocks = allocate([first, second, third], 3.5)

    assert blocks == [Block(first, 2), Block(second, 1.5)]
    assert sum(block.hours for block in blocks) == 3.5
    assert all(block.hours >= 0 for block in blocks)
