import pytest

from src.solutions.y2015.d07.logic.logic_gates import (
    AndGate,
    DoNothingGate,
    LeftShiftGate,
    NotGate,
    OrGate,
    RightShiftGate,
    evaluate_wire_value,
)

_CIRCUIT = [
    DoNothingGate(output_wire="x", input_wires=(123,)),
    DoNothingGate(output_wire="y", input_wires=(456,)),
    AndGate(output_wire="d", input_wires=("x", "y")),
    OrGate(output_wire="e", input_wires=("x", "y")),
    LeftShiftGate(output_wire="f", input_wires=("x", 2), num_bits=16),
    RightShiftGate(output_wire="g", input_wires=("y", 2), num_bits=16),
    NotGate(output_wire="h", input_wires=("x",), num_bits=16),
    NotGate(output_wire="i", input_wires=("y",), num_bits=16),
    AndGate(output_wire="j", input_wires=("h", "i")),
]


@pytest.mark.parametrize(
    ("wire", "expected"),
    [
        ("x", 123),
        ("y", 456),
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("j", 65028),
    ],
)
def test_logic_gates_circuit_evaluate_wire_without_overrides(wire, expected):
    output = evaluate_wire_value(wire=wire, circuit=_CIRCUIT)
    assert output == expected


@pytest.mark.parametrize(
    ("wire", "expected"),
    [
        ("x", 1234),
        ("y", 456),
        ("d", 192),
        ("e", 1498),
        ("f", 4936),
        ("g", 114),
        ("h", 4321),
        ("i", 65079),
        ("j", 4129),
    ],
)
def test_logic_gates_circuit_evaluate_wire_with_overrides(wire, expected):
    output = evaluate_wire_value(
        wire=wire, circuit=_CIRCUIT, override_wires={"x": 1234, "h": 4321}
    )
    assert output == expected
