package allyourbase

import (
	"fmt"
)

// ConvertToBase converts a number from one base to another
func ConvertToBase(inputBase int, inputDigits []int, outputBase int) ([]int, error) {
	var outputDigits []int
	var sum, r int

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
	for _, d := range inputDigits {
		if d < 0 || d >= inputBase {
			return []int{}, fmt.Errorf("all digits must satisfy 0 <= d < input base")
		}
		sum = sum*inputBase + d
	}

	if sum == 0 {
		return []int{0}, nil
	}

	// convert from decimal to output base
	for sum > 0 {
		sum, r = sum/outputBase, sum%outputBase
		outputDigits = append([]int{r}, outputDigits...)
	}

	return outputDigits, nil
}
