package grains

import "fmt"

const (
	minSquare int = 1
	maxSquare int = 64
)

// Square returns the number of grains on the nth square
func Square(n int) (uint64, error) {
	if n < minSquare || n > maxSquare {
		return 0, fmt.Errorf("n must be between 1 and 64")
	}

	// equivalent to 2**(n-1) but much faster
	return 1 << (n - 1), nil
}

// Total returns the total number of grains on the largest square
func Total() uint64 {
	return 0xFFFFFFFFFFFFFFFF // all the bits from 0 to 63 are all 1s
}
