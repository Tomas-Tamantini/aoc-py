from src.solutions.y2015.d19.logic.molecule_steps import (
    min_steps_to_generate_molecule,
)


def test_min_steps_to_generate_molecule() -> None:
    assert min_steps_to_generate_molecule("HOH") == 2
    assert min_steps_to_generate_molecule("HOHOHO") == 5
