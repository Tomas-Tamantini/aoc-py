from src.solutions.shared.geometry import Vector2D
from src.solutions.y2024.d18.logic.corrupted_memory import CorruptedMemory

memory = CorruptedMemory(width=7, height=7)

corrupted_positions = [
    Vector2D(5, 4),
    Vector2D(4, 2),
    Vector2D(4, 5),
    Vector2D(3, 0),
    Vector2D(2, 1),
    Vector2D(6, 3),
    Vector2D(2, 4),
    Vector2D(1, 5),
    Vector2D(0, 6),
    Vector2D(3, 3),
    Vector2D(2, 6),
    Vector2D(5, 1),
    Vector2D(1, 2),
    Vector2D(5, 5),
    Vector2D(2, 5),
    Vector2D(6, 5),
    Vector2D(1, 4),
    Vector2D(0, 4),
    Vector2D(6, 4),
    Vector2D(1, 1),
    Vector2D(6, 1),
    Vector2D(1, 0),
    Vector2D(0, 5),
    Vector2D(1, 6),
    Vector2D(2, 0),
]


def test_corrupted_memory_finds_shortest_path_avoiding_obstacles():
    assert 22 == memory.shortest_path_length(
        corrupted_positions=set(corrupted_positions[:12])
    )


def test_corrupted_memory_first_corrupted_position_which_blocks_path():
    assert 20 == memory.idx_of_first_blocking_byte(corrupted_positions)
