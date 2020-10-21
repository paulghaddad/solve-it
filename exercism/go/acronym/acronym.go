// Package acronym solves the Acronym Exercism problem
package acronym

import (
	"regexp"
	"strings"
)

var acronymWord = regexp.MustCompile("[a-zA-Z]+\\'?[a-zA-Z]*")

// Abbreviate converts a full name to its acronym
func Abbreviate(s string) string {
	acronymMatches := acronymWord.FindAllString(strings.ToUpper(s), -1)
	var abbreviation []byte

	for _, word := range acronymMatches {
		abbreviation = append(abbreviation, word[0])
	}

	return string(abbreviation)
}
