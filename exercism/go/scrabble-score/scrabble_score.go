package scrabble

import "unicode"

var letterValues = [26]int{1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10}

// Score calculates the Scrabble score for a word
func Score(input string) int {
	total := 0
	for _, letter := range input {
		total += letterValues[unicode.ToLower(letter)-'a']
	}

	return total
}
