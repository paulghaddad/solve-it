package isogram

import (
	"strings"
	"unicode"
)

// IsIsogram returns whether a word or phrase is an isogram
func IsIsogram(str string) bool {
	lettersSeen := make(map[rune]bool)

	for _, char := range strings.ToLower(str) {
		if unicode.IsLetter(char) {
			if lettersSeen[char] {
				return false
			}

			lettersSeen[char] = true
		}
	}

	return true
}
