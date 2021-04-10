package luhn

import (
	"strings"
	"unicode/utf8"
)

// Valid returns whether a given number is a valid Luhn checksum
func Valid(input string) bool {
	input = strings.ReplaceAll(input, " ", "")
	if utf8.RuneCountInString(input) <= 1 {
		return false
	}

	sum := 0
	double := false
	for i := len(input) - 1; i >= 0; i-- {
		char := input[i]

		if char < '0' || char > '9' {
			return false
		}

		digit := int(char - '0')

		if double {
			digit <<= 1
			if digit > 9 {
				digit -= 9
			}
			sum += digit
			double = false
		} else {
			sum += digit
			double = true
		}
	}

	return sum%10 == 0
}
