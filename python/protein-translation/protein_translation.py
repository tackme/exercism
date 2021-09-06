from enum import Enum
from more_itertools.more import chunked


class Protein(Enum):
    AUG = "Methionine"
    UUU = "Phenylalanine"
    UUC = "Phenylalanine"
    UUA = "Leucine"
    UUG = "Leucine"
    UCU = "Serine"
    UCC = "Serine"
    UCA = "Serine"
    UCG = "Serine"
    UAU = "Tyrosine"
    UAC = "Tyrosine"
    UGU = "Cysteine"
    UGC = "Cysteine"
    UGG = "Tryptophan"
    UAA = "STOP"
    UAG = "STOP"
    UGA = "STOP"

def proteins(strand):
    chunked_strand = ["".join(chunk) for chunk in chunked(strand, 3)]

    result = []

    for chunk in chunked_strand:
        if Protein[chunk].value == "STOP":
            break

        result.append(Protein[chunk].value)

    return result
