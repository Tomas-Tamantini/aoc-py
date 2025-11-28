import pytest

from src.solutions.y2023.d06.logic.boat_race import BoatRace, num_ways_to_beat


@pytest.mark.parametrize(
    ("duration", "record_distance", "expected"),
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
        (71530, 940200, 71503),
    ],
)
def test_num_ways_to_win_boat_race_is_calculated_efficiently(
    duration, record_distance, expected
):
    assert num_ways_to_beat(BoatRace(duration, record_distance)) == expected
