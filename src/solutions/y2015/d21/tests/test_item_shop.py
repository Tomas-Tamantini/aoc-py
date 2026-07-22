from src.solutions.y2015.d21.logic.item_shop import default_item_shop


def test_item_shops_iterates_through_all_item_combinations():
    item_shop = default_item_shop()
    combinations = list(item_shop.item_combinations())
    assert len(combinations) == 660
