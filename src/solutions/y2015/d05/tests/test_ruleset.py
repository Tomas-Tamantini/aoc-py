import pytest

from src.solutions.y2015.d05.logic.ruleset import (
    first_ruleset,
    is_nice,
    second_ruleset,
)


def test_string_is_nice_if_all_rules_pass():
    ruleset = [lambda text: "a" in text, lambda text: len(text) > 3]
    assert is_nice("abcde", ruleset)
    assert not is_nice("a", ruleset)
    assert not is_nice("bcde", ruleset)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_first_ruleset(text, expected):
    assert is_nice(text, first_ruleset) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_second_ruleset(text, expected):
    assert is_nice(text, second_ruleset) == expected
