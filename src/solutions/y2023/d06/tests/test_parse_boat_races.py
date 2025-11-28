import pytest

from src.solutions.y2023.d06.logic.boat_race import BoatRace
from src.solutions.y2023.d06.logic.parse_boat_races import parse_boat_races


@pytest.fixture
def parsed_boat_races(input_reader):
    reader = input_reader(
        """
        Time:       7   15  30
        Distance:   9   40  200
        """
    )
    return parse_boat_races(reader)


def test_parse_boat_races_with_spaces(parsed_boat_races):
    assert list(parsed_boat_races.races(ignore_spaces=False)) == [
        BoatRace(duration=7, record_distance=9),
        BoatRace(duration=15, record_distance=40),
        BoatRace(duration=30, record_distance=200),
    ]


def test_parse_boat_races_ignoring_spaces(parsed_boat_races):
    assert list(parsed_boat_races.races(ignore_spaces=True)) == [
        BoatRace(duration=71530, record_distance=940200)
    ]
