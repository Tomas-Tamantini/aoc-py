from src.solutions.shared.vm import Computer, Hardware, Processor
from src.solutions.y2019.d07.logic.amplifier_io import AmplifierIO
from src.solutions.y2019.intcode import IntcodeProgram


class Amplifier:
    def __init__(
        self,
        program: IntcodeProgram,
        input_queue: AmplifierIO,
        output_queue: AmplifierIO,
    ) -> None:
        self._program = program
        self._halted = False
        self._hardware = Hardware(
            processor=Processor(),
            memory=program,
            serial_input=input_queue,
            serial_output=output_queue,
        )

    def resume_execution(self) -> None:
        computer = Computer(self._hardware)
        try:
            computer.run(self._program)
            self._halted = True
        except AmplifierIO.EmptyQueueError:
            pass

    @property
    def halted(self) -> bool:
        return self._halted
