import re


def min_steps_to_generate_molecule(molecule: str) -> int:
    tokens = re.findall(r"[A-Z][a-z]?", molecule)
    return (
        len(tokens)
        - tokens.count("Rn")
        - tokens.count("Ar")
        - 2 * tokens.count("Y")
        - 1
    )
