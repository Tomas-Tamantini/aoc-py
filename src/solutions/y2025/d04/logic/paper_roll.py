from src.solutions.shared.geometry.vector_2d import Vector2D


def roll_is_reachable(roll_pos: Vector2D, other_rolls: set[Vector2D]) -> bool:
    num_neighbors = sum(
        n in other_rolls for n in roll_pos.neighbors(include_diagonals=True)
    )
    return num_neighbors < 4
