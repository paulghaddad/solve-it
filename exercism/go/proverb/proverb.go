// Package proverb contains functionality to produce Proverbs
package proverb

import "fmt"

const (
	middlePhrase = "For want of a %s the %s was lost."
	finalPhrase  = "And all for the want of a %s."
)

// Proverb generates a proverb given a list of inputs
func Proverb(rhyme []string) []string {
	if len(rhyme) == 0 {
		return []string{}
	}

	output := make([]string, len(rhyme))

	for i := 0; i < len(rhyme)-1; i++ {
		output[i] = fmt.Sprintf(middlePhrase, rhyme[i], rhyme[i+1])
	}

	output[len(rhyme)-1] = fmt.Sprintf(finalPhrase, rhyme[0])

	return output
}
