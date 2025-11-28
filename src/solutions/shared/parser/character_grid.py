from src.solutions.shared.geometry import Vector2D


class CharacterGrid:
    def __init__(self, symbols: dict[Vector2D, str]):
        self._pos_to_symbol = symbols
        self._symbol_to_positions: dict[str, set[Vector2D]] = {}

    @property
    def width(self) -> int:
        min_x = min(pos.x for pos in self._pos_to_symbol)
        max_x = max(pos.x for pos in self._pos_to_symbol)
        return max_x - min_x + 1

    @property
    def height(self) -> int:
        min_y = min(pos.y for pos in self._pos_to_symbol)
        max_y = max(pos.y for pos in self._pos_to_symbol)
        return max_y - min_y + 1

    def symbol_at(self, position: Vector2D) -> str:
        return self._pos_to_symbol[position]

    def positions(self, symbol: str) -> set[Vector2D]:
        if symbol not in self._symbol_to_positions:
            self._symbol_to_positions[symbol] = {
                pos
                for pos, sym in self._pos_to_symbol.items()
                if sym == symbol
            }
        return self._symbol_to_positions[symbol]
