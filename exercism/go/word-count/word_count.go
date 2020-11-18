package wordcount

import (
	"strings"
	"unicode"
)

// Frequency maps words to their counts
type Frequency map[string]int

// WordCount takes in an input string and produces a map of word count
// frequencies
func WordCount(input string) Frequency {
	fieldFn := func(c rune) bool {
		return !unicode.IsLetter(c) && !unicode.IsDigit(c) && c != '\''
	}

	counts := make(Frequency)
	for _, word := range strings.FieldsFunc(strings.ToLower(input), fieldFn) {
		if strings.HasPrefix(word, "'") && strings.HasSuffix(word, "'") {
			word = strings.Trim(word, "'")
		}

		counts[word]++
	}

	return counts
}
