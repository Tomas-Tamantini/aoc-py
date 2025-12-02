import pytest

from src.solutions.y2025.d02.logic.invalid_ids import invalid_ids


@pytest.mark.parametrize(
    ("range_start", "range_end", "expected"),
    [(11, 22, {11, 22}), (95, 115, {99}), (38593856, 38593862, {38593859})],
)
def test_invalid_ids_have_sequence_of_digits_repeated_with_given_multiplicity(
    range_start, range_end, expected
):
    invalid = invalid_ids(range_start, range_end, multiplicity=2)
    assert expected == invalid


@pytest.mark.parametrize(
    ("range_start", "range_end", "expected"),
    [(11, 22, {11, 22}), (95, 115, {99, 111}), (565653, 565659, {565656})],
)
def test_invalid_ids_have_sequence_of_digits_repeated_with_any_multiplicity(
    range_start, range_end, expected
):
    invalid = invalid_ids(range_start, range_end, multiplicity=None)
    assert expected == invalid
