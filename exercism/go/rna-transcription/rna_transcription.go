package strand

import "bytes"

// DnaToRna maps DNA nucleotides to RNA nucleotides
var DnaToRna = map[rune]rune{
	'C': 'G',
	'G': 'C',
	'T': 'A',
	'A': 'U',
}

// ToRNA transcribes a DNA strand to its RNA complement
func ToRNA(dna string) string {
	var buf bytes.Buffer

	for _, nuc := range dna {
		buf.WriteRune(DnaToRna[nuc])
	}

	return buf.String()
}
