from src.solutions.y2019.d25.logic.droid_controller import (
    AutomaticDroidController,
)


def test_automatic_droid_controller_yields_pre_configured_commands():
    commands = ["north", "take red ball"]
    controller = AutomaticDroidController(commands)
    assert controller.get_next_command() == commands[0]
    assert controller.get_next_command() == commands[1]
