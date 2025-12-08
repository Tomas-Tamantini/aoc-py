from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Optional

from src.solutions.shared.geometry import Vector3D
from src.solutions.shared.graph import DisjointSet


@dataclass(frozen=True)
class CircuitEdge:
    box_a: Vector3D
    box_b: Vector3D

    @property
    def dist_sq(self) -> int:
        return self.box_a.distance_squared(self.box_b)


class CircuitBuilder:
    def __init__(self, junction_boxes: list[Vector3D]):
        self._boxes = junction_boxes
        self._num_circuits = len(self._boxes)
        self._disjoint_set = DisjointSet()
        for b in self._boxes:
            self._disjoint_set.make_set(b)
        self._unvisited_edges = sorted(
            [CircuitEdge(a, b) for a, b in combinations(self._boxes, 2)],
            key=lambda e: -e.dist_sq,
        )
        self._most_recent_edge: Optional[CircuitEdge] = None

    @property
    def num_circuits(self) -> int:
        return self._num_circuits

    @property
    def most_recent_edge(self) -> CircuitEdge:
        if not self._most_recent_edge:
            raise ValueError("No edge has been set yet")
        return self._most_recent_edge

    def _are_connected(self, box_a: Vector3D, box_b: Vector3D) -> bool:
        return self._disjoint_set.find(box_a) == self._disjoint_set.find(box_b)

    def connect_next_smallest_edge(self) -> None:
        edge = self._unvisited_edges.pop()
        if not self._are_connected(edge.box_a, edge.box_b):
            self._num_circuits -= 1
            self._disjoint_set.union(edge.box_a, edge.box_b)
        self._most_recent_edge = edge

    def circuit_sizes(self) -> Iterable[int]:
        sizes = defaultdict(int)
        for box in self._boxes:
            sizes[self._disjoint_set.find(box)] += 1

        return sizes.values()
