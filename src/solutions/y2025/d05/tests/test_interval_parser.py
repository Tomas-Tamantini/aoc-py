from src.solutions.shared.number_theory.interval import Interval
from src.solutions.y2025.d05.logic.parser import (
    parse_ingredient_ids,
    parse_intervals,
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
    ranges = list(parse_intervals(reader))
    assert ranges == [Interval(3, 5), Interval(16, 20), Interval(12, 18)]


def test_parse_ingredient_ids(input_reader):
    reader = input_reader(CONTENT)
    ids = list(parse_ingredient_ids(reader))
    assert ids == [1, 5, 8]
