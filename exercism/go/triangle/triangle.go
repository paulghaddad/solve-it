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
	switch {
	case !ValidTriangle(a, b, c):
		return NaT
	case a == b && b == c:
		return Equ
	case a == b || b == c || a == c:
		return Iso
	default:
		return Sca
	}
}

// Return whether this is a valid triangle
func ValidTriangle(a, b, c float64) bool {
	if math.IsInf(a+b+c, 0) || math.IsNaN(a+b+c) {
		return false
	}

	if a <= 0 || b <= 0 || c <= 0 {
		return false
	}

	if a+b < c || b+c < a || a+c < b {
		return false
	}

	return true
}
