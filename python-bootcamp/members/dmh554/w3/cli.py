"""W3-3: Personal study-planner CLI for dmh554.

Wraps the shared pipeline (parse_csv → prioritise → allocate → render) with
error handling for missing files and malformed CSV data.

Usage::

    python -m members.dmh554.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
"""

import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="study_planner",
        description="Generate a nightly study plan from a CSV of tasks.",
    )
    parser.add_argument("csv", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        metavar="H",
        help="Total available study hours tonight",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="Reference date for priority scoring (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the W3-3 personal CLI.

    Returns 0 on success, 1 on any error.
    """
    args = _build_parser().parse_args(argv)
    csv_path = Path(args.csv)

    # Guard: file must exist before we attempt to open it
    if not csv_path.exists():
        print(f"error: file not found: {csv_path}", file=sys.stderr)
        return 1

    today = args.today or date.today()

    try:
        tasks = parse_csv(csv_path)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not tasks:
        print("error: no tasks found in CSV", file=sys.stderr)
        return 1

    blocks = allocate(prioritise(tasks, today), args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    output = render(blocks)
    if output:
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
