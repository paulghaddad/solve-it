package allyourbase

import (
	"fmt"
	"math"
)

// ConvertToBase converts a number from one base to another
func ConvertToBase(inputBase int, inputDigits []int, outputBase int) ([]int, error) {
	var outputDigits []int
	var n, r int

	if inputBase < 2 {
		return outputDigits, fmt.Errorf("input base must be >= 2")
	}

	if outputBase < 2 {
		return outputDigits, fmt.Errorf("output base must be >= 2")
	}

	if len(inputDigits) == 0 {
		return []int{0}, nil
	}

	// convert to decimal
	for i, j := len(inputDigits)-1, 0; i >= 0; i, j = i-1, j+1 {
		inputDigit := inputDigits[i]
		if inputDigit < 0 || inputDigit >= inputBase {
			return []int{}, fmt.Errorf("all digits must satisfy 0 <= d < input base")
		}
		n += inputDigit * int(math.Pow(float64(inputBase), float64(j)))
	}

	if n == 0 {
		return []int{0}, nil
	}

	// convert from decimal to output base
	for n > 0 {
		n, r = n/outputBase, n%outputBase
		outputDigits = append(outputDigits, r)
	}

	// reverse digits
	for i, j := 0, len(outputDigits)-1; i < j; i, j = i+1, j-1 {
		outputDigits[i], outputDigits[j] = outputDigits[j], outputDigits[i]
	}

	return outputDigits, nil
}
