import json
from datetime import date

import pytest

from .errors import InfeasiblePlan, check_feasible
from .io_utils import load_tasks, save_json
from .models import Task


def test_days_left_and_never_negative():
    t = Task("a", 3, 1.0, date(2026, 10, 30))
    assert t.days_left(date(2026, 10, 27)) == 3
    assert t.days_left(date(2026, 11, 5)) == 0


def test_importance_out_of_range():
    with pytest.raises(ValueError):
        Task("a", 6, 1.0, date(2026, 10, 30))


def test_load_tasks(tmp_path):
    p = tmp_path / "t.csv"
    p.write_text("title,importance,effort_h,deadline\nA,5,6,2026-10-30\n")
    assert load_tasks(p) == [Task("A", 5, 6.0, date(2026, 10, 30))]


def test_load_tasks_reports_line_number(tmp_path):
    p = tmp_path / "t.csv"
    p.write_text("title,importance,effort_h,deadline\nA,5,6,2026-10-30\nB,x,1,2026-10-30\n")
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(p)


def test_save_json(tmp_path):
    p = tmp_path / "o.json"
    save_json([Task("A", 5, 6.0, date(2026, 10, 30))], p)
    assert json.loads(p.read_text())[0]["deadline"] == "2026-10-30"


def test_check_feasible():
    tasks = [Task("A", 5, 6.0, date(2026, 10, 30))]
    check_feasible(tasks, 6)
    with pytest.raises(InfeasiblePlan) as err:
        check_feasible(tasks, 4)
    assert err.value.needed_h == 6 and err.value.available_h == 4
    assert "needs 6 h" in str(err.value)
