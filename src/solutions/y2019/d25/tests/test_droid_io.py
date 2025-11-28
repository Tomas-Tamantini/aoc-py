from src.solutions.y2019.d25.logic.droid_controller import (
    AutomaticDroidController,
)
from src.solutions.y2019.d25.logic.droid_input import DroidInput
from src.solutions.y2019.d25.logic.droid_output import DroidOutput


def test_droid_input_converts_commands_to_ascii():
    commands = ["north", "take red ball"]
    controller = AutomaticDroidController(commands)
    droid_input = DroidInput(controller)
    expected = "\n".join(commands) + "\n"
    ascii = [droid_input.read_next() for _ in range(20)]
    assert "".join(chr(n) for n in ascii) == expected


def test_droid_ouput_matches_password_sentence():
    sentence = "Hi! You should be able to get in by typing 12345 on the keypad"
    output = DroidOutput()
    for c in sentence:
        output.put(ord(c))
    assert output.password == 12345
