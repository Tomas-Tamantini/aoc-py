import json

from src.core.io_handler import IOHandler


def _json_sum(data, ignore_red: bool) -> int:
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(_json_sum(item, ignore_red) for item in data)
    elif isinstance(data, dict):
        if ignore_red and "red" in data.values():
            return 0
        else:
            return sum(_json_sum(value, ignore_red) for value in data.values())
    else:
        return 0


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 12

    raw_input = io_handler.input_reader(*prob_id).read_input()
    parsed = json.loads(raw_input)

    sum_p1 = _json_sum(parsed, ignore_red=False)
    io_handler.write_result(*prob_id, part=1, result=sum_p1)

    sum_p2 = _json_sum(parsed, ignore_red=True)
    io_handler.write_result(*prob_id, part=2, result=sum_p2)
