"""Load and display the sample tasks when this package is run as a module."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load the bootcamp sample CSV and print its tasks."""
    bootcamp_dir = Path(__file__).resolve().parents[3]
    sample_path = bootcamp_dir / "samples" / "tasks.csv"
    tasks = load_tasks(sample_path)

    for task in tasks:
        print(
            f"{task.title} - importance {task.importance}, "
            f"{task.effort_h:g} h, deadline {task.deadline}"
        )


if __name__ == "__main__":
    main()
