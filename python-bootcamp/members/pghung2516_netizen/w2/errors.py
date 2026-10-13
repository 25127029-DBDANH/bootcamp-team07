"""Custom exceptions and validation for tasks."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when total task effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float, message: str | None = None) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        if message is None:
            message = (
                f"Infeasible plan: needed {needed_h} hours, but only {available_h} hours available."
            )
        super().__init__(message)


def check_feasible(tasks: list["Task"], available_h: float) -> None:
    """Validate whether the tasks can be completed within available hours.

    Raises:
        InfeasiblePlan: If total required effort exceeds available hours.
    """
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
