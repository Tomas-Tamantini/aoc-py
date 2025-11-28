from src.solutions.shared.geometry import Direction
from src.solutions.y2023.d14.logic.parabolic_dish import ParabolicDish


def run_cycle(
    dish: ParabolicDish, cycle: tuple[Direction, ...], num_cycles: int
) -> ParabolicDish:
    states: dict[ParabolicDish, int] = dict()
    for i in range(num_cycles):
        for direction in cycle:
            dish = dish.tilt(direction)
        if dish in states:
            previous_idx = states[dish]
            period = i - previous_idx
            target = (num_cycles - 1 - previous_idx) % period + previous_idx
            return next(s for s, idx in states.items() if idx == target)
        else:
            states[dish] = i
    return dish
