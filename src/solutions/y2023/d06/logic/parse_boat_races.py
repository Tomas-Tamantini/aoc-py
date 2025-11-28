from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.parser import parse_csv
from src.solutions.y2023.d06.logic.boat_race import BoatRace


class ParsedRaces:
    def __init__(
        self, durations: tuple[int, ...], record_distances: tuple[int, ...]
    ):
        self._durations = durations
        self._record_distances = record_distances

    @staticmethod
    def _merge_values(values: tuple[int, ...]) -> int:
        return int("".join(map(str, values)))

    def races(self, ignore_spaces: bool) -> Iterator[BoatRace]:
        if ignore_spaces:
            duration = self._merge_values(self._durations)
            record_distance = self._merge_values(self._record_distances)
            yield BoatRace(duration, record_distance)
        else:
            for args in zip(self._durations, self._record_distances):
                yield BoatRace(*args)


def parse_boat_races(input_reader: InputReader) -> ParsedRaces:
    return ParsedRaces(
        *parse_csv(
            input_reader,
            separator=" ",
            mapper=lambda values: tuple(int(v) for v in values[1:] if v),
        )
    )
