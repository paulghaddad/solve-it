package isogram

import (
	"strings"
	"unicode"
)

// IsIsogram returns whether a word or phrase is an isogram
// Map version
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

// IsIsogram returns whether a word or phrase is an isogram
// Array version
// func IsIsogram(str string) bool {
// 	var letterPresent [26]int
//
// 	for _, char := range strings.ToLower(str) {
// 		if unicode.IsLetter(char) {
// 			offset := int(char) - 'a'
// 			if letterPresent[offset] > 0 {
// 				return false
// 			}
//
// 			letterPresent[offset] = 1
// 		}
// 	}
//
// 	return true
// }
