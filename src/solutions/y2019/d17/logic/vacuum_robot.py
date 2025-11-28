from dataclasses import dataclass

from src.solutions.shared.geometry.direction import Turn
from src.solutions.shared.geometry.vector_2d import Direction, Vector2D


@dataclass(frozen=True)
class VacuumRobot:
    position: Vector2D
    direction: Direction

    def move_forward(self, num_steps) -> "VacuumRobot":
        return VacuumRobot(
            position=self.position.move(self.direction, num_steps),
            direction=self.direction,
        )

    def turn(self, turn_direction: Turn) -> "VacuumRobot":
        return VacuumRobot(
            position=self.position,
            direction=self.direction.turn(turn_direction),
        )

    def adjacent_tile(self, turn_direction: Turn) -> Vector2D:
        new_direction = self.direction.turn(turn_direction)
        return self.position.move(new_direction)
