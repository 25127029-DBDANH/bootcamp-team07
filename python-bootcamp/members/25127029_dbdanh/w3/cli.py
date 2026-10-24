import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

from ..w2.io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    """Build parser for the study planner command-line tool."""
    parser = argparse.ArgumentParser(prog="study-planner")
    parser.add_argument("csv", help="path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="available study hours")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="reference date (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run CLI study planner workflow."""
    args = build_parser().parse_args(argv)
    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"error: file not found: {csv_path}", file=sys.stderr)
        return 1

    today = args.today or date.today()
    try:
        tasks = load_tasks(csv_path)
    except (OSError, ValueError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 1

    blocks = allocate(prioritise(tasks, today), args.hours)
    print(f"Tonight ({args.hours:.1f} h):")
    plan = render(blocks)
    if plan:
        print(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
