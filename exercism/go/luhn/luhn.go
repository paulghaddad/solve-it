package luhn

import (
	"strings"
	"unicode"
	"unicode/utf8"
)

// Valid returns whether a given number is a valid Luhn checksum
func Valid(input string) bool {
	input = strings.TrimSpace(input)

	if utf8.RuneCountInString(input) <= 1 {
		return false
	}

	// convert to slice of ints
	digits := []int{}
	for _, char := range input {
		if validLuhnChar(char) {
			return false
		}

		if unicode.IsDigit(char) {
			digits = append(digits, int(char)-'0')
		}
	}

	// double every second number from right
	// sum all the numbers
	sum := 0
	j := 0
	for i := len(digits) - 1; i >= 0; i-- {
		if j%2 == 1 {
			product := 2 * digits[i]
			if product > 9 {
				product -= 9
			}

			digits[i] = product
		}

		sum += digits[i]
		j++
	}

	return sum%10 == 0
}

func validLuhnChar(char rune) bool {
	return !unicode.IsDigit(char) && !unicode.IsSpace(char)
}
