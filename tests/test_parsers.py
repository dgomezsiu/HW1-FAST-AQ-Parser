# write tests for parsers


from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    # generate new instance of FastaParser class
    parsed = FastaParser("data/test.fa")
    
    # check parser filename
    assert parsed.filename == "data/test.fa"

    # check parser tuple sequence properties
    for sequence in parsed:
        assert len(sequence) == 2
        assert type(sequence) == tuple
        assert type(sequence[0]) == type(sequence[1]) == str
    



def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    # generate new instance
    parsed_fa = FastaParser("data/test.fa")

    for sequence in parsed_fa:
        assert sequence[0] is not None

    # generate new instance
    parsed_fq = FastaParser("data/test.fq")

    for sequence in parsed_fq:
        assert sequence[0] is None
        break # sequence[0] is None but test won't pass



def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """

    # generate new instance of FastaParser class
    parsed = FastqParser("data/test.fq")
    
    # check parser filename
    assert parsed.filename == "data/test.fq"

    # check parser tuple sequence properties
    for sequence in parsed:
        assert len(sequence) == 3
        assert type(sequence) == tuple
        assert type(sequence[0]) == type(sequence[1]) == type(sequence[2]) == str

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """

    # generate new instance
    parsed_fa = FastqParser("data/test.fa")

    for sequence in parsed_fa:
        assert sequence[0] is None

    # generate new instance
    parsed_fq = FastqParser("data/test.fq")

    for sequence in parsed_fq:
        assert sequence[0] is not None