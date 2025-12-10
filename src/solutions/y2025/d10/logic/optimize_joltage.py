from functools import partial
from typing import Iterator

from src.solutions.shared.graph import min_path_length_with_bfs
from src.solutions.y2025.d10.logic.machine import (
    ButtonWiring,
    JoltageLevels,
    Machine,
)


def min_presses_to_reach_joltage(machine: Machine) -> int:
    def _neighboring_states(
        joltage_levels: JoltageLevels,
        button_wirings: tuple[ButtonWiring, ...],
    ) -> Iterator[JoltageLevels]:
        for wiring in button_wirings:
            new_joltage = list(joltage_levels)
            for idx in wiring:
                new_joltage[idx] += 1
            yield tuple(new_joltage)

    start_state = (0,) * machine.num_lights

    return min_path_length_with_bfs(
        start_node=start_state,
        is_final_state=lambda n: n == machine.target_joltage,
        neighbors=partial(
            _neighboring_states, button_wirings=machine.button_wirings
        ),
    )
