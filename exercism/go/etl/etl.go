package etl

import (
	"strings"
)

// Transform converts a map of scrabble scores to letters to a map of letters to
// scrablle scores
func Transform(scoresToLetters map[int][]string) map[string]int {
	lettersToScores := make(map[string]int)

	for score, letters := range scoresToLetters {
		for _, letter := range letters {
			lettersToScores[strings.ToLower(letter)] = score
		}
	}

	return lettersToScores
}
