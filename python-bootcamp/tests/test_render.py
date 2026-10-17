"""Tests for shared.study_planner.render."""

from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_empty_blocks():
    """Empty block list should render to empty string."""
    assert render([]) == ""


def test_render_single_block():
    """Single block should format line with index, title, and hours."""
    t = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    b = Block(t, 1.5)
    assert render([b]) == "1. Assignment - 1.5 h"


def test_render_multiple_blocks_and_hours_formatting():
    """Multiple blocks should render each on a new line with clean formatting."""
    t1 = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    t2 = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    blocks = [Block(t1, 1.5), Block(t2, 2.0)]
    expected = "1. Assignment - 1.5 h\n2. DS exam - 2 h"
    assert render(blocks) == expected
