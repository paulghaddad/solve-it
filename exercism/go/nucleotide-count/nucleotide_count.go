package dna

import "errors"

// Histogram is a mapping from nucleotide to its count in given DNA.
type Histogram map[byte]int

// DNA is a list of nucleotides. Choose a suitable data type.
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
func (d DNA) Counts() (Histogram, error) {
	var h = Histogram{'A': 0, 'C': 0, 'G': 0, 'T': 0}
	var err error = nil

	for _, nuc := range d {
		_, ok := h[byte(nuc)]

		if !ok {
			err = errors.New("The DNA strand has an invalid nucleotide")
			return h, err
		}

		h[byte(nuc)]++
	}

	return h, err
}
