package collatzconjecture

import "fmt"

// CollatzConjecture returns the number of steps needed to perform the collatz
// conjecture on n
func CollatzConjecture(n int) (int, error) {
	var steps int

	if n < 1 {
		return -1, fmt.Errorf("n must be larger than 0")
	}

	for n > 1 {
		if n&1 == 0 {
			n >>= 1
		} else {
			n = 3*n + 1
		}

		steps++
	}

	return steps, nil
}
