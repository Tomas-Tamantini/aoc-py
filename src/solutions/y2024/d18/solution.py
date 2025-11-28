from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser import parse_csv
from src.solutions.y2024.d18.logic.corrupted_memory import CorruptedMemory


def solve(io_handler: IOHandler) -> None:
    prob_id = 2024, 18

    corrupted_positions = list(
        parse_csv(
            io_handler.input_reader(*prob_id),
            mapper=lambda v: Vector2D(*map(int, v)),
        )
    )
    memory = CorruptedMemory(width=71, height=71)

    min_path = memory.shortest_path_length(set(corrupted_positions[:1024]))
    io_handler.write_result(*prob_id, part=1, result=min_path)

    idx_blocking = memory.idx_of_first_blocking_byte(corrupted_positions)

    blocking = corrupted_positions[idx_blocking]

    io_handler.write_result(
        *prob_id, part=2, result=f"{blocking.x},{blocking.y}"
    )
