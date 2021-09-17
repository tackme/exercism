from typing import List
from enum import Enum, auto
from more_itertools.more import chunked

class Methionine(Enum):
    AUG = auto()

class Phenylalanine(Enum):
    UUC = auto()
    UUU = auto()

class Leucine(Enum):
    UUA = auto()
    UUG = auto()

class Serine(Enum):
    UCA = auto()
    UCC = auto()
    UCG = auto()
    UCU = auto()

class Tyrosine(Enum):
    UAC = auto()
    UAU = auto()

class Cysteine(Enum):
    UGC = auto()
    UGU = auto()

class Tryptophan(Enum):
    UGG = auto()

class Proteins(Enum):
    methionine = Methionine
    phenylalanine = Phenylalanine
    leucine = Leucine
    serine = Serine
    tyrosine = Tyrosine
    cysteine = Cysteine
    tryptophan = Tryptophan

    @classmethod
    def from_codon(cls, codon):
        for i in Proteins:
            for j in i.value:
                if codon in j.name:
                    return type(j).__name__

        return None

def proteins(strand: str) -> List[str]:
    chunked_strand = ["".join(chunk) for chunk in chunked(strand, 3)]

    result = []

    for chunk in chunked_strand:
        if Proteins.from_codon(chunk):
            result.append(Proteins.from_codon(chunk))

        else:
            break

    return result
