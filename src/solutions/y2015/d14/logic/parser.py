from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2015.d14.logic.reindeer import Reindeer


def _parse_reindeer(line: str) -> Reindeer:
    parts = line.split()
    speed = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])
    return Reindeer(speed=speed, fly_time=fly_time, rest_time=rest_time)


def parse_reindeers(reader: InputReader) -> Iterator[Reindeer]:
    for line in reader.read_stripped_lines():
        yield _parse_reindeer(line)
