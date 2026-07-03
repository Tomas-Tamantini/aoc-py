from src.core.io_handler import IOHandler
from src.solutions.y2015.d07.logic.logic_gates import evaluate_wire_value
from src.solutions.y2015.d07.logic.parse_circuit import parse_circuit


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 7

    circuit = list(parse_circuit(io_handler.input_reader(*prob_id)))

    part1 = evaluate_wire_value(wire="a", circuit=circuit)
    io_handler.write_result(*prob_id, part=1, result=part1)

    part2 = evaluate_wire_value(
        wire="a", circuit=circuit, override_wires={"b": part1}
    )
    io_handler.write_result(*prob_id, part=2, result=part2)
