package reverse

import "bytes"

// Original Solution
// func Reverse(s string) string {
// 	strLength := utf8.RuneCountInString(s)
// 	reversed := make([]rune, strLength)
//
// 	i := strLength - 1
// 	for _, char := range s {
// 		reversed[i] = char
// 		i--
// 	}
//
// 	return string(reversed)
// }

// Reverse returns a new string with the characters of s in reverse order
func Reverse(s string) string {
	var reversed bytes.Buffer
	chars := []rune(s)

	for i := len(chars) - 1; i >= 0; i-- {
		reversed.WriteRune(chars[i])
	}

	return reversed.String()
}
