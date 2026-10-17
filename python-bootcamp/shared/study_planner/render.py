"""Render study plan blocks into human-readable text."""

from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Render a list of study blocks into a readable text plan.

    Each line formats the task and its allocated study hours.
    Returns an empty string if blocks is empty.

    Example:
        1. Assignment - 1.5 h
        2. DS exam - 2 h
    """
    if not blocks:
        return ""

    lines = []
    for i, block in enumerate(blocks, start=1):
        hours_str = f"{block.hours:g}" if isinstance(block.hours, (int, float)) else str(block.hours)
        lines.append(f"{i}. {block.task.title} - {hours_str} h")
    return "\n".join(lines)
