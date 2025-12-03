from src.core.io_handler import IOHandler
from src.solutions.y2025.d03.logic.optimize_joltage import optimize_joltage
from src.solutions.y2025.d03.logic.parser import parse_battery_banks


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 3
    battery_banks = list(
        parse_battery_banks(io_handler.input_reader(*prob_id))
    )
    total_output_p1 = sum(
        optimize_joltage(bank, num_digits=2) for bank in battery_banks
    )
    total_output_p2 = sum(
        optimize_joltage(bank, num_digits=12) for bank in battery_banks
    )
    io_handler.write_result(*prob_id, part=1, result=total_output_p1)
    io_handler.write_result(*prob_id, part=2, result=total_output_p2)
