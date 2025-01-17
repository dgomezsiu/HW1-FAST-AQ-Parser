# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """

    dna_seq = "ACTGGTCAA"
    transcribed = transcribe(dna_seq)

    assert transcribed == "UGACCAGUU"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """

    dna_seq = "ACTGGTCAA"
    rev_transcribed = reverse_transcribe(dna_seq)

    assert rev_transcribed == "UUGACCAGU"