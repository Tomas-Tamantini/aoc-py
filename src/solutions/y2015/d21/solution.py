from src.core.io_handler import IOHandler
from src.solutions.y2015.d21.logic.item_shop import default_item_shop
from src.solutions.y2015.d21.logic.parse_fighter import parse_fighter
from src.solutions.y2015.d21.logic.rpg_game import player_wins
from src.solutions.y2015.d21.logic.rpg_item import equip_fighter


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 21

    boss = parse_fighter(io_handler.input_reader(*prob_id))

    min_cost_to_win = 1_000_000_000
    max_cost_to_lose = 0

    shop = default_item_shop()
    for item_combination in shop.item_combinations():
        player = equip_fighter(hit_points=100, items=item_combination)
        cost = sum(item.cost for item in item_combination)
        if player_wins(player, boss):
            min_cost_to_win = min(min_cost_to_win, cost)
        else:
            max_cost_to_lose = max(max_cost_to_lose, cost)

    io_handler.write_result(*prob_id, part=1, result=min_cost_to_win)
    io_handler.write_result(*prob_id, part=2, result=max_cost_to_lose)
