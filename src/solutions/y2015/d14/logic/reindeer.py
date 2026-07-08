from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Reindeer:
    speed: int
    fly_time: int
    rest_time: int

    def _positions_generator(self) -> Iterator[int]:
        pos = 0
        while True:
            for _ in range(self.fly_time):
                pos += self.speed
                yield pos
            for _ in range(self.rest_time):
                yield pos

    def positions(self, race_duration: int) -> list[int]:
        gen = self._positions_generator()
        return [next(gen) for _ in range(race_duration)]


@dataclass(frozen=True)
class ReindeerRaceResults:
    max_position: int
    max_points: int


def reindeer_race_results(
    reindeers: list[Reindeer], race_duration: int
) -> ReindeerRaceResults:
    positions = [reindeer.positions(race_duration) for reindeer in reindeers]
    max_position = max(pos[-1] for pos in positions)
    reindeer_points = [0] * len(reindeers)
    for t in range(race_duration):
        max_distance_at_t = max(pos[t] for pos in positions)
        for i, pos in enumerate(positions):
            if pos[t] == max_distance_at_t:
                reindeer_points[i] += 1
    max_points = max(reindeer_points)
    return ReindeerRaceResults(
        max_position=max_position, max_points=max_points
    )
