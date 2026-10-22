"""CLI entrypoint for study planner.

Usage:
    python -m shared.study_planner <csv> --hours H [--today YYYY-MM-DD]
"""

import argparse
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser for study_planner CLI."""
    p = argparse.ArgumentParser(prog="study_planner", description="Generate a study plan from tasks CSV.")
    p.add_argument("csv", help="Path to tasks CSV file")
    p.add_argument("--hours", type=float, required=True, help="Total available study hours tonight")
    p.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Reference date in YYYY-MM-DD format (default: today)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    """Run study planner CLI pipeline."""
    args = build_parser().parse_args(argv)
    today = args.today or date.today()
    tasks = parse_csv(args.csv)
    blocks = allocate(prioritise(tasks, today), args.hours)
    print(f"Tonight ({args.hours:.1f} h):")
    output = render(blocks)
    if output:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
