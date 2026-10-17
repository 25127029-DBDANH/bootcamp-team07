"""Run ``python -m members.ankhang_maker.w2`` to load and print sample tasks."""

from pathlib import Path

from members.ankhang_maker.w2.io_utils import load_tasks


def main() -> None:
    """Load the sample CSV and print each task."""
    samples_dir = Path(__file__).resolve().parents[3] / "samples"
    csv_path = samples_dir / "tasks.csv"

    if not csv_path.exists():
        print(f"Error: sample file not found at {csv_path}")
        return

    tasks = load_tasks(csv_path)
    print(f"Loaded {len(tasks)} task(s) from {csv_path.name}:\n")
    for i, task in enumerate(tasks, start=1):
        print(
            f"  {i}. {task.title:<20s} "
            f"importance={task.importance}  "
            f"effort={task.effort_h}h  "
            f"deadline={task.deadline}"
        )


if __name__ == "__main__":
    main()
