package protein

import "errors"

// ErrStop is raised when one of the stop codons is seen
var ErrStop = errors.New("Reached Stop Codon")

// ErrInvalidBase is raised when there is an invalid base
var ErrInvalidBase = errors.New("Invalid Base")

// CodonToPolypeptide macodons to their associated polypeptides
var CodonToPolypeptide = map[string]string{
	"AUG": "Methionine",
	"UUU": "Phenylalanine",
	"UUC": "Phenylalanine",
	"UUA": "Leucine",
	"UUG": "Leucine",
	"UCG": "Serine",
	"UCC": "Serine",
	"UCA": "Serine",
	"UCU": "Serine",
	"UAU": "Tyrosine",
	"UAC": "Tyrosine",
	"UGU": "Cysteine",
	"UGC": "Cysteine",
	"UGG": "Tryptophan",
}

// StopCodons is the collection of codons that indicate a terminus of the strand
var StopCodons = [3]string{"UAA", "UAG", "UGA"}

// FromCodon translates a codon string to the polypeptide
func FromCodon(codon string) (string, error) {
	polypeptide := CodonToPolypeptide[codon]

	if isStopCodon(codon) {
		return "", ErrStop
	}

	if polypeptide == "" {
		return "", ErrInvalidBase
	}

	return polypeptide, nil
}

// FromRNA translates an RNA strand to a DNA strand
func FromRNA(rna string) ([]string, error) {
	var dna []string

	for i := 0; i <= len(rna)-3; i += 3 {
		codon := rna[i : i+3]

		if isStopCodon(codon) {
			return dna, nil
		}

		polypeptide, err := FromCodon(codon)

		if err != nil {
			return dna, err
		}

		dna = append(dna, polypeptide)
	}

	return dna, nil
}

func isStopCodon(codon string) bool {
	for _, stopCodon := range StopCodons {
		if codon == stopCodon {
			return true
		}
	}
	return false
}
