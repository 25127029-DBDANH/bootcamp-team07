"""Academic rules verification utilities."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if student is eligible to register for graduation thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return human-readable reasons if student is not yet eligible for thesis."""
    reasons: list[str] = []
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")
    if gpa < 2.0:
        needed_gpa = round(2.0 - gpa, 2)
        reasons.append(f"need {needed_gpa:.2f} higher GPA")
    return reasons
