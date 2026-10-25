"""Data model used by the Week 3 command-line planner."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Task:
    """Represent one study task loaded from a CSV row."""

    title: str
    importance: int
    effort_h: float
    deadline: date
