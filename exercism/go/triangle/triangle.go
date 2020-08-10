// My solution for Triangle
package triangle

import "math"

// Notice KindFromSides() returns this type. Pick a suitable data type.
type Kind string

const (
	NaT = "NaT"
	Equ = "Equ"
	Iso = "Iso"
	Sca = "Sca"
)

// Return type of triangle or if it's not a triangle
func KindFromSides(a, b, c float64) Kind {
	var k Kind

	if !ValidTriangle(a, b, c) {
		return NaT
	}

	if a == b && b == c {
		k = Equ
	} else if a == b || b == c || a == c {
		k = Iso
	} else {
		k = Sca
	}

	return k
}

// Return whether this is a valid triangle
func ValidTriangle(a, b, c float64) bool {
	if math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) {
		return false
	}

	if a <= 0 || b <= 0 || c <= 0 {
		return false
	}

	if !(a+b >= c && b+c >= a && a+c >= b) {
		return false
	}

	return true
}
