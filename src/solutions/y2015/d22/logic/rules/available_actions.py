from typing import Iterator

from src.solutions.y2015.d22.logic.actions.game_action import GameAction
from src.solutions.y2015.d22.logic.rules.effect_actions import effect_action
from src.solutions.y2015.d22.logic.rules.move_provider import MoveProvider
from src.solutions.y2015.d22.logic.state.attributes import (
    current_effect_state,
    is_over,
)
from src.solutions.y2015.d22.logic.state.game_state import GameState


def available_actions(
    game_state: GameState, move_provider: MoveProvider
) -> Iterator[GameAction]:
    if not is_over(game_state):
        if current_effect_state(game_state):
            yield effect_action(game_state)
        else:
            for move in move_provider.next_moves(game_state):
                yield move.action()
