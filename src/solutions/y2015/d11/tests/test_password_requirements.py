import pytest

from src.solutions.y2015.d11.logic.password_requirements import (
    has_no_forbidden_letters,
    has_three_increasing_straight,
    has_two_different_pairs,
    next_valid_password,
)

_FULL_REQUIREMENTS = [
    has_three_increasing_straight,
    has_no_forbidden_letters,
    has_two_different_pairs,
]


def test_next_valid_password_raises_if_no_possible_passwords():
    with pytest.raises(OverflowError):
        next_valid_password("zzzzzzzz", [])


@pytest.mark.parametrize(
    ("requirements", "current_password", "expected_next_password"),
    [
        ([], "abcdefgh", "abcdefgi"),
        ([], "zzzzzzzy", "zzzzzzzz"),
        ([], "azzzzzzz", "baaaaaaa"),
        ([has_three_increasing_straight], "abcdefgh", "abcdefgi"),
        ([has_three_increasing_straight], "aaaaaaaa", "aaaaaabc"),
        ([has_three_increasing_straight], "aaaazzzz", "aaabaabc"),
        ([has_three_increasing_straight], "aaaawxaa", "aaaawxya"),
        ([has_no_forbidden_letters], "abcdefgh", "abcdefgj"),
        ([has_no_forbidden_letters], "abclioab", "abcmaaaa"),
        ([has_two_different_pairs], "abcdefgh", "abcdffaa"),
        ([has_two_different_pairs], "aabbccdd", "aabbccde"),
        ([has_two_different_pairs], "abcdeegh", "abcdeehh"),
        (_FULL_REQUIREMENTS, "abcdefgh", "abcdffaa"),
    ],
)
def test_next_valid_password_satisfies_requirements(
    requirements, current_password, expected_next_password
):
    next_password = next_valid_password(current_password, requirements)
    assert next_password == expected_next_password
