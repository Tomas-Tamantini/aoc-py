from typing import Optional

from src.core.game_interface import GameInterface


class DroidOutput:
    def __init__(self, game_interface: Optional[GameInterface] = None):
        self._password = ""
        self._preamble = "You should be able to get in by typing"
        self._current_match_length = 0
        self._is_reading_password = False
        self._game_interface = game_interface

    @property
    def password(self) -> int:
        return int(self._password)

    def put(self, value: int) -> None:
        if self._game_interface:
            self._game_interface.put_character(chr(value))

        if self._current_match_length < len(self._preamble):
            if chr(value) == self._preamble[self._current_match_length]:
                self._current_match_length += 1
            else:
                self._current_match_length = 0
        elif self._is_reading_password:
            if chr(value) == " ":
                self._is_reading_password = False
            else:
                self._password += chr(value)
        else:
            self._is_reading_password = not self._password
