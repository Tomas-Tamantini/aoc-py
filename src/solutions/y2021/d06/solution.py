from functools import cache

from src.core.io_handler import IOHandler


@cache
def _recursive_population(timer: int, days: int) -> int:
    if days == 0:
        return 1
    elif timer > 0:
        return _recursive_population(timer - 1, days - 1)
    else:
        reset = _recursive_population(6, days - 1)
        respawn = _recursive_population(8, days - 1)
        return reset + respawn


def lantern_fish_population(initial_timers: tuple[int, ...], days: int):
    return sum(_recursive_population(timer, days) for timer in initial_timers)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2021, 6

    reader = io_handler.input_reader(*prob_id)
    initial_timers = tuple(map(int, reader.read_input().split(",")))

    pop_80 = lantern_fish_population(initial_timers, days=80)
    io_handler.write_result(*prob_id, part=1, result=pop_80)

    pop_256 = lantern_fish_population(initial_timers, days=256)
    io_handler.write_result(*prob_id, part=2, result=pop_256)
