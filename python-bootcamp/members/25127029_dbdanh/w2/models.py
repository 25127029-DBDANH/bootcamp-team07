from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with an importance level, effort and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject an importance outside 1-5."""
        if not 1 <= self.importance <= 5:
            raise ValueError(f"importance must be 1-5, got {self.importance}")

    def days_left(self, today: date) -> int:
        """Return the days from today to the deadline, never below 0."""
        return max(0, (self.deadline - today).days)
