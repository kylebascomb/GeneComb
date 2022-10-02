from genecomb.genecomb import GeneComb
from genecomb.genecomb import count_point_mutations
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("AGCT", {"A": 1, "C": 1, "G": 1, "T": 1, "X": 0}),
        ("AAGCCC", {"A": 2, "C": 3, "G": 1, "T": 0, "X": 0}),
        ("agct", {"A": 1, "C": 1, "G": 1, "T": 1, "X": 0}),
        ("", {"A": 0, "C": 0, "G": 0, "T": 0, "X": 0}),
        ("XXXNA", {"A": 1, "C": 0, "G": 0, "T": 0, "X": 4}),
    ],
)
def test_base_counter(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.base_counter() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("AGCT", 0.50),
        ("AAGCCC", 0.67),
        ("agct", 0.5),
        ("", 0),
        ("AXXG", 0.25),
        ("ACNGGGNNNTAC", 0.42),
    ],
)
def test_gc_content(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.gc_content() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("AGCT", []),
        ("AAGCCC", []),
        ("agct", []),
        ("", []),
        ("AXXG", [[1, 2]]),
        ("ACNGGGNNNTAC", [[2, 2], [6, 8]]),
    ],
)
def test_non_nucleotide_counter(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.non_nucleotide_counter() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("AGCT", [[0, 3]]),
        ("AAGCCC", [[2, 3]]),
        ("agct", [[0, 3]]),
        ("", []),
        ("AXXG", []),
        ("ACNGGGNNNTAC", [[9, 10]]),
        ("AAAATTTT", [[0, 7]]),
    ],
)
def test_palindromes_no_overlap(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.find_palindromes() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("AGCT", [[0, 3]]),
        ("AAGCCC", [[2, 3]]),
        ("agct", [[0, 3]]),
        ("", []),
        ("AXXG", []),
        ("ACNGGGNNNTAC", [[9, 10]]),
        ("AAAATTTT", [[0, 7]]),
    ],
)
@pytest.mark.skip()
def test_palindromes_overlap(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.find_palindromes(removeOverlap=True) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("AGCT", "AGCT"),
        ("AAGCCC", "GGGCTT"),
        ("agct", "AGCT"),
        ("", ""),
        ("AXXG", "CXXT"),
        ("ACNGGGNNNTAC", "GTAXXXCCCXGT"),
        ("AAAATTTT", "AAAATTTT"),
    ],
)
def test_reverse_compliment(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.get_reverse_compliment() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("UCC", "S"),
        ("UCCGCU", "SA"),
        ("UCCGCUAAAGGG", "SAKG"),
        ("", ""),
        ("UCCGCUAAAGGGUAA", "SAKGSTOP"),
        ("AAAATTTT", "KI"),
        ("ACNGUU", ""),
        ("UCCCUN", "S"),
    ],
)
def test_translate_to_protein(test_input, expected):
    gene = GeneComb(test_input)
    assert gene.translate_to_protein() == expected


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [("AGCT", "AGCT", 0), ("AGTT", "AGCT", 1), ("AA", "GG", 2)],
)
def test_translate_to_protein(test_input_a, test_input_b, expected):
    assert count_point_mutations(test_input_a, test_input_b) == expected


@pytest.mark.parametrize(
    "test_input_a, test_input_b",
    [
        ("AGCTA", "AGCT"),
    ],
)
def test_translate_to_protein_length_mismatch(test_input_a, test_input_b):
    with pytest.raises(Exception):
        count_point_mutations(test_input_a, test_input_b)
