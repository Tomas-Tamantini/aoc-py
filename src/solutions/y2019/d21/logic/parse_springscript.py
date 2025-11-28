from typing import Iterator

from src.core.input_reader import InputReader


def _is_valid_springscript_command(words: list[str]) -> bool:
    start_commands = {"WALK", "RUN"}
    move_commands = {"AND", "OR", "NOT"}
    target_registers = "TJ"
    valid_registers = "ABCDEFGHITJ"
    if len(words) == 1:
        return words[0] in start_commands
    elif len(words) == 3:
        return (
            words[0] in move_commands
            and words[1] in valid_registers
            and words[2] in target_registers
        )
    else:
        return False


def _parse_springscript_instruction(instruction: str) -> Iterator[int]:
    words = instruction.split()
    if not _is_valid_springscript_command(words):
        raise ValueError(f"Invalid springscript command: {instruction}")

    for i, word in enumerate(words):
        if i != 0:
            yield ord(" ")
        yield from (ord(c) for c in word)


def parse_springscript(input_reader: InputReader) -> Iterator[int]:
    for line in input_reader.read_stripped_lines():
        yield from _parse_springscript_instruction(line)
        yield ord("\n")
