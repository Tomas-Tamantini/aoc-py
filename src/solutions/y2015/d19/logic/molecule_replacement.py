from dataclasses import dataclass
from typing import Iterable, Iterator


@dataclass(frozen=True)
class MoleculeReplacement:
    source: str
    target: str


def neighboring_molecules(
    molecule: str, replacements: Iterable[MoleculeReplacement]
) -> Iterator[str]:
    for replacement in replacements:
        start = 0
        while True:
            start = molecule.find(replacement.source, start)
            if start == -1:
                break
            yield (
                molecule[:start]
                + replacement.target
                + molecule[start + len(replacement.source) :]
            )
            start += 1
