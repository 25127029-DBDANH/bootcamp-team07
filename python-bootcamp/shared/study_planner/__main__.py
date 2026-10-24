"""CLI entrypoint for study planner.

Usage:
    python -m shared.study_planner <csv> --hours H [--today YYYY-MM-DD]
"""

import argparse
import sys
from datetime import date

from shared.study_planner.allocate import allocate

# Thêm import InfeasiblePlan và check_feasible từ file errors.py của bạn
from shared.study_planner.errors import InfeasiblePlan, check_feasible
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="study_planner", description="Generate a study plan from tasks CSV.")
    p.add_argument("csv", help="Path to tasks CSV file")
    p.add_argument("--hours", type=float, required=True, help="Total available study hours tonight")
    p.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Reference date in YYYY-MM-DD format (default: today)",
    )
    p.add_argument("--strict", action="store_true", help="Fail if plan is infeasible")
    return p


def main(argv: list[str] | None = None) -> int:
    """Run study planner CLI pipeline."""
    args = build_parser().parse_args(argv)
    today = args.today or date.today()
    
    try:
        tasks = parse_csv(args.csv)
        if not tasks:
            print("error: CSV file is empty", file=sys.stderr)
            return 1
            
        try:
            check_feasible(tasks, args.hours)
        except InfeasiblePlan as e:
            print(f"warning: {e}", file=sys.stderr)
            if args.strict:
                return 1 
        blocks = allocate(prioritise(tasks, today), args.hours)
        print(f"Tonight ({args.hours:.1f} h):")
        output = render(blocks)
        if output:
            print(output)
        return 0
        
    except FileNotFoundError:
        print(f"error: File '{args.csv}' not found", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())