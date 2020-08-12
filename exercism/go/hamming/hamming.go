package hamming

import "fmt"

func Distance(a, b string) (int, error) {
	difference := 0

	if len(a) != len(b) {
		return difference, fmt.Errorf("The lengths of the two strands are different: %d and %d", len(a), len(b))
	}

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			difference += 1
		}
	}

	return difference, nil
}
