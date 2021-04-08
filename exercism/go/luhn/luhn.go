package luhn

import (
	"strings"
	"unicode/utf8"
)

// Valid returns whether a given number is a valid Luhn checksum
func Valid(input string) bool {
	if utf8.RuneCountInString(strings.TrimSpace(input)) <= 1 {
		return false
	}

	sum := 0
	for i, j := len(input)-1, 0; i >= 0; i-- {
		char := input[i]

		if char == ' ' {
			continue
		}

		if char < '0' || char > '9' {
			return false
		}

		digit := int(char - '0')

		if j%2 == 1 {
			digit <<= 1
			if digit > 9 {
				digit -= 9
			}
			sum += digit
		} else {
			sum += digit
		}

		j++
	}

	return sum%10 == 0
}
