package darts

import "math"

// Score gives the dart score for the given coordinates
func Score(x, y float64) int {
	distance := math.Sqrt(math.Pow(x, 2) + math.Pow(y, 2))

	switch {
	case distance <= 1:
		return 10
	case distance <= 5:
		return 5
	case distance <= 10:
		return 1
	default:
		return 0
	}
}
