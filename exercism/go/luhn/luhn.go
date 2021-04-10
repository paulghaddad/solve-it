package luhn

import (
	"strings"
)

// Valid returns whether a given number is a valid Luhn checksum
func Valid(input string) bool {
	input = strings.ReplaceAll(input, " ", "")
	if len(input) <= 1 {
		return false
	}

	sum := 0
	double := len(input)%2 == 0

	for _, char := range input {
		if char < '0' || char > '9' {
			return false
		}

		digit := int(char - '0')

		if double {
			digit *= 2
			if digit > 9 {
				digit -= 9
			}
		}

		sum += digit
		double = !double
	}

	return sum%10 == 0
}
