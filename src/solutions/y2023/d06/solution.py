from math import prod

from src.core.io_handler import IOHandler
from src.solutions.y2023.d06.logic.boat_race import num_ways_to_beat
from src.solutions.y2023.d06.logic.parse_boat_races import parse_boat_races


def solve(io_handler: IOHandler) -> None:
    prob_id = 2023, 6

    parsed_races = parse_boat_races(io_handler.input_reader(*prob_id))

    p1 = prod(
        num_ways_to_beat(race)
        for race in parsed_races.races(ignore_spaces=False)
    )
    io_handler.write_result(*prob_id, part=1, result=p1)

    p2 = next(
        num_ways_to_beat(race)
        for race in parsed_races.races(ignore_spaces=True)
    )
    io_handler.write_result(*prob_id, part=2, result=p2)
