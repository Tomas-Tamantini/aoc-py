from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

from src.solutions.shared.geometry import Vector3D
from src.solutions.shared.graph import DisjointSet


@dataclass(frozen=True)
class _CircuitEdge:
    box_a: Vector3D
    box_b: Vector3D

    @property
    def dist_sq(self) -> int:
        return self.box_a.distance_squared(self.box_b)


class CircuitsBuilder:
    def __init__(self, junction_boxes: list[Vector3D]):
        self._boxes = junction_boxes
        self._disjoint_set = DisjointSet()
        for b in self._boxes:
            self._disjoint_set.make_set(b)
        self._unvisited_edges = sorted(
            [_CircuitEdge(a, b) for a, b in combinations(self._boxes, 2)],
            key=lambda e: -e.dist_sq,
        )

    def connect_next_smallest_edge(self) -> None:
        edge = self._unvisited_edges.pop()
        self._disjoint_set.union(edge.box_a, edge.box_b)

    def circuit_sizes(self) -> Iterable[int]:
        circuit_sizes = defaultdict(int)
        for box in self._boxes:
            circuit_sizes[self._disjoint_set.find(box)] += 1

        return circuit_sizes.values()
