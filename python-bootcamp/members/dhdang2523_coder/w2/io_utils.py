import csv
import json
from datetime import date
from pathlib import Path
from typing import Iterable

from .models import Task

EXPECTED_HEADER = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file. Raise ValueError with line number on invalid rows."""
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            header = [col.strip() for col in next(reader)]
        except StopIteration as exc:
            raise ValueError("Line 1: empty CSV file") from exc

        if header != EXPECTED_HEADER:
            raise ValueError(f"Line 1: invalid header {header}")

        for line_no, row in enumerate(reader, start=2):
            if len(row) != 4:
                raise ValueError(
                    f"Line {line_no}: expected 4 columns, got {len(row)}"
                )
            raw_title, raw_imp, raw_effort, raw_deadline = [
                cell.strip() for cell in row
            ]
            if not raw_title:
                raise ValueError(f"Line {line_no}: title cannot be empty")
            try:
                importance = int(raw_imp)
                effort_h = float(raw_effort)
                if effort_h <= 0:
                    raise ValueError("effort_h must be positive")
                deadline = date.fromisoformat(raw_deadline)
                task = Task(
                    title=raw_title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            except ValueError as exc:
                raise ValueError(f"Line {line_no}: {exc}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: Iterable[Task], path: str | Path) -> None:
    """Save a collection of Task objects to a JSON file."""
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)