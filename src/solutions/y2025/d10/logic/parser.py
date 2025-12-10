from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2025.d10.logic.machine import (
    ButtonWiring,
    IndicatorLights,
    JoltageLevels,
    Machine,
)


def _parse_indicator_lights(diagram: str) -> IndicatorLights:
    return tuple(c == "#" for c in diagram[1:-1])


def _parse_button_wiring(diagram: str) -> ButtonWiring:
    return eval(diagram.replace(")", ",)"))


def _parse_joltage_requirements(diagram: str) -> JoltageLevels:
    return eval(diagram.replace("{", "(").replace("}", ",)"))


def _parse_machine(line: str) -> Machine:
    parts = line.split()
    return Machine(
        target_indicator_lights=_parse_indicator_lights(parts[0]),
        target_joltage=_parse_joltage_requirements(parts[-1]),
        button_wirings=tuple(_parse_button_wiring(p) for p in parts[1:-1]),
    )


def parse_machines(input_reader: InputReader) -> Iterator[Machine]:
    for line in input_reader.read_stripped_lines():
        yield _parse_machine(line)
