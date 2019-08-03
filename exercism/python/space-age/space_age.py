import re


class SpaceAge(object):
    RELATIVE_ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }
    ORBITAL_PERIODS = [(planet, relative_earth_year * 31557600) for planet,
                       relative_earth_year in RELATIVE_ORBITAL_PERIODS.items()]


    def __init__(self, seconds):
        self.seconds = seconds
        for planet, period in self.ORBITAL_PERIODS:
            period_calculation = lambda period=period: round(seconds / period, 2)
            setattr(self, f"on_{planet}", period_calculation)
