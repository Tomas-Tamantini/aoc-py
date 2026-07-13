from typing import Iterator

from src.core.io_handler import IOHandler
from src.solutions.shared.number_theory import divisors


def _house_with_divisors() -> Iterator[tuple[int, set[int]]]:
    house = 1
    while True:
        yield house, divisors(house)
        house += 1


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 20

    threshold = int(io_handler.input_reader(*prob_id).read_input())
    io_handler.progress_monitor(*prob_id, part=1).estimate_remaining_time(
        estimation="20s"
    )

    house_p1 = house_p2 = -1
    for house, divs in _house_with_divisors():
        if sum(divs) * 10 >= threshold and house_p1 == -1:
            house_p1 = house
            if house_p2 != -1:
                break

        if (
            sum(elf for elf in divs if house // elf <= 50) * 11 >= threshold
            and house_p2 == -1
        ):
            house_p2 = house
            if house_p1 != -1:
                break

    io_handler.write_result(*prob_id, part=1, result=house_p1)
    io_handler.write_result(*prob_id, part=2, result=house_p2)
