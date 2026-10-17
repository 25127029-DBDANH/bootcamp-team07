"""W2-2: Load and save – CSV reader and JSON writer for Task objects."""

import csv
import json
from datetime import date
from pathlib import Path

from members.ankhang_maker.w2.models import Task


def load_tasks(path: Path | str) -> list[Task]:
    """Read tasks from a CSV file with header ``title,importance,effort_h,deadline``.

    Parameters
    ----------
    path : Path or str
        Path to the CSV file.

    Returns
    -------
    list[Task]
        Parsed task objects.

    Raises
    ------
    ValueError
        If a row has invalid data, with the 1-based line number.
    """
    tasks: list[Task] = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # line 1 is header
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (KeyError, ValueError, TypeError) as exc:
                msg = f"line {i}: {exc}"
                raise ValueError(msg) from exc
            tasks.append(task)
    return tasks


def save_json(tasks: list[Task], path: Path | str) -> None:
    """Write tasks to a JSON file.

    Each task is serialised as a dict with ``deadline`` as an ISO string.

    Parameters
    ----------
    tasks : list[Task]
        Task objects to serialise.
    path : Path or str
        Output file path.
    """
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
