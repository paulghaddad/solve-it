class SpaceAge:
    earth_years = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }

    earth_seconds = 31557600


    def __init__(self, seconds):
        self.age_seconds = seconds
        self.earth_year = round(self.age_seconds / SpaceAge.earth_seconds, 2)

        for planet, p_years in SpaceAge.earth_years.items():
            earth_years = lambda p_years=p_years: round(self.earth_year / p_years, 2)
            setattr(self, f'on_{planet}', earth_years)
