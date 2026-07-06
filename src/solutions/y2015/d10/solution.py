from src.core.io_handler import IOHandler
from src.solutions.y2015.d10.logic.look_and_say import next_look_and_say


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 10

    first_term = io_handler.input_reader(*prob_id).read_input().strip()
    progress_monitor = io_handler.progress_monitor(*prob_id, part=1)
    current_term = first_term
    for _ in range(40):
        current_term = next_look_and_say(current_term)

    io_handler.write_result(*prob_id, part=1, result=len(current_term))
    for _ in progress_monitor.track(range(10)):
        current_term = next_look_and_say(current_term)

    io_handler.write_result(*prob_id, part=2, result=len(current_term))
