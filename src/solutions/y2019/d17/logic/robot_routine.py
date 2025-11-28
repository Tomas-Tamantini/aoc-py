from src.solutions.y2019.d17.logic.memory_specs import VacuumRobotMemorySpecs
from src.solutions.y2019.d17.logic.navigate_scaffold import (
    scaffold_movement_instructions,
)
from src.solutions.y2019.d17.logic.optimize_routine import optimize_routine
from src.solutions.y2019.d17.logic.scaffolds_map import ScaffoldsMap


def vacuum_robot_routine(
    scaffolds: ScaffoldsMap,
    memory_specs: VacuumRobotMemorySpecs,
    see_video_feed: bool,
) -> str:
    path = list(scaffold_movement_instructions(scaffolds))
    optimized = optimize_routine(path, memory_specs)
    instructions = [
        optimized.main_movement_routine,
        *optimized.movement_functions(),
        "y" if see_video_feed else "n",
    ]
    return "\n".join(instructions) + "\n"
