from dataclasses import dataclass
from typing import Optional

from src.solutions.shared.geometry import Direction
from src.solutions.shared.vm import Computer, Hardware, Processor
from src.solutions.y2019.intcode import IntcodeProgram, SimpleSerialOutput


@dataclass(frozen=True)
class DroidOutputInfo:
    hit_wall: bool
    found_oxygen_system: bool


class _RepairDroidInput:
    class EmptyQueueError(Exception):
        pass

    def __init__(self) -> None:
        self._input_value: Optional[int] = None

    def set_input(self, input_value: int) -> None:
        self._input_value = input_value

    def read_next(self) -> int:
        if not self._input_value:
            raise _RepairDroidInput.EmptyQueueError()
        input_value = self._input_value
        self._input_value = None
        return input_value


class RepairDroidIO:
    def __init__(self, instructions: list[int]) -> None:
        self._program = IntcodeProgram(instructions)
        self._serial_input = _RepairDroidInput()
        self._serial_output = SimpleSerialOutput()
        self._computer = Computer(
            Hardware(
                processor=Processor(),
                memory=self._program,
                serial_input=self._serial_input,
                serial_output=self._serial_output,
            )
        )

    @staticmethod
    def _input_value(direction: Direction) -> int:
        return {
            Direction.UP: 1,
            Direction.DOWN: 2,
            Direction.LEFT: 3,
            Direction.RIGHT: 4,
        }[direction]

    @staticmethod
    def _parse_output(raw_ouput: int) -> DroidOutputInfo:
        return DroidOutputInfo(
            hit_wall=(raw_ouput == 0), found_oxygen_system=(raw_ouput == 2)
        )

    def try_move(self, direction: Direction) -> DroidOutputInfo:
        try:
            self._serial_input.set_input(self._input_value(direction))
            self._computer.run(self._program)
        except _RepairDroidInput.EmptyQueueError:
            return self._parse_output(self._serial_output.last_output)
