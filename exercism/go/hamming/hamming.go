package hamming

import "fmt"

// Distance calculates the hamming distance for two DNA strands
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, fmt.Errorf("lengths of the two strands are different")
	}

	difference := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			difference++
		}
	}

	return difference, nil
}
