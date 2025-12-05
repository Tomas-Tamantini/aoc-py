from src.solutions.y2025.d05.logic.number_range import NumberRange
from src.solutions.y2025.d05.logic.parser import (
    parse_ingredient_ids,
    parse_number_ranges,
)

CONTENT = """
          3-5
          16-20
          12-18

          1
          5
          8
          """


def test_parse_number_ranges(input_reader):
    reader = input_reader(CONTENT)
    ranges = list(parse_number_ranges(reader))
    assert ranges == [
        NumberRange(3, 5),
        NumberRange(16, 20),
        NumberRange(12, 18),
    ]


def test_parse_ingredient_ids(input_reader):
    reader = input_reader(CONTENT)
    ids = list(parse_ingredient_ids(reader))
    assert ids == [1, 5, 8]
