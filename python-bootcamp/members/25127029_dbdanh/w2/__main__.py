import sys
from pathlib import Path

from .io_utils import load_tasks

SAMPLE_CSV = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> int:
    """Print the tasks from a CSV file and return an exit code."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else SAMPLE_CSV
    try:
        tasks = load_tasks(path)
    except (OSError, ValueError) as err:
        print(f"Cannot load {path}: {err}")
        return 1
    for task in tasks:
        print(
            f"{task.title} | importance {task.importance} | "
            f"{task.effort_h} h | due {task.deadline}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
