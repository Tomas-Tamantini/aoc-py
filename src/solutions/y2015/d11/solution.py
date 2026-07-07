from src.core.io_handler import IOHandler
from src.solutions.y2015.d11.logic.password_requirements import (
    has_no_forbidden_letters,
    has_three_increasing_straight,
    has_two_different_pairs,
    next_valid_password,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 11

    current_password = io_handler.input_reader(*prob_id).read_input()

    requirements = [
        has_three_increasing_straight,
        has_no_forbidden_letters,
        has_two_different_pairs,
    ]
    password_1 = next_valid_password(current_password, requirements)
    io_handler.write_result(*prob_id, part=1, result=password_1)

    password_2 = next_valid_password(password_1, requirements)
    io_handler.write_result(*prob_id, part=2, result=password_2)
