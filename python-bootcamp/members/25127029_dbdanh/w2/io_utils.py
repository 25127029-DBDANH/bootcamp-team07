import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read a CSV with header title,importance,effort_h,deadline into Tasks.

    Raise ValueError naming the line number of the first invalid row.
    """
    tasks: list[Task] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Line 1 is the header, so the first data row is line 2.
        for line_no, row in enumerate(reader, start=2):
            try:
                tasks.append(
                    Task(
                        title=row["title"],
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except (KeyError, TypeError, ValueError) as err:
                raise ValueError(f"line {line_no}: invalid row ({err})") from err
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Write the tasks to a JSON file, with the deadline as YYYY-MM-DD."""
    data = [{**asdict(t), "deadline": t.deadline.isoformat()} for t in tasks]
    Path(path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
