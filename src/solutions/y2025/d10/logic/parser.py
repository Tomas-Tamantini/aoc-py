from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2025.d10.logic.indicator_lights import (
    IndicatorLightsDiagram,
)


def _parse_target_configuration(raw_config: str) -> int:
    return int("0b" + raw_config[1:-1].replace(".", "0").replace("#", "1"), 2)


def _parse_button(raw_button: str, num_lights: int) -> int:
    num = ["0"] * num_lights
    index_tuple = eval(raw_button.replace(")", ",)"))
    for idx in index_tuple:
        num[idx] = "1"
    return int("0b" + "".join(num), 2)


def _parse_indicator_lights_diagram(line: str) -> IndicatorLightsDiagram:
    parts = line.split()
    num_lights = len(parts[0]) - 2
    buttons = set()
    for part in parts[1:-1]:
        buttons.add(_parse_button(part, num_lights))
    return IndicatorLightsDiagram(
        target_configuration=_parse_target_configuration(parts[0]),
        buttons=buttons,
    )


def parse_indicator_lights_diagrams(
    input_reader: InputReader,
) -> Iterator[IndicatorLightsDiagram]:
    for line in input_reader.read_stripped_lines():
        yield _parse_indicator_lights_diagram(line)
