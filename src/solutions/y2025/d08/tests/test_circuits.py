from src.solutions.shared.geometry import Vector3D
from src.solutions.y2025.d08.logic.circuits import CircuitsBuilder


def test_smallest_edges_get_connected_first():
    junction_boxes = [
        Vector3D(162, 817, 812),
        Vector3D(57, 618, 57),
        Vector3D(906, 360, 560),
        Vector3D(592, 479, 940),
        Vector3D(352, 342, 300),
        Vector3D(466, 668, 158),
        Vector3D(542, 29, 236),
        Vector3D(431, 825, 988),
        Vector3D(739, 650, 466),
        Vector3D(52, 470, 668),
        Vector3D(216, 146, 977),
        Vector3D(819, 987, 18),
        Vector3D(117, 168, 530),
        Vector3D(805, 96, 715),
        Vector3D(346, 949, 466),
        Vector3D(970, 615, 88),
        Vector3D(941, 993, 340),
        Vector3D(862, 61, 35),
        Vector3D(984, 92, 344),
        Vector3D(425, 690, 689),
    ]
    circuit_builder = CircuitsBuilder(junction_boxes)
    for _ in range(10):
        circuit_builder.connect_next_smallest_edge()
    circuit_sizes = sorted(circuit_builder.circuit_sizes())
    assert circuit_sizes == [1, 1, 1, 1, 1, 1, 1, 2, 2, 4, 5]
