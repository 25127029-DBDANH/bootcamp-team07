"""Task data model for Week 2."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a task with title, importance, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate fields after initialization."""
        if isinstance(self.deadline, str):
            self.deadline = date.fromisoformat(self.deadline)

        if not (1 <= self.importance <= 5):
            raise ValueError(f"importance must be between 1 and 5, got {self.importance}")

        if self.effort_h < 0:
            raise ValueError(f"effort_h must be non-negative, got {self.effort_h}")

    def days_left(self, today: date | None = None) -> int:
        """Calculate the number of days left until deadline.

        Returns 0 if the deadline has passed.
        """
        if today is None:
            today = date.today()
        elif isinstance(today, str):
            today = date.fromisoformat(today)

        delta = (self.deadline - today).days
        return max(0, delta)
