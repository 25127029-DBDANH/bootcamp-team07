"""CSV input helpers for the Week 3 planner."""

import csv
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from a CSV file and report malformed rows by line number."""
    tasks: list[Task] = []
    with Path(path).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
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
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(f"line {line_no}: {error}") from error
    return tasks
