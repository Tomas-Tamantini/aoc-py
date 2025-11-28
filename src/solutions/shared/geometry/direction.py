from enum import Enum


class Turn(Enum):
    NO_TURN = 0
    RIGHT = 1
    U_TURN = 2
    LEFT = 3


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def turn(self, turn_direction: Turn) -> "Direction":
        return Direction((self.value + turn_direction.value) % 4)

    @property
    def is_horizontal(self) -> bool:
        return self in {Direction.LEFT, Direction.RIGHT}
