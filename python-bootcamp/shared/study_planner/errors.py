
from shared.contract import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(self.__str__())

    def __str__(self):
        return f"need {self.needed_h:.1f} h but only {self.available_h:.1f} h available"

def check_feasible(tasks: list[Task], available_h: float) -> None:
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)