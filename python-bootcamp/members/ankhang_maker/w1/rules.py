"""W1-3: Thesis eligibility – check whether a student can register."""

CREDITS_REQUIRED = 120
GPA_REQUIRED = 2.0


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return ``True`` if *credits* >= 120 **and** *gpa* >= 2.0."""
    return credits >= CREDITS_REQUIRED and gpa >= GPA_REQUIRED


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of human-readable reasons why registration is denied.

    An empty list means the student qualifies.

    Examples
    --------
    >>> missing(118, 3.1)
    ['need 2 more credits']
    """
    reasons: list[str] = []
    if credits < CREDITS_REQUIRED:
        reasons.append(f"need {CREDITS_REQUIRED - credits} more credits")
    if gpa < GPA_REQUIRED:
        reasons.append(f"GPA must be at least {GPA_REQUIRED}, currently {gpa}")
    return reasons
