dna_to_rna = str.maketrans('CGTA', 'GCAU')

def to_rna(dna_strand):
    return dna_strand.translate(dna_to_rna)
