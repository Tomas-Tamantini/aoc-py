from dataclasses import dataclass


@dataclass(frozen=True)
class VacuumRobotMemorySpecs:
    num_subroutines: int
    max_characters: int
