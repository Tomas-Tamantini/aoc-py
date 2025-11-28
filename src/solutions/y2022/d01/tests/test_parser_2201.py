from typing import Callable

from src.core.input_reader import InputReader
from src.solutions.y2022.d01.logic.parser import parse_calories


def test_calories_are_grouped_by_line_break(
    input_reader: Callable[[str], InputReader],
):
    reader = input_reader("""12
                             123

                             5
                             -6
                             3

                             1""")
    calories = list(parse_calories(reader))
    assert calories == [(12, 123), (5, -6, 3), (1,)]
