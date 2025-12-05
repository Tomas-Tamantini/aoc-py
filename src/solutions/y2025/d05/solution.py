from src.core.io_handler import IOHandler

from src.solutions.y2025.d05.logic.number_range import NumberRange


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 5

    ranges = []
    ids = []
    for line in io_handler.input_reader(*prob_id).read_stripped_lines():
        if "-" in line:
            num_range = NumberRange(*map(int, line.split("-")))
            ranges.append(num_range)
        else:
            ids.append(int(line))

    total = sum(any(r.contains(id) for r in ranges) for id in ids)

    io_handler.write_result(*prob_id, part=1, result=total)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
