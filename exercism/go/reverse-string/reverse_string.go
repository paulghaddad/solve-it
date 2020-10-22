package reverse

import "unicode/utf8"

// Reverse returns a new string with the characters of s in reverse order
func Reverse(s string) string {
	strLength := utf8.RuneCountInString(s)
	reversed := make([]rune, strLength)

	i := strLength - 1
	for _, char := range s {
		reversed[i] = char
		i--
	}

	return string(reversed)
}
