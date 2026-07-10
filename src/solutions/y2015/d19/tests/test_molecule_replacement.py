from src.solutions.y2015.d19.logic.molecule_replacement import (
    MoleculeReplacement,
    neighboring_molecules,
)


def test_molecule_yields_expected_replacements():
    replacements = [
        MoleculeReplacement(source="H", target="HO"),
        MoleculeReplacement(source="H", target="OH"),
        MoleculeReplacement(source="O", target="HH"),
    ]
    molecule = "HOH"
    expected_replacements = {"HOOH", "HOHO", "OHOH", "HHHH"}

    actual_replacements = set(neighboring_molecules(molecule, replacements))

    assert actual_replacements == expected_replacements
