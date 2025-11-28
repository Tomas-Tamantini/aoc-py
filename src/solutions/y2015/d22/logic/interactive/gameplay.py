from typing import Optional

from src.core.game_interface import GameInterface
from src.solutions.y2015.d22.logic.actions.game_action import GameAction
from src.solutions.y2015.d22.logic.interactive.to_str import (
    action_to_str,
    game_state_to_str,
)
from src.solutions.y2015.d22.logic.rules.available_actions import (
    available_actions,
)
from src.solutions.y2015.d22.logic.rules.move_provider import MoveProvider
from src.solutions.y2015.d22.logic.state.attributes import is_over, player_won
from src.solutions.y2015.d22.logic.state.game_state import GameState


class Gameplay:
    def __init__(
        self,
        initial_state: GameState,
        move_provider: MoveProvider,
        game_interface: GameInterface,
    ) -> None:
        self._state = initial_state
        self._move_provider = move_provider
        self._game_interface = game_interface
        self._mana_spent = 0
        self._delay_ms = 50

    @property
    def mana_spent(self) -> int:
        return self._mana_spent

    def _is_turn_start(self) -> bool:
        return self._state.next_effect_idx == 0

    def _handle_game_over(self) -> None:
        if player_won(self._state):
            self._game_interface.put_string(
                "This kills the boss, and the player wins!", self._delay_ms
            )
        else:
            self._mana_spent = -1
            self._game_interface.put_string(
                "This kills the player, and the boss wins!", self._delay_ms
            )

    def _handle_out_of_mana(self) -> None:
        self._mana_spent = -1
        self._game_interface.put_string(
            "Player cannot afford any spells, and loses!", self._delay_ms
        )

    def _mana_msg(self) -> str:
        return f"Mana spent so far: {self._mana_spent}"

    def _handle_current_state(self) -> None:
        if is_over(self._state):
            self._handle_game_over()
        elif self._is_turn_start():
            self._game_interface.put_string(self._mana_msg())
            for line in game_state_to_str(self._state):
                self._game_interface.put_string(line, self._delay_ms)

    def _next_action(self) -> Optional[GameAction]:
        try:
            return next(available_actions(self._state, self._move_provider))
        except StopIteration:
            return None

    def _display_action(self, action: GameAction) -> None:
        for line in action_to_str(action, self._state):
            self._game_interface.put_string(line, self._delay_ms)

    def play(self) -> None:
        self._handle_current_state()
        while action := self._next_action():
            self._display_action(action)
            self._mana_spent += action.mana_cost
            self._state = action.apply(self._state)
            self._handle_current_state()

        if not is_over(self._state):
            self._handle_out_of_mana()
