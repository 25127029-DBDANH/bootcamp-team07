import csv
from datetime import date
from pathlib import Path

from shared.contract import Task

REQUIRED_COLUMNS = ("title", "importance", "effort_h", "deadline")


def parse_csv(path: str | Path) -> list[Task]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"missing column(s): {', '.join(missing)}")

        tasks: list[Task] = []
        for row in reader:
            line_no = reader.line_num
            try:
                tasks.append(_parse_row(row))
            except (TypeError, ValueError) as err:
                raise ValueError(f"line {line_no}: {err}") from err
    return tasks


def _parse_row(row: dict[str, str]) -> Task:
    if any(row[c] is None for c in REQUIRED_COLUMNS):
        raise ValueError("row has too few columns")

    title = row["title"].strip()
    if not title:
        raise ValueError("title is empty")

    importance = int(row["importance"])
    if not 1 <= importance <= 5:
        raise ValueError(f"importance must be 1-5, got {importance}")

    effort_h = float(row["effort_h"])
    if effort_h < 0:
        raise ValueError(f"effort_h must not be negative, got {effort_h}")

    deadline = date.fromisoformat(row["deadline"])
    return Task(title, importance, effort_h, deadline)
