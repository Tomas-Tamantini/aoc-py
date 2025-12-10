from functools import partial
from typing import Iterator

from src.solutions.shared.graph import min_path_length_with_bfs


def _neighboring_states(lights: int, buttons: set[int]) -> Iterator[int]:
    for button in buttons:
        yield lights ^ button


def min_button_presses(target_configuration: int, buttons: set[int]) -> int:
    return min_path_length_with_bfs(
        start_node=0,
        is_final_state=lambda n: n == target_configuration,
        neighbors=partial(_neighboring_states, buttons=buttons),
    )
