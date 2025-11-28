from src.solutions.shared.graph import min_path_length_with_dijkstra
from src.solutions.y2015.d22.logic.rules.available_actions import (
    available_actions,
)
from src.solutions.y2015.d22.logic.rules.move_provider import MoveProvider
from src.solutions.y2015.d22.logic.state.attributes import player_won
from src.solutions.y2015.d22.logic.state.game_state import GameState


def min_mana_to_win(initial_state: GameState, move_provider: MoveProvider):
    def weighted_neighbors(state):
        for action in available_actions(state, move_provider):
            yield action.apply(state), action.mana_cost

    return min_path_length_with_dijkstra(
        start_node=initial_state,
        is_final_state=player_won,
        weighted_neighbors=weighted_neighbors,
    )
