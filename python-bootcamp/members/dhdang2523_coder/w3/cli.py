import argparse
import sys
from datetime import date

from members.dhdang2523_coder.w2.io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="study_planner_cli")
    parser.add_argument("csv")
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    return parser

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    today = args.today or date.today()
    try:
        tasks = load_tasks(args.csv)
        print(f"Tonight ({args.hours:.1f} h):")
        allocated_hours = 0
        for i, task in enumerate(tasks, 1):
             if allocated_hours + task.effort_h <= args.hours:
                  print(f"{i}. {task.title} - {task.effort_h} h")
                  allocated_hours += task.effort_h
             else:
                  remaining = args.hours - allocated_hours
                  if remaining > 0:
                       print(f"{i}. {task.title} - {remaining:.1f} h")
                  break
        return 0
    except FileNotFoundError:
        print(f"error: File '{args.csv}' not found", file=sys.stderr)
        return 1
    except ValueError as e:
         print(f"error: {e}", file=sys.stderr)
         return 1

if __name__ == "__main__":
    sys.exit(main())