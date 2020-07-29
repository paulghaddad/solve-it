package space

type Planet string

const SECONDS_TO_EARTH_YEAR = 31557600

var orbital_periods = map[Planet]float64{
	"Mercury": 0.2408467,
	"Venus":   0.61519726,
	"Earth":   1.0,
	"Mars":    1.8808158,
	"Jupiter": 11.862615,
	"Saturn":  29.447498,
	"Uranus":  84.016846,
	"Neptune": 164.79132,
}

func Age(age float64, planet Planet) float64 {
	earth_years := age / SECONDS_TO_EARTH_YEAR
	return earth_years / orbital_periods[planet]
}
