package wordcount

import (
	"regexp"
	"strings"
)

// Frequency maps words to their counts
type Frequency map[string]int

const wordRegex = `\w+(\'\w+)?`

// WordCount takes in an input string and produces a map of word count
// frequencies
func WordCount(input string) Frequency {
	wordRegex := regexp.MustCompile(wordRegex)

	counts := make(Frequency)
	for _, word := range wordRegex.FindAllString(strings.ToLower(input), -1) {
		_, ok := counts[word]

		if ok {
			counts[word]++
		} else {
			counts[word] = 1
		}
	}

	return counts
}
