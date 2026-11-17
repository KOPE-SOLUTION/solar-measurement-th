"""Synthetic teaching examples for chapters 01 and 04. Python 3, no dependencies."""

from fractions import Fraction


def irradiation_wh_m2(irradiance_w_m2, minutes):
    """Constant irradiance, or the true time average over the stated interval."""
    if irradiance_w_m2 < 0 or minutes < 0:
        raise ValueError("This teaching example requires nonnegative inputs.")
    return Fraction(irradiance_w_m2) * Fraction(minutes) / 60


def compare(reference, test):
    """Percentages are defined here only for a positive reference value."""
    difference = test - reference
    percentage = 100 * Fraction(difference, reference) if reference > 0 else None
    return difference, abs(difference), percentage


if __name__ == "__main__":
    print("SYNTHETIC EXAMPLES ONLY")
    print("Chapter 01: constant irradiance [W/m2], duration [min], energy [Wh/m2]")
    for level, duration in [(800, 30), (400, 60), (500, 15)]:
        print(level, duration, irradiation_wh_m2(level, duration))
    total = irradiation_wh_m2(800, 15) + irradiation_wh_m2(400, 15)
    print("Two intervals (800 for 15 min, 400 for 15 min):", total, "Wh/m2")

    print("Chapter 04: reference, test, signed difference, magnitude, percent")
    for reference, test in [(800, 840), (800, 760), (1000, 1020), (200, 220),
                            (20, 40), (0, 20), (0, 0), (500, 470),
                            (200, 212), (10, 15), (0, 3)]:
        difference, magnitude, percentage = compare(reference, test)
        label = f"{float(percentage):+g}%" if percentage is not None else "undefined (reference <= 0)"
        print(reference, test, f"{difference:+g}", magnitude, label)
