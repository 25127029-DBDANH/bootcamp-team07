"""Load tasks from CSV and save them as JSON."""

import csv
import json
from dataclasses import asdict
from datetime import date

try:
    from .models import Task
except ImportError:  # imported as a top-level module (e.g. by the test runner)
    from models import Task

COLUMNS = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path) -> list[Task]:
    """Read a CSV with header title,importance,effort_h,deadline.

    An invalid row raises ValueError that mentions the line number.
    """
    tasks = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"line 1: header must be {','.join(COLUMNS)}")
        for line_no, row in enumerate(reader, start=2):  # line 1 is the header
            try:
                title = (row["title"] or "").strip()
                if not title:
                    raise ValueError("title is empty")
                tasks.append(
                    Task(
                        title=title,
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except (ValueError, TypeError) as err:
                raise ValueError(f"line {line_no}: {err}") from err
    return tasks


def save_json(tasks: list[Task], path) -> None:
    """Write tasks to a JSON file (dates are saved as YYYY-MM-DD)."""
    data = []
    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
