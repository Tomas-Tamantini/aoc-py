from typing import Optional

from src.solutions.shared.vm.memory import Memory
from src.solutions.shared.vm.processor import Processor
from src.solutions.shared.vm.serial_io import SerialInput, SerialOutput


class Hardware:
    def __init__(
        self,
        processor: Processor,
        memory: Optional[Memory] = None,
        serial_input: Optional[SerialInput] = None,
        serial_output: Optional[SerialOutput] = None,
    ) -> None:
        self._processor = processor
        self._memory = memory
        self._serial_input = serial_input
        self._serial_output = serial_output

    @property
    def processor(self) -> Processor:
        return self._processor

    @property
    def memory(self) -> Memory:
        if not self._memory:
            raise AttributeError("Memory has not been set")
        return self._memory

    @property
    def serial_input(self) -> SerialInput:
        if not self._serial_input:
            raise AttributeError("Serial input has not been set")
        return self._serial_input

    @property
    def serial_output(self) -> SerialOutput:
        if not self._serial_output:
            raise AttributeError("Serial output has not been set")
        return self._serial_output
