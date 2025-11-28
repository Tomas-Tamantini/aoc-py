from src.core.io_handler import IOHandler
from src.solutions.y2015.d22.logic.auto.optimize_mana import min_mana_to_win
from src.solutions.y2015.d22.logic.factory.game_state import initial_state
from src.solutions.y2015.d22.logic.factory.moves import build_move_provider
from src.solutions.y2015.d22.logic.interactive.gameplay import Gameplay
from src.solutions.y2015.d22.logic.parser.parse_stats import parse_boss_stats


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 22

    boss_stats = parse_boss_stats(io_handler.input_reader(*prob_id))

    for part in (1, 2):
        easy_mode = part == 1
        state = initial_state(easy_mode, boss_stats.hit_points)
        game_interface = io_handler.game_interface(*prob_id, part=part)
        move_provider = build_move_provider(boss_stats.damage, game_interface)
        if game_interface:
            gameplay = Gameplay(
                initial_state=state,
                move_provider=move_provider,
                game_interface=game_interface,
            )
            gameplay.play()
            mana = gameplay.mana_spent
        else:
            mana = min_mana_to_win(state, move_provider)
        io_handler.write_result(
            *prob_id, part=part, result=mana, supports_play=True
        )
