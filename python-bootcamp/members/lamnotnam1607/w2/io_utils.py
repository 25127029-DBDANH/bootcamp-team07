import csv
from datetime import date
from .models import Task

def load_tasks(path):
    tasks = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(f"Invalid row at line {line_number}") from error

            tasks.append(task)

    return tasks
import csv
import json
from datetime import date
from pathlib import Path

from members.lamnotnam1607.w2.models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file with a header row."""
    tasks = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid row at line {line_number}: {error}"
                ) from error

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks as a readable JSON array."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
