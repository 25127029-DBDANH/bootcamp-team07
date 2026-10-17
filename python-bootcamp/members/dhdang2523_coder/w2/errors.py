from typing import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when total required effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: needed {self.needed_h}h, "
            f"but only {self.available_h}h available."
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> bool:
    """Check if tasks fit within available_h; raise InfeasiblePlan otherwise."""
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
    return True