def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether the student meets the thesis registration rules."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Describe which thesis registration requirements are still unmet."""
    reasons: list[str] = []

    if credits < 120:
        reasons.append(f"need {120-credits} more credits")

    if gpa < 2.0:
        reasons.append(f"need {round(2.0-gpa, 2)} more GPA")

    return reasons
