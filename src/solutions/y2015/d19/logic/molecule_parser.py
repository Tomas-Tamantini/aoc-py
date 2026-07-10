from typing import Iterator

from src.core.io_handler import InputReader
from src.solutions.y2015.d19.logic.molecule_replacement import (
    MoleculeReplacement,
)


def parse_molecule_replacements(
    reader: InputReader,
) -> Iterator[MoleculeReplacement]:
    for line in reader.read_stripped_lines():
        if "=>" in line:
            source, target = line.split(" => ")
            yield MoleculeReplacement(source=source, target=target)


def parse_medicine_molecule(reader: InputReader) -> str:
    for line in reader.read_stripped_lines():
        if "=>" not in line:
            return line
    raise ValueError("No initial molecule found")
