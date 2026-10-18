from pathlib import Path

from .io_utils import load_tasks


def main():
    bootcamp_dir = Path(__file__).resolve().parents[3]
    sample = bootcamp_dir / "samples" / "tasks.csv"
    tasks = load_tasks(sample)
    for t in tasks:
        print(f"{t.title} - importance {t.importance}, {t.effort_h}h, due {t.deadline}")


if __name__ == "__main__":
    main()
