from .models import Task


class InfeasiblePlan(Exception):
    """Raised when the tasks need more hours than are available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        super().__init__(needed_h, available_h)
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return (
            f"plan is infeasible: needs {self.needed_h} h "
            f"but only {self.available_h} h available"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the total effort exceeds available_h."""
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
