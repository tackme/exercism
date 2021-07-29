def to_rna(dna_strand):
    conversion_table = {"G": "C", "C": "G", "T": "A", "A": "U"}

    rna_strand = dna_strand.translate(str.maketrans(conversion_table))

    return rna_strand
