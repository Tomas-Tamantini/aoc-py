from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass(frozen=True)
class LogicGate(ABC):
    output_wire: str
    input_wires: tuple[str | int, ...]

    @abstractmethod
    def evaluate(self, *input_values: int) -> int: ...


@dataclass(frozen=True)
class DoNothingGate(LogicGate):
    def evaluate(self, *input_values: int) -> int:  # noqa: PLR6301
        return input_values[0]


@dataclass(frozen=True)
class AndGate(LogicGate):
    def evaluate(self, *input_values: int) -> int:  # noqa: PLR6301
        return input_values[0] & input_values[1]


@dataclass(frozen=True)
class OrGate(LogicGate):
    def evaluate(self, *input_values: int) -> int:  # noqa: PLR6301
        return input_values[0] | input_values[1]


@dataclass(frozen=True)
class LeftShiftGate(LogicGate):
    num_bits: int = 16

    def evaluate(self, *input_values: int) -> int:
        return (input_values[0] << input_values[1]) & (
            (1 << self.num_bits) - 1
        )


@dataclass(frozen=True)
class RightShiftGate(LogicGate):
    num_bits: int = 16

    def evaluate(self, *input_values: int) -> int:
        return (input_values[0] >> input_values[1]) & (
            (1 << self.num_bits) - 1
        )


@dataclass(frozen=True)
class NotGate(LogicGate):
    num_bits: int = 16

    def evaluate(self, *input_values: int) -> int:
        return (~input_values[0]) & ((1 << self.num_bits) - 1)


def evaluate_wire_value(
    wire: str,
    circuit: list[LogicGate],
    override_wires: Optional[dict[str, int]] = None,
) -> int:
    evaluator = _CircuitEvaluator(
        circuit=circuit, override_wires=override_wires or dict()
    )
    return evaluator.evaluate_wire(wire)


class _CircuitEvaluator:
    def __init__(
        self, circuit: list[LogicGate], override_wires: dict[str, int]
    ):
        self._circuit = circuit
        self._known_signals = override_wires.copy()
        self._output_to_gate = {gate.output_wire: gate for gate in circuit}

    def _gate_input_values(self, gate: LogicGate) -> Iterator[int]:
        for input_wire in gate.input_wires:
            if isinstance(input_wire, int):
                yield input_wire
            else:
                yield self.evaluate_wire(input_wire)

    def evaluate_wire(self, wire: str) -> int:
        if wire in self._known_signals:
            return self._known_signals[wire]
        gate = self._output_to_gate[wire]
        self._known_signals[wire] = gate.evaluate(
            *self._gate_input_values(gate)
        )
        return self._known_signals[wire]


def _evaluate_wire_recursive(
    wire: str,
    circuit: list[LogicGate],
    known_signals: dict[str, int],
) -> int:
    if wire in known_signals:
        return known_signals[wire]
    gate = next(g for g in circuit if g.output_wire == wire)
    input_values = []
    for input_wire in gate.input_wires:
        if isinstance(input_wire, int):
            input_values.append(input_wire)
        else:
            input_values.append(
                _evaluate_wire_recursive(input_wire, circuit, known_signals)
            )
    known_signals[wire] = gate.evaluate(*input_values)
    return known_signals[wire]
