from src.core.io_handler import IOHandler
from src.solutions.y2021.d07.logic.optimal_fuel_consumption import (
    optimal_linear_fuel_consumption,
    optimal_triangular_fuel_consumption,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2021, 7
    reader = io_handler.input_reader(*prob_id)
    crab_positions = list(map(int, reader.read_input().split(",")))

    consumption_p1 = optimal_linear_fuel_consumption(crab_positions)
    io_handler.write_result(*prob_id, part=1, result=consumption_p1)

    consumption_p2 = optimal_triangular_fuel_consumption(crab_positions)
    io_handler.write_result(*prob_id, part=2, result=consumption_p2)
