import re
from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2015.d07.logic.logic_gates import (
    AndGate,
    DoNothingGate,
    LeftShiftGate,
    LogicGate,
    NotGate,
    OrGate,
    RightShiftGate,
)

_NUM_BITS = 16

_NOT_RE = re.compile(r"^NOT (\w+) -> (\w+)$")
_BINARY_RE = re.compile(r"^(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)$")
_ASSIGN_RE = re.compile(r"^(\w+) -> (\w+)$")


def _wire_or_int(value: str) -> str | int:
    return int(value) if value.isdigit() else value


def _parse_gate(line: str) -> LogicGate:
    if m := _NOT_RE.match(line):
        src, out = m.groups()
        return NotGate(
            output_wire=out,
            input_wires=(_wire_or_int(src),),
            num_bits=_NUM_BITS,
        )
    if m := _BINARY_RE.match(line):
        left, op, right, out = m.groups()
        left_v = _wire_or_int(left)
        right_v = _wire_or_int(right)
        if op == "AND":
            return AndGate(output_wire=out, input_wires=(left_v, right_v))
        if op == "OR":
            return OrGate(output_wire=out, input_wires=(left_v, right_v))
        if op == "LSHIFT":
            return LeftShiftGate(
                output_wire=out,
                input_wires=(left_v, right_v),
                num_bits=_NUM_BITS,
            )
        if op == "RSHIFT":
            return RightShiftGate(
                output_wire=out,
                input_wires=(left_v, right_v),
                num_bits=_NUM_BITS,
            )
    if m := _ASSIGN_RE.match(line):
        src, out = m.groups()
        return DoNothingGate(output_wire=out, input_wires=(_wire_or_int(src),))
    raise ValueError(f"Cannot parse gate: {line!r}")


def parse_circuit(input_reader: InputReader) -> Iterator[LogicGate]:
    for line in input_reader.read_stripped_lines():
        yield _parse_gate(line)
