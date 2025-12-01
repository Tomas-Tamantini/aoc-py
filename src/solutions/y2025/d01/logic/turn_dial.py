from dataclasses import dataclass


@dataclass(frozen=True)
class TurnDial:
    size: int
    start_position: int


def num_times_landed_in_zero(dial: TurnDial, offsets: list[int]) -> int:
    num_zeros = 0
    pos = dial.start_position
    for offset in offsets:
        pos += offset
        if pos % dial.size == 0:
            num_zeros += 1

    return num_zeros


def _num_zero_clicks(dial_pos: int, dial_size: int, offset: int) -> int:
    new_pos = offset + dial_pos
    if offset >= 0:
        return new_pos // dial_size
    else:
        return abs((dial_size - new_pos) // dial_size) - (dial_pos == 0)


def num_times_clicked_zero(dial: TurnDial, offsets: list[int]) -> int:
    num_zeros = 0
    pos = dial.start_position
    for offset in offsets:
        num_zeros += _num_zero_clicks(pos, dial.size, offset)
        pos = (pos + offset) % dial.size
    return num_zeros
