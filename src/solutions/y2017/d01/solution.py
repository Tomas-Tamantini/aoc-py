from typing import Iterator

from src.core.io_handler import IOHandler


def _matching_digits(sequence: str, offset: int) -> Iterator[int]:
    num_digits = len(sequence)
    for i in range(num_digits):
        if sequence[i] == sequence[(i + offset) % num_digits]:
            yield int(sequence[i])


def solve(io_handler: IOHandler) -> None:
    prob_id = 2017, 1
    sequence = io_handler.input_reader(*prob_id).read_input().strip()

    part1_sum = sum(_matching_digits(sequence, offset=1))
    io_handler.write_result(*prob_id, part=1, result=part1_sum)

    part2_sum = sum(_matching_digits(sequence, offset=len(sequence) // 2))
    io_handler.write_result(*prob_id, part=2, result=part2_sum)
