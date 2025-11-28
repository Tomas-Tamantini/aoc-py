from dataclasses import dataclass

from src.solutions.y2015.d22.logic.actions.atomic import AtomicTransformation
from src.solutions.y2015.d22.logic.state.game_state import GameState


@dataclass(frozen=True)
class CompositeAction:
    transformations: tuple[AtomicTransformation, ...]
    mana_cost: int = 0

    def apply(self, game_state: GameState) -> GameState:
        state = game_state
        for transformation in self.transformations:
            state = transformation.apply(state)
        return state
