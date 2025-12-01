from src.solutions.y2025.d01.logic.parser import parse_dial_offsets


def test_parse_dial_offsets(input_reader):
    reader = input_reader(
        """
        L1
        R2
        L3
        R40
        """
    )
    offsets = list(parse_dial_offsets(reader))
    assert offsets == [-1, 2, -3, 40]
