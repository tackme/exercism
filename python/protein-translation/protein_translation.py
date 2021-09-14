from typing import List
from enum import Enum
from more_itertools.more import chunked


class Codon(Enum):
    AUG = 'Methionine'
    UUU = UUC = 'Phenylalanine'
    UUA = UUG = 'Leucine'
    UCU = UCC = UCA = UCG = 'Serine'
    UAU = UAC = 'Tyrosine'
    UGU = UGC = 'Cysteine'
    UGG = 'Tryptophan'
    UAA = UAG = UGA = 'STOP'

def proteins(strand: str) -> List[str]:
    chunked_strand = ["".join(chunk) for chunk in chunked(strand, 3)]

    result = []

    for chunk in chunked_strand:
        if Codon[chunk].value == "STOP":
            break

        result.append(Codon[chunk].value)

    return result
