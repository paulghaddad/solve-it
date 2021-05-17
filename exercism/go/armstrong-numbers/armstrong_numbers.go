package armstrong

import (
	"math"
)

// IsNumber determines whether a number is an Armstrong Number
func IsNumber(num int) bool {
	if num == 0 {
		return true
	}

	var numDigits, armstrongSum int

	for base := num; base > 0; numDigits++ {
		base /= 10
	}

	for base := num; base > 0; base /= 10 {
		digit := base % 10
		// base /= 10

		armstrongSum += int(math.Pow(float64(digit), float64(numDigits)))
	}

	return num == armstrongSum
}
