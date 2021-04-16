package pythagorean

import "math"

// Triplet is a slice of three values denoting a Pythogorean Triplet
type Triplet [3]int

// Range returns a list of Pythagorean Triplets with sides in the range min to
// max inclusive
func Range(min, max int) []Triplet {
	triplets := []Triplet{}

	for a := min; a <= max; a++ {
		for b := a + 1; b <= max; b++ {
			c := int(math.Sqrt(math.Pow(float64(a), 2.0) + math.Pow(float64(b), 2.0)))

			if c > min && c <= max && isTriplet(a, b, c) {
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

func isTriplet(a, b, c int) bool {
	return a < b && b < c && a*a+b*b == c*c
}
