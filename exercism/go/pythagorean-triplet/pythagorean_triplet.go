package pythagorean

import (
	"math"
)

// Triplet is a slice of three values denoting a Pythogorean Triplet
type Triplet [3]int

// Range returns a list of Pythagorean Triplets with sides in the range min to
// max inclusive
func Range(min, max int) []Triplet {
	triplets := []Triplet{}

	for a := min; a <= max; a++ {
		for b := a + 1; b <= max; b++ {
			sqr := a*a + b*b
			c := int(math.Sqrt(float64(sqr)))

			if c*c == sqr && c > min && c <= max {
				triplets = append(triplets, Triplet{a, b, c})
			}
		}
	}

	return triplets
}

// Sum returns a list of all Pythagorean triplets where the sum a+b+c
// (the perimeter) is equal to p.
func Sum(p int) []Triplet {
	triplets := []Triplet{}

	possibleTriplets := Range(1, p)

	for _, trip := range possibleTriplets {
		if trip[0]+trip[1]+trip[2] == p {
			triplets = append(triplets, trip)
		}
	}

	return triplets
}
