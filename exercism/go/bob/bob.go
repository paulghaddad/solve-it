package bob

import (
	"strings"
	"unicode"
)

const (
	responseToSilence         = "Fine. Be that way!"
	responseToYellingQuestion = "Calm down, I know what I'm doing!"
	responseToQuestion        = "Sure."
	responseToShouting        = "Whoa, chill out!"
	defaultResponse           = "Whatever."
)

// Hey produces the response from Bob
func Hey(remark string) string {
	remark = strings.TrimSpace(remark)

	switch {
	case silence(remark):
		return responseToSilence
	case yellingQuestion(remark):
		return responseToYellingQuestion
	case question(remark):
		return responseToQuestion
	case shouting(remark):
		return responseToShouting
	default:
		return defaultResponse
	}
}

func silence(s string) bool {
	return len(s) == 0
}

func question(s string) bool {
	return strings.HasSuffix(s, "?")
}

func yellingQuestion(s string) bool {
	return strings.HasSuffix(s, "?") && containsLetters(s) && s == strings.ToUpper(s)
}

func shouting(s string) bool {
	return containsLetters(s) && s == strings.ToUpper(s)
}

func containsLetters(s string) bool {
	for _, char := range s {
		if unicode.IsLetter(char) {
			return true
		}
	}

	return false
}
