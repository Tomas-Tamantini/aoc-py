from functools import partial
from typing import Iterator

from src.solutions.shared.graph import min_path_length_with_bfs
from src.solutions.y2025.d10.logic.machine import (
    ButtonWiring,
    IndicatorLights,
    Machine,
)


def min_presses_to_turn_lights_on(machine: Machine) -> int:
    def _neighboring_states(
        indicator_lights: IndicatorLights,
        button_wirings: tuple[ButtonWiring, ...],
    ) -> Iterator[IndicatorLights]:
        for wiring in button_wirings:
            new_lights = list(indicator_lights)
            for idx in wiring:
                new_lights[idx] = not new_lights[idx]
            yield tuple(new_lights)

    start_state = (False,) * machine.num_lights

    return min_path_length_with_bfs(
        start_node=start_state,
        is_final_state=lambda n: n == machine.target_indicator_lights,
        neighbors=partial(
            _neighboring_states, button_wirings=machine.button_wirings
        ),
    )
