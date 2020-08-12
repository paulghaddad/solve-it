package hamming

import "fmt"

func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return -1, fmt.Errorf("The lengths of the two strands are different: %d and %d", len(a), len(b))
	}

	difference := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			difference++
		}
	}

	return difference, nil
}
