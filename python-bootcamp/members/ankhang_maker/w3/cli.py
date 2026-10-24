"""W3-3: Command-line study planner.

Usage::

    python -m members.ankhang_maker.w3.cli tasks.csv --hours 2 --today 2026-10-26
"""

import argparse
import sys
from datetime import date
from pathlib import Path

from members.ankhang_maker.w2.io_utils import load_tasks
from members.ankhang_maker.w2.models import Task


def _days_left(task: Task, today: date) -> int:
    """Days until the deadline, never below 0."""
    return max(0, (task.deadline - today).days)


def _priority_score(task: Task, today: date) -> float:
    """Priority score: importance / days_left (min 1 to avoid division by zero)."""
    return task.importance / max(1, _days_left(task, today))


def _prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Sort tasks by priority score, highest first."""
    return sorted(tasks, key=lambda t: _priority_score(t, today), reverse=True)


def _allocate(tasks: list[Task], hours: float) -> list[tuple[Task, float]]:
    """Greedily allocate *hours* across *tasks* in order."""
    result: list[tuple[Task, float]] = []
    remaining = hours
    for task in tasks:
        if remaining <= 0:
            break
        h = min(task.effort_h, remaining)
        result.append((task, h))
        remaining -= h
    return result


def main(argv: list[str] | None = None) -> int:
    """Run the CLI study planner."""
    parser = argparse.ArgumentParser(
        prog="study_planner",
        description="Generate a nightly study plan from a CSV of tasks.",
    )
    parser.add_argument("csv", help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Reference date YYYY-MM-DD (default: today)",
    )
    args = parser.parse_args(argv)

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"error: file not found: {csv_path}", file=sys.stderr)
        return 1

    today = args.today or date.today()

    try:
        tasks = load_tasks(csv_path)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    ordered = _prioritise(tasks, today)
    blocks = _allocate(ordered, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    for i, (task, h) in enumerate(blocks, start=1):
        hours_str = f"{h:g}"
        print(f"  {i}. {task.title} {'.' * (14 - len(task.title))} {hours_str} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
