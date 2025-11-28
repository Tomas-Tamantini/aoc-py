class SimpleSerialOutput:
    def __init__(self) -> None:
        self._output_values: list[int] = []

    def put(self, value: int) -> None:
        self._output_values.append(value)

    @property
    def output_values(self) -> list[int]:
        return self._output_values

    @property
    def last_output(self) -> int:
        return self._output_values[-1]


class SimpleSerialInput:
    def __init__(self, input_values: list[int]) -> None:
        self._input_values = input_values
        self._current_idx = 0

    def read_next(self) -> int:
        self._current_idx = (self._current_idx + 1) % len(self._input_values)
        return self._input_values[self._current_idx - 1]
