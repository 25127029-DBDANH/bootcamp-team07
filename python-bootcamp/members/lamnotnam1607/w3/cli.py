"""Command-line study planner for the individual Week 3 exercise."""

import argparse
import sys
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

from ..w2.io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    """Build the parser for the study-planner command."""
    parser = argparse.ArgumentParser(prog="study-planner")
    parser.add_argument("csv", help="path to the task CSV file")
    parser.add_argument("--hours", type=float, required=True, help="available study time")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="reference date used for prioritisation (defaults to today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Load tasks, plan study time, and return a process exit code."""
    args = build_parser().parse_args(argv)
    today = args.today or date.today()

    try:
        tasks = load_tasks(args.csv)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    blocks = allocate(prioritise(tasks, today), args.hours)
    print(f"Tonight ({args.hours:.1f} h):")
    plan = render(blocks)
    if plan:
        print(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
