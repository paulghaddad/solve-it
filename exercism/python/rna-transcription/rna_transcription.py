dna_to_rna = dict(zip("CGTA", "GCAU"))


def to_rna(dna_strand):
    rna_strand = [dna_to_rna[nucleotide] for nucleotide in dna_strand]

    return "".join(rna_strand)
