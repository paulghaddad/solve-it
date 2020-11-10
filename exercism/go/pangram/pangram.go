package pangram

import (
	"strings"
	"unicode"
)

// IsPangram determines if a string contains all the lowercase letters
func IsPangram(input string) bool {
	letters := 0x0

	for _, char := range strings.ToLower(input) {
		if unicode.IsLower(char) {
			letters |= 1 << (char - 'a')
		}
	}

	return 0x3ffffff == letters
}
