from src.core.io_handler import IOHandler
from src.solutions.y2015.d14.logic.parser import parse_reindeers
from src.solutions.y2015.d14.logic.reindeer import (
    reindeer_race_results,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 14

    reindeers = list(parse_reindeers(io_handler.input_reader(*prob_id)))
    results = reindeer_race_results(reindeers, race_duration=2503)
    io_handler.write_result(*prob_id, part=1, result=results.max_position)
    io_handler.write_result(*prob_id, part=2, result=results.max_points)
