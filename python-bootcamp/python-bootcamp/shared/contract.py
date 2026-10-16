from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """One thing to study or finish."""

    title: str
    importance: int
    effort_h: float 
    deadline: date


@dataclass
class Block:
    """Hours of study planned for one task."""

    task: Task
    hours: float