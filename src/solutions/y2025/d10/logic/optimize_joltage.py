import numpy as np
from scipy.optimize import LinearConstraint, milp

from src.solutions.y2025.d10.logic.machine import Machine


def min_presses_to_reach_joltage(machine: Machine) -> int:
    objective_coefficents = np.ones(machine.num_buttons)
    integrality = np.ones_like(objective_coefficents)
    A_eq = np.array(
        [
            [i in wiring for wiring in machine.button_wirings]
            for i in range(machine.num_lights)
        ]
    )
    b_eq = np.array(machine.target_joltage)
    constraints = LinearConstraint(A_eq, b_eq, b_eq)
    result = milp(
        c=objective_coefficents,
        integrality=integrality,
        constraints=constraints,
    )
    return round(result.fun)
