from dataclasses import dataclass
from math import ceil, floor, sqrt


@dataclass(frozen=True)
class BoatRace:
    duration: int
    record_distance: int


def num_ways_to_beat(race: BoatRace) -> int:
    delta = race.duration**2 - 4 * race.record_distance
    lb = floor((race.duration - sqrt(delta)) / 2) + 1
    ub = ceil((race.duration + sqrt(delta)) / 2) - 1
    return ub - lb + 1
