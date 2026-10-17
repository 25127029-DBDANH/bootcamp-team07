"""W2-3: Custom exception – InfeasiblePlan and feasibility checker."""

from members.ankhang_maker.w2.models import Task


class InfeasiblePlan(Exception):
    """Raised when the total effort exceeds the available hours.

    Attributes
    ----------
    needed_h : float
        Total hours needed for all tasks.
    available_h : float
        Hours actually available.
    """

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: need {self.needed_h} h "
            f"but only {self.available_h} h available"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise ``InfeasiblePlan`` if total effort exceeds *available_h*.

    Parameters
    ----------
    tasks : list[Task]
        Tasks to check.
    available_h : float
        Maximum hours available.

    Raises
    ------
    InfeasiblePlan
        If the sum of ``effort_h`` across tasks exceeds *available_h*.
    """
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)
