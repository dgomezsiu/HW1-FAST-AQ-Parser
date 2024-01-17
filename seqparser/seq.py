# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    # make sure DNA sequence has only allowed nucleotides
    assert all(nucleotide in ALLOWED_NUC for nucleotide in seq), "Input string contains unallowed nucleotides."

    # iterate through sequence and transcribe
    rna_seq = ''
    rna_seq = rna_seq.join(TRANSCRIPTION_MAPPING[nucleotide] for nucleotide in seq)
    return rna_seq



def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """

    return transcribe(seq)[::1]