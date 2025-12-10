from functools import partial
from typing import Iterator

from src.solutions.shared.graph import min_path_length_with_bfs
from src.solutions.y2025.d10.logic.indicator_lights import (
    IndicatorLightsDiagram,
)


def _neighboring_states(lights: int, buttons: set[int]) -> Iterator[int]:
    for button in buttons:
        yield lights ^ button


def min_presses_to_turn_lights_on(diagram: IndicatorLightsDiagram) -> int:
    return min_path_length_with_bfs(
        start_node=0,
        is_final_state=lambda n: n == diagram.target_configuration,
        neighbors=partial(_neighboring_states, buttons=diagram.buttons),
    )
