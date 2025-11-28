import pytest

from src.solutions.y2019.d21.logic.parse_springscript import parse_springscript


def test_invalid_springscript_raises_error(input_reader):
    reader = input_reader("AND A T\nINVALID COMMAND")
    with pytest.raises(
        ValueError, match="Invalid springscript command: INVALID COMMAND"
    ):
        _ = list(parse_springscript(reader))


def test_valid_springscript_parses_correctly(input_reader):
    reader = input_reader("NOT  D J\nWALK")
    assert list(parse_springscript(reader)) == [
        ord("N"),
        ord("O"),
        ord("T"),
        ord(" "),
        ord("D"),
        ord(" "),
        ord("J"),
        ord("\n"),
        ord("W"),
        ord("A"),
        ord("L"),
        ord("K"),
        ord("\n"),
    ]
