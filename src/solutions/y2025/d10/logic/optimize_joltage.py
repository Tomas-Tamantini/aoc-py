from src.solutions.shared.optimization.milp_model import MilpModel, Sense
from src.solutions.y2025.d10.logic.machine import Machine


def min_presses_to_reach_joltage(machine: Machine) -> int:
    model = MilpModel()
    x = [
        model.add_variable(integer=True, lb=0)
        for _ in range(machine.num_buttons)
    ]

    for i in range(machine.num_lights):
        wired = sum(
            x[b]
            for b, wiring in enumerate(machine.button_wirings)
            if i in wiring
        )
        model.add_constraint(wired == machine.target_joltage[i])  # type: ignore

    model.set_objective(sum(x), sense=Sense.MINIMIZE)  # type: ignore
    return round(model.solve())
