from src.solutions.y2025.d02.logic.parser import parse_ranges


def test_ranges_parser(input_reader):
    reader = input_reader("11-22,95-115")
    ranges = list(parse_ranges(reader))
    assert ranges == [(11, 22), (95, 115)]
