from dataclasses import dataclass
from typing import Optional

from src.solutions.shared.vm import Instruction
from src.solutions.y2016.assembunny.instructions import (
    CopyInstruction,
    DecrementInstruction,
    IncrementInstruction,
    JumpNotZeroInstruction,
    LiteralValue,
    NoOpInstruction,
    RegisterValue,
)


@dataclass(frozen=True)
class _Optimization:
    start_idx: int
    new_block: list[Instruction]

    @property
    def end_idx(self) -> int:
        return self.start_idx + len(self.new_block)


def _validate_type(obj, cls):
    if isinstance(obj, cls):
        return obj


def _find_addition_optimization(
    instructions: list[Instruction],
) -> Optional[_Optimization]:
    block_size = 3
    for i in range(len(instructions) + 1 - block_size):
        block = instructions[i : i + block_size]
        if (
            (inc := _validate_type(block[0], IncrementInstruction))  # noqa: PLR0916
            and (dec := _validate_type(block[1], DecrementInstruction))
            and (jnz := _validate_type(block[2], JumpNotZeroInstruction))
            and (jnz.offset == 1 - block_size)
            and (jnz_reg := _validate_type(jnz.value, RegisterValue))
            and (jnz_reg.register == dec.register)
        ):
            return _Optimization(
                start_idx=i,
                new_block=[
                    IncrementInstruction(
                        register=inc.register,
                        value=RegisterValue(dec.register),
                    ),
                    CopyInstruction(
                        register=dec.register, value=LiteralValue(0)
                    ),
                    NoOpInstruction(),
                ],
            )


def _find_optimization(
    instructions: list[Instruction],
) -> Optional[_Optimization]:
    if opt := _find_addition_optimization(instructions):
        return opt


def optimize_assembunny_code(
    instructions: list[Instruction],
) -> list[Instruction]:
    optimized = instructions[:]
    while next_optimization := _find_optimization(optimized):
        optimized[next_optimization.start_idx : next_optimization.end_idx] = (
            next_optimization.new_block
        )
    return optimized
