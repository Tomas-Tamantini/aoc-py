from src.solutions.y2015.d14.logic.reindeer import (
    Reindeer,
    reindeer_race_results,
)


def test_reindeer_yields_dynamic_position():
    comet = Reindeer(speed=14, fly_time=10, rest_time=127)
    comet_positions = comet.positions(race_duration=1000)
    assert comet_positions[0] == 14
    assert comet_positions[-1] == 1120


def test_reindeer_race_returns_final_status():
    comet = Reindeer(speed=14, fly_time=10, rest_time=127)
    dancer = Reindeer(speed=16, fly_time=11, rest_time=162)
    results = reindeer_race_results(
        reindeers=[comet, dancer], race_duration=1000
    )
    assert results.max_position == 1120
    assert results.max_points == 689
