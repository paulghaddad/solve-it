package strand

// DnaToRna maps DNA nucleotides to RNA nucleotides
var DnaToRna = map[string]string{
	"C": "G",
	"G": "C",
	"T": "A",
	"A": "U",
}

// ToRNA transcribes a DNA strand to its RNA complement
func ToRNA(dna string) string {
	rna := ""

	for _, nuc := range dna {
		rna += DnaToRna[string(nuc)]
	}

	return rna
}
