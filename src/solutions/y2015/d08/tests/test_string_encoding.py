import pytest

from src.solutions.y2015.d08.logic.string_encoding import (
    encoded_length,
    memory_length,
)


# AoC 2015 Day 8 examples
@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ('""', 0),
        ('"abc"', 3),
        (r'"aaa\"aaa"', 7),
        (r'"\x27"', 1),
    ],
)
def test_memory_length(code, expected):
    assert memory_length(code) == expected


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ('""', 6),
        ('"abc"', 9),
        (r'"aaa\"aaa"', 16),
        (r'"\x27"', 11),
    ],
)
def test_encoded_length(code, expected):
    assert encoded_length(code) == expected
