package pythagorean

// Triplet is a slice of three values denoting a Pythogorean Triplet
type Triplet [3]int

// Range returns a list of Pythagorean Triplets with sides in the range min to
// max inclusive
func Range(min, max int) []Triplet {
	triplets := []Triplet{}

	for a := min; a <= max; a++ {
		for b := a + 1; b <= max; b++ {
			for c := b + 1; c <= max; c++ {
				if isTriplet(a, b, c) {
					triplets = append(triplets, Triplet{a, b, c})
				}
			}
		}
	}

	return triplets
}

// Sum returns a list of all Pythagorean triplets where the sum a+b+c
// (the perimeter) is equal to p.
func Sum(p int) []Triplet {
	triplets := []Triplet{}

	for c := p; c > 0; c-- {
		for b := c; b > 0; b-- {
			for a := b; a > 0; a-- {
				if a+b+c == p && isTriplet(a, b, c) {
					triplets = append(triplets, Triplet{a, b, c})
				}
			}
		}
	}

	return triplets
}

func isTriplet(a, b, c int) bool {
	return a*a+b*b == c*c
}
