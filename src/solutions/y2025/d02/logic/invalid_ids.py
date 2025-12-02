from typing import Iterator


def invalid_ids(range_start: int, range_end: int) -> Iterator[int]:
    component = 1
    while (candidate := int(f"{component}{component}")) <= range_end:
        if candidate >= range_start:
            yield candidate
        component += 1
