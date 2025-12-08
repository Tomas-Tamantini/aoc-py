from math import prod

from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector3D
from src.solutions.shared.parser import parse_csv
from src.solutions.y2025.d08.logic.circuits import CircuitBuilder


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 8

    junction_boxes = list(
        parse_csv(
            io_handler.input_reader(*prob_id),
            mapper=lambda values: Vector3D(*map(int, values)),
        )
    )

    circuit_builder = CircuitBuilder(junction_boxes)

    for _ in range(1000):
        circuit_builder.connect_next_smallest_edge()

    circuit_sizes = sorted(circuit_builder.circuit_sizes())
    result_p1 = prod(circuit_sizes[-3:])
    io_handler.write_result(*prob_id, part=1, result=result_p1)

    while circuit_builder.num_circuits > 1:
        circuit_builder.connect_next_smallest_edge()

    last_edge = circuit_builder.most_recent_edge
    result_p2 = last_edge.box_a.x * last_edge.box_b.x
    io_handler.write_result(*prob_id, part=2, result=result_p2)
