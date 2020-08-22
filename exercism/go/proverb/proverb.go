// Package proverb contains functionality to produce Proverbs
package proverb

import "fmt"

const middlePhrase string = "For want of a %s the %s was lost."
const finalPhrase string = "And all for the want of a %s."

// Proverb generates a proverb given a list of inputs
func Proverb(rhyme []string) []string {
	output := []string{}
	if len(rhyme) == 0 {
		return output
	}

	for i := 0; i < len(rhyme)-1; i++ {
		output = append(output, fmt.Sprintf(middlePhrase, rhyme[i], rhyme[i+1]))
	}

	output = append(output, fmt.Sprintf(finalPhrase, rhyme[0]))

	return output
}
