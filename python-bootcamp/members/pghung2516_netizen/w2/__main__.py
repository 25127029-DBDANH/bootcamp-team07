"""Entrypoint for running python -m members.pghung2516_netizen.w2."""

import argparse
import sys
from datetime import date
from pathlib import Path

from .errors import InfeasiblePlan, check_feasible
from .io_utils import load_tasks, save_json


def main(argv: list[str] | None = None) -> int:
    """Run CLI to inspect and plan tasks."""
    parser = argparse.ArgumentParser(
        description="Inspect tasks from CSV, check plan feasibility, and optionally export to JSON."
    )
    # Default sample path relative to python-bootcamp
    default_sample = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    parser.add_argument(
        "csv_path",
        nargs="?",
        default=str(default_sample),
        help=f"Path to tasks CSV file (default: {default_sample})",
    )
    parser.add_argument(
        "--available-hours",
        type=float,
        default=10.0,
        help="Total available hours to check feasibility (default: 10.0)",
    )
    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Optional output path to export tasks to JSON",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date for days_left calculation (YYYY-MM-DD, default: today)",
    )

    args = parser.parse_args(argv)
    csv_file = Path(args.csv_path)

    if not csv_file.exists():
        print(f"Error: File not found: {csv_file}", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(csv_file)
    except (ValueError, OSError) as e:
        print(f"Error loading tasks: {e}", file=sys.stderr)
        return 1

    ref_date = date.fromisoformat(args.today) if args.today else date.today()
    total_effort = sum(t.effort_h for t in tasks)

    print(f"Loaded {len(tasks)} tasks from {csv_file.name}:")
    for t in tasks:
        days = t.days_left(ref_date)
        print(
            f" - [{t.importance}/5] {t.title}: {t.effort_h}h (deadline: {t.deadline}, {days} days left)"
        )

    print(f"\nTotal effort needed: {total_effort}h | Available hours: {args.available_hours}h")

    try:
        check_feasible(tasks, args.available_hours)
        print("Status: Feasible plan! You have enough time.")
    except InfeasiblePlan as exc:
        print(f"Status: Infeasible! {exc}", file=sys.stderr)

    if args.out:
        out_path = Path(args.out)
        save_json(tasks, out_path)
        print(f"Saved tasks to {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
