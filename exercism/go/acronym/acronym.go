// Package acronym solves the Acronym Exercism problem
package acronym

import (
	"regexp"
	"strings"
)

// Abbreviate converts a full name to its acronym
func Abbreviate(s string) string {
	upperString := strings.ToUpper(s)
	var letters []byte

	for _, word := range regexp.MustCompile("[-_\\s]").Split(upperString, -1) {
		letters = append(letters, word[0])
	}

	return string(letters)
}
