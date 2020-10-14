package isogram

import (
	"fmt"
	"strings"
)

// IsIsogram determines whether a string is an isogram
func IsIsogram(str string) bool {
	if str == "" {
		return false
	}

	lettersPresent := 0 << 26

	for _, char := range strings.ToLower(str) {
		bitOffset := char << (char - 'a')
		fmt.Printf("Char value: %d\n", bitOffset)
		if lettersPresent&int(bitOffset) > 0 {
			return false
		}

		lettersPresent |= int(bitOffset)
	}

	return true
}
