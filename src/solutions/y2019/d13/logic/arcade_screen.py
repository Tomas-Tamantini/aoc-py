from src.solutions.shared.geometry import BoundingBox, Vector2D
from src.solutions.y2019.d13.logic.tile_type import TileType


class ArcadeScreen:
    def __init__(self) -> None:
        self._tiles: dict[Vector2D, TileType] = dict()
        self._score = 0
        self._ball_pos = Vector2D(0, 0)
        self._paddle_pos = Vector2D(0, 0)

    def set_score(self, score: int) -> None:
        self._score = score

    def set_tile(self, position: Vector2D, tile_type: TileType) -> None:
        if tile_type == TileType.EMPTY:
            self._tiles.pop(position, None)
        else:
            self._tiles[position] = tile_type
        if tile_type == TileType.PADDLE:
            self._paddle_pos = position
        elif tile_type == TileType.BALL:
            self._ball_pos = position

    def num_tiles(self, tile_type: TileType) -> int:
        return len([t for t in self._tiles.values() if t == tile_type])

    @property
    def score(self) -> int:
        return self._score

    def ball_position(self) -> Vector2D:
        return self._ball_pos

    def paddle_position(self) -> Vector2D:
        return self._paddle_pos

    def render(self) -> str:
        bb = BoundingBox(self._tiles.keys())
        chrs = {
            TileType.EMPTY: " ",
            TileType.WALL: "#",
            TileType.BLOCK: "x",
            TileType.PADDLE: "-",
            TileType.BALL: "o",
        }
        result = ""
        for y in range(bb.min_y, bb.max_y + 1):
            for x in range(bb.min_x, bb.max_x + 1):
                result += chrs[self._tiles.get(Vector2D(x, y), TileType.EMPTY)]
            result += "\n"
        result += f"Score: {self._score}\n"
        return result
