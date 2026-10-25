"""Command-line study planner tool for bootcamp week 3 (W3-3)."""

import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

from ..w2.io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    """Build and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="study-planner",
        description="Plan study hours tonight from a tasks CSV file.",
    )
    parser.add_argument(
        "csv",
        type=str,
        help="Path to tasks CSV file",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Total study hours available tonight",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="Reference date for priority calculation (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, compute allocated blocks, and render the study plan."""
    args = build_parser().parse_args(argv)

    csv_path = Path(args.csv)
    if not csv_path.exists() or not csv_path.is_file():
        print(f"Error: Tasks file not found: {csv_path}", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(csv_path)
    except (OSError, ValueError) as exc:
        print(f"Error loading tasks from {csv_path}: {exc}", file=sys.stderr)
        return 1

    today = args.today or date.today()
    prioritised_tasks = prioritise(tasks, today)
    blocks = allocate(prioritised_tasks, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    plan = render(blocks)
    if plan:
        print(plan)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
