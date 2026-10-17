"""Planning errors and feasibility checks."""

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when tasks need more study time than is available."""

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return (
            f"Need {self.needed_h} hours, "
            f"but only {self.available_h} hours are available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the tasks exceed the available hours."""
    needed_h = 0.0

    for task in tasks:
        needed_h += task.effort_h

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
