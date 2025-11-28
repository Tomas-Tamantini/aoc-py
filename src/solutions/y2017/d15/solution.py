from typing import Iterator

from src.core.io_handler import IOHandler
from src.core.progress_monitor import ProgressMonitor
from src.solutions.shared.parser import parse_csv


def _sequence_generator(
    initial_term: int, factor: int, mod: int, filter_multiples_of: int = 1
) -> Iterator[int]:
    term = initial_term
    while True:
        if term % filter_multiples_of == 0:
            yield term
        term = (term * factor) % mod


def _terms_match(term_a: int, term_b: int) -> bool:
    num_bits_to_match = 16
    mask = 2**num_bits_to_match - 1
    return term_a & mask == term_b & mask


def _num_matches(
    generator_a: Iterator[int],
    generator_b: Iterator[int],
    num_pairs: int,
    progress_monitor: ProgressMonitor,
) -> int:
    num_matches = 0
    step_granularity = num_pairs // 100
    for i in range(num_pairs):
        if _terms_match(next(generator_a), next(generator_b)):
            num_matches += 1
        progress_monitor.update_progress_bar(i, num_pairs, step_granularity)
    return num_matches


def solve(io_handler: IOHandler) -> None:
    prob_id = 2017, 15
    initial_term_a, initial_term_b = tuple(
        parse_csv(
            io_handler.input_reader(*prob_id),
            separator=" ",
            mapper=lambda v: int(v[-1]),
        )
    )
    factor_a, factor_b = 16807, 48271
    mod = 2147483647

    generator_a = _sequence_generator(initial_term_a, factor_a, mod)
    generator_b = _sequence_generator(initial_term_b, factor_b, mod)

    num_matches = _num_matches(
        generator_a,
        generator_b,
        num_pairs=40_000_000,
        progress_monitor=io_handler.progress_monitor(*prob_id, part=1),
    )

    io_handler.write_result(*prob_id, part=1, result=num_matches)

    generator_a = _sequence_generator(
        initial_term_a, factor_a, mod, filter_multiples_of=4
    )
    generator_b = _sequence_generator(
        initial_term_b, factor_b, mod, filter_multiples_of=8
    )

    num_matches = _num_matches(
        generator_a,
        generator_b,
        num_pairs=5_000_000,
        progress_monitor=io_handler.progress_monitor(*prob_id, part=2),
    )

    io_handler.write_result(*prob_id, part=2, result=num_matches)
