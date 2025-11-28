from dataclasses import dataclass
from typing import Callable, Iterator

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d19.logic.beam_sensor import BeamSensor


@dataclass(frozen=True)
class _BeamDiagonalSlice:
    start: Vector2D
    size: int


def _binary_search(
    low: int, high: int, meets_criteria: Callable[[int], bool]
) -> int:
    while low < high:
        mid = (low + high) // 2
        if meets_criteria(mid):
            high = mid
        else:
            low = mid + 1
    return low


def _diagonal_x_candidates(diagonal_idx: int) -> Iterator[int]:
    # Bit of a cheat - for my input, beam middle is ~ y=2x/3
    for numerator in (2, 1):
        yield (numerator * diagonal_idx) // 3
    # Still yield every possible candidate to solve other inputs
    yield from range(diagonal_idx + 1)


def _some_x_inside_beam(diagonal_idx: int, beam_sensor: BeamSensor) -> int:
    for x in _diagonal_x_candidates(diagonal_idx):
        if beam_sensor.is_inside_beam(Vector2D(x, diagonal_idx - x)):
            return x
    return -1


def _beam_edges(
    diagonal_idx: int, beam_sensor: BeamSensor
) -> _BeamDiagonalSlice:
    x_inside_beam = _some_x_inside_beam(diagonal_idx, beam_sensor)
    if x_inside_beam < 0:
        return _BeamDiagonalSlice(start=Vector2D(0, 0), size=-1)
    beam_start_x = _binary_search(
        low=0,
        high=x_inside_beam,
        meets_criteria=lambda x: beam_sensor.is_inside_beam(
            Vector2D(x, diagonal_idx - x)
        ),
    )
    beam_end_x = _binary_search(
        low=x_inside_beam,
        high=diagonal_idx,
        meets_criteria=lambda x: not beam_sensor.is_inside_beam(
            Vector2D(x, diagonal_idx - x)
        ),
    )
    return _BeamDiagonalSlice(
        start=Vector2D(beam_start_x, diagonal_idx - beam_start_x),
        size=beam_end_x - beam_start_x,
    )


def _first_matching_square(
    square_size: int, beam_sensor: BeamSensor
) -> Vector2D:
    diagonal_idx = square_size - 1
    while True:
        beam_slice = _beam_edges(diagonal_idx, beam_sensor)
        diff = square_size - beam_slice.size
        if diff == 0:
            return beam_slice.start - Vector2D(0, square_size - 1)
        else:
            diagonal_idx = (diagonal_idx * square_size) // beam_slice.size


def closest_square(square_size: int, beam_sensor: BeamSensor) -> Vector2D:
    square = _first_matching_square(square_size, beam_sensor)
    tolerance = 2
    diagonal_idx = square.x + square.y + square_size - 1
    while True:
        diagonal_idx -= 1
        beam_slice = _beam_edges(diagonal_idx, beam_sensor)
        diff = square_size - beam_slice.size
        if diff == 0:
            square = beam_slice.start - Vector2D(0, square_size - 1)
        elif diff >= tolerance:
            return square
