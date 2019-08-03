"""
Exercism Problem 2: Leap
"""


def is_leap_year(year):
    """Return True if the year is a leap year"""
    mod = divider(year)
    return mod(4) and not mod(100) or mod(400)


def divider(year):
    return lambda d: year % d == 0
