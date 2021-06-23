package piglatin

import (
	"strings"
)

// Sentence performs the Pig Latin transformation on the input string
func Sentence(s string) string {
	words := strings.Split(s, " ")
	trans := make([]string, len(words))

	for i, word := range words {
		switch {
		case word[0:2] == "yt" || word[0:2] == "xr":
			trans[i] = word + "ay"
		case word[0] == 'y':
			trans[i] = word[1:] + string(word[0]) + "ay"
		case vowelSound(word[0]):
			trans[i] = word + "ay"
		case strings.Contains(word, "qu"):
			start := strings.Index(word, "qu")
			trans[i] = word[start+2:] + word[:start+2] + "ay"
		case consonant(word[0]):
			var j int

			for _, c := range word {
				if !consonant(byte(c)) {
					break
				}
				j++
			}

			trans[i] = word[j:] + word[:j] + "ay"
		}
	}

	return strings.Join(trans, " ")
}

func vowelSound(b byte) bool {
	return b == 'a' || b == 'e' || b == 'i' || b == 'o' || b == 'u'
}

func consonant(b byte) bool {
	return b != 'a' && b != 'e' && b != 'i' && b != 'o' && b != 'u' && b != 'y'
}
