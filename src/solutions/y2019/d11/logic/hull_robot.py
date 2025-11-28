from dataclasses import dataclass

from src.solutions.shared.geometry import Direction, Turn, Vector2D


@dataclass(frozen=True)
class HullRobot:
    position: Vector2D
    direction: Direction

    def turn_and_move(self, turn: Turn) -> "HullRobot":
        new_direction = self.direction.turn(turn)
        new_position = self.position.move(new_direction)
        return HullRobot(new_position, new_direction)
