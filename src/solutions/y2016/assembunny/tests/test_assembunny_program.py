from src.solutions.shared.vm.computer import Computer
from src.solutions.shared.vm.hardware import Hardware
from src.solutions.shared.vm.processor import Processor
from src.solutions.shared.vm.program import ImmutableProgram
from src.solutions.y2016.assembunny.instructions import (
    CopyInstruction,
    DecrementInstruction,
    IncrementInstruction,
    JumpNotZeroInstruction,
    LiteralValue,
    RegisterValue,
)


def test_simple_assembunny_program_can_be_executed():
    processor = Processor()
    computer = Computer(Hardware(processor))
    program = ImmutableProgram(
        [
            CopyInstruction("counter", LiteralValue(3)),
            CopyInstruction("result", LiteralValue(5)),
            IncrementInstruction("result"),
            IncrementInstruction("result"),
            DecrementInstruction("counter"),
            JumpNotZeroInstruction(RegisterValue("counter"), -3),
        ]
    )
    computer.run(program)
    assert processor.get_value_at_register("result") == 11
