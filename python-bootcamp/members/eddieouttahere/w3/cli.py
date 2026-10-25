"""Command-line study planner for the Week 3 exercise."""

import argparse
import sys
from datetime import date
from pathlib import Path

from .io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(prog="study_planner")
    parser.add_argument("csv", type=Path)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    return parser


def plan_lines(csv_path: Path, hours: float, today: date) -> list[str]:
    """Load tasks and allocate the available hours to the earliest deadlines."""
    tasks = sorted(
        load_tasks(csv_path),
        key=lambda task: ((task.deadline - today).days, -task.importance, task.title),
    )
    remaining = hours
    lines: list[str] = []
    for task in tasks:
        if remaining <= 0:
            break
        allocated = min(task.effort_h, remaining)
        lines.append(f"{len(lines) + 1}. {task.title} - {allocated:g} h")
        remaining -= allocated
    return lines


def main(argv: list[str] | None = None) -> int:
    """Run the planner and return a conventional process exit code."""
    args = build_parser().parse_args(argv)
    try:
        lines = plan_lines(args.csv, args.hours, args.today or date.today())
    except (FileNotFoundError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Tonight ({args.hours:.1f} h):")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
