from src.solutions.y2015.d19.logic.molecule_parser import (
    parse_medicine_molecule,
    parse_molecule_replacements,
)
from src.solutions.y2015.d19.logic.molecule_replacement import (
    MoleculeReplacement,
)

_EXAMPLE = """
           H => HO
           H => OH
           O => HH

           HOH
           """


def test_parse_medicine_molecule(input_reader):
    reader = input_reader(_EXAMPLE)
    initial_molecule = parse_medicine_molecule(reader)
    assert initial_molecule == "HOH"


def test_parse_molecule_replacements(input_reader):
    reader = input_reader(_EXAMPLE)
    replacements = list(parse_molecule_replacements(reader))
    assert replacements == [
        MoleculeReplacement(source="H", target="HO"),
        MoleculeReplacement(source="H", target="OH"),
        MoleculeReplacement(source="O", target="HH"),
    ]
