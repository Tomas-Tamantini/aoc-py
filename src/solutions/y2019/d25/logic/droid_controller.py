from typing import Protocol

from src.core.game_interface import GameInterface


class DroidController(Protocol):
    def get_next_command(self) -> str: ...


class AutomaticDroidController:
    def __init__(self, commands: list[str]) -> None:
        self._commands = commands
        self._current_idx = 0

    def get_next_command(self) -> str:
        self._current_idx += 1
        return self._commands[self._current_idx - 1]


class ManualDroidController:
    def __init__(self, game_interface: GameInterface):
        self._game_interface = game_interface

    def get_next_command(self) -> str:
        return self._game_interface.prompt_input().strip().lower()
