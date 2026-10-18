from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_empty_blocks():
    assert render([]) == ""


def test_render_single_block():
    t = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    b = Block(t, 1.5)
    assert render([b]) == "1. Assignment - 1.5 h"


def test_render_multiple_blocks_and_hours_formatting():
    t1 = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    t2 = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    blocks = [Block(t1, 1.5), Block(t2, 2.0)]
    expected = "1. Assignment - 1.5 h\n2. DS exam - 2 h"
    assert render(blocks) == expected


def test_render_zero_hours_edge_case():
    t = Task("Rest", 1, 1.0, date(2026, 10, 27))
    b = Block(t, 0.0)
    result = render([b])
    
    assert "Rest" in result
    assert "0" in result or "0.0" in result


def test_render_special_characters_title():
    t = Task("Thi Cuối Kỳ (Nhập môn IT)!", 5, 2.0, date(2026, 10, 30))
    b = Block(t, 2.0)
    result = render([b])
    
    assert "Thi Cuối Kỳ (Nhập môn IT)!" in result