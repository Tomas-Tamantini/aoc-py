from typing import Iterator, Optional


def _numbers_with_repeated_sequence(
    range_start: int, range_end: int, multiplicity: int
) -> Iterator[int]:
    component = 1
    while (candidate := int(str(component) * multiplicity)) <= range_end:
        if candidate >= range_start:
            yield candidate
        component += 1


def invalid_ids(
    range_start: int, range_end: int, multiplicity: Optional[int]
) -> set[int]:
    if multiplicity is not None:
        multiplicities = [multiplicity]
    else:
        num_digits = len(str(range_end))
        multiplicities = range(2, num_digits + 1)

    ids = set()
    for mult in multiplicities:
        ids.update(
            set(_numbers_with_repeated_sequence(range_start, range_end, mult))
        )

    return ids
