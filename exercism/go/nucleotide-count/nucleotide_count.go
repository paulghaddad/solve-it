package dna

import "fmt"

// Histogram is a mapping from nucleotide to its count in given DNA.
type Histogram map[rune]int

// DNA is a list of nucleotides. Choose a suitable data type.
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
func (d DNA) Counts() (Histogram, error) {
	h := Histogram{'A': 0, 'C': 0, 'G': 0, 'T': 0}

	for _, nuc := range d {
		_, ok := h[nuc]

		if !ok {
			return nil, fmt.Errorf("The DNA strand has an invalid nucleotide: %c", nuc)
		}

		h[nuc]++
	}

	return h, nil
}
