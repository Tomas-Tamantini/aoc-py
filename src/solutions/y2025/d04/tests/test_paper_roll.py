from src.solutions.shared.geometry.vector_2d import Vector2D
from src.solutions.shared.parser.grid_parser import parse_grid
from src.solutions.y2025.d04.logic.paper_roll import (
    removable_rolls,
    roll_is_reachable,
)


def test_paper_roll_is_reachable_if_fewer_than_four_neighbors():
    rolls = {Vector2D(i, j) for i in range(3) for j in range(2)}
    assert roll_is_reachable(roll_pos=Vector2D(0, 0), other_rolls=rolls)
    assert not roll_is_reachable(roll_pos=Vector2D(1, 0), other_rolls=rolls)


def test_paper_rolls_are_removed_recursively(input_reader):
    reader = input_reader(
        "..@@.@@@@.\n"
        "@@@.@.@.@@\n"
        "@@@@@.@.@@\n"
        "@.@@@@..@.\n"
        "@@.@@@@.@@\n"
        ".@@@@@@@.@\n"
        ".@.@.@.@@@\n"
        "@.@@@.@@@@\n"
        ".@@@@@@@@.\n"
        "@.@.@@@.@.\n"
    )
    roll_positions = parse_grid(reader).positions("@")
    removed = removable_rolls(roll_positions)
    assert len(removed) == 43
