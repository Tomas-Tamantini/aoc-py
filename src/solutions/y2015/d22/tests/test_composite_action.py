from src.solutions.y2015.d22.logic.actions.atomic import DealDamage, ToggleTurn
from src.solutions.y2015.d22.logic.actions.composite import CompositeAction
from src.solutions.y2015.d22.logic.state.attributes import hit_points
from src.solutions.y2015.d22.logic.state.character import Character


def test_composite_action_runs_all_transformations(initial_state):
    action = CompositeAction(
        transformations=(
            DealDamage(target=Character.PLAYER, damage=13),
            ToggleTurn(),
        )
    )
    next_state = action.apply(initial_state)
    assert hit_points(next_state, Character.PLAYER) == 37
    assert next_state.next_character_idx == 1
