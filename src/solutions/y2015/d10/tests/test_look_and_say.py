import pytest

from src.solutions.y2015.d10.logic.look_and_say import next_look_and_say


@pytest.mark.parametrize(
    ("input_str", "expected_output"),
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
        ("312211", "13112221"),
        ("13112221", "1113213211"),
    ],
)
def test_next_look_and_say(input_str, expected_output):
    assert next_look_and_say(input_str) == expected_output
