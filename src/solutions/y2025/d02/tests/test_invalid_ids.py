import pytest

from src.solutions.y2025.d02.logic.invalid_ids import invalid_ids


@pytest.mark.parametrize(
    ("range_start", "range_end", "expected"),
    [(11, 22, [11, 22]), (95, 115, [99]), (38593856, 38593862, [38593859])],
)
def test_invalid_ids_contain_sequence_of_digits_repeated_twice(
    range_start, range_end, expected
):
    invalid = list(invalid_ids(range_start, range_end))
    assert expected == invalid
