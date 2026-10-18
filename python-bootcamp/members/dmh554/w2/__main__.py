"""Run with: python -m members.dmh554.w2 [csv_path]"""

import sys
from pathlib import Path

from .io_utils import load_tasks


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    path = argv[0] if argv else Path(__file__).parent / "sample_tasks.csv"
    for task in load_tasks(path):
        print(f"{task.title}: importance {task.importance}, "
              f"{task.effort_h:g} h, due {task.deadline}")


if __name__ == "__main__":
    main()
