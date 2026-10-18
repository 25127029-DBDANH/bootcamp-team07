"""Custom exception and feasibility check."""

try:
    from .models import Task
except ImportError:  # imported as a top-level module (e.g. by the test runner)
    from models import Task


class InfeasiblePlan(Exception):
    """Raised when the tasks need more hours than are available."""

    def __init__(self, needed_h: float, available_h: float):
        super().__init__(needed_h, available_h)
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return (
            f"Infeasible plan: needs {self.needed_h:g} h "
            f"but only {self.available_h:g} h available"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if total effort exceeds the available hours."""
    needed = sum(task.effort_h for task in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)
