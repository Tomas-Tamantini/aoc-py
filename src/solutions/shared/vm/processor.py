from typing import Hashable, Optional


class Processor:
    def __init__(
        self,
        register_values: Optional[dict[Hashable, int]] = None,
        program_counter: int = 0,
    ):
        self._program_counter = program_counter
        self._register_values = register_values if register_values else dict()

    @property
    def program_counter(self) -> int:
        return self._program_counter

    def set_program_counter(self, program_counter: int) -> None:
        self._program_counter = program_counter

    def increment_program_counter(self, increment: int = 1) -> None:
        self._program_counter += increment

    def get_value_at_register(self, register: Hashable) -> int:
        return self._register_values.get(register, 0)

    def set_value_at_register(self, register: Hashable, value: int) -> None:
        self._register_values[register] = value
