from src.solutions.y2015.d07.logic.logic_gates import (
    AndGate,
    DoNothingGate,
    LeftShiftGate,
    NotGate,
    OrGate,
    RightShiftGate,
)
from src.solutions.y2015.d07.logic.parse_circuit import parse_circuit


def test_parse_circuit(input_reader):
    reader = input_reader(
        """
        123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i
        1 AND cx -> cy
        """
    )
    gates = list(parse_circuit(reader))
    assert gates == [
        DoNothingGate(output_wire="x", input_wires=(123,)),
        DoNothingGate(output_wire="y", input_wires=(456,)),
        AndGate(output_wire="d", input_wires=("x", "y")),
        OrGate(output_wire="e", input_wires=("x", "y")),
        LeftShiftGate(output_wire="f", input_wires=("x", 2), num_bits=16),
        RightShiftGate(output_wire="g", input_wires=("y", 2), num_bits=16),
        NotGate(output_wire="h", input_wires=("x",), num_bits=16),
        NotGate(output_wire="i", input_wires=("y",), num_bits=16),
        AndGate(output_wire="cy", input_wires=(1, "cx")),
    ]
