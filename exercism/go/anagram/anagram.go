package anagram

import (
	"sort"
	"strings"
)

// Detect returns the anagrams for a subject word from a list of candidate words
func Detect(subject string, candidates []string) []string {
	anagrams := make([]string, 0)
	lowerSubject := strings.ToLower(subject)
	sortedSubject := sortLetters(lowerSubject)

	for _, candidate := range candidates {
		lowerCandidate := strings.ToLower(candidate)

		if lowerSubject == lowerCandidate {
			continue
		}

		sortedCandidate := sortLetters(lowerCandidate)
		if sortedSubject == sortedCandidate {
			anagrams = append(anagrams, candidate)
		}
	}

	return anagrams
}

func sortLetters(word string) string {
	letters := strings.Split(word, "")
	sort.Strings(letters)

	return strings.Join(letters, "")
}
