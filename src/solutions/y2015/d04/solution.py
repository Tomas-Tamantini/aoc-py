from hashlib import md5
from typing import Iterator

from src.core.io_handler import IOHandler


def _hashes_sequence(prefix: str) -> Iterator[tuple[int, str]]:
    number = 1
    while True:
        message = f"{prefix}{number}"
        hashed_message = md5(message.encode()).hexdigest()
        yield number, hashed_message
        number += 1


def _first_with_leading_zeros(prefix: str, num_leading_zeros: int) -> int:
    leading_zeros = "0" * num_leading_zeros
    return next(
        number
        for number, hashed in _hashes_sequence(prefix)
        if hashed.startswith(leading_zeros)
    )


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 4

    prefix = io_handler.input_reader(*prob_id).read_input()

    result_p1 = _first_with_leading_zeros(prefix, num_leading_zeros=5)
    io_handler.write_result(*prob_id, part=1, result=result_p1)

    result_p2 = _first_with_leading_zeros(prefix, num_leading_zeros=6)
    io_handler.write_result(*prob_id, part=2, result=result_p2)
