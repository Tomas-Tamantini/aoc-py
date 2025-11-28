from bisect import bisect
from collections import defaultdict
from math import inf
from typing import Iterator, Optional

from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.graph import dfs
from src.solutions.y2018.d06.logic.voronoi_cell import VoronoiCell


class Voronoi:
    def __init__(self, seeds: set[Vector2D]) -> None:
        self._seeds = sorted(seeds)
        self._cached_seed_is_finite: dict[Vector2D, bool] = dict()

    def finite_cells(self) -> Iterator[VoronoiCell]:
        visited: set[Vector2D] = set()
        areas: defaultdict[Vector2D, int] = defaultdict(int)
        stack = [s for s in self._seeds]
        while stack:
            current_position = stack.pop()
            if current_position in visited:
                continue
            visited.add(current_position)
            closest_seed = self._closest_seed(current_position)
            if closest_seed and self._seed_yields_finite_region(closest_seed):
                areas[closest_seed] += 1
                for neighbor in current_position.neighbors():
                    if neighbor not in visited:
                        stack.append(neighbor)
        return (VoronoiCell(seed, area) for seed, area in areas.items())

    def _seed_yields_finite_region(self, seed: Vector2D) -> bool:
        if seed not in self._cached_seed_is_finite:
            self._cached_seed_is_finite[seed] = self._cell_is_finite(seed)
        return self._cached_seed_is_finite[seed]

    def _cell_is_finite(self, seed: Vector2D) -> bool:
        free_directions = {"U", "D", "L", "R"}
        for other in self._seeds:
            if other == seed:
                continue
            diff = other - seed
            dx, dy = diff.x, diff.y
            if dy >= abs(dx):
                free_directions.discard("U")
            if -dy >= abs(dx):
                free_directions.discard("D")
            if dx >= abs(dy):
                free_directions.discard("R")
            if -dx >= abs(dy):
                free_directions.discard("L")
            if not free_directions:
                return True

        return len(free_directions) == 0

    def _closest_seed(self, position: Vector2D) -> Optional[Vector2D]:
        min_dist = inf
        closest_seed: Optional[Vector2D] = None
        idx = bisect(self._seeds, position)
        indices_left = range(idx - 1, -1, -1)
        indices_right = range(idx, len(self._seeds))
        for index_iterator in (indices_left, indices_right):
            for i in index_iterator:
                seed = self._seeds[i]
                dist = position.manhattan_distance(seed)
                if dist < min_dist:
                    min_dist = dist
                    closest_seed = seed
                elif dist == min_dist:
                    closest_seed = None
                elif abs(seed.x - position.x) > min_dist:
                    break
        return closest_seed

    def _center_of_mass(self) -> Vector2D:
        acc = sum(self._seeds, start=Vector2D(0, 0))
        return acc // len(self._seeds)

    def safe_area(self, sum_dist_less_than: int) -> int:
        def _is_valid(position: Vector2D) -> bool:
            total_distance = sum(
                seed.manhattan_distance(position) for seed in self._seeds
            )
            return total_distance < sum_dist_less_than

        def _neighbors(cell: Vector2D) -> Iterator[Vector2D]:
            return (n for n in cell.neighbors() if _is_valid(n))

        area = 0
        for _ in dfs(start_node=self._center_of_mass(), neighbors=_neighbors):
            area += 1
        return area
