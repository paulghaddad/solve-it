package pangram

import (
	"strings"
	"unicode"
)

// IsPangram determines if a string contains all the lowercase letters
func IsPangram(input string) bool {
	letters := make(map[rune]bool)
	for char := 'a'; char <= 'z'; char++ {
		letters[char] = false
	}

	for _, char := range strings.ToLower(input) {
		if unicode.IsLower(char) {
			letters[char] = true
		}
	}

	for _, present := range letters {
		if present == false {
			return false
		}
	}

	return true
}
