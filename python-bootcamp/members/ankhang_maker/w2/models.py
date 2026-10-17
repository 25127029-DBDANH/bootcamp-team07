"""W2-1: Task model – a dataclass for study tasks with deadline tracking."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with importance, effort estimate, and deadline.

    Attributes
    ----------
    title : str
        Short description of the task.
    importance : int
        Priority level from 1 (low) to 5 (high).
    effort_h : float
        Estimated effort in hours.
    deadline : date
        Due date for the task.
    """

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate that importance is between 1 and 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return the number of days until the deadline, never below 0.

        Parameters
        ----------
        today : date
            The reference date to count from.
        """
        diff = (self.deadline - today).days
        return max(0, diff)
