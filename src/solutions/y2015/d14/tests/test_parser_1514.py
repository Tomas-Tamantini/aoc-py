from src.solutions.y2015.d14.logic.parser import parse_reindeers
from src.solutions.y2015.d14.logic.reindeer import Reindeer


def test_parse_reindeers(input_reader):
    example = """
              Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
              Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
              """  # noqa: E501
    reindeers = list(parse_reindeers(input_reader(example)))
    assert reindeers == [
        Reindeer(speed=14, fly_time=10, rest_time=127),
        Reindeer(speed=16, fly_time=11, rest_time=162),
    ]
